# Laporan Implementasi URL-by-URL & Proteksi Arsitektur SEO Geodipo

Dokumen ini memetakan seluruh 300 URL halaman aktif di WordPress `geodipo.com` ke dalam arsitektur desain baru. Tujuannya adalah menjamin nol kehilangan peringkat Google (*zero ranking drop*), integritas kanonikal 100%, perlindungan struktur permalink, dan kepatuhan penuh terhadap standar *Information Gain* Google 2026.

---

## 1. Ringkasan Eksekutif Sensus URL (Total 300 Halaman)

| Kategori Halaman | Total Halaman | Template Target Geodipo Design System | Tingkat Prioritas SEO | Perlindungan Teknis |
| :--- | :---: | :--- | :--- | :--- |
| **Homepage Utama** | 1 | `page-no-title` (Custom Engineering Layout) | **Tier 1 — Critical** | Slug `/`, ID: 12, canonical root |
| **Service Detail Pages (Pilar)** | 13 | `single-service` (Technical Editorial) | **Tier 1 — Core Pillar** | Slug statis, skema Service + FAQPage |
| **Local SEO Landing Pages (Spoke)** | 279 | `single-location` (Litologi Regional & GIS) | **Tier 1 — High (Transaksional)** | Zero slug change, skema LocalBusiness |
| **Directory & Archive Hubs** | 2 | `page-directory` (Index Wilayah & CAT) | **Tier 2 — High (Navigasi)** | Silo internal link hub-and-spoke |
| **Educational & Guide Pages** | 3 | `page-editorial` (Long-form Technical) | **Tier 2 — Otoritas Informasi** | Breadcrumb list, infografis teknis |
| **Company & Contact Pages** | 2 | `page-company` (Trust, Legalitas & Kontak) | **Tier 2 — Kepercayaan & E-E-A-T** | Legalitas ESDM, NPWP, NIB, Peta Kantor |
| **Total Keseluruhan** | **300** | **6 Arketipe Template Terpadu** | — | **100% URL Terproteksi** |

---

## 2. Pemetaan Komprehensif Berdasarkan Template & Kategori

### A. Homepage (1 URL — Tier 1 Critical)
* **URL:** `https://geodipo.com/` (ID: 12)
* **Status Indeks:** Terindeks kuat untuk kata kunci brand dan kata kunci payung industri.
* **Perlindungan Slug:** Tetap root (`/`). Tidak boleh ada pengalihan 301 ke subfolder.
* **Metadata & Skema:**
  * Title: `Geodipo | Jasa Geolistrik, Sumur Bor Deep Well & Penyelidikan Tanah PBG`
  * Meta Description: `Layanan rekayasa kebumian: survei geolistrik resistivitas 2D, pengeboran sumur bor industri tembus batu 200m, uji tanah sondir CPT PBG, dan izin SIPA ESDM.`
  * JSON-LD: `Organization`, `WebSite`, `LocalBusiness`, `FAQPage`.
* **Protokol Implementasi:** Validasi di draft staging terlebih dahulu. Penggantian blok `<!-- wp:html -->` di Page ID 12 dilakukan hanya setelah persetujuan tertulis pengguna.

---

### B. Core Service Pillars (13 Halaman — Tier 1 Core Pillar)
Halaman pilar ini berfungsi sebagai pusat otoritas semantik (*semantic hub*) untuk setiap disiplin rekayasa. Seluruh *local landing pages* menginduk (*link up*) ke halaman-halaman ini.

