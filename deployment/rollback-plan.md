# Rencana Pencadangan, Perlindungan SEO & Pemulihan (Rollback Plan)

Dokumen ini memuat prosedur perlindungan ekuitas SEO eksisting dan langkah-langkah pemulihan sistem jika terjadi kendala teknis dalam proses penerapan perancangan ulang situs Geodipo.

---

## 1. Perlindungan Ekuitas SEO & Integritas WordPress

Situs Geodipo memiliki lebih dari 664 URL terindeks (300 halaman dan 364 pos edukasi) dengan peringkat kata kunci pencarian lokal dan nasional. Aturan perlindungan mutlak yang diterapkan:

1. **Struktur Permalink Terkunci**:
   - Tidak ada perubahan slug halaman, format permalink (`/%postname%/`), atau hierarki URL.
   - Semua URL eksisting (contoh: `/jasa-geolistrik/`, `/jasa-sondir-jogja/`, `/jasa-sumur-bor-semarang/`, `/biaya-sumur-bor/`) tetap aktif 100%.
2. **Kanonikal & Meta Deskripsi**:
   - Konfigurasi Yoast SEO dipertahankan penuh tanpa merusak tag `canonical` otomatis.
   - Peta situs XML (`https://geodipo.com/sitemap_index.xml`) tetap valid dan dapat diakses oleh Googlebot tanpa interupsi.
3. **Penyelamatan Skrip Analitik & Pelacakan Konversi**:
   - Integrasi Google Site Kit (GA4 Measurement ID & Search Console Verification) tetap beroperasi normal.
   - Skrip penangkap klik WhatsApp (`geodipo_whatsapp_click` dan `dataLayer.push`) yang terpasang di footer dilestarikan dan disesuaikan agar menangkap setiap klik tombol baru tanpa mengubah skema nama event.
4. **Pencegahan Beban Tambahan (*No Heavy Plugins*)**:
   - Tidak memasang builder berat pihak ketiga (seperti Divi atau Visual Composer).
   - Seluruh pembaruan visual menggunakan native CSS tokens dan Gutenberg block patterns Twenty Twenty-Five, memastikan waktu respon server (*TTFB*) dan Core Web Vitals tetap optimal.

---

## 2. Lokasi Berkas Cadangan (*Backup Files*)

Salinan data mentah sebelum dilakukan modifikasi disimpan secara permanen di:
- **Halaman Utama (Page ID: 12)**:
  `deployment/backups/original_page_12.json`
- **Bagian Templat Footer (Global Template Part)**:
  `deployment/backups/original_footer_template_part.json`
- **Pangkalan Data Pos & Halaman Lengkap**:
  Tercatat pada repositori log sistem dan plugin `UpdraftPlus` aktif di server.

---

## 3. Prosedur Pemulihan Kilat (*Emergency Rollback Procedure*)

Jika terdeteksi anomali pada tata letak atau performa:

### Skenario A: Mengembalikan Halaman Utama (Homepage)
Jalankan pemulihan konten halaman ID 12 melalui perintah WordPress MCP:
```json
{
  "page_id": 12,
  "content": "<isi konten dari deployment/backups/original_page_12.json>"
}
```
Hasil: Halaman utama seketika kembali ke kondisi sebelum perubahan dalam hitungan detik.

### Skenario B: Mengembalikan Templat Global Footer
Jalankan pemulihan templat part `twentytwentyfive//footer`:
```json
{
  "template_id": "twentytwentyfive//footer",
  "type": "template_part",
  "content": "<isi konten dari deployment/backups/original_footer_template_part.json>"
}
```
Hasil: Seluruh gaya footer dan mobile CTA kembali ke konfigurasi awal.

### Skenario C: Pembersihan Cache Server
Setelah pemulihan konten dijalankan, bersihkan cache LiteSpeed melalui perintah `wp_clear_cache` agar perubahan langsung terlihat oleh pengunjung tanpa jeda caching.
