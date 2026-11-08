import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from rag_knowledge_base.rag_engine import GeodipoRAGEngine

engine = GeodipoRAGEngine()
with open('rag_knowledge_base/mappings/unified_queue.json', 'r', encoding='utf-8') as f:
    queue = json.load(f)

test_indices = [0, 50, 100, 500, 1000, 1500, 1920]
for idx in test_indices:
    item = queue[idx]
    try:
        html = engine.render_section(item['slug'], format_type='html')
        print(f"Queue [{idx}] ID {item['id']} ({item['slug']}) -> SUCCESS: Rendered {len(html)} chars HTML")
    except Exception as e:
        print(f"Queue [{idx}] ID {item['id']} ERROR: {e}")
