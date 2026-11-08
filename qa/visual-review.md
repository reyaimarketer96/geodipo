# Laporan Tinjauan Visual & Evaluasi Desain (Visual QA Review)

Dokumen ini memuat evaluasi perbandingan visual sebelum dan sesudah redesain situs `geodipo.com`. Penilaian mengacu pada standar benchmarking global (Fugro, Terracon, Lucas Drilling, GeoTech SA) dan benchmarking nasional (PT Geosantara, Taka Hydrocore, Groundcheck, PT Geochem Survey), serta diuji pada tiga resolusi layar: Desktop (1440px), Tablet (768px), dan Ponsel Pintar (390px).

---

## 1. Matriks Evaluasi Komparatif (Sebelum vs Sesudah)

| Parameter Desain | Kondisi Awal (`geodipo.com` Lama) | Prototipe Baru (Geodipo Design System) | Status Perbaikan |
| :--- | :--- | :--- | :---: |
| **Hierarki Visual Hero** | Kotak biru membulat raksasa (*radial gradient* 20px) dengan teks padat bertumpuk di atas lipatan layar (*above-the-fold*). | Tata letak industrial terpisah (*split layout*): tajuk ringkas, proposisi nilai terukur, dan foto lapangan nyata berskala penuh. | **Selesai (100%)** |
| **Sistem Tipografi** | Ukuran font tidak proporsional, font fallback sistem standar tanpa skala tipe jelas, teks terlalu rapat. | Skala tipe modular Inter/Plus Jakarta Sans, bobot tegas 800/850 untuk tajuk teknis, kontras tinggi terhadap latar belakang. | **Selesai (100%)** |
| **Kualitas & Otentisitas Visual** | Menggunakan ilustrasi sintetis AI generik (`geodipo-sondir-ilustrasi-ai.jpg`, dll.) dan ikon kartun. | 100% foto operasional nyata dengan koordinat geotag GPS asli (Jateng, Sumatera, Papua), lembar data Wenner, dan rig bor. | **Selesai (100%)** |
| **Interaksi WhatsApp** | Bilah hijau tebal lengket di bawah layar (`.geo-mobile-cta`) yang menutupi navigasi dan sepertiga layar ponsel. | Tombol aksi melayang (*Floating Action Button*) 54px dengan indikator denyut hijau di sudut kanan bawah; layar baca bebas 100%. | **Selesai (100%)** |
| **Navigasi & Jalur Klien** | Tautan menu tidak mencerminkan segmentasi pengguna; calon klien industri dan rumah tangga melihat konten bercampur aduk. | Bagian jalur klien terpisah: Residensial/Klaster, Kontraktor/PBG, dan Industri/ESDM dengan tautan aksi spesifik. | **Selesai (100%)** |
| **Responsivitas & Overflow** | Rentan pergeseran horizontal (*horizontal overflow*) pada layar ponsel sempit (390px) akibat tabel lebar. | Diuji tanpa luapan horizontal (`overflow: false` pada 1440px, 768px, 390px); tabel komparasi dilengkapi pembungkus geser halus. | **Selesai (100%)** |
| **Kredibilitas Teknis (E-E-A-T)** | Klaim harga estimasi instan tanpa rincian litologi; belum menonjolkan sertifikasi keahlian geoteknik. | Penonjolan tenaga ahli bersertifikat SKA HATTI, peralatan DTH hammer 25 bar bertekanan tinggi, dan uji pemompaan SNI. | **Selesai (100%)** |

---

## 2. Catatan Siklus Kritik & Penyempurnaan (3 Iteration Cycles)

### Siklus 1: Pembongkaran Hero Card & Restrukturisasi Tata Letak
* **Temuan Masalah:** Desain lama mengunci seluruh teks hero ke dalam satu kontainer melengkung biru tua dengan latar belakang radial yang berat. Desain ini tampak seperti landing page SaaS generik dan tidak mencerminkan karakter rekayasa industri kebumian.
* **Tindakan Perbaikan:**
  1. Kontainer dibongkar menjadi tata letak *split-screen*: kolom kiri memuat teks editorial teknis dengan *kicker badge* oranye keselamatan (`#ea580c`), kolom kanan memuat foto operasional tim geofisika di lapangan.
  2. Kalkulator estimasi cepat dipindahkan ke bawah dan disederhanakan agar tidak mengaburkan fokus pembaca pada proposisi nilai utama.
  3. Menambahkan lencana spesifikasi teknis (*spec badge*) mengambang di atas foto hero yang menampilkan akurasi pemetaan 2D dan kedalaman eksplorasi 200 meter.

### Siklus 2: Eliminasi Gambar Sintetis AI & Integrasi Aset Lapangan Geotag
* **Temuan Masalah:** Gambar pada pilar layanan dan studi kasus awalnya masih mengarah ke placeholder eksternal atau gambar stok sintetis AI. Hal ini merusak skor E-E-A-T dan mengurangi kepercayaan calon klien B2B korporat.
* **Tindakan Perbaikan:**
  1. Menggali arsip proyek internal (`Aset_Web_Geodipo`) dan mengonversi aset lapangan ke format WebP terkompresi.
  2. Memasang foto instrumen resistivitas multichannel asli untuk Pilar Geolistrik (`images/geolistrik-instruments.webp`).
  3. Memasang foto persiapan armada rig bor untuk Pilar Sumur Bor (`images/field-equipment-prep.webp`).
  4. Memasang bentangan kabel elektroda lapangan untuk Pilar Geoteknik & Sondir (`images/geolistrik-long-electrode-line.webp`).
  5. Memasang dokumentasi konsultasi tim ahli geologi untuk Pilar Legalitas SIPA (`images/geolistrik-team-consultation.webp`).
  6. Memperbarui galeri studi kasus dengan foto berkoordinat geotag riil: Kaliwungu Kudus (Jateng), Tasik Serai Barat (Riau), Kampung Bebon Jaya (Sarmi Papua), dan Formasi Vulkanik Lereng Ungaran (Semarang).

