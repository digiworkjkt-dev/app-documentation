# Standar industri, SNI, dan regulasi Indonesia

Baseline penelitian: 2026-10-05. Halaman publik yang diperiksa memuat metadata
dan abstrak; teks lengkap standar berbayar belum diperiksa. Referensi ini
memandu pemilihan acuan, bukan menyatakan pemenuhan klausul atau sertifikasi.
Periksa ulang edisi/status dan perubahan hukum pada setiap proyek.

## 1. Bedakan jenis acuan

- **Standar internasional:** acuan praktik/kontrak; jangan menyebutnya SNI
  tanpa verifikasi adopsi oleh BSN.
- **SNI:** standar nasional yang ditetapkan BSN. Penerapannya dapat sukarela
  atau diberlakukan wajib. Status "Berlaku" di katalog bukan bukti wajib
  untuk semua aplikasi.
- **Hukum/regulasi:** kewajiban sesuai ruang lingkup, subjek, dan aturan berlaku.
  SNI dan hukum bukan istilah yang saling menggantikan.
- **Kontrak/pengadaan:** dapat mensyaratkan standar tertentu walaupun tidak
  wajib secara umum; catat dasar kontraknya.

UU 20/2014 Pasal 20 membedakan penerapan sukarela/wajib; Pasal 24 mengatur
pemberlakuan wajib melalui peraturan menteri/kepala lembaga berwenang.
Tentukan dasar wajib per sektor, bukan berdasarkan judul standar saja.

Sumber teks:
https://peraturan.bpk.go.id/Download/27975/UU%20Nomor%2020%20Tahun%202014.pdf
Metadata:
https://peraturan.bpk.go.id/Details/38663

## 2. Baseline yang metadata/abstraknya telah diperiksa

### STD-001 — ISO/IEC/IEEE 29148:2018

- Jenis: standar internasional; adopsi SNI belum diverifikasi di penelitian ini.
- Topik: requirements engineering, proses, information items, isi, dan format.
- Halaman ISO: Published; sedang direncanakan revisi, bukan bukti edisi
  penggantinya sudah berlaku.
- Pemetaan topik: konteks, PRD/SRS, sumber requirement, kualitas requirement,
  acceptance criteria, traceability, review dan change management.
- Bukti yang perlu dipersiapkan: baseline requirement, review record, matriks
  keterlacakan, approval/change log. Mapping topik belum berarti clause-compliant.
- Sumber: https://www.iso.org/standard/72089.html

### STD-002 — SNI ISO/IEC 25010:2011

- Jenis: SNI; katalog BSN menampilkan status Berlaku pada tanggal cek.
- Judul: model mutu perangkat lunak dan sistem dalam keluarga SQuaRE.
- Pemetaan topik: NFR/model mutu, kriteria penerimaan, evaluasi dan test plan.
- Tetapkan kualitas yang relevan, target yang dapat diukur, metode/lingkungan
  pengukuran, dan hasil evaluasi. Daftar karakteristik/subkarakteristik lengkap
  serta pemetaan klausul harus diperiksa dari edisi resmi yang dipilih.
- Jangan mengganti edisi SNI hanya karena ISO menerbitkan edisi lebih baru.
- Sumber: https://pesta.bsn.go.id/produk/detail/14116-sniisoiec250102011

### STD-003 — SNI ISO/IEC 27001:2022

- Jenis: SNI; katalog BSN menampilkan status Berlaku pada tanggal cek.
- Judul: keamanan informasi, keamanan siber, dan proteksi privasi — sistem
  manajemen keamanan informasi — persyaratan.
- Ruang lingkup adalah SMKI organisasi yang ditetapkan, bukan sekadar fitur
  aplikasi atau template security. Dokumentasi software saja tidak cukup.
- Pemetaan topik: scope SMKI, risiko, kontrol, kebijakan, ownership, operasi,
  evaluasi, dan perbaikan; verifikasi detail persyaratan melalui teks lengkap.
- Jika penerapan SMKI dipilih/dipersyaratkan, siapkan risk assessment/treatment,
  Statement of Applicability, bukti operasi kontrol, audit dan tindakan
  perbaikan sesuai persyaratan terverifikasi. Jangan mengarang hasil audit.
- Daftar kontrol terkait perlu diperiksa dari standar resmi; jangan menganggap
  semua kontrol otomatis wajib pada semua aplikasi atau bisa diabaikan tanpa
  justifikasi sesuai aturan standar.
- Sumber: https://pesta.bsn.go.id/produk/detail/14325-sniisoiec270012022

### REG-001 — UU 27/2022 tentang Pelindungan Data Pribadi

- Jenis: hukum Indonesia, bukan SNI.
- Halaman BPK menampilkan Berlaku dan mencatat putusan pengujian materi
  terkait Pasal 53 ayat (1) huruf b. Periksa teks terkini, putusan, aturan
  pelaksanaan, dan kewajiban yang relevan sebelum menyimpulkan kepatuhan.
