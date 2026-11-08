# Audit Menyeluruh Arsitektur & Antarmuka Geodipo.com

Audit ini mendokumentasikan kondisi eksisting infrastruktur WordPress, tata letak antarmuka, struktur URL, performa teknis, dan profil kredibilitas konten situs Geodipo per November 2026.

---

## 1. Profil Infrastruktur & Tumpukan Teknologi (Tech Stack)

| Komponen | Spesifikasi Eksisting | Catatan Analisis Teknis |
| :--- | :--- | :--- |
| **Versi WordPress** | 7.1.3 (Aktif) | Menggunakan rilis modern dengan kapabilitas Full Site Editing (FSE). |
| **Tema Aktif** | **Twenty Twenty-Five** (v1.5) | Tema blok baku WordPress (*Block Theme*). Tidak menggunakan tema anak (*child theme*). Styling kustom diinjeksikan melalui bagian templat `twentytwentyfive//footer` dan blok HTML halaman. |
| **Page Builder** | Elementor v4.3.5 terpasang | **Temuan**: Elementor terpasang namun halaman utama (`page_on_front: 12`) dan mayoritas halaman direktori dibangun menggunakan blok Gutenberg native FSE (`wp:html`, `wp:group`, `wp:paragraph`), bukan kanvas Elementor murni. Hal ini menguntungkan karena memangkas beban JavaScript berlebih. |
| **Caching & Performa** | **LiteSpeed Cache** (v7.9.2) | Konfigurasi cache tingkat server aktif dengan web server LiteSpeed. |
| **SEO & Indeksasi** | **Yoast SEO** (v28.7) + Instant Indexing (Rank Math) | Yoast mengelola peta situs XML (`sitemap_index.xml`), canonical tags, dan meta deskripsi. Plugin Instant Indexing terhubung ke Google Indexing API. |
| **Pelacakan & Analitik** | **Site Kit by Google** (v1.189.0) + Skrip Kustom | Terhubung ke GA4 dan Google Search Console. Skrip konversi WhatsApp kustom tertanam di footer (`geodipo_whatsapp_click`). |
| **Lingkungan PHP** | PHP 8.3.36 | Lingkungan runtime server mutakhir dengan performa eksekusi prima. |

---

## 2. Inventaris URL & Pemetaan Struktur Situs

Berdasarkan audit pangkalan data WordPress, seluruh URL diklasifikasikan ke dalam 5 kelompok struktural:

```
geodipo.com (Total 664 Konten Terindeks)
├── Halaman Statis & Pilar (300 Halaman)
│   ├── [1 URL] Homepage (ID: 12) ── Template: page-no-title
│   ├── [13 URL] Service Detail Core Pillars ── Template: page (Gutenberg)
│   │   ├── /layanan/ (Induk Navigasi)
│   │   ├── /jasa-geolistrik/
│   │   ├── /jasa-sondir/ & /jasa-sondir-dan-boring/
│   │   ├── /jasa-sumur-bor/
│   │   ├── /jasa-pengurusan-sipa/
│   │   ├── /jasa-penyelidikan-tanah/
│   │   ├── /uji-laboratorium-tanah/
│   │   ├── /jasa-uji-cbr/
│   │   ├── /jasa-georadar/
│   │   ├── /jasa-downhole-seismic/
│   │   ├── /kajian-hidrologi/
│   │   ├── /kajian-hidrogeologi/
│   │   └── /jasa-eksplorasi-tambang/
│   ├── [279 URL] Local SEO Landing Pages (Kabupaten/Kota se-Indonesia)
│   │   ├── Klaster Sumur Bor Regional (Jawa Tengah, Jabar, Jatim, DKI, Luar Jawa)
│   │   ├── Klaster Uji Sondir & Boring SPT (PBG/SIMBG PUPR)
│   │   └── Klaster Deep Well Kawasan Industri (Cikarang, Karawang, Gresik, Morowali, dll)
│   ├── [2 URL] Directory Hubs
│   │   ├── /cakupan-wilayah/
│   │   └── /cakupan-wilayah-sondir/
│   └── [2 URL] Trust & Legalitas
│       ├── /tentang-geodipo/
│       └── /kontak/
└── Basis Pengetahuan Edukasi (364 Pos Terbit)
    ├── Panduan Sumur Bor (156 Pos)
    ├── Pengurusan SIPA ESDM (84 Pos)
    ├── Jasa Geolistrik (76 Pos)
    └── Blog & Edukasi Teknik (48 Pos)
```

