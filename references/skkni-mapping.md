# Pemetaan SKKNI untuk dokumentasi aplikasi

Penelitian sumber resmi: 2026-10-05. SKKNI mengatur kemampuan kerja, bukan
sertifikasi produk atau format universal semua dokumen aplikasi.

Scope pengguna: hanya dokumentasi pembangunan aplikasi. Gunakan mapping
untuk memastikan aktivitas dan artefak relevan tercakup, bukan membuat
portofolio personel, formulir asesmen, atau paket sertifikasi. Bukti kerja
berarti referensi implementasi/hasil uji yang menjaga dokumen tetap akurat.

## Definisi dan acuan terverifikasi

Portal Kemnaker mendefinisikan SKKNI sebagai rumusan kemampuan kerja yang
mencakup pengetahuan, keterampilan/keahlian dan sikap kerja sesuai tugas/jabatan,
dikembangkan dengan konsultasi industri. Digunakan antara lain untuk pelatihan,
rekrutmen, penilaian unjuk kerja dan acuan sertifikasi.

- Definisi: https://skkni.kemnaker.go.id/
- Keputusan: Kepmenaker 282 Tahun 2016, Software Development Subbidang
  Pemrograman; halaman JDIH menampilkan Berlaku pada tanggal cek.
- Metadata/status:
  https://jdih.kemnaker.go.id/peraturan/detail/1381/keputusan-menteri-ketenagakerjaan-nomor-282-tahun-2016
- Lampiran resmi:
  https://skkni-api.kemnaker.go.id/v1/public/documents/d50d2dc3-6fe7-42ec-926c-cd13b8cb929e/download

Lingkup yang dibaca pada penelitian ini: pendahuluan, daftar unit, uraian awal
termasuk unit arsitektur/UX, serta uraian J.620100.023.02. Tidak seluruh lampiran
dibaca atau diaudit. Untuk unit lainnya, tabel berikut mapping tingkat unit
berdasarkan daftar, bukan audit KUK lengkap.

## Pilih acuan sesuai aktivitas

Kepmenaker 282/2016 adalah baseline pemrograman, bukan klaim cakupan semua
profesi SDLC. Bila perlu cakupan analis sistem, desain, database, security,
operasi, atau manajemen, cari SKKNI terkait dan cek status terbarunya.
Jangan menganggap semua role terwakili lengkap oleh satu keputusan.
Bedakan SKKNI, KKNI, dan skema sertifikasi: ketiganya bukan sinonim.

## Mapping tingkat unit awal

Pembagian role dan artefak di bawah adalah usulan workflow skill, bukan
pernyataan nama jabatan atau skema sertifikasi resmi.

| Kode/judul pada daftar resmi | Aktivitas dan artefak yang direncanakan |
|---|---|
| J.620100.002.01 — Menganalisis Skalabilitas Perangkat Lunak | NFR kapasitas, asumsi workload, capacity analysis dan evidence pengukuran bila tersedia |
| J.620100.006.01 — Merancang User Experience | UX flow, interaksi, desain/validasi sesuai kebutuhan |
| J.620100.008.01 — Merancang Arsitektur Aplikasi | Diagram data, komponen/interaksi, integrasi eksternal, keputusan desain |
| J.620100.023.02 — Membuat Dokumen Kode Program | Developer guide, dokumentasi modul/fungsi, generation tools, version linkage |
| J.620100.032.01 — Menerapkan Code Review | Review plan, checklist, review record nyata jika dilakukan |
| J.620100.033.02 — Melaksanakan Pengujian Unit Program | Unit test plan dan hasil uji aktual bila dijalankan |
| J.620100.034.02 — Melaksanakan Pengujian Integrasi Program | Integration test plan dan hasil uji aktual |
| J.620100.035.02 — Melaksanakan Pengujian Program Sistem | System test plan dan evidence aktual |
| J.620100.038.01 — Melaksanakan Pengujian Oleh Pengguna (UAT) | Skenario UAT, data/lingkungan, pelaksanaan dan hasil/sign-off bila tersedia |
| J.620100.039.02 — Memberikan Petunjuk Teknis Kepada Pelanggan | User/admin guide dan rencana/bukti pemberian petunjuk |
| J.620100.041.01 — Melaksanakan Cutover Aplikasi | Cutover plan, dependency, go/no-go, evidence eksekusi |
| J.620100.042.01 — Melaksanakan Konfigurasi Perangkat Lunak Sesuai Environment (Development, Staging, Production) | Environment/configuration guide dan evidence konfigurasi tanpa secret |
| J.620100.043.01 — Menganalisis Dampak Perubahan Terhadap Aplikasi | Impact analysis, perubahan requirement dan downstream documentation |

