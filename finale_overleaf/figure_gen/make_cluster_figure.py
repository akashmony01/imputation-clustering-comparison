#!/usr/bin/env python3
"""
make_cluster_figure.py
----------------------
Generates the conference paper's cluster-structure figure for the leading
pipeline MICE/KM (kmeans_df_mice_no_context) from SAVED cluster labels.
No re-clustering: this only projects and plots the saved output, mirroring
the visualisation cell of notebooks/11_comparing-clustering.ipynb
(PCA to 2 components on the feature matrix, scatter coloured by the saved
`kmeans_cluster` label).

Outputs (written next to this script):
  clusters_micekm.png         -- (a) PCA scatter + (b) report-year distribution
                                  [notebook-faithful: PCA on raw values]
  clusters_micekm_scaled.png  -- same, but features standardised before PCA
                                  [closer to what the clustering itself saw]

PCA is computed with numpy SVD (deterministic; identical to sklearn's full-SVD
PCA up to harmless sign flips), so no sklearn dependency is needed.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "datasets", "kmeans", "kmeans_df_mice_no_context.xlsx")

C0_COLOR = "#004C99"   # paper accent blue
C1_COLOR = "#D55E00"   # colourblind-safe vermillion


def pca_2d(X):
    """Centre + SVD = classical PCA to 2 components (deterministic)."""
    Xc = X - X.mean(axis=0, keepdims=True)
    U, S, _ = np.linalg.svd(Xc, full_matrices=False)
    return U[:, :2] * S[:2]


def make_figure(df, scale, outfile):
    cl = df["kmeans_cluster"].values
    X = df.drop(columns=["kmeans_cluster"]).values.astype(float)

    # the saved imputed matrix should be complete; guard for stray NaNs anyway
    if np.isnan(X).any():
        col_mean = np.nanmean(X, axis=0)
        X = np.where(np.isnan(X), col_mean, X)
        print(f"  note: filled {int(np.isnan(df.drop(columns=['kmeans_cluster']).values.astype(float)).sum())} stray NaNs with column means for plotting")

    if scale:  # standardise features first (as the clustering pipeline did)
        sd = X.std(axis=0)
        sd[sd == 0] = 1.0
        X = (X - X.mean(axis=0)) / sd

    P = pca_2d(X)
    years = df["suicide_year"].round().astype(int).values

    # stacked layout, designed at true IEEE column width (~3.5 in) so fonts
    # render at their actual size without shrinking
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 5.6))

    # ---- panel (a): PCA scatter -------------------------------------------
    for cid, color in [(0, C0_COLOR), (1, C1_COLOR)]:
        m = cl == cid
        ax_a.scatter(P[m, 0], P[m, 1], s=6, alpha=0.6, linewidths=0,
                     color=color, label=f"Cluster {cid} (n={m.sum()})")
    ax_a.set_xlabel("PC 1", fontsize=8)
    ax_a.set_ylabel("PC 2", fontsize=8)
    ax_a.tick_params(labelsize=7)
    ax_a.legend(frameon=False, fontsize=7.5, loc="best")
    ax_a.set_title("(a) PCA projection of the two clusters", fontsize=9)

    # ---- panel (b): report-year distribution per cluster ------------------
    yr_min, yr_max = years.min(), years.max()
    yr_range = np.arange(yr_min, yr_max + 1)
    width = 0.4
    for cid, color, off in [(0, C0_COLOR, -width / 2), (1, C1_COLOR, width / 2)]:
        m = cl == cid
        counts = [(years[m] == y).sum() for y in yr_range]
        ax_b.bar(yr_range + off, counts, width=width, color=color,
                 label=f"Cluster {cid} (n={m.sum()})")
    ax_b.set_xlabel("Report year", fontsize=8)
    ax_b.set_ylabel("Cases", fontsize=8)
    ax_b.set_xticks(yr_range)
    ax_b.tick_params(labelsize=7)
    ax_b.legend(frameon=False, fontsize=7.5)
    ax_b.set_title("(b) Report year by cluster", fontsize=9)

    fig.tight_layout()
    fig.savefig(outfile, dpi=300, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    print(f"  wrote {os.path.basename(outfile)}")


def main():
    df = pd.read_excel(DATA)
    assert "kmeans_cluster" in df.columns, "cluster label column missing"
    print(f"loaded {DATA}: {df.shape[0]} rows, clusters "
          f"{df['kmeans_cluster'].value_counts().sort_index().to_dict()}")
    make_figure(df, scale=False, outfile=os.path.join(HERE, "clusters_micekm.png"))
    make_figure(df, scale=True, outfile=os.path.join(HERE, "clusters_micekm_scaled.png"))


if __name__ == "__main__":
    main()