---

## 3. Masalah Desain & UX Eksisting (Hasil Tangkapan Layar Peramban)

Inspeksi visual peramban pada resolusi 1440px (desktop), 768px (tablet), dan 390px (mobile) menunjukkan 5 kelemahan kritis:

### A. *Oversized Blue Hero Card* (Kotak Biru Raksasa Cembung)
- **Kondisi Eksisting**: Bagian *hero* dibungkus kontainer kartu dengan radius lengkung 20px dan latar belakang gradien radial gelap (`radial-gradient(circle at 85% 15%, #1e3a8a 0%, #0f172a 70%)`).
- **Dampak Negatif**: Tampilan menyerupai template SaaS murah atau *landing page* promosi kilat. Tidak mencerminkan wibawa perusahaan rekayasa geologi dan kontraktor pengeboran air tanah kelas industri.

### B. Kepadatan Teks Ekstrem di Atas Lipatan Layar (*Above the Fold Clutter*)
- **Kondisi Eksisting**: Paragraf pembuka memuat kalimat bertumpuk panjang, 3 poin keunggulan teks padat, 3 tombol tautan, dan widget kalkulator simulasi harga dalam satu layar sempit.
- **Dampak Negatif**: Pengunjung mengalami kelelahan kognitif (*cognitive overload*). Tidak ada satu titik fokus visual (*focal point*) yang memandu mata pembaca.

### C. Ketiadaan Fotografi Operasional Lapangan Riil di Bagian Kritis
- **Kondisi Eksisting**: Di atas lipatan layar sama sekali tidak tampak foto alat berat, rig pengeboran, atau aktivitas teknisi. Di bawah lipatan layar dan halaman layanan, ditemukan penggunaan gambar ilustrasi sintetis AI bertuliskan *"Ilustrasi konseptual, dibuat dengan AI"*.
- **Dampak Negatif**: Menurunkan skor kepercayaan klien teknik (B2B/industri). Klien geoteknik dan pengeboran membutuhkan bukti fisik bahwa Geodipo memiliki armada alat nyata di lapangan Indonesia, bukan perantara fiktif.

### D. Bilah Tombol WhatsApp Mengambang Sangat Intrusif pada Mobile
- **Kondisi Eksisting**: Terdapat bilah hijau terang bertuliskan `✆ Konsultasi Lokasi via WhatsApp` yang menempel permanen di bagian bawah layar ponsel (`position: fixed; z-index: 9999; bottom: 0`).
- **Dampak Negatif**: Bilah setinggi 58px ini menutupi teks bacaan, menghalangi navigasi menu, dan memberikan kesan agresif (*spammy*).

### E. Hirarki Tipografi Lemah & Ketiadaan Identitas Merek Visual
- **Kondisi Eksisting**: Hanya menggunakan font sistem standar (`-apple-system, BlinkMacSystemFont, Segoe UI, Roboto`) tanpa diferensiasi ketebalan yang anggun. Logo header hanya berupa teks hitam polos tanpa simbol atau *treatment* visual teknik.

---

## 4. Evaluasi Konten, Etika Klaim Teknis & Standar Google Information Gain

Sesuai arahan kerja SuperSEO dan integritas ilmiah:
1. **Pemisahan Fakta dan Rekomendasi**:
   - Geolistrik resistivitas (1D VES / 2D ERT) mendeteksi respon tahanan jenis lapisan batuan dan saturasi fluida air. **Bukan jaminan 100% debit air instan**. Klaim seperti *"Anti-Zonk"* harus disempurnakan menjadi bahasa rekayasa presisi: *"Meminimalkan Risiko Kegagalan Pengeboran Berdasarkan Pemetaan Sebaran Resistivitas Akuifer"*.
2. **Kapasitas Rig & Kedalaman**:
   - Penetrasi batuan keras menggunakan armada DTH Hammer pneumatik kompresor bertekanan tinggi (20–25 bar) untuk formasi vulkanik/breksi andesit masif. Hal ini merupakan spesifikasi mekanikal riil yang harus didukung foto operasional asli.
3. **Pemanfaatan Aset Lapangan Orisinal**:
   - Direktori `Aset_Web_Geodipo` menyimpan foto-foto otentik geotag berkoordinat riil di Jawa Tengah (Kudus/Kaliwungu), Riau Sumatera (Tasik Serai Barat), dan Papua (Kampung Bebon Jaya & Gwin Jaya). Aset berharga ini harus diangkat sebagai bukti kerja utama pada portofolio halaman.