Jika kode versi berbeda antara daftar unit dan uraian unit, catat discrepancy
dan minta verifikasi dokumen/otoritas, jangan memilih versi diam-diam.
Pada ekstraksi lampiran yang dibaca ditemukan perbedaan suffix untuk beberapa
unit di luar tabel ini; karena itu jangan menganggap daftar unit saja cukup
untuk menetapkan seluruh KUK atau paket asesmen.

## Unit dokumentasi kode yang telah diperiksa

J.620100.023.02 mencakup identifikasi kode, dokumentasi modul, dokumentasi
fungsi/prosedur/method, serta generasi dokumentasi. Uraiannya antara lain
mencakup identitas modul, parameter, penjelasan algoritma, exception,
pelacakan identitas dokumen, revisi mengikuti perubahan kode, dan pemilihan
serta penggunaan tool generasi dokumentasi.

Mapping berikut adalah ringkasan interpretatif sebagian KUK yang dibaca,
bukan reproduksi lengkap atau pernyataan seluruh unit telah dipenuhi:

| KUK | Implikasi pada paket dokumen | Bukti yang dibutuhkan |
|---|---|---|
| 1.1–1.3 | Inventaris modul, parameter, penjelasan algoritma | Referensi kode/revisi dan penjelasan yang cocok dengan implementasi |
| 2.1–2.4 | Dokumentasi identitas/kegunaan modul serta update mengikuti kode | Dokumen modul, version/change link dan review akurasi |
| 3.1–3.3 | Fungsi/prosedur/method, kemungkinan exception dan revisi | Kontrak fungsi nyata, exception handling dan riwayat update |
| 4.1–4.2 | Tool dan prosedur generasi dokumentasi | Tool/config yang dipilih, perintah aktual dan output/log jika dijalankan |

KUK 1.4 serta persyaratan lain pada unit tetap harus diperiksa dan ditangani
jika targetnya penilaian seluruh unit. Checklist praktis di atas tidak
menyatakan kelengkapan terhadap seluruh KUK, batasan, atau panduan penilaian.

Sebelum ada kode, tandai developer guide sebagai planned. Jangan mengarang
signature fungsi, algoritma implementasi, hasil doc generation, atau review.
Sebelum menyatakan suatu KUK didukung, baca batasan variabel, panduan penilaian,
persyaratan kompetensi, aspek kritis, serta bukti sesuai konteks.

## Workflow SKKNI

1. Tentukan aktivitas SDLC yang benar-benar ada dan tujuan penggunaan mapping.
2. Verifikasi keputusan/status, unit/kode versi, elemen/KUK, dan panduan penilaian.
3. Bedakan unit-list-only, KUK-partially-read, dan unit-fully-reviewed.
4. Petakan aktivitas ke task, role usulan, dokumen dan rencana bukti kerja.
5. Saat kode/testing/operasi tersedia, tautkan bukti nyata beserta revisi,
   tanggal, kondisi dan owner; jika tidak ada, tandai missing/planned.
6. Audit artifact coverage dan gap. Jangan menilai orang "kompeten" dari jumlah
   dokumen atau hasil generasi agent.
7. Jangan menambahkan keluaran asesmen/sertifikasi. Jika permintaan berikutnya
   memang mengenai sertifikasi, perlakukan sebagai pekerjaan terpisah di luar
   scope skill ini, bukan perluasan otomatis paket dokumen aplikasi.

## Batas hukum dan penilaian

Referensi peraturan lama pada lampiran SKKNI tidak berarti aturan tersebut
masih utuh/terbaru; cek revisi hukum secara terpisah.
Status Berlaku pada SKKNI tidak otomatis mewajibkan sertifikasi semua developer.
Kebutuhan sertifikasi/wajib harus punya dasar peraturan atau kontrak relevan.
Keluaran skill adalah dokumentasi, pemetaan dan evidence plan, bukan keputusan
asesmen kompetensi atau sertifikat.