- Screening ketika aplikasi memproses data pribadi: peran pengendali/prosesor,
  tujuan/dasar pemrosesan, hak subjek, data inventory, retention/deletion,
  keamanan, transfer, penanganan insiden, dan kewajiban organisasi.
- Jangan menyalin tenggat/prosedur dari ingatan; rujuk pasal yang dibaca.
- Sumber: https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022

## 3. Kandidat tambahan yang harus diverifikasi dahulu

Pertimbangkan menurut kebutuhan:
- ISO/IEC/IEEE 12207: proses siklus hidup software.
- ISO/IEC/IEEE 15289: documentation/information items siklus hidup.
- ISO/IEC/IEEE 42010: deskripsi arsitektur.
- ISO/IEC/IEEE 29119: pengujian software.
- Keluarga ISO/IEC 29110: entitas sangat kecil.
- ISO/IEC 25023: pengukuran mutu; katalog 25010 BSN mencantumkan SNI terkait,
  tetapi detail/status edisinya belum diperiksa dalam penelitian ini.
- ISO/IEC 27002: panduan kontrol keamanan terkait SMKI.
- Panduan OWASP ASVS dan WCAG bila relevan: acuan teknis tambahan,
  bukan SNI atau hukum Indonesia dengan sendirinya.

Jangan menulis kandidat sebagai acuan terverifikasi, menambahkan prefix SNI,
atau memakai nomor edisi/klausul yang belum dibaca. Cari penerbit resmi,
tentukan versi, status, scope, dan kebutuhan sebelum memasukkannya.

## 4. Screening sektor wajib

Tentukan sektor dan jenis operator dari sumber yang ada. Jika belum diketahui,
catat `Applicability belum ditentukan — sektor/operator belum diketahui`.

| Kondisi | Pemeriksaan lanjutan |
|---|---|
| PSE/layanan elektronik di Indonesia | Peraturan sistem elektronik, jenis PSE dan kewajiban registrasi/operasional yang berlaku |
| Keuangan/pembayaran | Aturan OJK/BI sesuai model usaha, izin, peran penyedia, kontrak, dan pengelolaan data |
| Kesehatan | Aturan Kemenkes sesuai fungsi aplikasi, rekam medis dan integrasi, serta klasifikasi data |
| Instansi pemerintah | Aturan SPBE, keamanan dan pengadaan sesuai sistem/instansi |
| E-commerce | Aturan perdagangan elektronik/perlindungan konsumen sesuai peran operator |
| Perangkat/IoT/safety-critical | Standar produk/perangkat dan keselamatan terkait, bukan hanya software umum |

Tabel adalah pemicu riset, bukan daftar regulasi yang otomatis berlaku.
Gunakan BSN, JDIH regulator, BPK/peraturan.go.id, dan penerbit standar resmi.
Periksa pencabutan, revisi, putusan, transisi, dan tanggal efektif. Jangan
menyimpulkan sektor "tidak diatur" hanya karena satu pencarian kosong.

## 5. Evidence-first compliance

Gunakan kolom pada katalog:
`Acuan → Topik/klausul → Applicability → Requirement → Control → Document →
Test → Evidence → Status → Gap → Owner/action`.

Aturan:
1. Nomor klausul/pasal hanya ditulis jika teksnya dibaca dari sumber sah.
2. Metadata/abstrak hanya mendukung identitas dan cakupan topik.
3. Requirement/acceptance criteria mendeskripsikan yang diinginkan;
   bukti implementasi dan hasil uji menjelaskan yang benar-benar tercapai.
4. SOP/risk register yang baru dibuat bukan bukti kontrol telah dijalankan.
5. Klaim reviewed-met-within-scope memerlukan bukti, reviewer, tanggal,
   metode penilaian, dan batas scope. Jangan otomatis memberi status ini.
6. Sertifikat memerlukan validasi issuer, scope, masa berlaku, dan edisi;
   jangan menyimpulkan seluruh produk certified dari sertifikat organisasi.
7. Gunakan review legal/auditor/LPK berwenang sesuai skema bila diperlukan.

## 6. Keluaran dan batas klaim

Selalu sampaikan:
- Acuan terverifikasi dan tanggal cek.
- Applicability confirmed/proposed/open, serta dasar wajib/sukarela/kontrak.
- Kedalaman mapping: topik atau klausul.
- Bukti yang tersedia dan yang belum ada.
- Gap, remediasi, owner, dan blocker.

Boleh: "Struktur dokumen mengacu pada topik standar berikut; mapping klausul
dan verifikasi implementasi belum dilakukan."
Tidak boleh: "Aplikasi sudah memenuhi seluruh SNI" hanya dari paket dokumen,
"tersertifikasi SNI" tanpa sertifikat sah, atau "seluruh regulasi terpenuhi"
tanpa scope/bukti/review yang mendukung.

Hormati lisensi: jangan mendistribusikan salinan teks standar berbayar atau
menyalin klausul panjang tanpa hak. Paket skill berisi instruksi, ringkasan
buatan sendiri, dan tautan, bukan salinan dokumen SNI.
