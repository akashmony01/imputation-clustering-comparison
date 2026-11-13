# Conference Paper Reframe Plan — "Imputation Helps, *Weight-Independently*"

**Status:** Phases 1-6 IMPLEMENTED (2026-07-19). Remaining: user supplies MICE/KM cluster
figure to replace the placeholder; Overleaf compile to confirm <=6 pages.
**Deviation from plan:** the separate "% in top-4" bar chart was NOT added; the sorted
`tbl:rankdist` (Silhouette / Mean rank / % top-4 / % #1) carries the percentages instead,
keeping the float count at 4 (fig:pipeline, fig:missingness, fig:clusters, tbl:rankdist).
The old cardinality table was already removed by a prior external edit (numbers survive in
prose). Add the % bar chart later only if a float is freed.
**Core move:** stop crowning a single best pipeline (which is weight-dependent); make the
**robust, weight-free** claim the headline: *imputation helps, and the result does not depend
on how the six validity metrics are weighted.* Keep a slim, honest cluster finding.

**Hard constraints (unchanged):**
- NO re-running clustering/imputation. All new computation is **post-hoc arithmetic on saved
  results** (metric values from the appendix table; cluster labels from `datasets/{algo}/`).
  This is the same allowed category as the old weight-sensitivity analysis.
- Stay within **6 pages**, IEEE 2-column.
- Local build blocked → verify on **Overleaf**.

---

## Locked decisions (from the design conversation)
1. **Headline = weight-independent robustness.** Report the rank *distribution* across 100k
   uniform-random weightings, not one composite score.
2. **Results table/figure = all 10 pipelines**, columns: **mean rank (/10) · % in top-4 · % #1**.
   No composite-score column, no fixed weighting to defend.
3. **Honest numbers:** the four strong imputed pipelines are top-4 in **>99.9%** of weightings
   (NOT 100%); the <0.1% exceptions concentrate weight on the **Dunn** index (known unstable).
   #1 alternates **MICE/KM ≈61% / MF/Agg ≈39% → no sole winner.**
4. **Cluster finding = cross-pipeline convergence.** Strong pipelines converge on the primary
   split (2020 source cohort vs. rest); finer contrasts (e.g., workplace) are pipeline-dependent
   → "structure recovery, not epidemiological discovery." Feature **MICE/KM**'s figure
   (placeholder until user confirms + supplies).
5. **Balance metric** motivated by observed degeneracy (mega-cluster + singletons; DBSCAN runs
   labelling ~1,611/1,617 points as noise while scoring silhouette 0.87).
6. **Keep** the LLM-rationalization contribution + AutoDCWorkflow positioning + honest limitations.

---

## Phase 1 — Analysis code (create · run · document)
**Deliverable:** `conference-latex/weight_robustness.py` (retire `weight_sensitivity.py`).

Contents:
- **Inputs (saved, hardcoded/read):** the 10 in-scope pipelines' six raw metric values
  (balance, silhouette, CH, Dunn, DB-inv, XB-inv) — from thesis appendix
  `tbl:full_per_case_results_across_a`. Flag which 4 are the strong imputed set.
- **100k weightings:** Dirichlet(1,…,1) = uniform over the 6-metric simplex, **fixed seed**.
  For each: rank the 10 by composite (rank-based aggregation), record each pipeline's rank.
- **Outputs (printed + saved to a small results block):**
  - per-pipeline: **mean rank**, **% in top-4**, **% ranked #1**
  - overall: **% of weightings with top-4 == the 4 strong imputed** (~99.9%); dominant metric in
    the failing cases (Dunn)
- **Post-hoc cluster profiles** from saved labels (no re-clustering):
  `datasets/kmeans/kmeans_df_mice_no_context.xlsx` (MICE/KM, `kmeans_cluster`) and
  `datasets/agg/agg_df_rf_no_context.xlsx` (MF/Agg, `agg_cluster`) → cluster sizes, year-mean
  (cohort check), gender, workplace. Emit the convergence/divergence summary.
- **Reproducibility:** seeded; ships in the repo.

**Actions:**
- [ ] Claude: write `weight_robustness.py`, run it, capture the numbers.
- [ ] Claude: delete `weight_sensitivity.py`.
- [ ] **User: run `weight_robustness.py` and confirm MICE/KM has the highest %#1** (the figure we
  feature depends on this). If a different pipeline wins, we feature that one instead.

---

