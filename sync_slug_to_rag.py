import json

with open("rag_knowledge_base/mappings/unified_queue.json", "r", encoding="utf-8") as f:
    queue = json.load(f)

full_map = {}
for item in queue:
    slug = item["slug"]
    folder_clean = item["rag_folder"].replace("database/", "")
    parts = folder_clean.split("/")
    prov_dir = parts[0]
    reg_dir = parts[1] if len(parts) > 1 else parts[0]
    
    full_map[slug] = {
        "page_id": item["id"],
        "type": item["type"],
        "title": item["title"],
        "service": item["service"],
        "province_dir": prov_dir,
        "region_dir": reg_dir,
        "rag_folder": item["rag_folder"],
        "is_regional": item["is_regional"]
    }

with open("rag_knowledge_base/mappings/slug_to_rag.json", "w", encoding="utf-8") as f:
    json.dump(full_map, f, indent=2, ensure_ascii=False)

print(f"Updated slug_to_rag.json with {len(full_map)} items with province_dir and region_dir!")
