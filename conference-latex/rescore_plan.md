# Conference Paper — Rescore + Weight-Sensitivity Plan

**Created:** 2026-07-13
**Owner:** Akash
**Paper:** `conference-latex/main.tex`
**Notebook:** `notebooks/11_comparing-clustering.ipynb`

## Goal
Two coupled changes to the conference paper:
1. **Rescore the composite to a 10-scale** — currently a max of 32 (because ranking is done against the full 32-pipeline benchmark and only 10 are shown), which is confusing.
2. **Broaden the weight-sensitivity study and add a principled weight justification** (Option B) — the current ±20% neighbourhood does not test extreme regimes; under equal weights the top-1 pipeline actually flips from MF/Agg to MICE/KM. Reviewers will notice; we should get ahead of it.

All qualitative claims survive both changes. Only numbers and the sensitivity paragraph change.

## Non-goals (explicitly preserved)
- Silhouette values (0.755–0.792 for strong imputed; ≤0.157 for baselines) — unchanged
- Balance value 0.685 for MF/Agg — unchanged
- Cluster sizes (759 vs 858), `k=2` claim, source-cohort confound — unchanged
- Raw per-metric values (CH, Dunn, DB, XB) — unchanged
- LMIC/SDG/LLM abbreviation cleanups from earlier passes — unchanged
- Em-dash / tone rewrites from earlier passes — unchanged
- Journal paper (in preparation) continues to use 32-scale — this rescore is conference-only

---

## Phase 1 — Rescore composite to 10-scale (notebook only)

**Scope:** notebook + a plain-text results file. No LaTeX edits.

### Steps
1. Open `notebooks/11_comparing-clustering.ipynb`.
2. In cell 11 (the scoring module), the function `composite_ranking(results_dict)` sets `n = len(results_dict)` and awards `(n - pos)` points to rank `pos`. It already works correctly for any subset — no code change needed, only the input dict.
3. Build a subset dict `subset10 = {name: all_evaluation_results[name] for name in TEN_PIPELINE_NAMES}` where `TEN_PIPELINE_NAMES` is:
   ```
   agg_rf_no_context, kmeans_rf_no_context,
   kmeans_mice_no_context, agg_mice_no_context,
   kmeans_knn_no_context, agg_knn_no_context,
   kmeans_encoded_20, agg_encoded_20,
   kmeans_encoded_40, agg_encoded_40
   ```
4. Call `composite_ranking(subset10)` → get `per_metric_sorted_10, final_ranking_10`.
5. Also produce the derived summary stats (means by imputer, baseline mean, all-imputed mean, lift ratios, K-Means-imputed mean and range).
6. Save results to `conference-latex/rescore_results.md` for reuse in Phase 3.

### Previewed numbers (hand-computed; Phase 1 will confirm)
| Pipeline | 32-scale (current paper) | 10-scale (previewed) |
|---|---|---|
| MF / Agg | 27.30 | **9.10** |
| MICE / KM | 26.60 | **8.90** |
| MF / KM | 23.65 | **8.10** |
| KNN / KM | 22.05 | **7.70** |
| None40 / Agg | 10.35 | **4.60** |
| MICE / Agg | 9.65 | **3.95** |
| KNN / Agg | 9.35 | **3.95** |
| None40 / KM | 9.35 | **3.55** |
| None20 / KM | 7.40 | **2.90** |
| None20 / Agg | 5.75 | **2.25** |

### Derived stats (previewed)
- Mean by imputer (K-Means + Agg / 2):
  - MissForest: 8.60 (was 25.30)
  - MICE: 6.43 (was 18.13)
  - KNN: 5.83 (was 15.70)
- Baseline mean (four cells): **3.33** (was 8.09)
- All-imputed pooled mean (six cells): **6.95** (was 19.71)
- Lift ratios:
  - All imputed vs baselines: **2.1×** (was 2.4×)
  - MF alone vs baselines: **2.6×** (was 3.1×)
- K-Means imputed cells:
  - Mean: 8.23 (was 23.98)
  - Range: 7.70 to 8.90 (was 22.05 to 26.60)
- Under Agglomerative:
  - MF/Agg: 9.10 (was 27.30)
  - Best baseline (None40/Agg): 4.60 (was 10.35)
  - MICE/Agg: 3.95 (was 9.65) — still below best baseline ✓
  - KNN/Agg: 3.95 (was 9.35) — still below best baseline ✓

### Risks / checks
- **Tie between MICE/Agg (3.95) and KNN/Agg (3.95)** — real, coarser resolution of 10-rank. Report the tie honestly.
- Hand math and notebook may differ by ±0.05 due to metric NaN-handling; take the notebook's number as authoritative.
- **Do not** edit `main.tex` in this phase.

### Deliverables
- `conference-latex/rescore_results.md` — table of 10-scale composites + derived stats, saved verbatim from the notebook.

