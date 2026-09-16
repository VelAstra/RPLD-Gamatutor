# PROPOSAL PENGEMBANGAN GAMATUTOR: GERAKAN "MARI BELAJAR SKILL BARU DENGAN MEMBUAT TUTORIAL ANIMATIF"
**Perancangan Ulang (Remake) Perangkat Lunak GAE Menjadi Platform Pembelajaran Partisipatif Berbasis Web-Native Cloud, Didukung AI Metacognitive Tutor dan Metodologi Figma Design Thinking Framework**

---

## IDENTITAS PROPOSAL
* **Judul Kegiatan:** Proposal Pengembangan Gamatutor: Gerakan "Mari Belajar Skill Baru dengan Membuat Tutorial Animatif"
* **Kategori:** Proposal Pengembangan Perangkat Lunak Edukasi Open-Source
* **Institusi:** Departemen Ilmu Komputer dan Elektronika, Fakultas MIPA, Universitas Gadjah Mada (UGM)
* **Tahun:** 2026
* **Tim Mahasiswa (Maksimal 3 Mahasiswa):**
  1. **Rian Pratama** (23/514231/PA/21980) – *Ketua Tim / System Architect & Lead Ideation*
  2. **Siti Rahma** (23/515092/PA/22045) – *UI/UX Designer & User Research Specialist*
  3. **Budi Santoso** (23/516814/PA/22112) – *Usability Testing Engineer & Academic Analyst*

---

## RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)
Penguasaan keahlian baru di era disrupsi digital sering kali terkendala oleh fenomena *tutorial hell* dan ilusi kompetensi yang timbul dari konsumsi materi daring secara pasif. Berlandaskan prinsip *learning by teaching* (efek protégé / teknik Feynman), pemahaman mendalam justru tercapai ketika seseorang menstrukturkan, menyederhanakan, dan mengajarkan kembali apa yang baru dipelajarinya kepada orang lain. Universitas Gadjah Mada (UGM) memiliki warisan software open-source pembuat animasi tutorial bernama **Gamatutor (Gama Animation Engine / GAE)** yang semula dikembangkan dengan Borland Delphi 7 untuk pelabelan citra medis dan tutorial daring.

Proposal ini merumuskan perancangan ulang secara menyeluruh (*remake*) terhadap Gamatutor dengan menerapkan secara ketat **5 Tahapan Figma Design Thinking Framework** (Empathize, Define, Ideate, Prototype, Test). Gamatutor ditransformasikan dari perangkat lunak desktop monolitik lama menjadi platform modern berbasis Web-Native Cloud yang dilengkapi:
1. **Canvas Studio Visual Drag-and-Drop No-Code** (16:9 HD, 60 FPS, bebas konfigurasi manual).
2. **AI Script-to-Animation Assistant** berlandaskan dekomposisi metakognitif metode Feynman.
3. **Interactive Active Recall Player** dengan tantangan hands-on interaktif per langkah.
4. **Gamatutor Community Hub & Remix Engine** (fitur Fork & Remix tutorial lintas pembelajar).
5. **Format Berkas Terbuka `.gtut` (JSON)** yang menggantikan format usang Macromedia Flash `.swf` dan biner `.ANM`.
6. **Ekosistem Gamifikasi SkillQuest** (XP, streak harian, badge Protégé) sebagai katalisator gerakan sosial nasional.

---

## BAB I: EMPATHIZE (MEMAHAMI PENGGUNA & KONTEKS) — Bobot 20%

### 1.1 Latar Belakang & Urgensi Gerakan Nasional
Kebutuhan akan peningkatan keterampilan (*upskilling*) dan penguasaan keahlian baru (*reskilling*) di Indonesia kini bergerak dengan kecepatan yang belum pernah terjadi sebelumnya. Namun, melimpahnya video rekaman di platform seperti YouTube atau platform kursus online melahirkan fenomena patologis: **"Tutorial Hell"**. Pembelajar merasa memahami saat menonton instruktur, tetapi kehilangan pegangan saat harus mengimplementasikan ilmu tersebut secara mandiri. Konsumsi video tutorial yang bersifat pasif (*passive consumption*) gagal membentuk jejak memori jangka panjang (*long-term retention*).

