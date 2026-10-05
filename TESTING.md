# Catatan verifikasi v1.4

Tanggal: 2026-10-05. Yang diuji adalah skill dan template, bukan aplikasi nyata.

## Pemeriksaan yang dijalankan

- `python scripts/validate.py`: lulus pemeriksaan metadata, referensi relatif,
  heading unik, anchor HTML, dependensi eksternal dan aturan cetak wajib.
- Render template dengan Chromium **152.0.7977.64**, headless, tanpa
  header/footer bawaan.
- `pdfinfo`: PDF **8 halaman**, ukuran **594.96 × 841.92 pt (A4)**.
- `pdftotext`: teks dapat diekstrak; semua delapan halaman berisi teks.
- Text bounding boxes seluruh halaman berada dalam area margin 3 cm dengan
  toleransi pemeriksaan 1 pt. Ini tidak memeriksa seluruh bounds objek grafis.
- Pemeriksaan visual sampel halaman 3 (tabel) dan 8 (aturan cetak/footer akhir):
  teks/tabel pada sampel tidak terlihat terpotong.

## Font dan pagination

CSS meminta Cambria 12 pt. Cambria tidak terpasang di lingkungan pengujian.
Font PDF aktual dari `pdffonts`: **Liberation Serif**, regular dan bold,
embedded sebagai subset. Hasil uji ini **bukan** verifikasi Cambria persis.

Footer yang diuji hanya footer akhir dokumen, bukan footer berulang.
Nomor halaman, CSS margin boxes dan total-page counters belum diuji;
dukungannya tetap tergantung engine.

## Reproduksi render

```sh
python scripts/validate.py
chromium --headless --no-sandbox --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf=/tmp/app-documentation-template.pdf \
  "file://$(pwd)/assets/report-a4.html"
pdfinfo /tmp/app-documentation-template.pdf
pdffonts /tmp/app-documentation-template.pdf
```

`--no-sandbox` hanya untuk lingkungan pengujian/container yang memerlukannya,
bukan rekomendasi menjalankan konten tidak tepercaya. Nama executable serta
flags dapat berbeda antar OS/versi; gunakan environment aman.

## Batas verifikasi

- Tidak seluruh halaman diperiksa visual satu per satu.
- Belum diuji pada Firefox, Safari, engine PDF lain, atau dengan Cambria.
- Belum stress-tested dengan tabel sangat panjang atau konten aplikasi nyata.
- Validator struktural tidak menilai kesesuaian klausul SNI, kepatuhan hukum,
  kompetensi SKKNI, atau sertifikasi.