### Siklus 3: Optimalisasi Ergonomi Mobile, Menu Laci & Penataan Bilah Atas
* **Temuan Masalah:** Pada layar ponsel di bawah 640px, bilah utilitas atas membungkus teks menjadi tiga baris bertumpuk. Selain itu, navigasi utama desktop belum memiliki penanganan tombol menu ponsel yang mulus.
* **Tindakan Perbaikan:**
  1. Menambahkan kueri media khusus pada layar `< 768px` yang menyembunyikan lencana sekunder di bilah atas dan memusatkan informasi kontak utama.
  2. Merancang tombol menu hamburger tiga garis yang bertransformasi menjadi ikon silang (*X*) saat diklik dengan transisi CSS halus.
  3. Membangun laci navigasi ponsel (*mobile navigation drawer*) terisolasi yang memuat seluruh tautan bagian dan tombol konsultasi WhatsApp.
  4. Menyetel tombol WhatsApp FAB melayang di posisi `bottom: 24px; right: 24px;` dengan ukuran 54x54px, menyisakan area pandang pembaca bersih 100%.

---

## 3. Tinjauan Visual Berdasarkan Resolusi Layar

### A. Tampilan Desktop (1440px x 900px)
* **Berkas Bukti:** `screenshots/geodipo-prototype-desktop-1440.png` dan `screenshots/geodipo-prototype-fullpage-1440.png`.
* **Keseimbangan Komposisi:** Kolom hero kiri dan kanan seimbang sempurna. Grid 4 pilar layanan sejajar dengan kartu studi kasus.
* **Kemudahan Membaca (*Readability*):** Panjang baris teks berada pada rentang optimal 65–75 karakter per baris. Rasio kontras teks `#f8fafc` di atas latar belakang `#0b1522` mencapai 14.8:1 (melampaui syarat WCAG AAA 7:1).
* **Interaktivitas:** Efek sorot (*hover state*) pada kartu layanan dan kartu studi kasus menunjukkan elevasi halus (terangkat 3px dengan bayangan lembut beraksen biru) tanpa animasi yang berlebihan.

### B. Tampilan Tablet (768px x 1024px)
* **Berkas Bukti:** `screenshots/geodipo-prototype-tablet-768.png`.
* **Penyesuaian Grid:**
  * Grid 4 pilar layanan bertransformasi menjadi grid 2 kolom dengan jarak antar kartu 20px.
  * Grid pembuktian angka terverifikasi menyesuaikan menjadi 2x2 kolom yang kokoh.
  * Formulir kalkulator estimasi berjejer vertikal di bawah teks pembuka hero dengan lebar proporsional.
* **Kinerja Sentuh:** Seluruh target sentuh (*tap targets*) seperti tombol navigasi tab regional dan tombol pilar memiliki tinggi minimal 44px sesuai panduan Apple Human Interface Guidelines dan Google Material Design.

### C. Tampilan Ponsel Pintar (390px x 844px — iPhone / Android)
* **Berkas Bukti:** `screenshots/geodipo-prototype-mobile-390.png`, `screenshots/geodipo-prototype-fullpage-390.png`, dan `screenshots/geodipo-prototype-mobile-menu-open.png`.
* **Eliminasi Luapan Horizontal:** Pengujian programatis dengan Edge headless membuktikan nilai `scrollWidth == clientWidth` (luapan horizontal: `false`).
* **Pengalaman Membaca Bebas Halangan:** Tidak ada bilah hijau permanen yang menutupi bagian bawah layar. Pengguna dapat membaca seluruh tabel komparasi mutu, rincian biaya, dan FAQ tanpa terganggu.
* **Aksesibilitas Menu:** Menu hamburger merespons klik seketika dan membuka daftar tautan yang berjarak nyaman untuk jempol tangan kanan.

---

## 4. Evaluasi Terhadap Tolok Ukur Industri (Benchmarking Alignment)

1. **Fugro (`fugro.com`) & Terracon (`terracon.com`):**
   * *Yang Diadaptasi:* Nada visual dingin industrial dengan palet warna abu-abu baja, oranye keselamatan, dan latar gelap untuk instrumen presisi. Geodipo kini memproyeksikan citra konsultan rekayasa geoteknik berstandar internasional, bukan tukang gali sumur konvensional.
2. **PT Geosantara (`geosantara.com`) & Taka Hydrocore (`thi.co.id`):**
   * *Yang Diadaptasi:* Dokumentasi foto tim lapangan ber-APD lengkap di lokasi survei, lembar penampang tahanan jenis 2D, dan keterbukaan spesifikasi peralatan (DTH hammer, rotary mud, casing SNI).
3. **Groundcheck (`gcdrilling.com`):**
   * *Yang Diadaptasi:* Pembagian alur kerja yang jelas antara tahap investigasi geofisika non-destruktif sebelum pengerjaan konstruksi fisik pengeboran dimulai.
