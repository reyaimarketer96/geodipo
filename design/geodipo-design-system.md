# Geodipo Design System: Panduan Identitas Visual & Komponen Teknik

Dokumen ini menetapkan spesifikasi desain resmi untuk perancangan ulang situs Geodipo. Sistem ini dirancang untuk mencerminkan positioning Geodipo sebagai konsultan geosains, geofisika, hidrogeologi, dan kontraktor pengeboran air tanah terkemuka di Indonesia.

---

## 1. Prinsip Desain (*Design Philosophy*)

1. **Rekayasa Industrial Presisi (*Industrial Engineering Aesthetic*)**
   - Menghilangkan estetika SaaS generik (kotak cembung biru, ilustrasi vektor kartun, gradien ungu acak, dan tombol mengambang agresif).
   - Menampilkan wibawa teknis seperti standar tolok ukur global (*Lucas Drilling, Fugro, GeoTech SA*).
2. **Kebenaran Fotografi Lapangan (*Authentic Field Proof*)**
   - Aset visual terkuat adalah dokumentasi operasional riil: teknisi berrompi keselamatan kerja (K3), alat geolistrik resistivitas, rig pengeboran hidraulik, dan foto geotag koordinat lapangan Indonesia (Kudus, Riau, Papua).
   - Banned: Gambar ilustrasi sintetis AI atau foto stok bule yang tidak merefleksikan realitas geologi Indonesia.
3. **Keterbacaan Editorial & Hirarki Tajam**
   - Membatasi panjang kalimat di atas lipatan layar (*above the fold*).
   - Memisahkan fakta saintifik teruji dari estimasi teknis.
4. **Konversi Fungsional Tanpa Spam**
   - Integrasi WhatsApp yang elegan, terarah ke peruntukan proyek (B2B Industri vs B2C Rumah Tangga), tanpa menutupi teks bacaan pada layar ponsel.

---

## 2. Palet Warna Teknik (*Color Palette*)

```
[Deep Basalt]      #0b1522  ── Latar belakang utama hero, header gelap, dan footer
[Technical Slate]  #1e293b  ── Teks judul utama pada latar terang, kontainer kartu sekunder
[Steel Border]     #e2e8f0  ── Garis pembatas grid, garis tabel, dan tepi kartu
[Surface Light]    #f8fafc  ── Latar belakang section berselang-seling, badge teknis
[Safety Amber]     #ea580c  ── Aksen oranye industrial untuk CTA utama (K3 / survey field standard)
[Safety Amber Hvr] #c2410c  ── Status hover tombol oranye
[Aquifer Blue]     #0284c7  ── Aksen indikator air tanah, diagram penampang, dan tautan teknis
[Subsurface Green] #16a34a  ── Indikator konversi WhatsApp resmi & status verifikasi lolos izin
```

### Rasio Kontras WCAG
- `#ffffff` di atas `#0b1522` = **16.5:1** (Memenuhi Standar WCAG AAA).
- `#0b1522` di atas `#ffffff` = **16.5:1** (Memenuhi Standar WCAG AAA).
- `#ea580c` (Safety Amber) dengan teks `#ffffff` = **3.6:1** untuk tombol besar 16px/Bold (Memenuhi Standar Kontras Elemen Interaktif).
- Teks deskripsi `#475569` di atas `#ffffff` = **7.1:1** (Memenuhi Standar WCAG AAA).

---

## 3. Sistem Tipografi (*Typography Scale*)

Menggunakan *font-family stack* modern berorientasi teknik:
`font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;`

| Tingkat Tipografi | Ukuran Desktop | Ukuran Mobile | Bobot | Line-Height | Kegunaan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kicker / Eyebrow** | 12px (0.75rem) | 11px (0.68rem) | 800 (Bold) | 1.4 | Label kategori teknik di atas H1/H2 (Huruf kapital, letter-spacing: 0.08em) |
| **Display H1** | 44px (2.75rem) | 30px (1.85rem) | 850 (Heavy) | 1.15 | Judul utama hero section |
| **Section H2** | 32px (2.00rem) | 24px (1.50rem) | 800 (Bold) | 1.25 | Judul setiap bab pilar layanan dan portofolio |
| **Subsection H3** | 20px (1.25rem) | 18px (1.12rem) | 750 (Semi) | 1.35 | Judul kartu layanan, studi kasus, dan fitur |
| **Subheading Hero** | 18px (1.12rem) | 15px (0.94rem) | 400 (Regular) | 1.65 | Paragraf penjelas ringkas di bawah H1 |
| **Body Text** | 15.5px (0.97rem) | 15px (0.94rem) | 400 (Regular) | 1.70 | Paragraf bacaan artikel dan deskripsi teknis |
| **Data / Monospace** | 13px (0.81rem) | 12px (0.75rem) | 700 (Mono) | 1.50 | Koordinat GPS, kedalaman meter, debit liter/menit, formasi CAT |

---

## 4. Spacing Scale & Tata Letak Grid

- **Unit Dasar**: 4px / 8px grid.
- **Tokens Spacing**:
  - `space-xs`: 4px
  - `space-sm`: 8px
  - `space-md`: 16px
  - `space-lg`: 24px
  - `space-xl`: 36px
  - `space-2xl`: 56px
  - `space-3xl`: 80px
- **Kontainer Maksimal**: `max-width: 1200px` dengan padding tepi aman `clamp(16px, 4vw, 32px)`.
- **Breakpoints**:
  - Mobile Small: 390px
  - Tablet: 768px
  - Desktop: 1024px
  - Large Desktop: 1440px

