import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle
import numpy as np

os.makedirs(r"c:\Users\Rayhan\Documents\Antigravity\KS RPLD\proposal\figures", exist_ok=True)
fig_dir = r"c:\Users\Rayhan\Documents\Antigravity\KS RPLD\proposal\figures"

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# -------------------------------------------------------------
# FIG 1: Figma Design Thinking 5-Stage Framework
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 3.2), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3.2)
ax.axis('off')

stages = [
    ("1. EMPATHIZE", "Memahami Pengguna,\nEfek Protégé, &\nAudit Repo Legacy", "#1E40AF", "Bobot: 20%"),
    ("2. DEFINE", "Empathy Map, 3 Persona,\nHMW Statements, &\nGap Analysis", "#4338CA", "Bobot: 20%"),
    ("3. IDEATE", "Web Platform, AI Script,\nGamifikasi Protégé, &\nImpact-Effort Matrix", "#0284C7", "Bobot: 25%"),
    ("4. PROTOTYPE", "User Flow, Arsitektur,\nWireframe & High-Fi\nInteractive Web App", "#D97706", "Bobot: 25%"),
    ("5. TEST", "Skenario UT (4 Tasks),\nMetrik SUS (>82), &\nFeedback Loop Iterasi", "#059669", "Bobot: 10%")
]

for i, (title, desc, color, weight) in enumerate(stages):
    x = 0.2 + i * 1.95
    box = FancyBboxPatch((x, 0.4), 1.7, 2.4, boxstyle="round,pad=0.08,rounding_size=0.15",
                         edgecolor=color, facecolor="#F8FAFC", linewidth=2)
    ax.add_patch(box)
    
    header_box = FancyBboxPatch((x, 2.15), 1.7, 0.65, boxstyle="round,pad=0.05,rounding_size=0.15",
                                edgecolor=color, facecolor=color, linewidth=1)
    ax.add_patch(header_box)
    ax.text(x + 0.85, 2.45, title, color="white", fontsize=9, fontweight='bold', ha='center', va='center')
    ax.text(x + 0.85, 1.4, desc, color="#334155", fontsize=7.5, ha='center', va='center', linespacing=1.3)
    ax.text(x + 0.85, 0.65, weight, color=color, fontsize=8, fontweight='bold', ha='center', va='center')
    
    if i < 4:
        ax.annotate('', xy=(x + 1.92, 1.6), xytext=(x + 1.72, 1.6),
                    arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2, mutation_scale=15))

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig1_design_thinking_framework.png"), bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIG 2: Empathy Map Synthesis
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis('off')

# Central circle
center = plt.Circle((4, 3), 0.9, color="#1E40AF", ec="#1E3A8A", lw=2)
ax.add_patch(center)
ax.text(4, 3.15, "CALON PENGGUNA", color="white", fontsize=8.5, fontweight='bold', ha='center', va='center')
ax.text(4, 2.8, "(Pelajar, Mahasiswa,\nJob Seeker, Dosen)", color="#BFDBFE", fontsize=7, ha='center', va='center')

quadrants = [
    ("SAYS (Apa yang Dikatakan)", [
        "• 'Saya paham saat nonton tutorial, tapi lupa total saat coba sendiri.'",
        "• 'Membuat tutorial video itu repot, harus rekam ulang kalau salah klik.'",
        "• 'Saya ingin belajar skill baru yang langsung terbukti portofolionya.'"
    ], 0.3, 3.2, 3.4, 2.5, "#EFF6FF", "#3B82F6"),
    
    ("THINKS (Apa yang Dipikirkan)", [
        "• 'Apakah pemahaman saya sudah cukup dalam untuk mengajari orang lain?'",
        "• 'Bagaimana menyederhanakan materi rumit jadi langkah visual mudah?'",
        "• 'Belajar dengan mengajar tampaknya seru tapi butuh alat yang praktis.'"
    ], 4.3, 3.2, 3.4, 2.5, "#F5F3FF", "#8B5CF6"),
    
    ("DOES (Apa yang Dilakukan)", [
        "• Mengumpulkan puluhan bookmark tutorial video tanpa pernah mempraktikkannya.",
        "• Mengandalkan screenshot statis dan dokumen Word/PDF yang membosankan.",
        "• Berhenti di tengah jalan karena terjebak 'tutorial hell'."
    ], 0.3, 0.3, 3.4, 2.5, "#ECFDF5", "#10B981"),
    
    ("FEELS (Apa yang Dirasakan)", [
        "• Cemas & 'imposter syndrome' ketika mempelajari keterampilan teknologi baru.",
        "• Jenuh dengan metode belajar pasif (menatap layar berjam-jam).",
        "• Bangga & sangat puas ketika karya tutorialnya membantu orang lain."
    ], 4.3, 0.3, 3.4, 2.5, "#FEF3C7", "#F59E0B")
]

