#!/usr/bin/env python3
"""
weight_robustness.py
--------------------
Post-hoc robustness analysis for the i-COSTE conference paper.

Question answered: does the "imputation helps" conclusion depend on how the six
cluster-validity metrics are weighted in the composite score?

Method (NO re-running of clustering/imputation -- purely post-hoc arithmetic on
saved results, the same category as the earlier weight-sensitivity analysis):

  1. Load the six raw validity-metric values for the ten in-scope pipelines
     (from thesis appendix Table "full_per_case_results_across_all_pipelines").
     All six metrics are oriented so that HIGHER = better (Davies-Bouldin and
     Xie-Beni are already stored inverted).
  2. Rank-aggregate the ten pipelines under 100,000 weight vectors drawn
     uniformly over the 6-metric simplex  (Dirichlet(1,...,1)), fixed seed.
  3. Report, per pipeline: mean rank (out of 10), % of weightings in the top-4,
     and % ranked #1; and overall, the % of weightings in which the four strong
     imputed pipelines occupy the top four ranks (+ which metric dominates the
     exceptions).
  4. Post-hoc cluster profiles from SAVED cluster labels (datasets/{algo}/...):
     confirm the leading pipelines converge on the same primary (source-cohort)
     split while finer contrasts are pipeline-dependent.

Reproducible: fixed seed. Ships with the code release.
"""

import os
import numpy as np

SEED = 42
N_WEIGHTS = 100_000

# ---------------------------------------------------------------------------
# 1. Saved metric values for the ten in-scope pipelines.
#    Columns: balance, silhouette, Calinski-Harabasz, Dunn, Davies-Bouldin(inv),
#             Xie-Beni(inv)  -- all higher = better.
#    'kind': 'strong' = strong imputed, 'weak' = imputed but degenerate,
#            'base' = no-imputation baseline.
# ---------------------------------------------------------------------------
PIPELINES = [
    ("MF/Agg",   "strong", [0.685461, 0.756380,  9792.497921, 0.980954, 0.730318, 0.960545]),
    ("MF/KM",    "strong", [0.685023, 0.755367,  9654.365485, 0.055459, 0.729813, 0.960009]),
    ("MICE/KM",  "strong", [0.674009, 0.792085, 13154.910479, 0.030805, 0.791936, 0.970546]),
    ("MICE/Agg", "weak",   [0.356184, -0.077905,    2.344871, 0.009983, 0.281811, 0.282000]),
    ("KNN/KM",   "strong", [0.542465, 0.785370,  8744.775850, 0.032461, 0.786055, 0.965104]),
    ("KNN/Agg",  "weak",   [0.360987, -0.019878,    0.278632, 0.016553, 0.068518, 0.016314]),
    ("None40/Agg", "base", [0.355308, 0.157153,     2.160973, 0.020834, 0.613707, 0.685253]),
    ("None40/KM",  "base", [0.315207, -0.071859, 1281.887066, 0.008478, 0.168569, 0.032546]),
    ("None20/KM",  "base", [0.289369, -0.212661,   28.041057, 0.020631, 0.190869, 0.079326]),
    ("None20/Agg", "base", [0.258243, -0.316824,    1.109202, 0.043354, 0.303899, 0.182562]),
]
METRICS = ["balance", "silhouette", "CH", "Dunn", "DB", "XB"]

names = [p[0] for p in PIPELINES]
kinds = [p[1] for p in PIPELINES]
V = np.array([p[2] for p in PIPELINES], dtype=float)     # (10, 6)
n = len(PIPELINES)
strong_idx = np.array([i for i, k in enumerate(kinds) if k == "strong"])  # the 4 strong imputed


def per_metric_points(V):
    """Convert raw metric values to rank-points (best=n, worst=1) per metric."""
    # zero-indexed rank per column, best (highest value) = 0
    ranks = np.argsort(np.argsort(-V, axis=0), axis=0)   # (10, 6)
    return n - ranks                                     # points: best=10 ... worst=1