---

## 5. Komponen Inti Antarmuka (*Component Library*)

### A. Global Navigation Header
- **Latar Belakang**: Putih bersih (`#ffffff`) dengan garis bawah tipis `#e2e8f0` dan bayangan lembut.
- **Logo Brand**: Tipografi arsitektural tebal *"GEODIPO"* dengan aksen titik oranye industrial (`#ea580c`), disertai deskripsi sub-teks: *"Geoscience & Drilling Engineering"*.
- **Menu Items**: Beranda, Layanan Rekayasa (Geolistrik, Sumur Bor, Sondir PBG, SIPA), Studi Kasus, Cakupan Wilayah, Tentang, Kontak.
- **Top Utility CTA**: Tombol oranye industrial kompak: *"Konsultasi Proyek →"*.

### B. Hero Section: Split Editorial Layout
- **Sisi Kiri (Teks & Aksi)**:
  - *Kicker Badge*: Label abu-abu gelap bertepi tajam: `KONSULTAN GEOFISIKA, HIDROGEOLOGI & SUMUR BOR INDONESIA`.
  - *Headline (H1)*: Solusi Rekayasa Kebumian & Pengeboran Air Tanah Terpadu.
  - *Sub-headline*: Analisis formasi akuifer berbasis sains geolistrik 2D, uji tanah fondasi CPT/SPT resmi PBG, dan konstruksi deep well berkapasitas tembus batuan keras se-Indonesia.
  - *Dual CTA*: Tombol oranye primer (*"Konsultasi Bersama Ahli Geologi →"*) + Tombol outline abu-abu (*"Eksplorasi Spesifikasi Layanan ↓"*).
  - *Tiga Indikator Nilai Ringkas*: Ikon centang teknis yang memuat poin kepastian data resistivitas, legalitas resmi SIPA ESDM, dan armada rig milik sendiri.
- **Sisi Kanan (Visual Bukti Nyata)**:
  - Foto resolusi tinggi kru teknisi Geodipo mengoperasikan instrumen geolistrik di lapangan (dari aset asli).
  - *Floating Technical Metric Badge*: Kotak ringkasan transparan di sudut foto yang menampilkan parameter nyata: `Data Cekungan Air Tanah (CAT) • Ketelitian Resistivitas 2D • Kedalaman hingga 200m+`.

### C. Kartu Jalur Pelanggan (*Customer Persona Pathways*)
Tiga pintu masuk terarah yang memudahkan calon klien menemukan solusi tanpa tersesat:
1. **Pemilik Hunian & Residensial**: Bebas air keruh/kuning dan kekeringan sumur bor dangkal (kedalaman 30–60m).
2. **Pengembang Gedung & Infrastruktur**: Uji sondir CPT 2.5 ton & deep boring SPT syarat persetujuan bangunan PBG/SIMBG.
3. **Pabrik Manufaktur & Kawasan Industri**: Sumur dalam *deep well* debit besar 100–200m, pumping test SNI, dan perizinan resmi SIPA ESDM.

### D. Komponen Portofolio Lapangan Terverifikasi (*Field Case Studies*)
Menampilkan dokumentasi lapangan dengan struktur data ketat:
- Label Kategori (Industri / Residensial / Geoteknik / Perkebunan)
- Lokasi Geografis Riil (Sleman DIY, Karawang Jabar, Semarang Jateng, Tasik Serai Riau, Bebon Jaya Papua)
- Parameter Litologi Batuan (Breksi vulkanik, aluvial pesisir, karst gamping)
- Kedalaman & Peralatan (Rotary mud drilling, DTH Hammer, CPT 2.5 Ton)
- Hasil Terukur (Debit liter/menit, kualitas air tawar, atau lolos verifikasi SIMBG)

### E. Tabel Komparasi Rekayasa (*Engineering Comparison Table*)
Matriks perbandingan kolom kontras tinggi:
- Fitur Teknis (Penentuan titik, pipa casing, pipa saringan screen, penyekat grouting, kapasitas tembus batuan, legalitas).
- Standar Rekayasa Geodipo (Pemeriksaan geologi CAT, PVC AW SNI / GIP Medium, screen pabrik presisi + silika, grouting semen 0-12m, DTH hammer kompresor 25 bar).
- Tukang Bor Konvensional (Tebakan kawat tembaga/kelapa, pipa tipis kelas D, paralon gergajian manual, tanpa semen pelindung, mesin modifikasi macet di batuan).

### F. Direktori Wilayah Nasional Terpadu (*Tabbed Regional Hub*)
Struktur tab navigasi bersih untuk 279+ landing page wilayah:
- Tab 1: Jabodetabek & Banten
- Tab 2: Jawa Barat & DIY
- Tab 3: Jawa Tengah & Jawa Timur
- Tab 4: Sumatera, Kalimantan, Sulawesi & Papua

### G. Optimasi Konversi WhatsApp Responsif
- **Desktop**: Tombol di header atas, tombol primer di hero, dan tombol di setiap kartu solusi.
- **Mobile**: Menghapus bilah horizontal raksasa yang menutupi konten. Menggantinya dengan:
  - Tombol aksi jelas di dalam kartu konten.
  - Floating action button (FAB) bundar mini di sudut kanan bawah (50x50px) dengan lambang WhatsApp dan dot hijau penanda aktif, dengan posisi aman `bottom: 20px; right: 20px;` sehingga ruang baca teks tetap 100% bebas hambatan.
