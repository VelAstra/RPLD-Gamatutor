import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

fig_dir = r"c:\Users\Rayhan\Documents\Antigravity\KS RPLD\proposal\figures"

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11, 7.2), dpi=300)

def draw_mockup_window(ax, title, color):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    # Window Frame
    win = FancyBboxPatch((0.1, 0.1), 9.8, 5.8, boxstyle="round,pad=0.05,rounding_size=0.15",
                         edgecolor="#CBD5E1", facecolor="#FFFFFF", linewidth=1.5)
    ax.add_patch(win)
    # Header bar
    hbar = FancyBboxPatch((0.1, 5.1), 9.8, 0.8, boxstyle="round,pad=0.03,rounding_size=0.15",
                          edgecolor="#CBD5E1", facecolor="#F8FAFC", linewidth=1)
    ax.add_patch(hbar)
    # Window Controls
    ax.plot([0.5, 0.8, 1.1], [5.5, 5.5, 5.5], 'o', color="#94A3B8", markersize=5)
    ax.text(5.0, 5.5, title, color="#0F172A", fontsize=8.5, fontweight='bold', ha='center', va='center')

# Panel 1: Community Movement Hub
draw_mockup_window(ax1, "1. Community Hub: Gerakan Nasional Belajar Skill Baru", "#1E40AF")
hero = FancyBboxPatch((0.5, 3.2), 9.0, 1.6, boxstyle="round,pad=0.04,rounding_size=0.1",
                      edgecolor="#1E3A8A", facecolor="#0F172A", linewidth=1)
ax1.add_patch(hero)
ax1.text(5.0, 4.2, "Mari Belajar Skill Baru dengan Membuat Tutorial Animatif", color="#38BDF8", fontsize=8, fontweight='bold', ha='center')
ax1.text(5.0, 3.6, "12,480+ Tutorial Dibuat  |  84,200+ Pembelajar  |  92.4% Retensi Feynman", color="#E2E8F0", fontsize=6.8, ha='center')

# Cards below
for i, (ctitle, ccat) in enumerate([("Git Rebase Workflow", "Vokasi & IT"), ("Labeling Rontgen Paru", "Medis UGM"), ("Otomasi Excel XLOOKUP", "Produktivitas")]):
    cbox = FancyBboxPatch((0.5 + i*3.1, 0.4), 2.8, 2.5, boxstyle="round,pad=0.04,rounding_size=0.08",
                          edgecolor="#E2E8F0", facecolor="#F8FAFC", linewidth=1)
    ax1.add_patch(cbox)
    ax1.text(1.9 + i*3.1, 2.4, ccat, color="#2563EB", fontsize=6.5, fontweight='bold', ha='center')
    ax1.text(1.9 + i*3.1, 1.8, ctitle, color="#0F172A", fontsize=7.2, fontweight='bold', ha='center')
    ax1.text(1.9 + i*3.1, 0.9, "[ Play ]   [ Remix ]", color="#475569", fontsize=6.5, ha='center')

# Panel 2: Studio Animation Editor
draw_mockup_window(ax2, "2. Studio Pembuat Animasi: Canvas & Drag-and-Drop Inspector", "#0284C7")
# Left tools
tbox = FancyBboxPatch((0.4, 1.4), 0.9, 3.4, boxstyle="round,pad=0.02,rounding_size=0.05",
                      edgecolor="#E2E8F0", facecolor="#F1F5F9", linewidth=1)
ax2.add_patch(tbox)
ax2.text(0.85, 4.3, "Cursor", fontsize=6, fontweight='bold', ha='center')
ax2.text(0.85, 3.5, "Balon", fontsize=6, fontweight='bold', ha='center')
ax2.text(0.85, 2.7, "Sorot", fontsize=6, fontweight='bold', ha='center')
ax2.text(0.85, 1.9, "Latar", fontsize=6, fontweight='bold', ha='center')

# Canvas
carea = FancyBboxPatch((1.6, 1.4), 5.5, 3.4, boxstyle="round,pad=0.04,rounding_size=0.1",
                       edgecolor="#334155", facecolor="#0F172A", linewidth=1.5)
ax2.add_patch(carea)
ax2.text(4.3, 3.8, "$ git checkout -b feature/login", color="#38BDF8", fontsize=7.5, fontfamily='monospace', ha='center')
ax2.text(3.5, 2.8, "(Pointer)", color="#F59E0B", fontsize=7, fontweight='bold')
cmsg = FancyBboxPatch((4.2, 2.2), 2.6, 1.0, boxstyle="round,pad=0.02,rounding_size=0.05",
                      edgecolor="#2563EB", facecolor="#FFFFFF", linewidth=1)
ax2.add_patch(cmsg)
ax2.text(5.5, 2.7, "Buat branch terisolasi!", color="#1E3A8A", fontsize=6.2, fontweight='bold', ha='center')

