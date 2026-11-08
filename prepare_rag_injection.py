"""
Prepares the RAG injection payload for pilot pages.
Backs up original content and inserts the RAG block cleanly into the content.
"""

import os
import json
import re
from rag_knowledge_base.rag_engine import GeodipoRAGEngine

BACKUP_DIR = "deployment/backups/rag_injection"
os.makedirs(BACKUP_DIR, exist_ok=True)

engine = GeodipoRAGEngine()

def prepare_page(page_id: int, slug: str, raw_content_file: str):
    with open(raw_content_file, "r", encoding="utf-8") as f:
        page_data = json.load(f)

    original_content = page_data.get("content", "")
    
    # Backup original
    backup_file = os.path.join(BACKUP_DIR, f"original_page_{page_id}.json")
    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2, ensure_ascii=False)
    print(f"Backed up Page {page_id} to {backup_file}")

    # Generate RAG block
    rag_block = engine.render_section(slug, "html")
    # Wrap in Gutenberg html comment
    wrapped_rag = f"\n<!-- wp:html -->\n{rag_block}\n<!-- /wp:html -->\n"

    # Check if already injected
    marker = "<!-- GEODIPO RAG KNOWLEDGE BLOCK"
    if marker in original_content:
        # Replace existing
        pattern = r"<!-- wp:html -->\s*<!-- GEODIPO RAG KNOWLEDGE BLOCK.*?<!-- END GEODIPO RAG KNOWLEDGE BLOCK -->\s*<!-- /wp:html -->"
        new_content = re.sub(pattern, wrapped_rag.strip(), original_content, flags=re.DOTALL)
        print(f"Replaced existing RAG block in Page {page_id}")
    else:
        # Determine injection spot
        new_content = None
        # 1. Page 111 pattern
        if 'id="proses-pemesanan' in original_content:
            idx = original_content.find('id="proses-pemesanan')
            # find preceding <section
            sec_start = original_content.rfind('<section', 0, idx)
            if sec_start != -1:
                new_content = original_content[:sec_start] + wrapped_rag + "\n" + original_content[sec_start:]
        
        # 2. Page 7218 pattern
        elif 'Kredensial Otoritas' in original_content:
            idx = original_content.find('Kredensial Otoritas')
            h2_start = original_content.rfind('<!-- wp:heading -->', 0, idx)
            if h2_start == -1:
                h2_start = original_content.rfind('<h2', 0, idx)
            if h2_start != -1:
                new_content = original_content[:h2_start] + wrapped_rag + "\n" + original_content[h2_start:]

        # 3. Page 3073 pattern
        elif 'Standar Konstruksi Rekayasa Deep Well' in original_content:
            idx = original_content.find('Standar Konstruksi Rekayasa Deep Well')
            h2_start = original_content.rfind('<!-- wp:heading -->', 0, idx)
            if h2_start == -1:
                h2_start = original_content.rfind('<h2', 0, idx)
            if h2_start != -1:
                new_content = original_content[:h2_start] + wrapped_rag + "\n" + original_content[h2_start:]

        # Fallback: append before footer / closing main
        if not new_content:
            if '</main>' in original_content:
                idx = original_content.rfind('</main>')
                new_content = original_content[:idx] + wrapped_rag + "\n" + original_content[idx:]
            else:
                new_content = original_content + wrapped_rag

        print(f"Injected new RAG block into Page {page_id}")

    # Save prepared content
    prepared_file = os.path.join(BACKUP_DIR, f"prepared_page_{page_id}.txt")
    with open(prepared_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Saved prepared payload to {prepared_file} (Length: {len(new_content)})\n")
    return new_content

if __name__ == "__main__":
    prepare_page(111, "jasa-sumur-bor-kudus", r"C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\139\output.txt")
    prepare_page(7218, "jasa-sondir-kudus", r"C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\157\output.txt")
    prepare_page(3073, "sumur-bor-industri-kitb-batang", r"C:\Users\Reyha\.gemini\antigravity\brain\a66ab4d7-378d-445a-9cef-1b3e4d2c4ead\.system_generated\steps\173\output.txt")
