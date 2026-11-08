# Laporan Evaluasi Perangkat & Keterampilan (Skill & Tool Discovery)

Laporan ini memetakan ketersediaan, kompatibilitas, dan status instalasi modul kemampuan (*skills*), pengaya (*plugins*), dan peladen protokol konteks mesin (*MCP servers*) untuk perancangan ulang situs Geodipo.

---

## 1. Inventaris Perangkat & Keterampilan yang Terpasang

| Kategori | Nama Modul / Alat | Sumber | Tujuan Fungsional | Status |
| :--- | :--- | :--- | :--- | :--- |
| **WordPress Engine** | `geodipo` MCP Server | `Easy MCP AI` (Endpoint REST API WordPress) | Akses baca/tulis penuh ke 243 fungsi WordPress: halaman, pos, blok Gutenberg, templat FSE, berkas media, pengaturan situs, taksonomi, dan riwayat revisi. | **Aktif & Terverifikasi** |
| **Otomasi Peramban** | Puppeteer-Core + Microsoft Edge Headless | Eksekutabel lokal `msedge.exe` (Chromium 128+) via skrip Node.js | Pengambilan tangkapan layar rendered pada viewport 1440px, 768px, dan 390px, inspeksi DOM, pengukuran layout shift, serta verifikasi visual multi-perangkat tanpa dependensi eksternal berbahaya. | **Aktif & Terverifikasi** |
| **Arsitektur Antarmuka** | `superior-ui` & `superior-responsive` | Plugin Superior Skills | Pembangunan komponen antarmuka teknik berbasis sistem desain terukur, pengendalian skala tipografi, grid responsif, dan penanganan overflow kontainer. | **Tersedia Lokal** |
| **Audit Visual & UX** | `superior-ui-audit` & `superior-ux` | Plugin Superior Skills | Evaluasi hirarki visual, keterbacaan kontras WCAG, alur tugas pengguna (B2B vs B2C), dan pencegahan pergeseran tata letak kumulatif (CLS). | **Tersedia Lokal** |
| **Aksesibilitas & Kinerja** | `superior-accessibility` & `superior-performance` | Plugin Superior Skills | Verifikasi rasio kontras teks, navigasi papan ketik, atribut ARIA semantik, optimasi LCP, dan pencegahan pemblokiran thread utama oleh skrip. | **Tersedia Lokal** |
| **SEO Teknis & Audit** | `seo-technical`, `seo-page`, `seo-audit` | Plugin Claude SEO | Pemeriksaan kanonikal, struktur meta tag, hierarki heading H1–H6, integrasi skema JSON-LD Schema.org, serta validasi peta situs XML. | **Tersedia Lokal** |
| **Standar Konten & Copy** | `superseo-skills` (`write-content`, `improve-content`) | Framework InhouseSEO | Penegakan aturan anti-AI-slop, penghilangan kosakata klise AI tingkat 1, ritme kalimat bervariasi (*burstiness*), dan pengujian fakta konkret (*horoscope test*). | **Tersedia Lokal (Aturan Aktif di GEMINI.md)** |

---

## 2. Evaluasi Kandidat Pasar Pengaya (*Marketplace Plugins*)

| Kandidat Pengaya | Sumber Katalog | Tujuan | Analisis Kompatibilitas & Kebutuhan | Rekomendasi Tindakan |
| :--- | :--- | :--- | :--- | :--- |
| **Chrome DevTools** | `antigravity-plugins-official/plugin/chrome-devtools-plugin` | Otomasi pengujian peramban Chrome, ekstraksi metrik Core Web Vitals, dan rekaman sesi Puppeteer. | Memerlukan instalasi plugin ke lingkungan sistem. Karena lingkungan lokal telah berhasil menjalankan Microsoft Edge headless + Puppeteer-core secara mandiri dengan hasil tangkapan layar 100% presisi, plugin ini tidak menjadi prasyarat mutlak. | **Disimpan sebagai cadangan opsional** (Tidak perlu instalasi agresif). |
| **WordPress Jetpack** | `antigravity-plugins-partners/plugin/wordpress` | Manajemen situs via antarmuka WordPress.com / Jetpack API. | Tidak kompatibel/tidak relevan untuk instalasi Geodipo yang menggunakan hosting mandiri (*self-hosted LiteSpeed*) dengan peladen lokal `Easy MCP AI`. | **Tidak Dipasang** (Gunakan `geodipo` MCP yang sudah terhubung langsung). |
| **Figma Code Connect** | `antigravity-plugins-partners/plugin/figma` | Sinkronisasi desain token dari berkas Figma. | Proyek ini tidak memiliki berkas master Figma eksternal; desain dibangun langsung menggunakan token kode CSS native dan Gutenberg FSE templates. | **Tidak Dipasang** (Tidak dibutuhkan). |

---

## 3. Inisiasi Keterampilan Khusus Proyek: `geodipo-design-system`

Untuk menjaga konsistensi perancangan dan standarisasi elemen antarmuka di seluruh 300+ halaman Geodipo, parameter desain dibakukan dalam spesifikasi sistem desain:
- **Lokasi Dokumentasi Desain**: `design/geodipo-design-system.md`
- **Tujuan**: Mengunci palet warna teknik geosains (*Deep Slate, Earth Amber, Clean Slate, Aquifer Teal*), skala tipografi modular, pola kartu studi kasus, tata letak tabel spesifikasi bor, dan aturan integrasi WhatsApp konversi tinggi tanpa mengorbankan kenyamanan membaca di perangkat seluler.