---

## Phase 2 — Broader weight-sensitivity study (Option B)

**Scope:** notebook only. Produces one small table for later insertion into §V.

### Weight regimes to test
Each row is a full weight vector over (balance, silhouette, CH, Dunn, DB, XB). All sum to 1.

| # | Regime name | balance | silhouette | CH | Dunn | DB | XB |
|---|---|---|---|---|---|---|---|
| 1 | **Ours (balance-weighted)** | 0.35 | 0.25 | 0.20 | 0.10 | 0.05 | 0.05 |
| 2 | Equal | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 |
| 3 | Silhouette-only | 0 | 1.00 | 0 | 0 | 0 | 0 |
| 4 | Balance-only | 1.00 | 0 | 0 | 0 | 0 | 0 |
| 5 | No-balance (5-way equal) | 0 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 |
| 6 | Separation-heavy | 0.10 | 0.35 | 0.25 | 0.10 | 0.10 | 0.10 |

Rationale for each:
- **#2 Equal**: the most "neutral" regime; tests whether our balance-weighting is doing the work.
- **#3 Silhouette-only**: shows what the field-standard single index would say.
- **#4 Balance-only**: adversarial to non-balance-emphasizing critics.
- **#5 No-balance**: tests whether the whole balance argument is load-bearing.
- **#6 Separation-heavy**: tests a reasonable "some balance, but separation matters more" regime.

### Steps
1. Refactor `composite_ranking` (locally in the notebook) to accept a `weights` dict argument, so we don't mutate the global `METRIC_WEIGHTS`.
2. For each of the 6 regimes, run `composite_ranking(subset10, weights=regime)`.
3. Record: top-1 pipeline name, MF/Agg rank, MICE/KM rank, and a boolean "all four strong imputed pipelines still in top 4-or-5".
4. Save the resulting table to `conference-latex/rescore_results.md` (appended to Phase 1 output).

### Expected result (from my mental math)
| Regime | Top pipeline | MF/Agg rank | MICE/KM rank | Strong-in-top-4? |
|---|---|---|---|---|
| Ours | MF/Agg | 1 | 2 | ✓ |
| Equal | MICE/KM | 2 | 1 | ✓ |
| Silhouette-only | MICE/KM (or KNN/KM) | 3 | 1 | ✓ (probably) |
| Balance-only | MF/Agg | 1 | 3 | ✓ |
| No-balance | MICE/KM | 3 | 1 | ✓ |
| Separation-heavy | MICE/KM | 2 | 1 | ✓ |

The load-bearing claim is **"strong imputed pipelines always occupy the top 4 (or 5); baselines always occupy the bottom 5 (or 6)"** — the identity of the very top pipeline flips between MF/Agg and MICE/KM depending on how much you weight balance.

Phase 2 will confirm or contradict this preview.

### Deliverables
- Robustness table (as above but with actual numbers) appended to `conference-latex/rescore_results.md`.
- One-line summary of the "always in top-4-or-5" property.

---

## Phase 3 — Patch LaTeX with the new numbers

**Scope:** `conference-latex/main.tex` only. Purely mechanical number substitutions using the numbers locked in Phase 1. No prose rewrites yet.

### Substitutions to make (~16 sites)

