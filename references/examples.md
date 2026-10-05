# Contoh penggunaan

Contoh adalah ilustrasi sintetis, bukan kebutuhan pengguna sebenarnya.

## Ide belum lengkap

Input: "Bikinin semua dokumen buat aplikasi booking lapangan."

Langkah:
1. Ambil detail yang sudah tersedia.
2. Jika belum diketahui, tanyakan apakah aplikasi untuk satu pengelola atau
   marketplace banyak pengelola. Ini mengubah otorisasi, data, dan alur bisnis.
3. Detail nonkritis seperti warna UI tidak menghalangi draft dokumentasi.
4. Jangan mengasumsikan pembayaran online; tandai sebagai keputusan terbuka.
5. Pilih Standard jika diminta semua dokumen; dokumen payment hanya jika perlu.

## Requirement ke test

Konteks confirmed untuk contoh: satu pengelola, user login, booking tanpa payment.

**FR-001 — Booking slot tersedia**
- Role: pelanggan.
- Scope: MVP; priority: Must.
- Perilaku: pelanggan dapat memesan satu slot yang tersedia. Sistem tidak
  boleh menerima dua booking aktif pada lapangan dan slot yang sama.
- AC-001: Given slot tersedia dan pelanggan login, When pemesanan berhasil,
  Then satu booking aktif tersimpan dan slot tidak lagi tersedia.
- AC-002: Given dua pelanggan memesan slot yang sama secara bersamaan,
  When keduanya diproses, Then hanya satu berhasil dan lainnya menerima
  pesan bahwa slot tidak tersedia.

**Desain usulan**
- Booking memakai slot eksplisit agar constraint uniqueness dapat ditentukan.
- Constraint untuk satu booking aktif per slot disesuaikan dengan database.
- Jika pindah ke waktu start/end bebas, revisi desain untuk overlap interval;
  constraint slot unik saja tidak lagi cukup.
- Kontrak usulan `POST /bookings`: input `slot_id`, user dari sesi;
  `201` sukses, `409` konflik, `401` tidak login. Verifikasi implementation
  aktual sebelum menyebut kontrak ini observed.

**Traceability**

| Requirement | AC | UX | Data/API | Task | Test |
|---|---|---|---|---|---|
| FR-001 | AC-001, AC-002 | Pilih slot → konfirmasi → hasil | Booking, Slot; POST /bookings | TASK-001 | TC-001, TC-002 |

TC-002: kirim dua request bersamaan untuk slot sama; expected satu sukses,
satu conflict, dan tepat satu booking aktif. Status: planned, belum dijalankan.

## Existing app

Input: "Update dokumen karena sekarang admin bisa batalkan booking."

Langkah:
- Baca requirement, role matrix, state booking, kontrak API, dan test existing.
- Tentukan aturan pembatalan dari sumber pengguna/kode; jangan mengarang refund.
- Buat atau revisi FR dengan ID stabil.
- Update permission, transition, API, backlog, test, dan panduan admin.
- Jika behavior kode berbeda dari request, catat observed vs proposed.
- Jangan menjalankan migrasi, commit, atau deploy karena hanya diminta dokumen.

## Acceptance checks untuk skill

Gunakan skenario ini saat mengevaluasi skill melalui penggunaan nyata:

| Input | Perilaku yang diharapkan |
|---|---|
| Ide singkat, "langsung buat" | Draft nyata, asumsi terlihat, pertanyaan kritis di daftar blocker |
| MVP frontend tanpa persistensi | Tidak mengarang database/backend; N/A dengan alasan |
| SaaS multi-tenant | Dokumen tenancy dan tes isolasi data muncul |
| Payment belum diputuskan | Payment tidak dinyatakan confirmed atau implemented |
| Aplikasi existing | As-is dan proposed dibedakan; bukti kode bukan bukti production |
| Revisi fitur | ID stabil dan dokumen downstream diperbarui |
| Tidak ada bukti testing | Semua test tetap planned, bukan passed |
| Permintaan hanya PRD | Arahkan ke workflow PRD, bukan paket dokumen yang berlebihan |
| "Harus sesuai semua SNI" | Tentukan scope/sector, verifikasi acuan, hasilkan register dan gap; tidak menjanjikan universal compliance |
| Hanya katalog standar tersedia | Mapping topik, tanpa nomor klausul atau klaim memenuhi persyaratan lengkap |
| Sertifikat SMKI organisasi | Periksa scope/issuer/masa berlaku; tidak menganggap tiap aplikasi tersertifikasi |
| ISO ada edisi lebih baru | Periksa status SNI terpisah sebelum mengganti acuan nasional |
| "Sesuai SKKNI" sebelum kode ada | Mapping unit/aktivitas, evidence plan; dokumentasi kode masih planned |
| Daftar unit tanpa uraian KUK | Mapping tingkat unit, tidak mengarang KUK atau menyatakan unit terpenuhi |
| Dokumentasi kode sudah dihasilkan | Review keterkaitan kode/revisi; tidak otomatis menyatakan developer kompeten |
