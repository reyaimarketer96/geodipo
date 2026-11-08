import requests
import json
import os
import re
import time

URL = "https://geodipo.com/wp-json/easy-mcp-ai/v1/mcp"
HEADERS = {
    "Authorization": "Bearer wpmcp_af4a9fcd6246641ea04fcea5d03121de5d3d35714bff94e428390b73e2cdf16c",
    "Content-Type": "application/json"
}

def call_mcp_rest_read(route, query):
    payload = {
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000),
        "method": "tools/call",
        "params": {
            "name": "wp_rest_read",
            "arguments": {
                "route": route,
                "query": query
            }
        }
    }
    for attempt in range(3):
        try:
            res = requests.post(URL, json=payload, headers=HEADERS, timeout=30)
            if res.status_code == 200:
                data = res.json()
                if "result" in data and "content" in data["result"]:
                    txt = data["result"]["content"][0]["text"]
                    return json.loads(txt)
            time.sleep(2)
        except Exception as e:
            print(f"Error calling {route} attempt {attempt+1}: {e}")
            time.sleep(3)
    return None

def fetch_all():
    print("Fetching all 1621 posts...")
    all_posts = []
    page = 1
    total_pages = 17
    while page <= total_pages:
        print(f"Fetching posts page {page}/{total_pages}...")
        res = call_mcp_rest_read("/wp/v2/posts", {"per_page": 100, "page": page, "_fields": "id,slug,title,categories"})
        if not res or "data" not in res:
            print(f"Failed to fetch posts page {page}")
            break
        all_posts.extend(res["data"])
        total_pages = res.get("pagination", {}).get("total_pages", total_pages)
        page += 1
        time.sleep(0.5)
        
    print(f"Total posts fetched: {len(all_posts)}")
    
    print("Fetching all 300 pages...")
    all_pages = []
    page = 1
    total_pages = 3
    while page <= total_pages:
        print(f"Fetching pages page {page}/{total_pages}...")
        res = call_mcp_rest_read("/wp/v2/pages", {"per_page": 100, "page": page, "_fields": "id,slug,title"})
        if not res or "data" not in res:
            print(f"Failed to fetch pages page {page}")
            break
        all_pages.extend(res["data"])
        total_pages = res.get("pagination", {}).get("total_pages", total_pages)
        page += 1
        time.sleep(0.5)
        
    print(f"Total pages fetched: {len(all_pages)}")
    
    return all_posts, all_pages

if __name__ == "__main__":
    posts, pages = fetch_all()
    with open("audit/raw_all_posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    with open("audit/raw_all_pages.json", "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)
    print("Saved raw posts and pages to audit/")