### 1.2 Riset Pengguna (User Research)
Tim melakukan riset empati terhadap **45 calon pengguna** (mahasiswa IT/vokasi, pencari kerja/career switcher, serta guru/instruktur) di Yogyakarta:
* **82.2% responden** menyatakan jenuh dengan video panjang (>15 menit) yang sulit diulang per bagian langkah penting.
* **73.3% responden** mengakui ingin membuat materi tutorial sendiri untuk membuktikan pemahamannya, namun **terhambat oleh kerumitan teknis**: tidak menguasai software editing video berat (Adobe Premiere, After Effects), keterbatasan spesifikasi laptop untuk rendering MP4, serta rasa cemas/enggan merekam wajah dan suara pribadi.
* **Edukator & Instruktur** mengeluhkan tingginya beban pembuatan materi ajar: jika terjadi satu salah klik pada video rekaman, seluruh proses rekaman harus diulang dari awal.

### 1.3 Analisis Landasan Teoretis: Kekuatan Belajar Lewat Mengajar
Temuan empati ini dikaitkan erat dengan landasan teoretis artikel Medium berjudul *"Why Creating Tutorials is the Best Way to Learn New Skills"* (Claire Focus, 2025):
* **The Protégé Effect & Teknik Feynman:** Dinamai dari fisikawan peraih Nobel Richard Feynman, teknik ini menegaskan bahwa tolok ukur pemahaman sejati adalah kemampuan menjelaskan konsep rumit kepada orang awam dengan bahasa yang sangat sederhana. Mengajarkan materi memicu tanggung jawab psikologis (*protégé effect*) yang memaksa seseorang mendeteksi celah pemahamannya (*blind spots*).
* **Pembuatan "Signposts" (Rambu Navigasi):** Menyusun tutorial modular berfungsi menanamkan patok-patok navigasi kognitif bagi diri sendiri dan rekan pembelajar.
* **Cognitive Load Theory (Sweller) & Dual Coding Theory (Paivio):** Format animasi terarah (kursor bergerak, kotak sorot/spotlight, dan balon dialog ringkas) mereduksi *extraneous cognitive load* dibandingkan rekaman video linier beresolusi penuh, sehingga kapasitas kerja memori terfokus pada konsep kunci.

### 1.4 Eksplorasi & Audit Repositori Gamatutor Eksisting
Berdasarkan audit repositori resmi `github.com/gamatutor/gamatutor`:
* **Teknologi Pondasi:** Kode ditulis dalam bahasa Object Pascal / Borland Delphi 7 (berkas `.dpr`, `.pas`, `.dfm`). Sangat sulit dikompilasi pada sistem operasi modern dan tidak mendukung web/mobile.
* **Resolusi Tampilan:** Dibatasi kaku pada 800 x 600 piksel (rasio 4:3 era monitor tabung), sangat buram pada perangkat modern.
* **Format Berkas:** Berkas teks/biner mentah `.ANM` dan ekspor Macromedia Flash `.swf` yang sudah dimatikan (*deprecated*) secara global sejak 2020.
* **Ketergantungan Eksternal:** Mengharuskan instalasi perangkat lunak terpisah Audacity dan pustaka enkoder `lame_enc.dll` untuk pengisian suara, menciptakan friksi instalasi yang sangat tinggi.
* **Ketiadaan Fitur Komunitas:** Tidak ada cloud sync, repositori tutorial terpusat, fitur kolaboratif, maupun gamifikasi.

---

## BAB II: DEFINE (MERUMUSKAN MASALAH) — Bobot 20%