## Phase 2 — Results section rewrite (core)
New subsection flow:
- **§ Does imputation help? (weight-independent)** — the 100k result: all 10 pipelines' mean rank
  + % in top-4; the four strong imputed dominate in >99.9% of weightings; degenerate imputed and
  all baselines essentially never in the top-4. State the Dunn caveat in one clause.
- **§ …but conditional on the combination** — the two imputed pipelines (MICE/Agg, KNN/Agg) that
  fall below baselines; "impute *and* choose the algorithm," not "impute and win."
- **§ Recovered structure (convergent)** — cross-pipeline convergence on the cohort-aligned split;
  finer contrasts pipeline-dependent; feature the MICE/KM cluster figure (placeholder).

**Swaps (as implemented):**
- Removed the composite bar chart (`fig:ranking`); the percentages are carried by the
  rank-distribution table instead (NO separate "% in top-4" bar chart was added).
- Replaced `tbl:results`/composite numbers → **`tbl:rankdist`** (Silhouette · mean rank · %top-4 · %#1).
- Removed `tbl:profile` (single-pipeline) → convergence statement.
- Deleted the sole-winner language and the MF/Agg-specific workplace contrast.

---

## Phase 3 — Methodology alignment
- **§ Composite:** keep the definition (balance-aware rank aggregation) — it's still the ranking
  mechanism. Reframe the weights as a *device*, not a committed choice: one sentence of principled
  tiering (balance = degeneracy guard; silhouette = field standard), then "we do not rely on any
  fixed weighting — see §Results." Add the **degeneracy/DBSCAN** motivation for the balance term.
- Remove the tiered-weight defense paragraph and the permutation/`tbl:weight_sens` table
  (superseded by the 100k robustness in Results).
- Keep encoding/imputer/algorithm citations (MacQueen, Ward, Saxena, Poslavskaya, Pargent, Junaid,
  Jäger, AutoDCWorkflow) and the LLM single-rater validation (>99% author acceptance).

---

## Phase 4 — Abstract / Contributions / Conclusion alignment
- **Abstract:** reframe to weight-independent robustness + conditional-on-combination + convergent
  structure. Drop the point-estimate composite numbers (25.30/8.09 etc.); use the % language.
- **Contributions (3):** (1) LLM-assisted categorical rationalization; (2) a controlled
  drop-vs-impute benchmark with a balance-aware composite *shown to be weight-robust*;
  (3) the robust finding — imputation helps weight-independently, conditional on the
  imputer×algorithm combination, yielding a convergent cohort-aligned structure.
- **Conclusion:** align to the robust claim; no sole winner; keep the SDG-3 utility sentence.
- **Limitations:** unchanged (single-run/grid-search caveat, MNAR, source-cohort confound,
  LLM single-rater). No new experiments claimed.

---

## Phase 5 — Figures / tables + placeholder workflow (as implemented)
- `fig:robustness` (% in top-4 bar chart) — NOT added; `tbl:rankdist` carries the percentages.
- `fig:clusters` — **MICE/KM** cluster structure → **PLACEHOLDER** (`\fbox`) until the user
  supplies the real PNG (`figures/clusters_micekm.png`). Caption written; image swapped later.
- `tbl:rankdist` — Silhouette · mean rank · %top-4 · %#1 for all 10 (from Phase-1). DONE.
- Removed: `fig:ranking` (composite chart), `tbl:results`, `tbl:profile`, `tbl:weight_sens`. DONE.

---

## Phase 6 — Consistency, page budget, verify
- [ ] Grep for orphaned refs (`tbl:weight_sens`, `tbl:profile`, `tbl:results`, `fig:ranking`,
  stray composite numbers like 27.30/25.30/8.60).
- [ ] All `\cite`/`\ref` resolve; float count sane (target ≤ 5).
- [ ] Every number in the paper matches `weight_robustness.py` output.
- [ ] User compiles on Overleaf → confirm **≤ 6 pages** and both figures render.
- [ ] Re-upload `main.tex`, `ref.bib`, `figures/` to Overleaf.

---

## Open user actions
1. Run `weight_robustness.py`; confirm **MICE/KM = highest %#1** (else tell Claude the winner).
2. Generate + supply the **MICE/KM cluster figure** → replaces the placeholder.
3. Compile on Overleaf; report page count + rendering.

## Execution order
Phase 1 → 2 → 3 → 4 → 5 (placeholder) → 6. Claude does 1–6 in one pass except the two user
actions above; the placeholder lets the paper compile before the real figure arrives.