# Right inspector
ibox = FancyBboxPatch((7.4, 1.4), 2.2, 3.4, boxstyle="round,pad=0.02,rounding_size=0.05",
                      edgecolor="#E2E8F0", facecolor="#F8FAFC", linewidth=1)
ax2.add_patch(ibox)
ax2.text(8.5, 4.3, "INSPEKTOR", color="#64748B", fontsize=6.5, fontweight='bold', ha='center')
ax2.text(8.5, 3.5, "Durasi: 5 Detik\nTransisi: Glide\nAudio: WebTTS\nTarget: Interaktif", color="#1E293B", fontsize=6.2, ha='center')

# Bottom timeline
tline = FancyBboxPatch((0.4, 0.3), 9.2, 0.9, boxstyle="round,pad=0.02,rounding_size=0.05",
                       edgecolor="#CBD5E1", facecolor="#E2E8F0", linewidth=1)
ax2.add_patch(tline)
ax2.text(5.0, 0.75, "TIMELINE: [Langkah 1 (5s)] - [Langkah 2 (5s)] - [Langkah 3 (5s)]  [+ Tambah Langkah]", color="#334155", fontsize=6.8, fontweight='bold', ha='center')

# Panel 3: Interactive Player
draw_mockup_window(ax3, "3. Player Interaktif: Pembelajaran Aktif & Active Recall", "#059669")
pscreen = FancyBboxPatch((1.2, 1.2), 7.6, 3.6, boxstyle="round,pad=0.04,rounding_size=0.1",
                         edgecolor="#1E293B", facecolor="#020617", linewidth=2)
ax3.add_patch(pscreen)
ax3.text(5.0, 4.0, "Langkah 2: Menandai Infiltrat pada Rontgen Toraks", color="#FFFFFF", fontsize=7.5, fontweight='bold', ha='center')
ax3.text(4.0, 2.8, "[ Citra Medis RME ]", color="#38BDF8", fontsize=7, ha='center')
tclick = FancyBboxPatch((5.4, 2.3), 2.8, 0.8, boxstyle="round,pad=0.02,rounding_size=0.05",
                        edgecolor="#10B981", facecolor="#064E3B", linewidth=1.5)
ax3.add_patch(tclick)
ax3.text(6.8, 2.7, "Titik Latihan: Klik Disini", color="#6EE7B7", fontsize=6.5, fontweight='bold', ha='center')
ax3.text(5.0, 0.6, "|<<   [ Play ]   >>|     ========O======== 00:04 / 00:15     Speed: 1.0x", color="#334155", fontsize=7, ha='center')

# Panel 4: AI Script Assistant & SkillQuest Gamification
draw_mockup_window(ax4, "4. AI Script-to-Animation Modal & SkillQuest Gamifikasi", "#D97706")
aimod = FancyBboxPatch((0.4, 0.5), 4.5, 4.3, boxstyle="round,pad=0.04,rounding_size=0.08",
                       edgecolor="#F59E0B", facecolor="#FFFBEB", linewidth=1.5)
ax4.add_patch(aimod)
ax4.text(2.65, 4.3, "AI Script Assistant", color="#92400E", fontsize=7.5, fontweight='bold', ha='center')
ax4.text(2.65, 3.6, "Skill: 'Pivot Table Excel'\nMetode: Feynman Simplification\n\nGenerated Steps:\n1. Blok Tabel Data Sumber\n2. Insert > Pivot Table\n3. Drag Kolom Kategori & Nilai", color="#78350F", fontsize=6.2, ha='center')
ax4.text(2.65, 0.9, "[ Terapkan ke Studio (+100 XP) ]", color="#059669", fontsize=6.8, fontweight='bold', ha='center')

gprof = FancyBboxPatch((5.2, 0.5), 4.4, 4.3, boxstyle="round,pad=0.04,rounding_size=0.08",
                       edgecolor="#3B82F6", facecolor="#EFF6FF", linewidth=1.5)
ax4.add_patch(gprof)
ax4.text(7.4, 4.3, "SkillQuest Gamifikasi", color="#1E40AF", fontsize=7.5, fontweight='bold', ha='center')
ax4.text(7.4, 3.5, "Level 4: Novice Tutor\nXP: 1,450 / 2,000\n5 Hari Streak Belajar", color="#1E3A8A", fontsize=6.8, ha='center')
ax4.text(7.4, 2.2, "Lencana Didapatkan:\n- Feynman Initiate\n- Signpost Maker\n- Remix Pioneer", color="#334155", fontsize=6.2, ha='center')
ax4.text(7.4, 0.9, "Leaderboard: #3 Nasional", color="#D97706", fontsize=6.5, fontweight='bold', ha='center')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "fig8_prototype_showcase.png"), bbox_inches='tight')
plt.close()
print("fig8_prototype_showcase.png cleanly regenerated without glyph warnings.")