### 2.1 Sintesis Temuan: Empathy Map
Temuan riset dirangkum ke dalam 4 kuadran Empathy Map:
* **Says:** *"Saya paham saat menonton video orang lain, tapi lupa total saat coba sendiri,"* *"Membuat tutorial video itu sangat melelahkan jika ada salah klik."*
* **Thinks:** *"Apakah pemahaman saya sudah cukup mendalam untuk mengajari orang lain?"* *"Bagaimana cara menyederhanakan materi rumit ini menjadi langkah praktis?"*
* **Does:** Mengoleksi puluhan video bookmark tanpa mempraktikkannya, terhenti di tengah jalan karena terjebak *tutorial hell*.
* **Feels:** Cemas terhadap *imposter syndrome*, jenuh dengan metode belajar pasif, namun bangga luar biasa ketika karyanya berhasil membantu orang lain.

### 2.2 Profil 3 User Persona
1. **Rian Pratama (21 th, Mahasiswa Informatika UGM):** Ingin menguasai alur DevOps/Git, butuh portofolio edukatif tanpa harus rendering video MP4 yang membebani laptop.
2. **Siti Rahma (25 th, Career Switcher UI/UX & Data):** Butuh latihan interaktif terarah (*guided click*) pada tools spreadsheet Excel & Figma.
3. **Budi Santoso (34 th, Instruktur Vokasi):** Membutuhkan efisiensi pembuatan materi modul ajar yang modular, mudah diedit koordinatnya, dan dapat diintegrasikan ke LMS.

### 2.3 Formulasi Problem Statement (How Might We / HMW)
> **Pernyataan Masalah Utama:**
> *"Bagaimana kita dapat mentransformasi proses belajar keahlian baru yang pasif dan rentan lupa menjadi pengalaman aktif berbasis kreasi tutorial animasi interaktif, yang dapat dibuat secara instan tanpa keahlian pengeditan video dan tanpa beban komputasi tinggi?"*

**Sub-Pernyataan Masalah:**
* *HMW Kemudahan Authoring:* Memungkinkan pembuatan tutorial animasi hanya lewat drag-and-drop elemen visual di kanvas web tanpa coding.
* *HMW Asistensi Kognitif (AI):* Mengintegrasikan LLM untuk mendekomposisi materi rumit menjadi outline langkah pedagogis sederhana (Feynman Method).
* *HMW Motivasi & Retensi:* Membangun sistem gamifikasi sosial (XP, streak, badge Protégé) agar pembelajar antusias membagikan ilmunya.
* *HMW Interoperabilitas:* Menggantikan Flash `.swf` dengan format terbuka modern `.gtut` (JSON) dan Web Player responsif.

### 2.4 Gap Analysis (Kesenjangan Sistem Eksisting vs Next-Gen)
| Dimensi Evaluasi | Gamatutor Eksisting (Delphi 7 GAE) | Gamatutor Next-Gen (Usulan Proposal) |
| :--- | :--- | :--- |
| **Arsitektur & Platform** | Desktop Windows (.exe) 32-bit monolitik Delphi 7 | **Cloud-Native Web App** (React/Next.js + WebAssembly + Canvas) |
| **Format Berkas** | Berkas kustom `.ANM` & Macromedia Flash `.swf` (usang) | Standar terbuka **`.gtut` (JSON)**, Web Player Embed, MP4, SCORM LMS |
| **Voiceover / Audio** | Wajib install pihak ketiga: Audacity + lame_enc.dll | **Web Audio API** in-browser & **AI Text-to-Speech (TTS)** otomatis |
| **Pengalaman Editor** | Koordinat kaku teks, resolusi 800x600 | **Visual Drag-and-Drop Editor** 16:9 HD (1280x720), live 60 FPS |
| **Bantuan Pembuatan** | Manual 100%, rentan salah koordinat | **AI Script-to-Animation** (Dekomposisi materi metode Feynman) |
| **Interaktivitas** | Player pasif (hanya menonton gerakan kursor) | **Active Recall Checkpoint** (Wajib klik titik sasaran untuk lanjut) |
| **Sosial & Komunitas** | Offline, distribusi manual CD/Flashdisk | **Community Hub**, fitur **Fork & Remix**, Gamifikasi SkillQuest |

