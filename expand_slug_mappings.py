import json
import os

with open("rag_knowledge_base/mappings/regency_map.json", "r", encoding="utf-8") as f:
    regency_map = json.load(f)

with open("audit/raw_all_posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

with open("audit/raw_all_pages.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

with open("rag_knowledge_base/mappings/slug_to_rag.json", "r", encoding="utf-8") as f:
    existing_page_map = json.load(f)

# Discover existing RAG folders
db_root = "rag_knowledge_base/database"
existing_rag_folders = set()
for prov in os.listdir(db_root):
    p_path = os.path.join(db_root, prov)
    if os.path.isdir(p_path):
        for reg in os.listdir(p_path):
            existing_rag_folders.add(f"database/{prov}/{reg}")

print(f"Existing physical RAG folders: {len(existing_rag_folders)}")

def clean_slug_to_regency(slug):
    s = slug.lower().replace("-", "_")
    prefixes = [
        "jasa_pengurusan_sipa_",
        "pengurusan_sipa_",
        "jasa_geolistrik_",
        "jasa_sumur_bor_",
        "jasa_sondir_",
        "sumur_bor_industri_",
        "sumur_bor_",
        "cara_mengatasi_",
        "biaya_sumur_bor_",
        "air_sumur_bor_"
    ]
    for pfx in prefixes:
        if s.startswith(pfx):
            s = s[len(pfx):]
            break
    # strip trailing numbers or words if needed
    return s

def resolve_rag_folder(slug, title, is_article):
    if is_article:
        return "database/nasional/standar_geoteknik_indonesia", False
        
    cleaned = clean_slug_to_regency(slug)
    
    # 1. Direct match in regency_map
    if cleaned in regency_map:
        prov, reg = regency_map[cleaned]
        cand = f"database/{prov}/{reg}"
        if cand in existing_rag_folders:
            return cand, True
        else:
            return f"database/{prov}/{reg}", True

    # 2. Check if any regency key is a substring of cleaned or vice versa
    # prioritize longer matches
    sorted_keys = sorted(regency_map.keys(), key=lambda x: len(x), reverse=True)
    for k in sorted_keys:
        if len(k) >= 4 and (k in cleaned or cleaned in k):
            prov, reg = regency_map[k]
            return f"database/{prov}/{reg}", True

    # 3. Check title
    title_lower = title.lower().replace(" ", "_")
    for k in sorted_keys:
        if len(k) >= 4 and k in title_lower:
            prov, reg = regency_map[k]
            return f"database/{prov}/{reg}", True

    return "database/nasional/standar_geoteknik_indonesia", False

unified_queue = []
regional_count = 0
guide_count = 0

# Process posts
for p in posts:
    post_id = p["id"]
    slug = p["slug"]
    title = p["title"]["rendered"]
    cats = p.get("categories", [])
    
    is_article = False
    if any(c in [4, 5, 1] for c in cats):
        if not any(slug.startswith(pfx) for pfx in ["jasa-", "pengurusan-", "sumur-bor-"]):
            is_article = True

    if "geolistrik" in slug:
        service = "geolistrik"
    elif "sipa" in slug:
        service = "sipa"
    elif "sumur" in slug:
        service = "sumur_bor"
    elif "sondir" in slug or "spt" in slug:
        service = "sondir_spt"
    else:
        service = "guide" if is_article else "geolistrik"

    rag_folder, is_reg = resolve_rag_folder(slug, title, is_article)
    if is_reg:
        regional_count += 1
    else:
        guide_count += 1

    unified_queue.append({
        "id": post_id,
        "type": "post",
        "slug": slug,
        "title": title,
        "service": service,
        "rag_folder": rag_folder,
        "is_regional": is_reg
    })

# Process pages
for pg in pages:
    page_id = pg["id"]
    slug = pg["slug"]
    title = pg["title"]["rendered"]
    
    if slug in existing_page_map:
        rag_folder = existing_page_map[slug].get("rag_folder")
        is_reg = True
        regional_count += 1
    else:
        rag_folder, is_reg = resolve_rag_folder(slug, title, False)
        if is_reg:
            regional_count += 1
        else:
            guide_count += 1

    unified_queue.append({
        "id": page_id,
        "type": "page",
        "slug": slug,
        "title": title,
        "service": "sondir_spt" if "sondir" in slug else "sumur_bor",
        "rag_folder": rag_folder,
        "is_regional": is_reg
    })

print(f"\nTotal Unified Queue: {len(unified_queue)} items")
print(f"Regional Target Pages (Enriched with Local Geology): {regional_count}")
print(f"Technical Guides & National Standards: {guide_count}")

with open("rag_knowledge_base/mappings/unified_queue.json", "w", encoding="utf-8") as f:
    json.dump(unified_queue, f, indent=2, ensure_ascii=False)
print("Saved unified queue to rag_knowledge_base/mappings/unified_queue.json")