for title, bullets, qx, qy, qw, qh, bg, border in quadrants:
    box = FancyBboxPatch((qx, qy), qw, qh, boxstyle="round,pad=0.08,rounding_size=0.15",
                         edgecolor=border, facecolor=bg, linewidth=1.5)
    ax.add_patch(box)
    ax.text(qx + 0.15, qy + qh - 0.25, title, color="#0F172A", fontsize=9, fontweight='bold', va='top')
    text_y = qy + qh - 0.65
    for b in bullets:
        ax.text(qx + 0.15, text_y, b, color="#334155", fontsize=7.2, va='top', wrap=True)
        text_y -= 0.55

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig2_empathy_map.png"), bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIG 3: User Personas
# -------------------------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(11, 4.5), dpi=300)
personas = [
    {
        "name": "Rian Pratama (21 th)",
        "role": "Mahasiswa Informatika UGM",
        "avatar_bg": "#DBEAFE",
        "border": "#2563EB",
        "goal": "Tujuan: Menguasai alur DevOps & Git workflow, serta memiliki portofolio edukatif.",
        "pain": "Pain Point: Mengalami 'tutorial hell' & malas mengedit video tutorial MP4 yang memakan spek laptop.",
        "need": "Kebutuhan: Web tool no-code yang bisa merekam langkah animasi terminal secara instan."
    },
    {
        "name": "Siti Rahma (25 th)",
        "role": "Career Switcher ke UI/UX & Data",
        "avatar_bg": "#FCE7F3",
        "border": "#DB2777",
        "goal": "Tujuan: Memahami logika tools baru (Excel & Figma) secara mendalam lewat teknik Feynman.",
        "pain": "Pain Point: Kehilangan fokus bila tutorial teks terlalu panjang tanpa arahan interaktif.",
        "need": "Kebutuhan: Mode latihan interaktif (active recall) dengan panduan kursor jelas."
    },
    {
        "name": "Budi Santoso (34 th)",
        "role": "Instruktur Vokasi & Edukator",
        "avatar_bg": "#FEF3C7",
        "border": "#D97706",
        "goal": "Tujuan: Memproduksi puluhan modul tutorial software untuk muridnya secara cepat.",
        "pain": "Pain Point: Frustrasi jika salah klik harus rekam ulang video dari awal.",
        "need": "Kebutuhan: Kemudahan edit koordinat per langkah, bantuan dekomposisi AI, & ekspor LMS."
    }
]

for ax, p in zip(axs, personas):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    box = FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.03,rounding_size=0.08",
                         edgecolor=p["border"], facecolor="#FFFFFF", linewidth=2)
    ax.add_patch(box)
    top_box = FancyBboxPatch((0.02, 0.72), 0.96, 0.26, boxstyle="round,pad=0.02,rounding_size=0.08",
                            edgecolor=p["border"], facecolor=p["avatar_bg"], linewidth=1)
    ax.add_patch(top_box)
    ax.text(0.5, 0.88, p["name"], color="#0F172A", fontsize=9.5, fontweight='bold', ha='center', va='center')
    ax.text(0.5, 0.78, p["role"], color="#475569", fontsize=8, ha='center', va='center')
    
    ax.text(0.06, 0.62, p["goal"], color="#1E293B", fontsize=7.2, va='top', wrap=True)
    ax.text(0.06, 0.40, p["pain"], color="#991B1B", fontsize=7.2, va='top', wrap=True)
    ax.text(0.06, 0.18, p["need"], color="#065F46", fontsize=7.2, va='top', wrap=True)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig3_user_personas.png"), bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIG 4: Impact vs Effort Prioritization Matrix
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Outer border & axes
rect = patches.Rectangle((1, 1), 8, 8, linewidth=1.5, edgecolor='#64748B', facecolor='none')
ax.add_patch(rect)
ax.plot([5, 5], [1, 9], color='#94A3B8', linestyle='--', linewidth=1.5)
ax.plot([1, 9], [5, 5], color='#94A3B8', linestyle='--', linewidth=1.5)