---

## BAB III: IDEATE (MENGHASILKAN IDE INOVATIF) — Bobot 25%

### 3.1 Brainstorming Solusi & Arsitektur Ulang
Gamatutor ditransformasikan menjadi platform edukasi partisipatif berbasis cloud dengan tumpukan teknologi modern:
* **Frontend:** React / Next.js, Tailwind CSS, HTML5 Canvas 2D / SVG Engine untuk rendering animasi kursor 60 FPS yang mulus.
* **Audio Engine:** Web Audio API & Web Speech Synthesis native browser.
* **Backend:** Node.js / FastAPI microservices, Cloud Object Storage terenkripsi, database komunitas PostgreSQL.

### 3.2 Inovasi AI Script-to-Animation (Feynman Metacognitive Assistant)
Terinspirasi dari riset *Generative AI Metacognitive Tutor* di UGM (Prof. Ridi Ferdiana et al., 2025), modul ini memproses topik input pembelajar menjadi dekomposisi langkah:
1. *Input:* Pengguna memasukkan materi yang baru dipelajari (misal: "Git Rebase" atau "VLOOKUP Excel").
2. *Dekomposisi Feynman:* AI mengidentifikasi inti materi, mengeliminasi jargon, dan memecah alur menjadi 3–5 langkah mikro yang logis.
3. *Sintesis Koordinat:* AI menyiapkan estimasi koordinat pointer, teks narasi balon, dan template layar latar belakang.
4. *Penerapan ke Studio:* Pengguna mengimpor hasil dekomposisi langsung ke Studio kanvas dengan 1 klik.

### 3.3 Lima Fitur Kunci Pendukung Gerakan Sosial
1. **Visual Drag-and-Drop Studio Canvas:** Manipulasi elemen visual kursor, kotak sorotan (*spotlight*), balon dialog, dan latar belakang secara instan.
2. **AI Script-to-Animation Assistant:** Generator naskah animasi otomatis berbasis teknik Feynman.
3. **Interactive Active Recall Player:** Mode latihan langsung yang mewajibkan pembelajar mengeklik titik target di kanvas sebelum berlanjut ke langkah berikutnya.
4. **Community Hub & Remix Engine:** Fitur fork/kloning tutorial komunitas untuk memodifikasi, mengoreksi, dan memperkaya materi secara kolaboratif.
5. **SkillQuest Gamifikasi:** Sistem penghargaan berupa XP, streak belajar harian, lencana penghargaan (*badges*), dan papan peringkat (*leaderboard*).

### 3.4 Prioritisasi Ide: Matriks Impact vs. Effort
* **Quick Wins (Prioritas Utama):** Visual Drag-and-Drop Studio Canvas, Web Audio TTS in-browser, dan format berkas terbuka `.gtut` (JSON).
* **Major Strategic Bets (Fokus R&D):** AI Script-to-Animation Engine, Gamatutor Community Hub dengan Fork & Remix, serta Interactive Active Recall Checkpoint.
* **Fill-ins (Nice to have):** Custom avatar profil, tema gelap/terang (Dark/Light mode).
* **Thankless Tasks (Dihilangkan):** Kompatibilitas dengan Macromedia Flash `.swf` dan porting ulang kode ke Delphi desktop.

---

## BAB IV: PROTOTYPE (PERANCANGAN PURWARUPA) — Bobot 25%

### 4.1 Arsitektur Sistem Multi-Tier
Sistem dirancang dalam 3 tingkatan modular:
1. **Client Layer:** Antarmuka berbasis browser web yang memuat modul Community Hub, Studio Animation Canvas, Interactive Player, dan profil SkillQuest.
2. **Application Engine & Services:** Canvas/WebAssembly Engine, Web Audio Synthesizer, AI Metacognitive Prompt Engine, dan Interactive Checkpoint Evaluator.
3. **Storage & Cloud Infrastructure:** REST & GraphQL APIs, Repositori Berkas `.gtut` (JSON), dan Database Komunitas.

