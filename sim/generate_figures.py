from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES_DIR = Path("latex/figures")
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def figure1_architecture():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_facecolor("#f8f9fa")
    fig.patch.set_facecolor("#f8f9fa")

    boxes = [
        (0.4,  1.8, 2.0, 1.4, "#4C72B0", "Scenario\nGenerator",   "sim/main.py"),
        (2.8,  1.8, 2.0, 1.4, "#55A868", "AI Threat\nPrioritizer","ai_threat_model.py"),
        (5.2,  1.8, 2.0, 1.4, "#C44E52", "Quantum\nOptimizer",    "quantum_optimizer.py"),
        (7.6,  1.8, 2.0, 1.4, "#8172B2", "Metrics\nModule",       "metrics.py"),
        (10.0, 1.8, 1.6, 1.4, "#CCB974", "Security\nLayer",       "security_layer.py"),
    ]

    for x, y, w, h, color, label, sublabel in boxes:
        rect = plt.Rectangle((x, y), w, h, linewidth=1.5,
                              edgecolor="white", facecolor=color, zorder=3)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2 + 0.15, label,
                ha="center", va="center", fontsize=9,
                fontweight="bold", color="white", zorder=4)
        ax.text(x + w/2, y + 0.18, sublabel,
                ha="center", va="center", fontsize=6.5,
                color="white", alpha=0.85, zorder=4)

    arrow_xs = [2.4, 4.8, 7.2, 9.6]
    for ax_pos in arrow_xs:
        ax.annotate("",
                    xy=(ax_pos + 0.4, 2.5),
                    xytext=(ax_pos, 2.5),
                    arrowprops=dict(arrowstyle="-|>",
                                   color="#333333", lw=1.8),
                    zorder=5)

    ax.text(6.0, 4.5,
            "Proposed Hybrid Pipeline Architecture",
            ha="center", va="center",
            fontsize=12, fontweight="bold", color="#222222")

    ax.text(6.0, 0.5,
            "Figure 1: Modular pipeline for quantum-assisted edge AI counter-UAV swarm defense.",
            ha="center", va="center", fontsize=8, color="#555555")

    plt.tight_layout()
    out = FIGURES_DIR / "figure1_architecture.pdf"
    plt.savefig(out, bbox_inches="tight", dpi=150)
    plt.savefig(str(out).replace(".pdf", ".png"), bbox_inches="tight", dpi=150)
    plt.close()
    print(f"[INFO] Saved: {out}")


def figure2_results():
    metrics    = ["avg_distance\n(km)", "max_distance\n(km)",
                  "threat_weighted\nscore", "unassigned\nhigh_threat"]
    baseline   = [13.8124, 17.4228, -4.6847, 0.78]
    ai_prior   = [13.2096, 16.8740, -1.1495, 0.14]
    quantum_ph = [13.2096, 16.8740, -1.1495, 0.14]

    x     = np.arange(len(metrics))
    width = 0.25

    fig, ax = plt.subplots(figsize=(11, 5))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")

    ax.bar(x - width, baseline,   width, label="Baseline",           color="#4C72B0", edgecolor="white")
    ax.bar(x,         ai_prior,   width, label="AI-Prioritized",      color="#55A868", edgecolor="white")
    ax.bar(x + width, quantum_ph, width, label="Quantum-Placeholder", color="#C44E52", edgecolor="white")

    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=9)
    ax.set_ylabel("Metric Value", fontsize=10)
    ax.set_title(
        "Figure 2: Aggregate Results over 50 Simulation Runs (N=5 attackers, M=3 defenders)",
        fontsize=10, fontweight="bold", pad=12)
    ax.legend(fontsize=9, loc="upper right")
    ax.axhline(0, color="#888888", linewidth=0.8, linestyle="--")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    for bars in [
        ax.containers[0],
        ax.containers[1],
        ax.containers[2]
    ]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2,
                    h + (0.15 if h >= 0 else -0.45),
                    f"{h:.2f}",
                    ha="center", va="bottom",
                    fontsize=7, color="#333333")

    plt.tight_layout()
    out = FIGURES_DIR / "figure2_results.pdf"
    plt.savefig(out, bbox_inches="tight", dpi=150)
    plt.savefig(str(out).replace(".pdf", ".png"), bbox_inches="tight", dpi=150)
    plt.close()
    print(f"[INFO] Saved: {out}")


if __name__ == "__main__":
    figure1_architecture()
    figure2_results()
    print("[INFO] Both figures generated in latex/figures/")