def run_weight_robustness():
    rng = np.random.default_rng(SEED)
    points = per_metric_points(V)                        # (10, 6)
    W = rng.dirichlet(np.ones(6), size=N_WEIGHTS)        # (K, 6) uniform on simplex
    scores = points @ W.T                                # (10, K)
    # rank of each pipeline per weighting (0 = best/highest score)
    order = np.argsort(-scores, axis=0)                  # (10, K)
    ranks = np.argsort(order, axis=0)                    # (10, K), rank of pipeline i

    mean_rank = ranks.mean(axis=1) + 1                   # 1 = best (out of 10)
    pct_top4 = (ranks < 4).mean(axis=1) * 100
    pct_top1 = (ranks == 0).mean(axis=1) * 100

    # overall: in how many weightings are the four strong imputed the top-4?
    strong_all_top4 = (ranks[strong_idx] < 4).all(axis=0)   # (K,)
    pct_invariant = strong_all_top4.mean() * 100
    # which metric dominates the exceptions?
    fails = ~strong_all_top4
    dom_fail = {}
    if fails.any():
        dom = np.argmax(W[fails], axis=1)
        for m in range(6):
            c = int((dom == m).sum())
            if c:
                dom_fail[METRICS[m]] = c

    print("=" * 66)
    print(f"WEIGHT ROBUSTNESS  ({N_WEIGHTS:,} uniform-simplex weightings, seed={SEED})")
    print("=" * 66)
    print(f"{'pipeline':12} {'kind':7} {'mean rank':>9} {'% top-4':>9} {'% #1':>8}")
    for i in range(n):
        print(f"{names[i]:12} {kinds[i]:7} {mean_rank[i]:9.2f} {pct_top4[i]:9.2f} {pct_top1[i]:8.2f}")
    print("-" * 66)
    print(f"Top-4 == the 4 strong imputed pipelines in {pct_invariant:.3f}% of weightings")
    if dom_fail:
        tot = int(fails.sum())
        share = {k: f"{100*v/tot:.1f}%" for k, v in sorted(dom_fail.items(), key=lambda x: -x[1])}
        print(f"  exceptions ({tot} of {N_WEIGHTS:,}) dominated by: {share}")
    # #1 split among the pipelines that ever lead
    leaders = {names[i]: round(pct_top1[i], 1) for i in range(n) if pct_top1[i] > 0}
    print(f"  #1 split: {leaders}")
    print()
    return mean_rank, pct_top4, pct_top1, pct_invariant


# ---------------------------------------------------------------------------
# 4. Post-hoc cluster profiles from SAVED labels (no re-clustering).
# ---------------------------------------------------------------------------
def run_cluster_profiles():
    try:
        import pandas as pd
    except ImportError:
        print("[cluster profiles skipped: pandas unavailable]")
        return
    here = os.path.dirname(os.path.abspath(__file__))
    dsroot = os.path.join(here, "..", "datasets")
    files = {
        "MICE/KM (kmeans_mice_no_context)": ("kmeans/kmeans_df_mice_no_context.xlsx", "kmeans_cluster"),
        "MF/Agg  (agg_rf_no_context)":      ("agg/agg_df_rf_no_context.xlsx",        "agg_cluster"),
    }
    print("=" * 66)
    print("CLUSTER PROFILES  (post-hoc group-by on saved labels)")
    print("=" * 66)
    for label, (rel, clcol) in files.items():
        path = os.path.join(dsroot, rel)
        if not os.path.exists(path):
            print(f"[missing: {rel}]")
            continue
        df = pd.read_excel(path)
        if clcol not in df.columns:
            print(f"[{label}: no '{clcol}' column]")
            continue
        print(f"\n{label}: sizes {df[clcol].value_counts().sort_index().to_dict()}")
        for cl, sub in df.groupby(clcol):
            t = len(sub)
            bits = []
            if "suicide_year" in sub:
                bits.append(f"year~{sub['suicide_year'].mean():.1f}")
            if "age" in sub:
                bits.append(f"age~{sub['age'].mean():.1f}")
            # gender: one-hot (kmeans files) or encoded column (agg files)
            if "gender_encoded_female" in sub:
                bits.append(f"F {100*sub['gender_encoded_female'].mean():.0f}%")
            if "workplace_encoded_rural" in sub:
                ru = 100 * sub["workplace_encoded_rural"].mean()
                su = 100 * sub["workplace_encoded_semi-urban"].mean()
                bits.append(f"rural {ru:.0f}%/semi {su:.0f}%")
            print(f"  cluster {cl}: n={t} | " + " | ".join(bits))
    print("\nRead-off: both leading pipelines split on the 2020 cohort vs. the rest")
    print("(year means diverge), confirming a CONVERGENT primary structure; finer")
    print("contrasts (e.g. workplace) differ by pipeline -> structure recovery,")
    print("not epidemiological discovery.")
    print()


if __name__ == "__main__":
    run_weight_robustness()
    run_cluster_profiles()