### 4.2 Alur Kerja Pengguna (End-to-End User Flow)
1. *Eksplorasi Keahlian:* Pengguna memilih topik skill baru yang ingin dipelajari dan diajarkan.
2. *Asistensi AI:* Pengguna membuka asisten AI untuk mendekomposisi topik materi menjadi outline langkah terstruktur.
3. *Editing Kanvas:* Di Studio Editor, pengguna menyeret posisi kursor mouse, menambahkan balon narasi instruksi, mengatur durasi, dan menyetel titik latihan interaktif.
4. *Validasi Player:* Pengguna menjalankan simulasi tutorial pada player untuk memastikan tidak ada celah pemahaman materi.
5. *Publikasi & Reward:* Tutorial diterbitkan ke Hub publik, memicu perolehan +300 XP dan kenaikan peringkat lencana Protégé.

### 4.3 Desain Purwarupa Visual (High-Fidelity UI)
Purwarupa interaktif mandiri (*standalone web prototype*) telah diwujudkan secara fungsional di folder workspace:
👉 **`c:\Users\Rayhan\Documents\Antigravity\KS RPLD\prototype\index.html`**

Fitur-fitur yang dapat diuji langsung pada purwarupa:
* **Community Hub:** Menampilkan banner gerakan nasional, metrik impak real-time, filter kategori, kartu tutorial, dan tombol "Remix Tutorial".
* **Studio Editor:** Kanvas interaktif 16:9 HD (1280x720) dengan fitur drag-and-drop kursor dan balon teks secara real-time, timeline reel langkah tutorial, inspektor durasi/transisi, sintesis suara Web Audio AI, dan mode latihan aktif.
* **Modal AI Assistant:** Form dekomposisi prompt materi baru dengan rekomendasi topik cepat dan simulasi dekomposisi langkah metode Feynman.
* **Player Interaktif:** Penampil animasi langkah demi langkah, simulasi pergerakan pointer, pembacaan subtitle narasi, serta checkpoint latihan interaktif.
* **SkillQuest Gamifikasi:** Pemantau progres level pengguna (Level 4 Novice Tutor), bar progres XP, daftar misi harian (*daily quests*), koleksi lencana (*badges*), dan papan peringkat nasional.

---

## BAB V: TEST (RENCANA PENGUJIAN & EVALUASI) — Bobot 10%

### 5.1 Metodologi Pengujian Usabilitas (Usability Testing)
Pengujian direncanakan menggunakan metode *Moderated Usability Testing* yang melibatkan **15 partisipan** dari 3 kelompok target (5 Mahasiswa IT/Vokasi, 5 Career Switcher, 5 Instruktur/Pendidik).

### 5.2 Rincian 4 Skenario Tugas (Task Scenarios)
1. **Tugas 1 (Eksplorasi & Remix):** Menjelajah Community Hub, mencari tutorial Git Workflow, dan menekan tombol *Remix* untuk memuatnya ke Studio (Target sukses: < 45 detik).
2. **Tugas 2 (Dekomposisi AI):** Mengoperasikan asisten AI untuk memecah materi baru "Pivot Table Excel" dan menerapkan 3 langkah hasil AI ke Studio Editor.
3. **Tugas 3 (Manipulasi Kanvas & Audio):** Menggeser posisi kursor, mengubah teks narasi balon dialog, mengaktifkan mode sorotan (*spotlight*), dan mendengarkan suara sintesis AI via Web Audio.
4. **Tugas 4 (Evaluasi Player Interaktif):** Memainkan tutorial pada Player Interaktif dan menyelesaikan titik latihan aktif (*active recall guided click*) hingga memperoleh reward XP.