| ID | Slug URL | Judul Layanan | Keyword Target Utama | Skema JSON-LD |
| :---: | :--- | :--- | :--- | :--- |
| 6861 | `/jasa-geolistrik/` | Jasa Geolistrik Resistivitas 2D | Jasa Geolistrik, Pemetaan Akuifer Air Tanah | `Service`, `FAQPage` |
| 6860 | `/jasa-sondir/` | Jasa Sondir CPT & Boring SPT | Jasa Sondir Tanah, Uji PBG, Cone Penetration | `Service`, `FAQPage` |
| 6862 | `/jasa-sumur-bor/` | Jasa Pengeboran Sumur Bor Deep Well | Jasa Sumur Bor, Pengeboran Air Bersih | `Service`, `FAQPage` |
| 6858 | `/jasa-pengurusan-sipa/` | Pengurusan Izin SIPA Air Tanah ESDM | Jasa Izin SIPA, Pemanfaatan Air Tanah OSS | `Service`, `GovernmentService` |
| 6857 | `/jasa-georadar-gpr/` | Jasa Pemetaan Georadar GPR | Jasa Georadar GPR, Deteksi Pipa Bawah Tanah | `Service`, `FAQPage` |
| 6856 | `/jasa-seismik-refraksi/` | Jasa Seismik Refraksi | Uji Seismik Refraksi, Gelombang Geser Vs30 | `Service`, `FAQPage` |
| 6855 | `/jasa-topografi/` | Jasa Pengukuran Topografi & Drone LiDAR | Pengukuran Topografi Total Station, Peta Kontur | `Service`, `FAQPage` |
| 6854 | `/jasa-downhole-seismic/` | Jasa Uji Downhole Seismic (PS Logging) | Uji Downhole Seismic, Analisis Dinamika Tanah | `Service`, `FAQPage` |
| 6853 | `/jasa-uji-pit-pet/` | Jasa Uji Integritas Tiang PIT & PET | Pile Integrity Test, Uji Fondasi Tiang Pancang | `Service`, `FAQPage` |
| 6852 | `/jasa-uji-pda/` | Jasa Uji Beban Dinamis Tiang PDA | Pile Driving Analyzer, Daya Dukung Fondasi | `Service`, `FAQPage` |
| 6851 | `/jasa-cbr-lapangan/` | Jasa Pengujian CBR Lapangan & DCP | California Bearing Ratio, Daya Dukung Subgrade Jalan | `Service`, `FAQPage` |
| 6850 | `/jasa-plate-bearing-test/` | Jasa Pengujian Plate Bearing Test | Plate Bearing Test, Modulus Reaksi Subgrade | `Service`, `FAQPage` |
| 6849 | `/jasa-laboratorium-mekanika-tanah/` | Jasa Laboratorium Mekanika Tanah | Uji Lab Mektan, Triaxial, Atterberg Limit, Direct Shear | `Service`, `FAQPage` |

* **Aturan Khusus Pilar:**
  1. Hapus gambar ilustrasi sintetis AI generik (`geodipo-sondir-ilustrasi-ai.jpg`, dll.) dan gantikan dengan dokumentasi alat lapangan nyata (misal: mesin sondir Dutch Cone Penetrometer 2.5 ton terkalibrasi, geolistrik SuperSting R8 / Multichannel OYO, alat bor hidraulik spindle).
  2. Tambahkan tabel parameter keluaran teknis (*deliverables*), lembar log bor resmi, dan sampel grafik perlawanan konus (*qc*) vs kedalaman.

---

### C. Local SEO Landing Pages (279 Halaman — Tier 1 High Local Rankings)
Sebanyak 279 URL halaman lokasi ditargetkan untuk mendominasi pencarian transaksional lokal di tingkat kota dan kabupaten di Indonesia (Jawa, Sumatera, Kalimantan, Sulawesi, Bali, Nusa Tenggara, hingga Papua).

#### Distribusi Wilayah Geografis:
1. **Klaster Jabodetabek & Banten (24 URL):**
   * Jakarta: `/jasa-sumur-bor-jakarta/`, `/jasa-sondir-jakarta/`, `/jasa-geolistrik-jakarta/`, dst.
   * Bogor, Depok, Tangerang, Tangerang Selatan, Bekasi, Cikarang.
   * Serang, Cilegon, Pandeglang, Lebak.
