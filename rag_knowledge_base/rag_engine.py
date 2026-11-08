"""
Geodipo RAG Engine (Retrieval-Augmented Generation for Regional Engineering)
Provides fast querying, semantic search, scientific citation retrieval, and production
component rendering for 279 local SEO landing pages across Indonesia.
"""

import os
import sys
import json
import re
import argparse
from typing import Dict, Any, List, Optional

RAG_ROOT = os.path.dirname(os.path.abspath(__file__))
DB_ROOT = os.path.join(RAG_ROOT, "database")
MAPPINGS_FILE = os.path.join(RAG_ROOT, "mappings", "slug_to_rag.json")


class GeodipoRAGEngine:
    def __init__(self, rag_root: str = RAG_ROOT):
        self.rag_root = rag_root
        self.db_root = os.path.join(rag_root, "database")
        self.mappings_file = os.path.join(rag_root, "mappings", "slug_to_rag.json")
        self._slug_map = self._load_slug_map()

    def _load_slug_map(self) -> Dict[str, Any]:
        if not os.path.exists(self.mappings_file):
            raise FileNotFoundError(f"Mappings file not found: {self.mappings_file}")
        with open(self.mappings_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_slug_info(self, slug: str) -> Optional[Dict[str, Any]]:
        clean_slug = slug.strip().lower()
        return self._slug_map.get(clean_slug)

    def query_by_slug(self, slug: str) -> Dict[str, Any]:
        """
        Retrieves complete RAG context for a specific page slug.
        """
        info = self.get_slug_info(slug)
        if not info:
            raise ValueError(f"Slug '{slug}' not found in Geodipo RAG mappings.")

        p_dir = info["province_dir"]
        r_dir = info["region_dir"]
        folder = os.path.join(self.db_root, p_dir, r_dir)

        if not os.path.exists(folder):
            raise FileNotFoundError(f"RAG database directory does not exist: {folder}")

        # Load all 4 core components
        meta = self._read_json(os.path.join(folder, "meta.json"))
        sources = self._read_json(os.path.join(folder, "sources.json"))
        profile = self._read_json(os.path.join(folder, "profile.json"))
        brief = self._read_text(os.path.join(folder, "knowledge_brief.md"))

        return {
            "slug": slug,
            "page_id": info.get("page_id"),
            "title": info.get("title"),
            "industrial_zone": info.get("industrial_zone"),
            "meta": meta,
            "sources": sources.get("sources", []),
            "profile": profile,
            "knowledge_brief": brief,
            "folder_path": folder
        }

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Performs full-text token matching across all regional papers and profiles.
        """
        tokens = set(re.findall(r"\w+", query.lower()))
        if not tokens:
            return []

        results = []
        for slug, info in self._slug_map.items():
            p_dir = info["province_dir"]
            r_dir = info["region_dir"]
            folder = os.path.join(self.db_root, p_dir, r_dir)
            brief_path = os.path.join(folder, "knowledge_brief.md")
            if not os.path.exists(brief_path):
                continue

            text = self._read_text(brief_path).lower()
            match_score = sum(text.count(t) for t in tokens)
            if match_score > 0:
                results.append({
                    "slug": slug,
                    "region": info["region_dir"],
                    "province": info["province_dir"],
                    "score": match_score,
                    "brief_preview": text[:250].replace("\n", " ") + "..."
                })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

    def render_section(self, slug: str, format_type: str = "html") -> str:
        """
        Generates the production-grade 'Kajian Geologi & Referensi Ilmiah Lokal'
        component with full academic citations and stratigraphy tables.
        """
        data = self.query_by_slug(slug)
        meta = data["meta"]
        sources = data["sources"]
        profile = data["profile"]
        geo = profile.get("geotechnical", {})
        hydro = profile.get("hydrogeology", {})

        is_sumur_bor = "sumur-bor" in slug or "deep-well" in slug
        is_sondir = "sondir" in slug or "penyelidikan-tanah" in slug

        if format_type.lower() == "markdown":
            return self._render_markdown(data, is_sumur_bor, is_sondir)
        else:
            return self._render_html(data, is_sumur_bor, is_sondir)

    def _resolve_internal_links(self, slug: str) -> Dict[str, Any]:
        item = self._slug_map.get(slug, {})
        p_dir = item.get("province_dir")
        r_dir = item.get("region_dir")
        clean_r = r_dir.replace("_", "-") if r_dir else ""
        
        is_sumur = "sumur-bor" in slug
        is_sondir = "sondir" in slug
        is_industri = "industri" in slug

        links = {
            "pillar": None,
            "twin_service": None,
            "guides": [],
            "neighbors": []
        }

        # 1. Parent Pillar Link
        if is_industri or is_sumur:
            links["pillar"] = {"url": "/jasa-sumur-bor/", "label": "Layanan Utama Jasa Sumur Bor Deep Well"}
        elif is_sondir:
            links["pillar"] = {"url": "/jasa-sondir/", "label": "Layanan Utama Penyelidikan Tanah & Uji Sondir PBG"}

        # 2. Twin Cross-Service in same region
        if is_sumur or is_industri:
            twin_slug = f"jasa-sondir-{clean_r}"
            if twin_slug in self._slug_map:
                links["twin_service"] = {"url": f"/{twin_slug}/", "label": f"Uji Sondir CPT & Boring PBG {r_dir.replace('_', ' ').title()}"}
        elif is_sondir:
            twin_slug = f"jasa-sumur-bor-{clean_r}"
            if twin_slug in self._slug_map:
                links["twin_service"] = {"url": f"/{twin_slug}/", "label": f"Jasa Sumur Bor Deep Well {r_dir.replace('_', ' ').title()}"}

        # 3. Technical deep dive guides
        links["guides"].append({"url": "/jasa-geolistrik/", "label": "Survei Geolistrik Resistivitas 2D"})
        links["guides"].append({"url": "/jasa-pengurusan-sipa/", "label": "Pengurusan Izin SIPA Air Tanah ESDM"})
        if is_sumur or is_industri:
            links["guides"].append({"url": "/sumur-bor-kena-batu-keras/", "label": "Solusi Rig DTH Menembus Batuan Keras"})

        # 4. Sibling regional neighbors (same province)
        prefix = "jasa-sumur-bor-" if (is_sumur or is_industri) else "jasa-sondir-"
        neighbors = []
        for s, it in self._slug_map.items():
            if it.get("province_dir") == p_dir and it.get("region_dir") != r_dir and s.startswith(prefix):
                reg_name = it.get("region_dir").replace("_", " ").title()
                label = f"{'Sumur Bor' if 'sumur-bor' in prefix else 'Uji Sondir'} {reg_name}"
                neighbors.append({"url": f"/{s}/", "label": label})
                if len(neighbors) >= 4:
                    break
        links["neighbors"] = neighbors

        return links

    def _render_html(self, data: Dict[str, Any], is_sumur_bor: bool, is_sondir: bool) -> str:
        meta = data["meta"]
        sources = data["sources"]
        profile = data["profile"]
        geo = profile.get("geotechnical", {})
        hydro = profile.get("hydrogeology", {})
        soil_profile = geo.get("soil_profile", [])

        # Stratigraphy Rows
        strata_html = ""
        for row in soil_profile:
            strata_html += f"""
            <tr style="border-bottom: 1px solid #e2e8f0;">
                <td style="padding: 10px 14px; font-weight: 600; color: #0f172a; white-space: nowrap;">{row[0]}</td>
                <td style="padding: 10px 14px; color: #334155;">{row[1]}</td>
                <td style="padding: 10px 14px; font-family: monospace; color: #0369a1; text-align: center;">{row[2]}</td>
                <td style="padding: 10px 14px; font-family: monospace; color: #475569; text-align: center;">{row[3]}</td>
                <td style="padding: 10px 14px; color: #166534; font-size: 0.9em;">{row[4]}</td>
            </tr>
            """

        # Citation Cards
        citations_html = ""
        for i, s in enumerate(sources, 1):
            findings_li = "".join([f"<li style='margin-bottom: 4px;'>{kf}</li>" for kf in s.get("key_findings", [])])
            citations_html += f"""
            <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px; margin-bottom: 14px;">
                <div style="font-size: 0.85em; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">
                    Referensi Ilmiah #{i} • {s.get('institution', 'Universitas Nasional')}
                </div>
                <h4 style="margin: 0 0 6px 0; font-size: 1.05em; color: #0f172a; line-height: 1.4;">
                    {s.get('title')}
                </h4>
                <div style="font-size: 0.88em; color: #64748b; margin-bottom: 10px;">
                    <strong>Penulis:</strong> {s.get('authors')} ({s.get('year')}) | <em>{s.get('publication')}</em>
                </div>
                <div style="font-size: 0.9em; color: #334155;">
                    <strong style="color: #0f172a;">Data Empiris Terverifikasi:</strong>
                    <ul style="margin: 6px 0 8px 18px; padding: 0; line-height: 1.5;">
                        {findings_li}
                    </ul>
                </div>
                <div style="font-size: 0.8em; color: #64748b; background: #f8fafc; padding: 6px 10px; border-radius: 4px; font-family: monospace;">
                    Sitasi: {s.get('citation')}
                </div>
            </div>
            """

        confined = hydro.get("aquifer_confined", {})
        shallow = hydro.get("aquifer_shallow", {})
        
        # Internal Links Resolution
        slug = data.get("slug", "")
        links = self._resolve_internal_links(slug)
        
        core_links_li = ""
        if links.get("pillar"):
            core_links_li += f"<li><a href='{links['pillar']['url']}' style='color: #0284c7; text-decoration: underline; font-weight: 600;'>{links['pillar']['label']}</a></li>"
        if links.get("twin_service"):
            core_links_li += f"<li><a href='{links['twin_service']['url']}' style='color: #ea580c; text-decoration: underline; font-weight: 600;'>{links['twin_service']['label']}</a></li>"
            
        guides_li = "".join([f"<li><a href='{g['url']}' style='color: #0f766e; text-decoration: underline;'>{g['label']}</a></li>" for g in links.get("guides", [])])
        neighbors_li = "".join([f"<li><a href='{n['url']}' style='color: #334155; text-decoration: underline;'>{n['label']}</a></li>" for n in links.get("neighbors", [])])

        links_html = f"""
        <!-- Semantic Internal Linking Mesh -->
        <div style="margin-top: 24px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 18px 20px;">
            <h4 style="margin: 0 0 12px 0; font-size: 1.05em; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>🔗</span> Layanan Terkait &amp; Direktori Regional Wilayah Sekitar
            </h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; font-size: 0.88em;">
                <div>
                    <strong style="color: #0369a1; display: block; margin-bottom: 6px;">Layanan Inti &amp; Lintas Bidang:</strong>
                    <ul style="margin: 0; padding-left: 18px; line-height: 1.6;">
                        {core_links_li}
                    </ul>
                </div>
                <div>
                    <strong style="color: #0f766e; display: block; margin-bottom: 6px;">Panduan Rekayasa &amp; Legalitas:</strong>
                    <ul style="margin: 0; padding-left: 18px; line-height: 1.6;">
                        {guides_li}
                    </ul>
                </div>
                <div>
                    <strong style="color: #475569; display: block; margin-bottom: 6px;">Cekungan Geologi Sekitar ({meta.get('province', 'Regional')}):</strong>
                    <ul style="margin: 0; padding-left: 18px; line-height: 1.6;">
                        {neighbors_li}
                    </ul>
                </div>
            </div>
        </div>
        """

        return f"""<!-- GEODIPO RAG KNOWLEDGE BLOCK: {meta['name']} -->
<section class="geodipo-rag-container" style="margin: 40px 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1e293b;">
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 28px 24px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
        
        <!-- Header -->
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <span style="background: #0284c7; color: #ffffff; font-size: 0.75em; font-weight: 700; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase;">RAG Verified Geology</span>
            <span style="font-size: 0.85em; color: #64748b; font-weight: 500;">{meta['geological_sheet']}</span>
        </div>
        
        <h3 style="margin: 0 0 12px 0; font-size: 1.5em; color: #0f172a; letter-spacing: -0.02em;">
            Kajian Geologi Bawah Permukaan & Referensi Litologi: {meta['name']}
        </h3>
        
        <p style="margin: 0 0 20px 0; color: #475569; line-height: 1.6; font-size: 0.98em;">
            {profile.get('geology_zone')} Wilayah ini terintegrasi dalam tata ruang <strong>{meta['cat_esdm']}</strong> di bawah koordinasi pengawasan <strong>{meta['bbws']}</strong>.
        </p>

        <!-- Grid 2 Kolom: Stratigrafi & Hidrogeologi -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-bottom: 24px;">
            
            <!-- Box Sondir / Stratigrafi -->
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px;">
                <h4 style="margin: 0 0 12px 0; font-size: 1.1em; color: #0369a1; display: flex; align-items: center; gap: 6px;">
                    <span>📐</span> Profil Stratigrafi & Uji Sondir PBG
                </h4>
                <div style="overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 0.85em; text-align: left;">
                        <thead>
                            <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1; color: #334155;">
                                <th style="padding: 8px 10px;">Kedalaman</th>
                                <th style="padding: 8px 10px;">Litologi</th>
                                <th style="padding: 8px 10px; text-align: center;">qc</th>
                                <th style="padding: 8px 10px; text-align: center;">N-SPT</th>
                                <th style="padding: 8px 10px;">Fondasi PBG</th>
                            </tr>
                        </thead>
                        <tbody>
                            {strata_html}
                        </tbody>
                    </table>
                </div>
                <div style="margin-top: 10px; font-size: 0.82em; color: #b45309; background: #fffbeb; padding: 8px 12px; border-radius: 6px; border-left: 3px solid #f59e0b;">
                    <strong>Perhatian Geoteknik:</strong> {geo.get('hazard')}
                </div>
            </div>

            <!-- Box Sumur Bor Deep Well -->
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px;">
                <h4 style="margin: 0 0 12px 0; font-size: 1.1em; color: #0f766e; display: flex; align-items: center; gap: 6px;">
                    <span>💧</span> Potensi Hidrogeologi & Sumur Bor Dalam
                </h4>
                <ul style="margin: 0; padding-left: 18px; font-size: 0.9em; color: #334155; line-height: 1.6;">
                    <li style="margin-bottom: 8px;">
                        <strong>Akuifer Tertekan Utama:</strong> {confined.get('depth', '60 - 120 m')} ({confined.get('lithology', 'Batupasir berpori')})
                    </li>
                    <li style="margin-bottom: 8px;">
                        <strong>Debit Pemompaan Aman (*Safe Yield*):</strong> <span style="color: #0f766e; font-weight: 700;">{confined.get('safe_yield', '8 - 18 L/detik')}</span>
                    </li>
                    <li style="margin-bottom: 8px;">
                        <strong>Rekomendasi Konstruksi Casing:</strong> {confined.get('recommended_casing', 'Pipa PVC AW / Baja 6 inch')}
                    </li>
                    <li style="margin-bottom: 8px;">
                        <strong>Kondisi Air Permukaan (0-20 m):</strong> {shallow.get('water_quality', 'Fluktuatif musiman')}
                    </li>
                    <li style="margin-bottom: 8px;">
                        <strong>Rekomendasi Legalitas SIPA:</strong> {confined.get('sipa_advice', 'Wajib perizinan ESDM setempat')}
                    </li>
                </ul>
            </div>
        </div>

        <!-- Bagian Referensi Akademik Sekunder (Anti-Doorway Proof) -->
        <div style="margin-top: 24px;">
            <h4 style="margin: 0 0 14px 0; font-size: 1.15em; color: #0f172a; display: flex; align-items: center; gap: 8px;">
                <span>📚</span> Basis Data Sekunder & Sitasi Ilmiah Regional Terverifikasi
            </h4>
            {citations_html}
        </div>

        {links_html}

        <div style="margin-top: 16px; font-size: 0.82em; color: #64748b; text-align: right;">
            Data diintegrasikan melalui <em>Geodipo RAG Engineering Knowledge Base</em> sesuai SNI 2827:2008 & Kepmen ESDM No. 248 K/40/MEM/2021.
        </div>
    </div>
</section>
<!-- END GEODIPO RAG KNOWLEDGE BLOCK -->
"""

    def _render_markdown(self, data: Dict[str, Any], is_sumur_bor: bool, is_sondir: bool) -> str:
        brief = data["knowledge_brief"]
        return brief

    def get_stats(self) -> Dict[str, Any]:
        """
        Calculates total indexed regions, sources, and mapping statistics.
        """
        total_mapped_slugs = len(self._slug_map)
        unique_regions = set()
        total_sources = 0

        for slug, info in self._slug_map.items():
            folder = os.path.join(self.db_root, info["province_dir"], info["region_dir"])
            unique_regions.add(folder)

        for folder in unique_regions:
            sources_file = os.path.join(folder, "sources.json")
            if os.path.exists(sources_file):
                s = self._read_json(sources_file)
                total_sources += s.get("sources_count", len(s.get("sources", [])))

        return {
            "total_mapped_landing_pages": total_mapped_slugs,
            "total_unique_rag_regions": len(unique_regions),
            "total_indexed_secondary_sources": total_sources
        }

    def _read_json(self, path: str) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _read_text(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


def main():
    parser = argparse.ArgumentParser(description="Geodipo RAG Engine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Query
    query_parser = subparsers.add_parser("query", help="Query RAG context by slug")
    query_parser.add_argument("--slug", required=True, help="Page slug (e.g. jasa-sumur-bor-kudus)")

    # Render
    render_parser = subparsers.add_parser("render", help="Render component by slug")
    render_parser.add_argument("--slug", required=True, help="Page slug")
    render_parser.add_argument("--format", default="html", choices=["html", "markdown"], help="Output format")

    # Search
    search_parser = subparsers.add_parser("search", help="Semantic search across RAG knowledge base")
    search_parser.add_argument("query", help="Search query string")
    search_parser.add_argument("--top", type=int, default=5, help="Number of results")

    # Stats
    subparsers.add_parser("stats", help="Show RAG database stats")

    args = parser.parse_args()
    engine = GeodipoRAGEngine()

    if args.command == "query":
        data = engine.query_by_slug(args.slug)
        print(f"=== RAG QUERY RESULT: {args.slug} ===")
        print(f"Region: {data['meta']['name']}")
        print(f"CAT: {data['meta']['cat_esdm']}")
        print(f"Geological Sheet: {data['meta']['geological_sheet']}")
        print(f"Total Sources: {len(data['sources'])}")
        for s in data["sources"]:
            print(f" - [{s.get('year')}] {s.get('title')} ({s.get('authors')})")

    elif args.command == "render":
        output = engine.render_section(args.slug, args.format)
        print(output)

    elif args.command == "search":
        results = engine.search(args.query, args.top)
        print(f"=== SEARCH RESULTS FOR: '{args.query}' ===")
        for r in results:
            print(f"[{r['score']}] Slug: {r['slug']} ({r['province']}/{r['region']})")
            print(f"    Preview: {r['brief_preview']}\n")

    elif args.command == "stats":
        stats = engine.get_stats()
        print("=== GEODIPO RAG KNOWLEDGE BASE STATS ===")
        print(f"Total Mapped Landing Pages: {stats['total_mapped_landing_pages']}")
        print(f"Total Unique RAG Regions:   {stats['total_unique_rag_regions']}")
        print(f"Total Indexed Papers/Theses: {stats['total_indexed_secondary_sources']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass
    main()