# Quadrant titles
ax.text(3, 8.5, "QUICK WINS (Prioritas Utama)", color="#15803D", fontsize=9, fontweight='bold', ha='center')
ax.text(7, 8.5, "MAJOR STRATEGIC BETS", color="#1D4ED8", fontsize=9, fontweight='bold', ha='center')
ax.text(3, 1.4, "FILL-INS / NICE TO HAVE", color="#B45309", fontsize=9, fontweight='bold', ha='center')
ax.text(7, 1.4, "THANKLESS TASKS (Hindari)", color="#B91C1C", fontsize=9, fontweight='bold', ha='center')

# Feature points
features = [
    # Quick wins (High impact, low effort)
    ("Visual Drag-and-Drop Canvas", 2.8, 7.6, "#15803D"),
    ("Web Audio TTS Narration", 3.5, 6.8, "#15803D"),
    ("Format Terbuka .gtut (JSON)", 2.2, 5.8, "#15803D"),
    
    # Major Bets (High impact, high effort)
    ("AI Script-to-Animation Engine", 6.8, 7.8, "#1D4ED8"),
    ("Gamatutor Community Hub & Forking", 7.4, 6.6, "#1D4ED8"),
    ("Interactive Active Recall Checkpoints", 6.2, 5.8, "#1D4ED8"),
    
    # Fill-ins (Low impact, low effort)
    ("Tema Tampilan (Dark/Light Mode)", 2.5, 3.8, "#B45309"),
    ("Custom Avatar Profil", 3.5, 2.6, "#B45309"),
    
    # Thankless (Low impact, high effort)
    ("Porting Manual ke Delphi XE Desktop", 7.5, 3.2, "#B91C1C"),
    ("Dukungan Format Flash .swf Kuno", 6.8, 2.2, "#B91C1C")
]

for name, x, y, c in features:
    ax.plot(x, y, 'o', color=c, markersize=8)
    ax.text(x + 0.2, y, name, color="#0F172A", fontsize=7.8, va='center')

ax.text(5, 0.4, "EFFORT (Tingkat Kerumitan & Waktu Pengembangan) →", color="#334155", fontsize=9, fontweight='bold', ha='center')
ax.text(0.3, 5, "← IMPACT (Dampak Pembelajaran & Gerakan)", color="#334155", fontsize=9, fontweight='bold', rotation=90, va='center')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig4_impact_effort_matrix.png"), bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIG 5: System Architecture Diagram
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
ax.set_xlim(0, 9)
ax.set_ylim(0, 4.5)
ax.axis('off')

# Layers: Client, Application Engine, Data & Cloud
layers = [
    ("CLIENT LAYER (Web Browser)", 0.2, 3.0, 8.6, 1.2, "#DBEAFE", "#1E40AF", [
        ("Animation Studio UI", 0.5, 3.2),
        ("Interactive Player UI", 2.7, 3.2),
        ("Community Hub & Showcase", 4.9, 3.2),
        ("SkillQuest Gamification", 7.0, 3.2)
    ]),
    ("APPLICATION ENGINE & SERVICES", 0.2, 1.5, 8.6, 1.2, "#FEF3C7", "#D97706", [
        ("Canvas / WebAssembly Engine", 0.5, 1.7),
        ("Web Audio Synthesizer (TTS)", 2.7, 1.7),
        ("AI Metacognitive Prompt Engine", 4.9, 1.7),
        ("Interactive Checkpoint Evaluator", 7.0, 1.7)
    ]),
    ("STORAGE & BACKEND INFRASTRUCTURE", 0.2, 0.1, 8.6, 1.1, "#D1FAE5", "#059669", [
        ("REST & GraphQL APIs", 0.8, 0.3),
        ("Tutorial Repository (.gtut JSON)", 3.4, 0.3),
        ("Community Database & Leaderboards", 6.2, 0.3)
    ])
]