| # | Location | Current | New (from Phase 1) |
|---|---|---|---|
| 1 | Abstract (line 97) | "25.30 against 8.09" | new MF-mean vs new baseline-mean |
| 2 | Abstract (line 97) | "roughly threefold gain" | "roughly 2.6-fold gain" (or as computed) |
| 3 | Methodology §III-F (line 251) | "top 14 of 32… rank 20 or worse" | (delete or replace; see Phase 4) |
| 4 | Methodology §III-F (line 251) | "1 (worst) to 32 (best)" | "1 (worst) to 10 (best)" |
| 5 | Methodology §III-F (line 251) | "ranked against the full 32-pipeline benchmark. We report the ten pipelines…" | Rewrite; see Phase 4 (methodology sentence) |
| 6 | Results §V opener (line 258) | "25.30 for MissForest, 18.13 for MICE, 15.70 for KNN, against only 8.09" | new by-imputer means |
| 7 | Results §V opener (line 258) | "19.71, a 2.4× lift… 3.1× for MissForest alone" | new pooled mean + new ratios |
| 8 | Results §V interaction (line 295) | "mean composite 23.98, range 22.05 to 26.60" | new KM-imputed mean + range |
| 9 | Results §V interaction (line 295) | "top rank at 27.30" | new MF/Agg composite |
| 10 | Results §V interaction (line 295) | "MICE (9.65) and KNN (9.35)… None (40%) on Agglomerative (10.35)" | new Agg-imputed + best-Agg-baseline |
| 11 | Results §V interaction (line 295) | "composites 22.05 to 26.60" | (same range as #8) |
| 12 | Cluster profile (line 300) | "composite 27.30, balance 0.685, silhouette 0.756" | composite → new; balance & silhouette unchanged |
| 13 | Cluster profile (line 300) | "composites 22.05 to 26.60" | same as #8 |
| 14 | Conclusion (line 327) | "MissForest reaching 27.30" | new MF/Agg composite |
| 15 | Figure 2 pgfplots (lines ~265–290) | ten bar heights currently 5.75, 7.40, 9.35, 9.35, 9.65, 10.35, 22.75, 23.65, 26.95, 27.65 | ten new 10-scale values |
| 16 | Figure 2 y-axis label / caption | "Composite cluster-validity score" (max implicit 32) | Optional: add "(out of 10)" to caption or axis |

### Files touched in Phase 3
- `conference-latex/main.tex` only

### Risk / check
- After all 16 substitutions, `grep` for the old numbers to catch any missed sites: `grep -n -E "27\.30|25\.30|18\.13|15\.70|8\.09|19\.71|23\.98|22\.05|26\.60|10\.35|9\.65|9\.35|2\.4\\\\times|3\.1\\\\times" main.tex`

---

## Phase 4 — Weight justification prose + robustness table

**Scope:** `conference-latex/main.tex` prose additions. Uses Phase 2 output.

### Additions

**4a. Principled weight-justification paragraph** in §III-F, replacing the current "The weights $\omega_m$ sum to one and take the values…" sentence with:

> The weights $\omega_m$ sum to one and take the values balance $0.35$, silhouette $0.25$, Calinski--Harabasz $0.20$, Dunn $0.10$, Davies--Bouldin $0.05$, and Xie--Beni $0.05$. Balance carries the largest weight because in unsupervised surveillance clustering, the most common failure mode is a single mega-cluster with singletons, which the geometric indices reward. Silhouette is the field-standard separation index. Calinski--Harabasz complements silhouette as a variance-ratio (between-cluster over within-cluster) rather than a nearest-neighbour statistic. Dunn, Davies--Bouldin, and Xie--Beni receive smaller weights because they are more sensitive to outliers and to cluster-shape assumptions.

**4b. Robustness paragraph + table** replacing the current sensitivity claim. Insert after 4a in §III-F, or move to §V results (decide during Phase 4). Draft prose:

> These weights emphasise balance over separation. We tested five alternative regimes to check that this choice does not drive the top-versus-bottom separation (Table~\ref{tbl:weight_sens}). The four strong imputed pipelines (three K-Means-imputed cells and MF/Agg) always occupy the top ranks, and the six degenerate pipelines (all baselines plus MICE/Agg and KNN/Agg) always occupy the bottom ranks. The identity of the top-ranked pipeline depends on how much weight is placed on balance versus separation-only metrics: MF/Agg leads under balance-weighted composites, MICE/KM leads under equal or separation-heavy weights. Both are two-cluster solutions with silhouette above $0.75$; the choice reflects a prior that balanced cluster sizes matter for interpretable public-health surveillance.

Then Table~\ref{tbl:weight_sens} = the 6-row table from Phase 2.

**4c. Update methodology §III-F sentence** on the ranking scope:

> The composite is ranked within the ten reported pipelines, giving a maximum score of $10$. The extended study (in preparation) reports scores within its own 32-pipeline factorial.

### Files touched in Phase 4
- `conference-latex/main.tex` (§III-F rewrite + new table environment)

### Risk / check
- 6-page IEEE limit. Adding a new table costs ~6–8 lines. If Phase 4 pushes over, we cut Table 3.1 (categorical cardinality) to inline text or reduce a paragraph.

---

## Order of execution and blocking dependencies
```
Phase 1  ───►  Phase 2  ───►  Phase 3  ───►  Phase 4
(numbers)     (robustness)   (LaTeX #s)     (weight prose + table)
```
- Phase 3 needs Phase 1 output.
- Phase 4 needs Phase 2 output.
- Phase 3 and Phase 4 do not block each other and could be interleaved, but the sequential order is cleaner.

## Rollback plan
- Each phase is committed separately: `phase1: rescore numbers`, `phase2: weight sensitivity data`, `phase3: apply rescored numbers to paper`, `phase4: weight justification and robustness table`.
- If Phase 3 lands but reviewers push back on 10-scale, revert with `git revert <phase3-sha>` — Phase 1 output (in `rescore_results.md`) is kept for future reference.

## Checklist to sign off before executing each phase
- [ ] Phase 1: notebook produces 10-scale composites; hand math within ±0.05 of notebook output.
- [ ] Phase 2: table produced; qualitative claim "always top-4-or-5" holds across all regimes.
- [ ] Phase 3: `grep` for old numbers returns zero hits; Overleaf compiles cleanly.
- [ ] Phase 4: 6-page limit still holds; the new table fits in one column.
