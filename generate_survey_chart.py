import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# Set font family and style
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8

fig, axes = plt.subplots(2, 2, figsize=(14, 9.5), dpi=300)
fig.patch.set_facecolor('#ffffff')

# Title & Subtitle banner
fig.suptitle(
    'VALIDASI KEBUTUHAN PENGGUNA TERHADAP GAMATUTOR NEXT-GEN (N = 20 RESPONDEN)',
    fontsize=14, fontweight='bold', color='#0f172a', y=0.98
)
fig.text(
    0.5, 0.95,
    'Hasil Analisis Survei Empiris Calon Pengguna Gerakan "Mari Belajar Skill Baru dengan Membuat Tutorial Animatif"',
    ha='center', fontsize=9.5, color='#475569', style='italic'
)

# -------------------------------------------------------------
# Panel 1: Hambatan Utama Batal Membuat Tutorial (Top Left)
# -------------------------------------------------------------
ax1 = axes[0, 0]
ax1.set_facecolor('#f8fafc')
barriers = [
    'Beban Salah Rekam (Retake)',
    'Keterbatasan Spek Laptop',
    'Faktor Psikologis / Malu',
    'Bingung Struktur Materi',
    'Repot Mengedit Video'
]
barrier_vals = [25.0, 30.0, 55.0, 65.0, 80.0]
barrier_counts = [5, 6, 11, 13, 16]
colors1 = ['#93c5fd', '#60a5fa', '#3b82f6', '#2563eb', '#1d4ed8']

bars1 = ax1.barh(barriers, barrier_vals, color=colors1, height=0.55, edgecolor='#1e40af', linewidth=0.7)
ax1.set_xlim(0, 100)
ax1.set_title('A. Faktor Penghambat Utama Batal Membuat Tutorial', fontsize=10.5, fontweight='bold', color='#1e3a8a', pad=10)
ax1.set_xlabel('Persentase Responden (%)', fontsize=8.5, color='#334155')
ax1.grid(axis='x', linestyle='--', alpha=0.5, color='#cbd5e1')

for bar, val, count in zip(bars1, barrier_vals, barrier_counts):
    ax1.text(val + 1.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}% ({count}/20)', 
             va='center', ha='left', fontsize=8, fontweight='bold', color='#1e293b')

# -------------------------------------------------------------
# Panel 2: Fitur Inovatif yang Paling Diharapkan (Top Right)
# -------------------------------------------------------------
ax2 = axes[0, 1]
ax2.set_facecolor('#f8fafc')
features = [
    'Suara Narasi AI (TTS)',
    'Timeline & Keyframe',
    'Asisten AI Script-to-Anim',
    'Gamifikasi & Badges',
    'Mode Latihan Interaktif'
]
feature_vals = [20.0, 40.0, 55.0, 65.0, 65.0]
feature_counts = [4, 8, 11, 13, 13]
colors2 = ['#a7f3d0', '#6ee7b7', '#34d399', '#10b981', '#059669']

bars2 = ax2.barh(features, feature_vals, color=colors2, height=0.55, edgecolor='#047857', linewidth=0.7)
ax2.set_xlim(0, 100)
ax2.set_title('B. Fitur Inovatif Paling Menarik Minat Belajar', fontsize=10.5, fontweight='bold', color='#065f46', pad=10)
ax2.set_xlabel('Persentase Responden (%)', fontsize=8.5, color='#334155')
ax2.grid(axis='x', linestyle='--', alpha=0.5, color='#cbd5e1')

for bar, val, count in zip(bars2, feature_vals, feature_counts):
    ax2.text(val + 1.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}% ({count}/20)', 
             va='center', ha='left', fontsize=8, fontweight='bold', color='#1e293b')

# -------------------------------------------------------------
# Panel 3: Kendala Video Konvensional & Tutorial Hell (Bottom Left)
# -------------------------------------------------------------
ax3 = axes[1, 0]
ax3.set_facecolor('#f8fafc')
pain_labels = [
    'Tutor Lewati Detail',
    'Susah Cari Langkah Tertentu',
    'Boros Kuota & Memori',
    'Pasif & Mudah Hilang Fokus',
    'Mengalami Tutorial Hell'
]
pain_vals = [25.0, 35.0, 40.0, 45.0, 90.0]
pain_counts = [5, 7, 8, 9, 18]
colors3 = ['#fed7aa', '#fdba74', '#fb923c', '#f97316', '#dc2626']

bars3 = ax3.barh(pain_labels, pain_vals, color=colors3, height=0.55, edgecolor='#991b1b', linewidth=0.7)
ax3.set_xlim(0, 105)
ax3.set_title('C. Kendala Video Konvensional & Validasi "Tutorial Hell"', fontsize=10.5, fontweight='bold', color='#991b1b', pad=10)
ax3.set_xlabel('Persentase Responden (%)', fontsize=8.5, color='#334155')
ax3.grid(axis='x', linestyle='--', alpha=0.5, color='#cbd5e1')

for bar, val, count in zip(bars3, pain_vals, pain_counts):
    note = " (Skala 3-5)" if val == 90.0 else f" ({count}/20)"
    ax3.text(val + 1.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}%{note}', 
             va='center', ha='left', fontsize=8, fontweight='bold', color='#1e293b')

# -------------------------------------------------------------
# Panel 4: Validasi Adopsi & Kebutuhan Solusi Gamatutor (Bottom Right)
# -------------------------------------------------------------
ax4 = axes[1, 1]
ax4.set_facecolor('#f8fafc')

metrics = [
    'Belum Tahu GAE (Pasar Terbuka)',
    'Belum Pernah Pakai GAE Lama',
    'Siap Mencoba Gamatutor Baru',
    'Butuh Solusi Tutorial Animatif'
]
metric_vals = [95.0, 100.0, 85.0, 80.0]
metric_details = ['19/20 Belum Tahu', '20/20 Non-pengguna', 'Rerata: 3.35/5.00', 'Rerata: 3.25/5.00']
colors4 = ['#c084fc', '#a855f7', '#0284c7', '#0369a1']

bars4 = ax4.barh(metrics, metric_vals, color=colors4, height=0.55, edgecolor='#581c87', linewidth=0.7)
ax4.set_xlim(0, 115)
ax4.set_title('D. Kesiapan Adopsi & Peluang Remake Gamatutor', fontsize=10.5, fontweight='bold', color='#4c1d95', pad=10)
ax4.set_xlabel('Persentase Responden (%)', fontsize=8.5, color='#334155')
ax4.grid(axis='x', linestyle='--', alpha=0.5, color='#cbd5e1')

for bar, val, detail in zip(bars4, metric_vals, metric_details):
    ax4.text(val + 1.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}% ({detail})', 
             va='center', ha='left', fontsize=8, fontweight='bold', color='#1e293b')

plt.tight_layout(rect=[0, 0.03, 1, 0.94])

output_chart = r"c:\Users\Rayhan\Documents\Antigravity\KS RPLD\proposal\figures\fig9_survey_findings.png"
plt.savefig(output_chart, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

print(f"Chart saved successfully at: {output_chart}")
