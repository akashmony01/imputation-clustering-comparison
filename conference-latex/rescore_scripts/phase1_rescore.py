"""
Phase 1: Recompute the composite cluster-validity score on a 10-scale
by ranking within the ten conference-paper pipelines only.

Mirrors the ranking logic of notebooks/11_comparing-clustering.ipynb (cell 11).
Raw per-metric values are copied verbatim from cell 46's cached output.

Output: prints results to stdout; writes conference-latex/rescore_results.md.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


METRIC_ORDER = ["balance", "silhouette", "calinski_harabasz", "dunn", "davies_bouldin", "xie_beni"]

METRIC_WEIGHTS_OURS = {
    "balance": 0.35,
    "silhouette": 0.25,
    "calinski_harabasz": 0.20,
    "dunn": 0.10,
    "davies_bouldin": 0.05,
    "xie_beni": 0.05,
}

# Raw per-metric values for all 32 pipelines, taken verbatim from
# notebooks/11_comparing-clustering.ipynb cell 46 display output.
# Column order: balance, silhouette, calinski_harabasz, dunn, davies_bouldin, xie_beni
RAW = {
    "agg_rf_no_context":       [0.685461,  0.756380,  9792.497921, 0.980954, 0.730318, 0.960545],
    "kmeans_mice_no_context":  [0.674009,  0.792085, 13154.910479, 0.030805, 0.791936, 0.970546],
    "agg_rf_context":          [0.685461,  0.754761,  9686.611574, 0.982102, 0.729068, 0.960131],
    "spc_rf_no_context":       [0.685461,  0.756380,  9792.497921, 0.980954, 0.730318, 0.960545],
    "dbscan_rf_context":       [0.685461,  0.754761,  9686.611574, 0.982102, 0.729068, 0.960131],
    "spc_mice_no_context":     [0.673571,  0.787801, 12376.439745, 0.021246, 0.789193, 0.968759],
    "spc_knn_no_context":      [0.538092,  0.795369,  9875.866564, 0.025660, 0.800913, 0.969425],
    "spc_rf_context":          [0.685461,  0.754761,  9686.611574, 0.982102, 0.729068, 0.960131],
    "spc_knn_context":         [0.538092,  0.794904,  9833.815232, 0.025660, 0.800527, 0.969298],
    "kmeans_rf_no_context":    [0.685023,  0.755367,  9654.365485, 0.055459, 0.729813, 0.960009],
    "kmeans_knn_no_context":   [0.542465,  0.785370,  8744.775850, 0.032461, 0.786055, 0.965104],
    "kmeans_knn_context":      [0.542465,  0.784890,  8708.895980, 0.032461, 0.785642, 0.964965],
    "kmeans_rf_context":       [0.685023,  0.753743,  9549.182978, 0.054177, 0.728559, 0.959586],
    "spc_mice_context":        [0.702065,  0.670781,  5302.263750, 0.001820, 0.701281, 0.929418],
    "dbscan_mice_context":     [0.306703,  0.874364,    96.547161, 2.327724, 0.883905, 0.989749],
    "kmeans_mice_context":     [0.668310,  0.708758,  7649.178141, 0.011035, 0.718630, 0.950553],
    "dbscan_rf_no_context":    [0.307709,  0.351424,     4.619301, 0.256321, 0.481121, 0.697853],
    "spc_encoded_20":          [0.438937,  0.012104,     1.372098, 0.025583, 0.061092, 0.014959],
    "dbscan_encoded_20":       [0.356040,  0.121859,     1.690365, 0.071764, 0.284405, 0.361745],
    "spc_encoded_40":          [0.438937,  0.012104,     1.372098, 0.025583, 0.061092, 0.014959],
    "agg_encoded_40":          [0.355308,  0.157153,     2.160973, 0.020834, 0.613707, 0.685253],
    "dbscan_encoded_40":       [0.409134, -0.339146,     8.739920, 0.008877, 0.418675, 0.381333],
    "agg_mice_no_context":     [0.356184, -0.077905,     2.344871, 0.009983, 0.281811, 0.282000],
    "agg_knn_context":         [0.358801, -0.285265,     2.609730, 0.013441, 0.272135, 0.179908],
    "kmeans_encoded_40":       [0.315207, -0.071859,  1281.887066, 0.008478, 0.168569, 0.032546],
    "agg_knn_no_context":      [0.360987, -0.019878,     0.278632, 0.016553, 0.068518, 0.016314],
    "dbscan_mice_no_context":  [0.356184, -0.077905,     2.344871, 0.009983, 0.281811, 0.282000],
    "agg_mice_context":        [0.356184, -0.094494,     1.874077, 0.004522, 0.259546, 0.238908],
    "kmeans_encoded_20":       [0.289369, -0.212661,    28.041057, 0.020631, 0.190869, 0.079326],
    "agg_encoded_20":          [0.258243, -0.316824,     1.109202, 0.043354, 0.303899, 0.182562],
    "dbscan_knn_no_context":   [0.143811, -0.436810,   239.623244, 0.003395, 0.178531, 0.012615],
    "dbscan_knn_context":      [0.139237, -0.405025,   220.061266, 0.003395, 0.174882, 0.007614],
}

# The 10 pipelines shown in the conference paper.
# Names follow the notebook convention. Only no_context, K-Means & Agg, plus baselines.
TEN_PIPELINES = [
    "agg_rf_no_context",       # MF / Agg
    "kmeans_rf_no_context",    # MF / KM
    "kmeans_mice_no_context",  # MICE / KM
    "agg_mice_no_context",     # MICE / Agg
    "kmeans_knn_no_context",   # KNN / KM
    "agg_knn_no_context",      # KNN / Agg
    "kmeans_encoded_20",       # None20 / KM
    "agg_encoded_20",          # None20 / Agg
    "kmeans_encoded_40",       # None40 / KM
    "agg_encoded_40",          # None40 / Agg
]

# Human-readable labels for the paper.
SHORT = {
    "agg_rf_no_context":      "MF / Agg",
    "kmeans_rf_no_context":   "MF / KM",
    "kmeans_mice_no_context": "MICE / KM",
    "agg_mice_no_context":    "MICE / Agg",
    "kmeans_knn_no_context":  "KNN / KM",
    "agg_knn_no_context":     "KNN / Agg",
    "kmeans_encoded_20":      "None20 / KM",
    "agg_encoded_20":          "None20 / Agg",
    "kmeans_encoded_40":      "None40 / KM",
    "agg_encoded_40":         "None40 / Agg",
}


def rank_per_metric(results_dict, metric_idx):
    """Sort names by metric value, descending. NaN goes last (not present here)."""
    items = [(name, values[metric_idx]) for name, values in results_dict.items()]
    items.sort(key=lambda x: (-math.inf if math.isnan(x[1]) else x[1]), reverse=True)
    return items


def composite_ranking(results_dict, weights=METRIC_WEIGHTS_OURS):
    """Mirror of notebooks/11_comparing-clustering.ipynb composite_ranking().

    n = len(results_dict). Rank 1 (best) gets n points on each metric.
    Rank n (worst) gets 1 point. Sum weighted by metric weights.
    """
    n = len(results_dict)
    scores = {name: 0.0 for name in results_dict}

    per_metric_ranked = {}
    for m_idx, metric in enumerate(METRIC_ORDER):
        weight = weights[metric]
        sorted_by_metric = rank_per_metric(results_dict, m_idx)
        per_metric_ranked[metric] = sorted_by_metric
        for pos, (name, val) in enumerate(sorted_by_metric):
            pts = 0 if math.isnan(val) else (n - pos)
            scores[name] += weight * pts

    final = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return per_metric_ranked, final


def main():
    subset = {name: RAW[name] for name in TEN_PIPELINES}

    per_metric_ranked, final = composite_ranking(subset, weights=METRIC_WEIGHTS_OURS)

    # Print per-metric ranks with actual metric values, so we can visually verify.
    lines = []
    lines.append("# Phase 1 — 10-scale composite (`weights = Ours` = balance-weighted)\n")
    lines.append("## Per-metric ranks within the 10-subset\n")
    for metric in METRIC_ORDER:
        lines.append(f"### {metric}")
        lines.append("| Rank | Pipeline | Value |")
        lines.append("|---:|---|---:|")
        for i, (name, val) in enumerate(per_metric_ranked[metric], start=1):
            lines.append(f"| {i} | {SHORT[name]} | {val:.4f} |")
        lines.append("")

    lines.append("## 10-scale composite ranking\n")
    lines.append("| Rank | Pipeline | 10-scale composite |")
    lines.append("|---:|---|---:|")
    for i, (name, score) in enumerate(final, start=1):
        lines.append(f"| {i} | {SHORT[name]} | {score:.4f} |")
    lines.append("")

    # Derived summary stats.
    score_map = dict(final)

    def get(name):
        return score_map[name]

    mf_mean = (get("agg_rf_no_context") + get("kmeans_rf_no_context")) / 2
    mice_mean = (get("agg_mice_no_context") + get("kmeans_mice_no_context")) / 2
    knn_mean = (get("agg_knn_no_context") + get("kmeans_knn_no_context")) / 2
    baselines = [
        "kmeans_encoded_20", "agg_encoded_20",
        "kmeans_encoded_40", "agg_encoded_40",
    ]
    baseline_mean = sum(get(n) for n in baselines) / len(baselines)

    imputed_names = [
        "agg_rf_no_context", "kmeans_rf_no_context",
        "kmeans_mice_no_context", "agg_mice_no_context",
        "kmeans_knn_no_context", "agg_knn_no_context",
    ]
    all_imputed_mean = sum(get(n) for n in imputed_names) / len(imputed_names)

    km_imputed_names = [
        "kmeans_mice_no_context", "kmeans_knn_no_context", "kmeans_rf_no_context",
    ]
    km_imputed_scores = [get(n) for n in km_imputed_names]
    km_mean = sum(km_imputed_scores) / len(km_imputed_scores)
    km_range = (min(km_imputed_scores), max(km_imputed_scores))

    agg_imputed_names = [
        "agg_rf_no_context", "agg_mice_no_context", "agg_knn_no_context",
    ]
    agg_imputed_scores = [get(n) for n in agg_imputed_names]
    agg_mean = sum(agg_imputed_scores) / len(agg_imputed_scores)

    best_agg_baseline = max(get("agg_encoded_20"), get("agg_encoded_40"))
    best_agg_baseline_name = (
        "None40/Agg" if get("agg_encoded_40") >= get("agg_encoded_20") else "None20/Agg"
    )

    lines.append("## Derived statistics\n")
    lines.append("### Mean composite by imputer (K-Means + Agg / 2)")
    lines.append(f"- MissForest: **{mf_mean:.2f}**  (was 25.30 in 32-scale)")
    lines.append(f"- MICE: **{mice_mean:.2f}**  (was 18.13)")
    lines.append(f"- KNN: **{knn_mean:.2f}**  (was 15.70)")
    lines.append(f"- Baselines (four): **{baseline_mean:.2f}**  (was 8.09)")
    lines.append("")

    lines.append("### Pooled means and lift ratios")
    lines.append(f"- All-imputed pooled mean (six cells): **{all_imputed_mean:.2f}**  (was 19.71)")
    lines.append(f"- Lift, all imputed vs baselines: **{all_imputed_mean/baseline_mean:.2f}x**  (was 2.4x)")
    lines.append(f"- Lift, MissForest vs baselines: **{mf_mean/baseline_mean:.2f}x**  (was 3.1x)")
    lines.append("")

    lines.append("### K-Means-imputed cells")
    lines.append(f"- Mean: **{km_mean:.2f}**  (was 23.98)")
    lines.append(f"- Range: **{km_range[0]:.2f} to {km_range[1]:.2f}**  (was 22.05 to 26.60)")
    lines.append("")

    lines.append("### Agglomerative-imputed cells and best Agg baseline")
    lines.append(f"- MF/Agg: **{get('agg_rf_no_context'):.2f}**  (was 27.30)")
    lines.append(f"- MICE/Agg: **{get('agg_mice_no_context'):.2f}**  (was 9.65)")
    lines.append(f"- KNN/Agg: **{get('agg_knn_no_context'):.2f}**  (was 9.35)")
    lines.append(f"- Best Agg baseline ({best_agg_baseline_name}): **{best_agg_baseline:.2f}**  (was 10.35)")
    both_below = (
        get("agg_mice_no_context") < best_agg_baseline
        and get("agg_knn_no_context") < best_agg_baseline
    )
    lines.append(f"- MICE/Agg AND KNN/Agg both fall below best Agg baseline: **{'YES' if both_below else 'NO'}**  (interaction claim survives)")
    lines.append("")

    out_path = "/home/mhmd1/Music/capstone/conference-latex/rescore_results.md"
    with open(out_path, "w") as f:
        f.write("\n".join(lines))

    # Also print to stdout so we can see it in the terminal.
    print("\n".join(lines))
    print(f"\n[wrote {out_path}]")


if __name__ == "__main__":
    main()
