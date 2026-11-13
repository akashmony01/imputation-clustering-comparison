"""
Phase 2: Broader weight-sensitivity study for the 10-scale composite.

Runs composite_ranking under 6 weight regimes and reports:
- top-1 pipeline
- MF/Agg rank
- MICE/KM rank
- whether all four strong imputed pipelines occupy the top 4
- whether the six degenerate pipelines occupy the bottom 6

Appends results to conference-latex/rescore_results.md.

Reuses raw metric values and ranking logic from phase1_rescore.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from phase1_rescore import (
    RAW,
    TEN_PIPELINES,
    SHORT,
    METRIC_ORDER,
    METRIC_WEIGHTS_OURS,
    composite_ranking,
)


REGIMES = [
    ("Ours (balance-weighted)", METRIC_WEIGHTS_OURS),
    ("Equal", {m: 1.0 / 6 for m in METRIC_ORDER}),
    ("Silhouette-only", {
        "balance": 0.0, "silhouette": 1.0, "calinski_harabasz": 0.0,
        "dunn": 0.0, "davies_bouldin": 0.0, "xie_beni": 0.0,
    }),
    ("Balance-only", {
        "balance": 1.0, "silhouette": 0.0, "calinski_harabasz": 0.0,
        "dunn": 0.0, "davies_bouldin": 0.0, "xie_beni": 0.0,
    }),
    ("No-balance (5-way equal)", {
        "balance": 0.0, "silhouette": 0.2, "calinski_harabasz": 0.2,
        "dunn": 0.2, "davies_bouldin": 0.2, "xie_beni": 0.2,
    }),
    ("Separation-heavy", {
        "balance": 0.10, "silhouette": 0.35, "calinski_harabasz": 0.25,
        "dunn": 0.10, "davies_bouldin": 0.10, "xie_beni": 0.10,
    }),
]

STRONG_IMPUTED = {
    "agg_rf_no_context",       # MF/Agg
    "kmeans_rf_no_context",    # MF/KM
    "kmeans_mice_no_context",  # MICE/KM
    "kmeans_knn_no_context",   # KNN/KM
}
DEGENERATE = {
    "agg_mice_no_context",     # MICE/Agg
    "agg_knn_no_context",      # KNN/Agg
    "kmeans_encoded_20",       # None20/KM
    "agg_encoded_20",           # None20/Agg
    "kmeans_encoded_40",       # None40/KM
    "agg_encoded_40",          # None40/Agg
}

# Sanity checks on regime coverage.
assert len(STRONG_IMPUTED) == 4
assert len(DEGENERATE) == 6
assert STRONG_IMPUTED.isdisjoint(DEGENERATE)
assert STRONG_IMPUTED | DEGENERATE == set(TEN_PIPELINES)


def rank_of(final, name):
    """Return 1-indexed rank of `name` in final = [(name, score), ...]."""
    for i, (n, _) in enumerate(final, start=1):
        if n == name:
            return i
    raise KeyError(name)


def main():
    subset = {name: RAW[name] for name in TEN_PIPELINES}

    lines = []
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# Phase 2 — Broader weight-sensitivity study (10-scale)\n")
    lines.append("Six weight regimes over (balance, silhouette, CH, Dunn, DB, XB).")
    lines.append("Each row sums to 1. Composite is ranked within the 10-subset only.\n")

    # First: show the regimes clearly.
    lines.append("## Regimes tested\n")
    lines.append("| # | Regime | balance | silhouette | CH | Dunn | DB | XB |")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|")
    for i, (name, w) in enumerate(REGIMES, start=1):
        row = f"| {i} | {name} |"
        for m in METRIC_ORDER:
            row += f" {w[m]:.3f} |"
        lines.append(row)
    lines.append("")

    # Now run each regime.
    regime_outputs = []
    for name, weights in REGIMES:
        _, final = composite_ranking(subset, weights=weights)
        top1_name, top1_score = final[0]

        mf_agg_rank = rank_of(final, "agg_rf_no_context")
        mice_km_rank = rank_of(final, "kmeans_mice_no_context")

        # Positions 0..9 (rank 1..10). Strong should occupy top 4 (ranks 1..4).
        top4_names = {n for n, _ in final[:4]}
        bottom6_names = {n for n, _ in final[4:]}

        strong_top4 = top4_names == STRONG_IMPUTED
        degen_bottom6 = bottom6_names == DEGENERATE

        # Also check the softer "top 5" claim in case the identity of position 4 flips.
        top5_names = {n for n, _ in final[:5]}
        strong_in_top5 = STRONG_IMPUTED.issubset(top5_names)

        regime_outputs.append({
            "name": name,
            "final": final,
            "top1": (SHORT[top1_name], top1_score),
            "mf_agg_rank": mf_agg_rank,
            "mice_km_rank": mice_km_rank,
            "strong_top4": strong_top4,
            "strong_in_top5": strong_in_top5,
            "degen_bottom6": degen_bottom6,
        })

    # Summary table (the money table for the paper).
    lines.append("## Robustness summary\n")
    lines.append("| Regime | Top pipeline | MF/Agg rank | MICE/KM rank | Strong-4 in top-4? | Strong-4 in top-5? | Degenerate-6 in bottom-6? |")
    lines.append("|---|---|---:|---:|:---:|:---:|:---:|")
    for r in regime_outputs:
        top_label, top_score = r["top1"]
        lines.append(
            f"| {r['name']} | {top_label} ({top_score:.2f}) | "
            f"{r['mf_agg_rank']} | {r['mice_km_rank']} | "
            f"{'YES' if r['strong_top4'] else 'no'} | "
            f"{'YES' if r['strong_in_top5'] else 'no'} | "
            f"{'YES' if r['degen_bottom6'] else 'no'} |"
        )
    lines.append("")

    # Full rankings per regime for auditability.
    lines.append("## Full rankings per regime (audit)\n")
    for r in regime_outputs:
        lines.append(f"### {r['name']}")
        lines.append("| Rank | Pipeline | Composite (10-scale) |")
        lines.append("|---:|---|---:|")
        for i, (name, score) in enumerate(r["final"], start=1):
            lines.append(f"| {i} | {SHORT[name]} | {score:.4f} |")
        lines.append("")

    # Load-bearing claim.
    all_top4 = all(r["strong_top4"] for r in regime_outputs)
    all_top5 = all(r["strong_in_top5"] for r in regime_outputs)
    all_bottom6 = all(r["degen_bottom6"] for r in regime_outputs)

    lines.append("## Load-bearing claim\n")
    lines.append(
        f"- The four strong imputed pipelines (MF/Agg, MICE/KM, MF/KM, KNN/KM) "
        f"occupy the **top 4** in all 6 regimes: **{'YES' if all_top4 else 'NO'}**"
    )
    lines.append(
        f"- The four strong imputed pipelines occupy the **top 5** in all 6 regimes: "
        f"**{'YES' if all_top5 else 'NO'}**"
    )
    lines.append(
        f"- The six degenerate pipelines occupy the **bottom 6** in all 6 regimes: "
        f"**{'YES' if all_bottom6 else 'NO'}**"
    )
    lines.append("")

    # Where does the top-1 identity flip?
    top1_map = [(r["name"], r["top1"][0]) for r in regime_outputs]
    top1_set = {t for _, t in top1_map}
    lines.append("### Top-1 identity across regimes")
    for regime_name, top_label in top1_map:
        lines.append(f"- **{regime_name}**: {top_label}")
    lines.append("")
    lines.append(
        f"Distinct top-1 pipelines across all 6 regimes: {sorted(top1_set)}"
    )
    lines.append("")

    # Append to rescore_results.md.
    out_path = "/home/mhmd1/Music/capstone/conference-latex/rescore_results.md"
    with open(out_path, "a") as f:
        f.write("\n".join(lines))

    print("\n".join(lines))
    print(f"\n[appended to {out_path}]")


if __name__ == "__main__":
    main()