2. **Klaster Jawa Barat (38 URL):**
   * Bandung Raya: `/jasa-sumur-bor-bandung/`, `/jasa-sondir-bandung/`, Cimahi, Bandung Barat.
   * Karawang, Purwakarta, Subang, Indramayu, Cirebon, Majalengka, Kuningan.
   * Sukabumi, Cianjur, Tasikmalaya, Garut, Ciamis, Banjar, Pangandaran.
3. **Klaster Jawa Tengah & D.I. Yogyakarta (46 URL):**
   * D.I. Yogyakarta: `/jasa-sumur-bor-jogja/`, Sleman, Bantul, Kulon Progo, Gunungkidul.
   * Semarang Raya: `/jasa-sumur-bor-semarang/`, Ungaran, Kendal, Demak.
   * Solo Raya: Surakarta, Sukoharjo, Karanganyar, Klaten, Boyolali, Wonogiri, Sragen.
   * Karesidenan Banyumas: Purwokerto, Banyumas, Cilacap, Purbalingga, Banjarnegara.
   * Pantura: Kudus, Pati, Jepara, Rembang, Pekalongan, Batang (KITB), Tegal, Brebes.
4. **Klaster Jawa Timur & Bali (52 URL):**
   * Surabaya Raya: `/jasa-sumur-bor-surabaya/`, Sidoarjo, Gresik (JIIPE).
   * Malang Raya: Kota Malang, Kab Malang, Batu.
   * Pasuruan (PIER), Mojokerto, Jombang, Kediri, Blitar, Tulungagung.
   * Probolinggo, Pasuruan, Jember, Banyuwangi, Situbondo, Bondowoso, Tuban, Lamongan, Madiun.
   * Bali: Denpasar, Badung, Gianyar, Tabanan, Buleleng.
5. **Klaster Luar Jawa — Sumatera, Kalimantan, Sulawesi, Papua (119 URL):**
   * Sumatera: Medan, Deli Serdang, Palembang, Pekanbaru, Batam, Padang, Bandar Lampung, Jambi, Bengkulu, Banda Aceh.
   * Kalimantan: Balikpapan (IKN), Samarinda, Banjarmasin, Banjarbaru, Pontianak, Palangkaraya, Tarakan.
   * Sulawesi: Makassar (KIMA), Gowa, Maros, Palu, Manado, Kendari, Gorontalo, Bitung.
   * Papua & Maluku: Jayapura, Timika, Sorong, Ambon.

#### Perlindungan Anti-Doorway Page (Standar Google Patent 2024 & SuperSEO):
Untuk mencegah sanksi *Scaled Content Abuse* Google terhadap 279 halaman ini:
* **Larangan:** Dilarang menggunakan *template copy-paste* yang hanya mengganti nama kota (misal: "Kami melayani jasa sumur bor di [Kota] dengan harga termurah...").
* **Kewajiban Konten Proprieter Lapangan (*OriginalContentScore*):**
  1. **Litologi Spesifik Kota/Kabupaten:** Setiap halaman wajib memuat kondisi geologi bawah tanah lokal (contoh: formasi batuan andesit vulkanik di Ungaran/Bandung, salinitas air payau aluvial pesisir di Demak/Jakarta Utara, tanah lempung ekspansif di Bojonegoro, atau lapisan gambut asam di Riau/Kalbar).
  2. **Regulasi Air Tanah Lokal:** Rujukan Balai Wilayah Sungai (BWS) atau Dinas ESDM provinsi terkait dan status zona konservasi air tanah setempat.
  3. **Logistik Lapangan & Base Mobilisasi:** Informasi rute mobilisasi rig bor dan estimasi durasi mobilisasi kru dari pool terdekat.

---

### D. Directory & Region Archives (2 Halaman — Tier 2 High Navigasi)
* `/cakupan-wilayah/` (ID: 7130) — Direktori wilayah layanan jasa sumur bor dan geolistrik nasional.
* `/cakupan-wilayah-sondir/` (ID: 7293) — Direktori wilayah layanan jasa uji sondir CPT dan boring SPT nasional.
* **Peran:** Mengelompokkan seluruh 279 halaman kota ke dalam klaster pulau dan provinsi dengan tata letak tabulasi terstruktur. Mencegah tautan yatim (*orphan pages*) dan menyalurkan *link equity* dari halaman beranda ke halaman spoke regional.

