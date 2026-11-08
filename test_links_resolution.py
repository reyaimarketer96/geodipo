import json

with open('rag_knowledge_base/mappings/slug_to_rag.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

def get_internal_links(slug):
    item = mapping.get(slug, {})
    p_dir = item.get('province_dir')
    r_dir = item.get('region_dir')
    clean_r = r_dir.replace("_", "-")
    
    is_sumur = "sumur-bor" in slug
    is_sondir = "sondir" in slug
    is_industri = "industri" in slug
    
    links = {
        "pillar": None,
        "twin_service": None,
        "deep_dive_guides": [],
        "neighbors": []
    }
    
    # 1. Parent Pillar
    if is_industri or is_sumur:
        links["pillar"] = {"url": "/jasa-sumur-bor/", "title": "Pilar Utama Jasa Sumur Bor Deep Well"}
    elif is_sondir:
        links["pillar"] = {"url": "/jasa-sondir/", "title": "Pilar Utama Penyelidikan Tanah & Uji Sondir PBG"}

    # 2. Twin Cross-Service in same region
    if is_sumur:
        twin_slug = f"jasa-sondir-{clean_r}"
        if twin_slug in mapping:
            links["twin_service"] = {"url": f"/{twin_slug}/", "title": f"Uji Sondir & Boring SPT {r_dir.title()} (Syarat PBG)"}
    elif is_sondir:
        twin_slug = f"jasa-sumur-bor-{clean_r}"
        if twin_slug in mapping:
            links["twin_service"] = {"url": f"/{twin_slug}/", "title": f"Jasa Sumur Bor Deep Well {r_dir.title()}"}

    # 3. Technical deep dive guides
    links["deep_dive_guides"].append({"url": "/jasa-geolistrik/", "title": "Survei Geolistrik Resistivitas 2D"})
    links["deep_dive_guides"].append({"url": "/jasa-pengurusan-sipa/", "title": "Panduan Izin SIPA Air Tanah ESDM"})
    if is_sumur or is_industri:
        links["deep_dive_guides"].append({"url": "/sumur-bor-kena-batu-keras/", "title": "Penetrasi Rig DTH Batuan Keras"})

    # 4. Sibling regional neighbors (same province)
    same_prov_slugs = []
    prefix = "jasa-sumur-bor-" if (is_sumur or is_industri) else "jasa-sondir-"
    for s, it in mapping.items():
        if it.get('province_dir') == p_dir and it.get('region_dir') != r_dir and s.startswith(prefix):
            reg_name = it.get('region_dir').replace('_', ' ').title()
            same_prov_slugs.append({"url": f"/{s}/", "title": f"{prefix.replace('-', ' ').title()} {reg_name}"})
            if len(same_prov_slugs) >= 4:
                break
    links["neighbors"] = same_prov_slugs

    return links

print("Links for jasa-sumur-bor-kudus:")
print(json.dumps(get_internal_links("jasa-sumur-bor-kudus"), indent=2))

print("\nLinks for jasa-sondir-kudus:")
print(json.dumps(get_internal_links("jasa-sondir-kudus"), indent=2))

print("\nLinks for sumur-bor-industri-kitb-batang:")
print(json.dumps(get_internal_links("sumur-bor-industri-kitb-batang"), indent=2))
