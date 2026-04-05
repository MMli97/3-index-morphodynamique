#!/usr/bin/env python3
"""
Paper 3 — Figure generation scripts
Inter-annotator Robustness and Structural Primacy of Gradients
in a Gradient-Based Organizational Classification

Usage: python paper3_figures.py
Outputs: paper3_fig1_gradient_space.pdf
         paper3_fig2_heatmap.pdf
         paper3_fig3_bland_altman.pdf
         paper3_fig4_a3a4.pdf
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from scipy.stats import spearmanr

# ============================================================
# DATA: 24 systems with complete scores from all 3 annotators
# (excluding Microbiome, Coral reef, Archive, PostgreSQL — no GPT-4 data)
# ============================================================

SYSTEMS = [
    'Cell', 'Supply ch.', 'LLM', 'Linux', 'Ant colony',
    'BGP', 'ECB', 'Wikipedia', 'Forest', 'Market',
    'Bitcoin', 'Neural net', 'Benedictine', 'Grid', 'Pipeline',
    'Constit.', 'Bureaucr.', 'Thermostat', 'NaCl', 'Occupy',
    'Startup', 'Pr. army', 'Parliament', 'Coll. art.'
]

# A0 (human + Claude) scores: [A1, A2, A3, A4, A5]
A0 = np.array([
    [0.9,1.0,1.0,1.0,0.6], [0.9,1.0,0.4,0.6,0.7], [0.7,1.0,0.6,0.2,0.1],
    [1.0,0.9,0.9,0.9,1.0], [0.9,0.9,0.8,0.8,0.5],
    [0.9,1.0,0.6,0.8,0.4], [0.9,1.0,0.8,1.0,0.7], [0.9,0.9,0.8,0.9,0.8],
    [1.0,1.0,0.8,0.8,0.8], [0.9,0.8,0.7,0.8,0.4],
    [0.8,0.9,0.9,0.8,0.4], [1.0,1.0,1.0,1.0,0.9], [0.9,0.9,0.9,1.0,0.7],
    [1.0,1.0,0.9,0.9,0.6], [0.8,0.8,0.8,0.9,0.4],
    [0.9,1.0,0.8,1.0,0.7], [0.9,0.7,0.8,1.0,0.5],
    [0.7,0.7,0.9,0.7,0.1], [0.5,0.8,0.6,0.5,0.2], [0.6,0.9,0.4,0.3,0.7],
    [0.6,0.8,0.5,0.5,1.0], [0.9,0.9,0.8,1.0,0.4],
    [0.9,1.0,0.3,0.2,0.2], [0.6,0.8,0.4,0.4,0.8],
], dtype=float)

# Gemini v2 scores
Gem = np.array([
    [1.0,1.0,0.9,0.9,0.6], [1.0,1.0,0.4,0.7,1.0], [0.7,1.0,0.8,0.2,0.0],
    [1.0,0.9,1.0,1.0,0.8], [0.9,1.0,1.0,1.0,0.9],
    [1.0,1.0,0.7,0.9,0.4], [1.0,1.0,0.8,1.0,0.9], [1.0,0.9,1.0,0.9,0.9],
    [1.0,1.0,0.9,0.9,0.9], [0.9,0.9,0.9,1.0,0.7],
    [0.9,1.0,1.0,1.0,0.4], [1.0,1.0,1.0,1.0,1.0], [0.9,1.0,1.0,1.0,0.8],
    [1.0,0.9,1.0,0.9,0.8], [0.9,0.9,1.0,0.9,0.2],
    [1.0,1.0,1.0,1.0,0.6], [1.0,0.9,0.9,1.0,0.6],
    [0.6,0.7,0.8,0.7,0.0], [0.5,0.7,0.5,0.3,0.2], [0.0,0.7,0.3,0.2,0.8],
    [0.9,1.0,1.0,0.8,1.0], [1.0,1.0,1.0,0.8,0.4],
    [0.9,1.0,0.2,0.1,0.9], [0.5,1.0,0.7,0.7,1.0],
], dtype=float)

# GPT-4 scores
GPT = np.array([
    [1.0,1.0,1.0,0.9,0.8], [1.0,1.0,1.0,0.9,0.9], [0.8,0.9,0.7,0.5,0.0],
    [1.0,0.9,1.0,0.9,0.9], [1.0,0.9,0.9,0.8,0.7],
    [1.0,1.0,0.7,0.9,0.7], [1.0,1.0,0.9,1.0,0.9], [1.0,1.0,0.9,1.0,0.9],
    [1.0,1.0,1.0,0.8,0.8], [0.8,0.8,0.7,0.8,0.4],
    [1.0,1.0,1.0,0.8,0.6], [1.0,1.0,1.0,0.8,0.9], [0.9,0.8,0.9,0.9,0.5],
    [1.0,1.0,1.0,0.9,0.9], [1.0,0.9,0.9,1.0,0.5],
    [1.0,1.0,1.0,1.0,1.0], [0.9,1.0,0.8,1.0,0.4],
    [0.5,0.8,0.8,0.7,0.1], [0.8,1.0,0.8,0.7,0.3], [0.9,0.9,0.8,0.8,1.0],
    [1.0,1.0,0.7,0.7,1.0], [0.9,1.0,0.6,1.0,0.9],
    [0.6,1.0,0.1,0.4,0.3], [0.5,0.9,0.4,0.5,0.9],
], dtype=float)

N = len(SYSTEMS)

# Gradient functions
def d23(s): return s[1] - s[2]
def d45(s): return s[3] - s[4]


# ============================================================
# FIGURE 1: Gradient space Delta23 x Delta45, three annotators
# ============================================================
def fig1_gradient_space(outpath='paper3_fig1_gradient_space.pdf'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    colors = {'A0': '#2166ac', 'Gemini': '#b2182b', 'GPT-4': '#4dac26'}

    for idx in range(N):
        xs = [d23(A0[idx]), d23(Gem[idx]), d23(GPT[idx])]
        ys = [d45(A0[idx]), d45(Gem[idx]), d45(GPT[idx])]

        # Inter-annotator triangle
        ax.plot(xs, ys, color='gray', alpha=0.25, linewidth=0.8, zorder=1)

        # Points per annotator
        ax.scatter(xs[0], ys[0], c=colors['A0'], marker='o', s=35, zorder=3, alpha=0.8)
        ax.scatter(xs[1], ys[1], c=colors['Gemini'], marker='s', s=35, zorder=3, alpha=0.8)
        ax.scatter(xs[2], ys[2], c=colors['GPT-4'], marker='^', s=35, zorder=3, alpha=0.8)

        # Label at centroid
        ax.annotate(SYSTEMS[idx], (np.mean(xs), np.mean(ys)),
                    fontsize=5.5, ha='center', va='bottom',
                    xytext=(0, 4), textcoords='offset points', color='#333333')

    # Regime boundaries
    ax.axhline(y=0.40, color='red', linestyle='--', alpha=0.3, linewidth=1)
    ax.axhline(y=0.05, color='green', linestyle='--', alpha=0.3, linewidth=1)
    ax.axvline(x=0.23, color='purple', linestyle='--', alpha=0.3, linewidth=1)

    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['A0'], markersize=8, label='A0 (human+Claude)'),
        Line2D([0], [0], marker='s', color='w', markerfacecolor=colors['Gemini'], markersize=8, label='Gemini v2'),
        Line2D([0], [0], marker='^', color='w', markerfacecolor=colors['GPT-4'], markersize=8, label='GPT-4'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=8)
    ax.set_xlabel('Δ₂₃ = A2 − A3  (propagation − integration)', fontsize=10)
    ax.set_ylabel('Δ₄₅ = A4 − A5  (normativity − revision)', fontsize=10)
    ax.set_title('Figure 1 — Gradient space across three annotators', fontsize=11)
    ax.grid(True, alpha=0.15)
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.savefig(outpath.replace('.pdf', '.png'), dpi=200)
    plt.close()
    print(f"  {outpath} saved")


# ============================================================
# FIGURE 2: Heatmap of divergences system × axis
# ============================================================
def fig2_heatmap(outpath='paper3_fig2_heatmap.pdf'):
    fig, axes_arr = plt.subplots(1, 2, figsize=(14, 8))
    diff_gem = np.abs(A0 - Gem)
    diff_gpt = np.abs(A0 - GPT)
    axis_labels = ['A1', 'A2', 'A3', 'A4', 'A5']

    for ax_idx, (diff, title) in enumerate([(diff_gem, 'A0 vs Gemini v2'), (diff_gpt, 'A0 vs GPT-4')]):
        ax = axes_arr[ax_idx]
        im = ax.imshow(diff, cmap='YlOrRd', vmin=0, vmax=0.6, aspect='auto')
        ax.set_xticks(range(5))
        ax.set_xticklabels(axis_labels, fontsize=9)
        ax.set_yticks(range(N))
        ax.set_yticklabels(SYSTEMS, fontsize=6.5)
        ax.set_title(title, fontsize=10)
        for i in range(N):
            for j in range(5):
                val = diff[i, j]
                color = 'white' if val > 0.35 else 'black'
                ax.text(j, i, f'{val:.1f}', ha='center', va='center', fontsize=5.5, color=color)

    plt.colorbar(im, ax=axes_arr, shrink=0.6, label='|Δ score|')
    plt.suptitle('Figure 2 — Absolute divergence by system × axis', fontsize=12)
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.savefig(outpath.replace('.pdf', '.png'), dpi=200)
    plt.close()
    print(f"  {outpath} saved")


# ============================================================
# FIGURE 3: Bland-Altman plots for Delta45
# ============================================================
def fig3_bland_altman(outpath='paper3_fig3_bland_altman.pdf'):
    fig, axes_arr = plt.subplots(1, 3, figsize=(15, 5))
    pairs = [('A0', 'Gemini v2', A0, Gem), ('A0', 'GPT-4', A0, GPT), ('Gemini v2', 'GPT-4', Gem, GPT)]

    for ax_idx, (name1, name2, d1, d2) in enumerate(pairs):
        ax = axes_arr[ax_idx]
        d45_1 = np.array([d45(d1[i]) for i in range(N)])
        d45_2 = np.array([d45(d2[i]) for i in range(N)])

        mean_val = (d45_1 + d45_2) / 2
        diff_val = d45_1 - d45_2

        ax.scatter(mean_val, diff_val, c='#2166ac', s=50, alpha=0.7, edgecolors='white', linewidth=0.5)

        md = np.mean(diff_val)
        sd = np.std(diff_val)
        ax.axhline(y=md, color='red', linestyle='-', linewidth=1, label=f'Mean: {md:.2f}')
        ax.axhline(y=md+1.96*sd, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
        ax.axhline(y=md-1.96*sd, color='red', linestyle='--', linewidth=0.8, alpha=0.5)
        ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

        # Label outliers
        for i in range(N):
            if abs(diff_val[i]) > 0.4:
                ax.annotate(SYSTEMS[i], (mean_val[i], diff_val[i]), fontsize=6,
                           xytext=(5, 5), textcoords='offset points')

        rho, p = spearmanr(d45_1, d45_2)
        ax.set_title(f'{name1} vs {name2}\nρ = {rho:.3f}', fontsize=10)
        ax.set_xlabel('Mean Δ₄₅', fontsize=9)
        ax.set_ylabel('Difference Δ₄₅', fontsize=9)
        ax.legend(fontsize=7)
        ax.set_ylim(-0.9, 0.9)
        ax.grid(True, alpha=0.15)

    plt.suptitle('Figure 3 — Bland-Altman plots for Δ₄₅', fontsize=12)
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.savefig(outpath.replace('.pdf', '.png'), dpi=200)
    plt.close()
    print(f"  {outpath} saved")


# ============================================================
# FIGURE 4: A3-A4 correlation per annotator
# ============================================================
def fig4_a3a4(outpath='paper3_fig4_a3a4.pdf'):
    fig, axes_arr = plt.subplots(1, 3, figsize=(15, 5))
    annotator_list = [('A0', A0, '#2166ac'), ('Gemini v2', Gem, '#b2182b'), ('GPT-4', GPT, '#4dac26')]

    for ax_idx, (name, data, color) in enumerate(annotator_list):
        ax = axes_arr[ax_idx]
        a3 = data[:, 2]
        a4 = data[:, 3]

        ax.scatter(a3, a4, c=color, s=50, alpha=0.7, edgecolors='white', linewidth=0.5)
        for i in range(N):
            ax.annotate(SYSTEMS[i], (a3[i], a4[i]), fontsize=5, alpha=0.6,
                       xytext=(3, 3), textcoords='offset points')

        # Regression line
        z = np.polyfit(a3, a4, 1)
        p_fn = np.poly1d(z)
        xs = np.linspace(0, 1.05, 50)
        ax.plot(xs, p_fn(xs), color=color, alpha=0.4, linestyle='--')

        rho, pval = spearmanr(a3, a4)
        ax.set_title(f'{name}: ρ = {rho:.3f} (p = {pval:.4f})', fontsize=10)
        ax.set_xlabel('A3 (Integration)', fontsize=9)
        ax.set_ylabel('A4 (Normativity)', fontsize=9)
        ax.set_xlim(-0.05, 1.1)
        ax.set_ylim(-0.05, 1.1)
        ax.plot([0,1], [0,1], 'k--', alpha=0.15)
        ax.grid(True, alpha=0.15)

    plt.suptitle('Figure 4 — A3–A4 correlation across annotators', fontsize=12)
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.savefig(outpath.replace('.pdf', '.png'), dpi=200)
    plt.close()
    print(f"  {outpath} saved")


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("Generating Paper 3 figures...")
    fig1_gradient_space()
    fig2_heatmap()
    fig3_bland_altman()
    fig4_a3a4()
    print("Done.")