---

### E. Educational & Guide Pages (3 Halaman — Tier 2 Otoritas Informasi)
* `/biaya-sumur-bor/` (ID: 6864) — Panduan estimasi biaya, rincian harga bor per meter, dan simulasi RAB.
* `/pumping-test-sumur-bor/` (ID: 6863) — Panduan uji pemompaan air tanah, *step-drawdown test*, dan analisis kurva Theis/Cooper-Jacob.
* `/kedalaman-sumur-bor/` (ID: 6859) — Panduan penentuan zona kedalaman akuifer dangkal vs akuifer tertekan dalam (*deep well*).
* **Peran:** Menarik pencarian tahap awal (*top-of-funnel*) dari pengguna yang mencari edukasi teknis, kemudian mengarahkan mereka ke pilar layanan terkait melalui *in-text context linking*.

---

### F. Company, About & Contact (2 Halaman — Tier 2 Kepercayaan & E-E-A-T)
* `/tentang-geodipo/` (ID: 6848) — Profil perusahaan, latar belakang sarjana geologi/geofisika, legalitas izin berusaha (NIB, KBLI 71102 / 43120), sertifikasi keahlian HATTI, dan standar K3 alat berat.
* `/kontak/` (ID: 6847) — Saluran konsultasi cepat WhatsApp (`0813-3824-0851`), formulir permintaan proposal teknis/RAB, dan informasi jam operasional tim lapangan.

---

## 3. Matriks Kompatibilitas Tag & Integrasi Pihak Ketiga

| Komponen Integrasi | Status di Situs Saat Ini | Status Setelah Redesain | Tindakan Validasi |
| :--- | :--- | :--- | :--- |
| **Google Site Kit (GA4)** | Aktif (`G-B1FGEESL69`) | **Dipertahankan Utuh** | Pastikan tag terpasang otomatis via plugin resmi Site Kit |
| **Google Search Console** | Terverifikasi via DNS/HTML Tag | **Dipertahankan Utuh** | Verifikasi kepemilikan tidak boleh terganggu |
| **Yoast SEO v28.7** | Aktif, mengelola meta & sitemap | **Dipertahankan Utuh** | XML sitemap (`/sitemap_index.xml`) tetap valid |
| **LiteSpeed Cache v7.9.2** | Aktif, server LiteSpeed | **Dioptimalkan** | Bersihkan cache (*Purge All*) setelah pembaruan CSS |
| **WhatsApp Event Tracking** | Skrip `geodipo_whatsapp_click` | **Ditingkatkan (Non-Intrusif)** | Dipindahkan dari bar lengket bawah ke Floating Action Button (FAB) |

---

## 4. Protokol Peluncuran Bertahap (Staged Deployment Protocol)

Untuk menjamin ketiadaan gangguan pada performa produksi:
1. **Langkah 1 (Selesai):** Pembuatan dan validasi mandiri prototipe responsif `prototype/index.html` dengan nol kesalahan gambar dan nol luapan horizontal.
2. **Langkah 2 (Selesai):** Pencadangan data asli Page ID 12 dan template part footer ke format JSON di `deployment/backups/`.
3. **Langkah 3 (Staging):** Publikasi prototipe ke status **Draft** WordPress menggunakan slug terisolasi (`prototype-beranda-staging`) untuk peninjauan langsung di lingkungan WordPress tanpa mengeksposnya ke publik.
4. **Langkah 4 (Persetujuan Pengguna):** Pengajuan tinjauan visual dan performa kepada pengguna.
5. **Langkah 5 (Produksi Terjadwal):** Setelah persetujuan tertulis diterima, blok `<!-- wp:html -->` pada Page ID 12 diperbarui, skrip footer FSE dimutakhirkan, dan pembersihan cache LiteSpeed dieksekusi secara instan.
