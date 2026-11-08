# Geodipo RAG Engineering Knowledge Base

Sistem basis data terstruktur **Retrieval-Augmented Generation (RAG)** untuk mendukung keunikan konten teknis, sitasi ilmiah sekunder, dan parameter geologi lokal pada **279 Halaman Landing Page Daerah** di situs Geodipo.

---

## 1. Arsitektur Direktori

```
rag_knowledge_base/
├── README.md                           # Dokumentasi & panduan teknis
├── rag_engine.py                       # Mesin pencarian, query, & rendering komponen (CLI & Library)
├── schema/
│   └── region_schema.json              # Validasi JSON Schema untuk struktur data daerah
├── mappings/
│   └── slug_to_rag.json                # Pemetaan 279 slug WordPress ke folder RAG kanonikal
└── database/                           # 128 Folder Regional se-Indonesia
    ├── jawa_tengah/
    │   ├── semarang/                   # [meta.json, sources.json, profile.json, knowledge_brief.md]
    │   ├── kudus/
    │   ├── batang/
    │   ├── kendal/
    │   └── ... (31 kabupaten/kota Jateng)
    ├── jawa_barat/
    │   ├── bekasi/                     # Mencakup Cikarang & 6 kawasan industri besar
    │   ├── karawang/                   # Mencakup KIIC, Suryacipta, KNIC
    │   ├── purwakarta/
    │   └── ... (17 kabupaten/kota Jabar)
    ├── jawa_timur/
    │   ├── surabaya/                   # Mencakup SIER & Margomulyo
    │   ├── gresik/                     # Mencakup JIIPE & Maspion
    │   ├── sidoarjo/
    │   ├── pasuruan/                   # Mencakup PIER Rembang
    │   └── ... (24 kabupaten/kota Jatim)
    ├── banten/
    │   ├── tangerang/                  # Balaraja, Cikupa, Jatake, Manis
    │   ├── tangerang_selatan/          # BSD, Serpong, Pamulang
    │   ├── serang/                     # Cikande Modern & Pancatama
    │   └── cilegon/                    # KIEC Krakatau
    ├── dki_jakarta/
    │   └── jakarta/                    # JIEP Pulogadung & 5 kota administrasi
    ├── di_yogyakarta/
    │   ├── yogyakarta/
    │   ├── sleman/
    │   └── bantul/
    ├── sumatera/
    │   ├── medan/
    │   ├── batam/                      # Batamindo Industrial Park
    │   ├── pekanbaru/
    │   └── ... (12 klaster Sumatera)
    ├── kalimantan/
    │   ├── balikpapan/                 # Kariangau Industrial Zone
    │   ├── ikn_nusantara/              # KIPP IKN Sepaku
    │   ├── samarinda/
    │   └── ... (11 klaster Kalimantan)
    ├── sulawesi/
    │   ├── morowali/                   # IMIP Bahodopi (Smelter RKEF)
    │   ├── makassar/
    │   ├── kendari/
    │   └── ... (7 klaster Sulawesi)
    ├── bali_nusa/
    │   ├── bali/                       # Denpasar, Badung, Gianyar, Nusa Dua
    │   ├── lombok/
    │   └── labuan_bajo/
    └── maluku_papua/
        ├── papua_tengah_timika/        # Area Freeport & Pelabuhan Pomako
        ├── jayapura/
        ├── sorong/
        └── ambon/
```

---

## 2. Struktur 4 Berkas Inti di Setiap Folder Kabupaten

Setiap folder kabupaten di dalam `database/` memiliki 4 berkas baku:

1. **`meta.json`**:
   Data administratif, koordinat geografis, Cekungan Air Tanah (CAT) Kepmen ESDM No. 248 K/40/MEM/2021, Balai Wilayah Sungai (BBWS/BWS PUPR), nama Lembar Peta Geologi P3G/Badan Geologi, dan daftar kawasan industri terafiliasi.

2. **`sources.json`**:
   Kumpulan literatur ilmiah sekunder terverifikasi (jurnal terindeks SINTA/Scopus, skripsi/tesis universitas regional seperti UNDIP, ITB, UGM, ITS, UNHAS, UNPAD, USU, UNCEN, dan publikasi Badan Geologi). Memuat judul penelitian, penulis, tahun, publikasi, temuan empiris kuantitatif, dan teks sitasi baku.

3. **`profile.json`**:
   Data teknis rekayasa bawah permukaan:
   - **Hidrogeologi:** Karakteristik akuifer dangkal (0-20 m), kedalaman akuifer tertekan produktif (*confined deep well*), litologi batuan pembawa air, debit jenis pemompaan aman (*safe yield*), spesifikasi pipa casing & screen, serta rambu-rambu izin SIPA ESDM.
   - **Geoteknik:** Tabel stratigrafi 4 lapis kedalaman tanah, nilai tahanan konus sondir ($q_c$), N-SPT, rekomendasi jenis fondasi untuk persetujuan PBG/SIMBG PUPR, serta mitigasi bahaya lokal (amblesan, likuifaksi, rob).

4. **`knowledge_brief.md`**:
   Ringkasan teknis padat informasi (*Technical Geo-Brief*) yang dirancang khusus untuk konteks model kecerdasan buatan (LLM). Bebas dari klise kata-kata AI (*Anti-AI-slop*), kaya parameter metrik, dan siap disintesis ke halaman landing page.

---

## 3. Cara Penggunaan Mesin RAG (`rag_engine.py`)

### A. Melalui Command Line Interface (CLI)

1. **Cek Statistik Basis Data:**
   ```bash
   python rag_knowledge_base/rag_engine.py stats
   ```

2. **Kueri Data Lengkap Berdasarkan Slug URL:**
   ```bash
   python rag_knowledge_base/rag_engine.py query --slug jasa-sumur-bor-kudus
   ```

3. **Pencarian Semantik / Kata Kunci Litologi:**
   ```bash
   python rag_knowledge_base/rag_engine.py search "intrusi air laut pesisir" --top 5
   python rag_knowledge_base/rag_engine.py search "batuan ultramafik serpentinit DTH hammer"
   ```

4. **Render Komponen HTML Siap Pasang ke Halaman:**
   ```bash
   python rag_knowledge_base/rag_engine.py render --slug sumur-bor-industri-kitb-batang --format html
   ```

### B. Melalui Modul Python (Integrasi Kode)

```python
from rag_knowledge_base.rag_engine import GeodipoRAGEngine

engine = GeodipoRAGEngine()

# Mengambil konteks data RAG untuk injeksi prompt atau generator
context = engine.query_by_slug("jasa-sumur-bor-kudus")
print(context["meta"]["name"])
print(context["sources"][0]["title"])

# Menghasilkan blok HTML rekayasa geologi lokal
html_block = engine.render_section("jasa-sumur-bor-kudus", format_type="html")
```

---

## 4. Keunggulan Terhadap Algoritma Google Information Gain

- **Bukan Template Variabel Kosong:** Tidak sekadar mengganti kata `{{nama_kota}}`. Setiap kabupaten memiliki referensi paper, kedalaman akuifer, dan nilai sondir $q_c$ yang secara ilmiah dan empiris berbeda.
- **Skor OriginalContentScore Maksimal:** Menghadirkan sintesis data sekunder akademik yang tidak ada di situs kontraktor pemboran lain di Indonesia.
- **Kebal Pinalti Doorway Pages:** Menghilangkan risiko duplikasi karena setiap halaman menyajikan pembuktian teknis dan referensi ilmiah independen.