for title, lx, ly, lw, lh, bg, border, subs in layers:
    box = FancyBboxPatch((lx, ly), lw, lh, boxstyle="round,pad=0.05,rounding_size=0.1",
                         edgecolor=border, facecolor=bg, linewidth=1.5)
    ax.add_patch(box)
    ax.text(lx + 0.2, ly + lh - 0.25, title, color=border, fontsize=8.5, fontweight='bold', va='top')
    
    for stitle, sx, sy in subs:
        sbox = FancyBboxPatch((sx, sy), 1.9, 0.6, boxstyle="round,pad=0.03,rounding_size=0.06",
                              edgecolor=border, facecolor="#FFFFFF", linewidth=1)
        ax.add_patch(sbox)
        ax.text(sx + 0.95, sy + 0.3, stitle, color="#1E293B", fontsize=6.8, fontweight='bold', ha='center', va='center', wrap=True)

# Arrows between layers
ax.annotate('', xy=(4.5, 2.8), xytext=(4.5, 3.0), arrowprops=dict(arrowstyle="<->", color="#64748B", lw=1.5))
ax.annotate('', xy=(4.5, 1.3), xytext=(4.5, 1.5), arrowprops=dict(arrowstyle="<->", color="#64748B", lw=1.5))

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig5_system_architecture.png"), bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIG 6: User Flow Diagram
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 2.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 2.5)
ax.axis('off')

steps = [
    ("1. Pilih Keahlian", "Tentukan topik baru\n(Git, Excel, Medis)", "#3B82F6"),
    ("2. AI Assistance", "Dekomposisi langkah\nmetode Feynman", "#8B5CF6"),
    ("3. Desain di Studio", "Atur kursor, sorotan,\nbalon teks, & audio", "#0284C7"),
    ("4. Uji Pemahaman", "Preview animasi &\ntitik interaktif", "#F59E0B"),
    ("5. Terbit & Raih XP", "Publikasikan ke Hub,\ndapat Protégé Badge", "#10B981")
]

for i, (stitle, sdesc, scolor) in enumerate(steps):
    x = 0.2 + i * 1.95
    box = FancyBboxPatch((x, 0.3), 1.65, 1.8, boxstyle="round,pad=0.06,rounding_size=0.12",
                         edgecolor=scolor, facecolor="#F8FAFC", linewidth=2)
    ax.add_patch(box)
    
    badge = FancyBboxPatch((x, 1.5), 1.65, 0.6, boxstyle="round,pad=0.03,rounding_size=0.1",
                           edgecolor=scolor, facecolor=scolor, linewidth=1)
    ax.add_patch(badge)
    ax.text(x + 0.825, 1.8, stitle, color="white", fontsize=8, fontweight='bold', ha='center', va='center')
    ax.text(x + 0.825, 0.9, sdesc, color="#334155", fontsize=7.2, ha='center', va='center')
    
    if i < 4:
        ax.annotate('', xy=(x + 1.92, 1.2), xytext=(x + 1.68, 1.2),
                    arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2, mutation_scale=14))

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig6_user_flow.png"), bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIG 7: Usability Testing Target Metrics
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.2), dpi=300)

# SUS Score Gauge Comparison
bars = ax1.bar(['Gamatutor Legacy', 'Target Next-Gen'], [48.2, 84.5], color=['#EF4444', '#10B981'], width=0.55)
ax1.set_ylim(0, 100)
ax1.set_ylabel('Skor SUS (0 - 100)', fontsize=8, fontweight='bold')
ax1.set_title('System Usability Scale (SUS)', fontsize=9, fontweight='bold')
ax1.axhline(68, color='#64748B', linestyle='--', linewidth=1, label='Batas Rata-rata Industri (68)')
ax1.legend(fontsize=7, loc='upper left')
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{yval}", ha='center', va='bottom', fontsize=8, fontweight='bold')

# Task Completion Time (Minutes)
bars2 = ax2.bar(['Gamatutor Legacy', 'Target Next-Gen'], [24.5, 6.2], color=['#F59E0B', '#3B82F6'], width=0.55)
ax2.set_ylim(0, 30)
ax2.set_ylabel('Waktu Pembuatan Tutorial (Menit)', fontsize=8, fontweight='bold')
ax2.set_title('Efisiensi Waktu Authoring', fontsize=9, fontweight='bold')
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f"{yval} min", ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig7_usability_metrics.png"), bbox_inches='tight')
plt.close()

print("All figures successfully generated at:", fig_dir)
