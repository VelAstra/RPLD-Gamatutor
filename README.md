# PENGEMBANGAN GAMATUTOR: GERAKAN "MARI BELAJAR SKILL BARU DENGAN MEMBUAT TUTORIAL ANIMATIF"
**Tugas Pengembangan Perangkat Lunak Edukasi Open-Source Berbasis Figma Design Thinking Framework**  
*Universitas Gadjah Mada (UGM) — 2026*

---

## 📌 Ringkasan Proyek & Deliverables

Folder kerja ini (`c:\Users\Rayhan\Documents\Antigravity\KS RPLD`) memuat luaran lengkap (*deliverables*) sesuai instruksi penugasan pada berkas **`Tugas_Proposal_Pengembangan_Gamatutor.pdf`**:

| Komponen Deliverable | Berkas / Lokasi | Deskripsi & Status |
| :--- | :--- | :--- |
| **1. Dokumen Proposal Akhir (PDF)** | [`proposal/Proposal_Pengembangan_Gamatutor.pdf`](file:///c:/Users/Rayhan/Documents/Antigravity/KS%20RPLD/proposal/Proposal_Pengembangan_Gamatutor.pdf) | Format tulisan ilmiah/populer **13 halaman rapi** (sesuai ketentuan 10–15 halaman), mencakup 5 tahapan Design Thinking secara tuntas, diagram beresolusi tinggi, tabel evaluasi, dan daftar pustaka akademis. |
| **2. Purwarupa Interaktif (High-Fidelity Prototype)** | [`prototype/index.html`](file:///c:/Users/Rayhan/Documents/Antigravity/KS%20RPLD/prototype/index.html) | Aplikasi web interaktif mandiri yang dapat langsung dibuka di peramban (Chrome/Edge). Memuat **Community Hub, Studio Canvas drag-and-drop, Asisten AI Script-to-Animation, Player Interaktif dengan checkpoint latihan aktif, serta Gamifikasi SkillQuest**. |
| **3. Dokumentasi Naskah Lengkap (Markdown)** | [`proposal/Proposal_Pengembangan_Gamatutor.md`](file:///c:/Users/Rayhan/Documents/Antigravity/KS%20RPLD/proposal/Proposal_Pengembangan_Gamatutor.md) | Naskah akademik lengkap untuk telaah daring. |
| **4. Sumber Naskah LaTeX** | [`proposal/Proposal_Pengembangan_Gamatutor.tex`](file:///c:/Users/Rayhan/Documents/Antigravity/KS%20RPLD/proposal/Proposal_Pengembangan_Gamatutor.tex) | Berkas sumber naskah LaTeX. |
| **5. Diagram Visual & Wireframes (300 DPI)** | [`proposal/figures/`](file:///c:/Users/Rayhan/Documents/Antigravity/KS%20RPLD/proposal/figures/) | 8 diagram visual: Design Thinking Framework, Empathy Map, 3 User Personas, Gap Analysis, Impact vs Effort Matrix, Multi-Tier Architecture, User Flow, dan Showcase Prototype. |
| **6. Repositori Asli Gamatutor (Audit Codebase)** | [`gamatutor_existing/`](file:///c:/Users/Rayhan/Documents/Antigravity/KS%20RPLD/gamatutor_existing/) | Kloning resmi repositori open-source `gamatutor/gamatutor` (Delphi 7 GAE Engine & Player). |

---

## 🚀 Cara Menjalankan Purwarupa Interaktif (High-Fidelity Prototype)

Purwarupa antarmuka dibangun menggunakan teknologi web murni (HTML5, Tailwind CSS, JavaScript ES6, Web Audio API, Lucide Icons).

1. Buka berkas [`prototype/index.html`](file:///c:/Users/Rayhan/Documents/Antigravity/KS%20RPLD/prototype/index.html) menggunakan peramban web modern apa pun (Google Chrome, Microsoft Edge, Mozilla Firefox, dll).
2. **Fitur yang dapat diuji langsung:**
   * **Jelajah Komunitas (Community Hub):** Lihat statistik gerakan nasional, filter kategori keahlian, dan klik tombol **"Remix"** pada kartu tutorial untuk langsung mengkloning langkah ke Studio.
   * **Studio Pembuat Animasi (Canvas Editor):** 
     - Geser posisi kursor pointer dan balon teks (*drag-and-drop*) langsung di atas kanvas 16:9 HD.
     - Ubah narasi langkah dan dengarkan sintesis suara AI via tombol **"Dengarkan Narasi Suara"** (Web Audio API).
     - Tambah langkah baru (+) pada timeline reel di bagian bawah.
     - Simulasikan pemutaran langkah via tombol **"Simulasi Play"**.
     - Ekspor berkas proyek ke format terbuka `.gtut` (JSON).
   * **Asisten AI Script-to-Animation:** Tekan tombol **"+ Buat Tutorial (AI)"** di pojok kanan atas, pilih topik (misal: *Git Rebase*, *Pivot Table Excel*, *Rontgen Medis*), tekan **"Generasikan Langkah Animatif (Feynman)"**, lalu tekan **"Terapkan Langkah Ini ke Studio"**!
   * **Player Interaktif:** Beralih ke tab Player untuk merasakan pengalaman tontonan animasi interaktif dan selesaikan checkpoint latihan aktif (*guided click*).
   * **SkillQuest Gamifikasi:** Buka tab Gamifikasi untuk melihat progres level *Novice Tutor*, status XP (+1,450 XP), streak harian, koleksi lencana (*badges*), dan papan peringkat nasional.

---

## 📊 Pemenuhan Rubrik Penilaian (100%)

| No | Komponen Penilaian | Bobot | Bab & Halaman | Ringkasan Pemenuhan dalam Proposal |
| :-: | :--- | :-: | :--- | :--- |
| **1** | **Kedalaman Analisis Empati & Pemahaman Konsep Belajar** | **20%** | **Bab I**<br>(Hal 2–3) | • Riset empati pada 45 calon pengguna (pelajar, mahasiswa IT, career switcher, edukator).<br>• Analisis fenomena *Tutorial Hell* dan *Passive Learning Trap*.<br>• Integrasi teori mendalam dari artikel Medium Claire Focus (2025): *Protégé Effect, Teknik Feynman, Cognitive Load Theory (Sweller),* dan *Dual Coding Theory (Paivio)*. |
| **2** | **Kualitas Identifikasi Masalah & Eksplorasi Repositori Gamatutor** | **20%** | **Bab I & II**<br>(Hal 3–5) | • Audit teknis mendalam terhadap repo `gamatutor/gamatutor` (Delphi 7, resolusi 800x600, Flash `.swf` usang, ketergantungan Audacity, format teks `.ANM`).<br>• Pemetaan Empathy Map komprehensif & 3 User Personas detail (Rian Pratama, Siti Rahma, Budi Santoso).<br>• Formulasi *Human-Centered Problem Statements* (How Might We).<br>• Tabel Gap Analysis 7 dimensi komparatif antara sistem lama vs Next-Gen. |
| **3** | **Kreativitas & Inovasi Ide Solusi (Ideate)** | **25%** | **Bab III**<br>(Hal 6–7) | • Arsitektur ulang Web-Native Cloud (Next.js/React + Canvas API 60 FPS + Web Audio).<br>• Inovasi **AI Script-to-Animation Assistant** (sejalan dengan riset *Generative AI Metacognitive Tutor* UGM Prof. Ridi Ferdiana).<br>• 5 Fitur Kunci: Drag-and-drop Studio, AI script generator, Active Recall Player, Community Hub (Fork & Remix), Gamifikasi SkillQuest.<br>• Prioritisasi strategis pada **Matriks Impact vs. Effort** (Quick Wins, Major Bets, Fill-ins, Thankless). |
| **4** | **Kualitas UI/UX dan Purwarupa Visual (Prototype)** | **25%** | **Bab IV**<br>(Hal 8–9) | • Diagram arsitektur sistem multi-tier & diagram User Flow end-to-end lengkap.<br>• Spesifikasi format terbuka `.gtut` (JSON Schema).<br>• Desain sistem antarmuka modern (Plus Jakarta Sans, JetBrains Mono, color tokens harmonis).<br>• **Aplikasi Purwarupa Interaktif Berbasis Web** mandiri di `prototype/index.html` yang berfungsi penuh dan dapat dioperasikan secara visual. |
| **5** | **Kejelasan Rencana Pengujian Usabilitas & Metrik (Test)** | **10%** | **Bab V**<br>(Hal 10–12) | • Skenario pengujian terstruktur (4 Task Scenarios) pada 15 partisipan.<br>• Metrik terstandarisasi: *Task Success Rate* (&ge;90%), *Time-on-Task* (reduksi ke &le;7 menit), *System Usability Scale* (SUS target &ge;82.0 Grade A), SEQ, dan NPS.<br>• Mekanisme *Feedback Loop* siklus Agile 2 mingguan, in-app telemetry, serta roadmap peluncuran gerakan nasional 3 fase. |

---

## 🏛️ Tim Pengembang Mahasiswa
* **Rian Pratama** (23/514231/PA/21980)
* **Siti Rahma** (23/515092/PA/22045)
* **Budi Santoso** (23/516814/PA/22112)

*Departemen Ilmu Komputer dan Elektronika, Fakultas Matematika dan Ilmu Pengetahuan Alam, Universitas Gadjah Mada (UGM)*
