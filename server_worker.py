#!/usr/bin/env python3
"""
Geodipo Autonomous RAG Server Worker
Designed to run in background on Geodipo server (or any cloud runner) 24/7 without user intervention.
Uses standard Python 3 libraries only.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error
import logging

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("worker.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("RAGWorker")

# Add current dir to path to import rag_engine
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from rag_knowledge_base.rag_engine import GeodipoRAGEngine

MCP_URL = "https://geodipo.com/wp-json/easy-mcp-ai/v1/mcp"
BEARER_TOKEN = "wpmcp_af4a9fcd6246641ea04fcea5d03121de5d3d35714bff94e428390b73e2cdf16c"
CHECKPOINT_FILE = os.path.join(BASE_DIR, "checkpoint.json")
QUEUE_FILE = os.path.join(BASE_DIR, "rag_knowledge_base", "mappings", "unified_queue.json")

def call_mcp_tool(tool_name: str, arguments: dict, retries: int = 3) -> dict:
    payload = {
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000),
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Geodipo-Autonomous-RAG-Worker/1.0"
    }
    
    for attempt in range(retries):
        try:
            req = urllib.request.Request(MCP_URL, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                res_body = resp.read().decode("utf-8")
                res_json = json.loads(res_body)
                if "result" in res_json and "content" in res_json["result"]:
                    txt = res_json["result"]["content"][0]["text"]
                    try:
                        return json.loads(txt)
                    except Exception:
                        return {"raw_text": txt}
                return res_json
        except Exception as e:
            logger.warning(f"Tool {tool_name} attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(2 * (attempt + 1))
            
    return None

def load_checkpoint() -> dict:
    if os.path.exists(CHECKPOINT_FILE):
        try:
            with open(CHECKPOINT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading checkpoint, starting fresh: {e}")
    return {"completed_ids": [], "already_enriched_ids": [], "failed_ids": []}

def save_checkpoint(cp: dict):
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(cp, f, indent=2, ensure_ascii=False)

def inject_rag_into_content(content: str, rag_html: str) -> str:
    # Look for natural injection targets before closing footer/consult/contact blocks
    targets = [
        '<div class="gd-consult">',
        '<div class="gd-cta">',
        '<section class="gd-cta',
        '<footer',
        '<!-- wp:block {"ref":',
        '<!-- wp:template-part {"slug":"footer"'
    ]
    for t in targets:
        if t in content:
            parts = content.split(t, 1)
            return parts[0] + "\n\n" + rag_html + "\n\n" + t + parts[1]
            
    # Fallback: append before closing </div> or at very end
    if "</div>\n<!-- /wp:html -->" in content:
        return content.replace("</div>\n<!-- /wp:html -->", "\n" + rag_html + "\n</div>\n<!-- /wp:html -->")
    
    return content + "\n\n" + rag_html

def process_item(engine: GeodipoRAGEngine, item: dict) -> bool:
    item_id = item["id"]
    item_type = item["type"]
    slug = item["slug"]
    title = item["title"]

    # 1. Fetch current content with retry
    tool_get = "wp_get_post" if item_type == "post" else "wp_get_page"
    arg_get = {"post_id": item_id} if item_type == "post" else {"page_id": item_id}
    
    data = None
    content = ""
    for attempt in range(3):
        data = call_mcp_tool(tool_get, arg_get)
        if data and isinstance(data, dict):
            content = data.get("content", "")
            if content:
                break
        time.sleep(1.5 * (attempt + 1))

    if not content:
        logger.warning(f"Empty content in {item_type} ID {item_id} ({slug}) after 3 attempts")
        return False

    # 2. Check if already enriched
    if "<!-- GEODIPO RAG KNOWLEDGE BLOCK" in content or "geodipo-rag-container" in content or "<!-- rk-rag-block-start -->" in content:
        logger.info(f"Skipping ID {item_id} ({slug}) - Already enriched with RAG")
        return "ALREADY_DONE"

    # 3. Render RAG section
    try:
        rag_html = engine.render_section(slug, format_type="html")
    except Exception as e:
        logger.error(f"Error rendering RAG for {slug}: {e}")
        return False

    # 4. Inject
    new_content = inject_rag_into_content(content, rag_html)
    if new_content == content:
        logger.warning(f"Injection had no effect on ID {item_id}")
        return False

    # 5. Update WordPress
    tool_update = "wp_update_post" if item_type == "post" else "wp_update_page"
    arg_update = {
        "post_id" if item_type == "post" else "page_id": item_id,
        "content": new_content
    }
    
    res = call_mcp_tool(tool_update, arg_update)
    if res:
        bytes_added = len(new_content) - len(content)
        logger.info(f"SUCCESS: {item_type.upper()} {item_id} '{title[:30]}...' (+{bytes_added:,} chars)")
        return True
    else:
        logger.error(f"Failed to update WordPress for ID {item_id}")
        return False

def main():
    logger.info("=== Starting Geodipo Autonomous RAG Server Worker ===")
    
    if not os.path.exists(QUEUE_FILE):
        logger.error(f"Queue file not found: {QUEUE_FILE}")
        sys.exit(1)

    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        queue = json.load(f)

    total_items = len(queue)
    checkpoint = load_checkpoint()
    completed_set = set(checkpoint.get("completed_ids", []))
    already_done_set = set(checkpoint.get("already_enriched_ids", []))
    failed_set = set(checkpoint.get("failed_ids", []))

    logger.info(f"Total Queue: {total_items} URLs | Already processed: {len(completed_set)} | Prior already enriched: {len(already_done_set)}")

    engine = GeodipoRAGEngine()

    for idx, item in enumerate(queue, 1):
        item_id = item["id"]
        if item_id in completed_set or item_id in already_done_set:
            continue

        pct = (idx / total_items) * 100
        logger.info(f"[{idx}/{total_items}] ({pct:.1f}%) Processing {item['type']} {item_id}: {item['slug']}...")

        result = process_item(engine, item)
        if result == "ALREADY_DONE":
            already_done_set.add(item_id)
            checkpoint["already_enriched_ids"] = list(already_done_set)
            save_checkpoint(checkpoint)
        elif result is True:
            completed_set.add(item_id)
            checkpoint["completed_ids"] = list(completed_set)
            if item_id in failed_set:
                failed_set.remove(item_id)
                checkpoint["failed_ids"] = list(failed_set)
            save_checkpoint(checkpoint)
        else:
            failed_set.add(item_id)
            checkpoint["failed_ids"] = list(failed_set)
            save_checkpoint(checkpoint)

        # Gentle throttle
        time.sleep(0.7)

    logger.info("=== All items in queue have been processed! ===")

if __name__ == "__main__":
    main()