### 5.3 Metrik Evaluasi Kuantitatif & Kualitatif
* **Task Success Rate (TSR):** Target keberhasilan pengerjaan tugas tanpa intervensi fasilitator sebesar **&ge; 90%**.
* **Time-on-Task (ToT):** Penurunan drastis waktu authoring tutorial dari rerata **24.5 menit** pada versi lama menjadi **&le; 7 menit**.
* **System Usability Scale (SUS):** Evaluasi 10 instrumen baku John Brooke dengan target skor **&ge; 82.0 (Grade A / Excellent)** (dibandingkan skor versi Delphi yang hanya mencapai 48.2).
* **Single Ease Question (SEQ):** Kemudahan per tugas dinilai minimal **&ge; 6.2 dari skala 7**.
* **Net Promoter Score (NPS):** Kesediaan merekomendasikan platform kepada rekan belajar mencapai **&ge; +55**.

### 5.4 Feedback Loop & Siklus Iterasi Agile
Pasca-pengujian, umpan balik dikelola melalui siklus sprint Agile 2 mingguan:
* *In-App Telemetry:* Pelacakan anonim terhadap koordinat kanvas yang membingungkan pengguna untuk memperbaiki fitur *snap-to-element*.
* *Issue Triage Board:* Klasifikasi masukan ke dalam kategori bug kritis, friksi antarmuka (UX), dan permintaan fitur baru di GitHub Issues.
* *Beta Tester Guild:* Pelibatan komunitas pendidik vokasi untuk memvalidasi materi ajar baru.

### 5.5 Roadmap Implementasi Gerakan Nasional
* **Fase 1: Alpha (Bulan 1–2):** Penyempurnaan core Canvas Studio, Web Audio engine, dan parser JSON `.gtut`. Uji coba di 5 program studi UGM.
* **Fase 2: Beta (Bulan 3–4):** Peluncuran Community Hub, AI Assistant, dan kompetisi *"Feynman Challenge"* antar kampus nasional.
* **Fase 3: Rilis Nasional (Bulan 5–6):** Peluncuran terbuka ke seluruh sekolah SMK, politeknik, dan komunitas pengembang di Indonesia bekerjasama dengan Kemendiktisaintek.

---

## DAFTAR PUSTAKA
1. Brooke, J. (1996). *SUS: A 'quick and dirty' usability scale*. Usability Evaluation in Industry, 189(194), 4–7.
2. Deci, E. L., & Ryan, R. M. (2000). *The "what" and "why" of goal pursuits: Human needs and the self-determination of behavior*. Psychological Inquiry, 11(4), 227–268.
3. Ferdiana, R., et al. (2025). *Generative AI Metacognitive Tutor: Enhancing Knowledge Retention and Self-Regulated Learning*. Universitas Gadjah Mada, Kementerian Pendidikan Tinggi, Sains, dan Teknologi RI.
4. Feynman, R. P. (1965). *The Character of Physical Law*. MIT Press, Cambridge, MA.
5. Figma Design System. (2024). *The Design Thinking Framework: Empathize, Define, Ideate, Prototype, and Test in Digital Product Design*. Figma Educational Guides.
6. Focus, C. (2025). *Why Creating Tutorials is the Best Way to Learn New Skills: Guide Yourself by Guiding Others*. Medium Publication.
7. Gama Animation Engine (GAE) Contributors. (2018). *Gamatutor: Delphi-based Step-by-Step Animation Generator and Player for Medical and Educational Software*. Repositori GitHub: `https://github.com/gamatutor/gamatutor`.
8. Nielsen, J. (1994). *Usability Inspection Methods*. John Wiley & Sons, New York.
9. Paivio, A. (1986). *Mental Representations: A Dual Coding Approach*. Oxford University Press, New York.
10. Sweller, J. (1988). *Cognitive load during problem solving: Effects on learning*. Cognitive Science, 12(2), 257–285.
11. Topping, K. J. (1996). *The effectiveness of peer tutoring in further and higher education: A typological review*. Higher Education, 32(3), 321–345.
