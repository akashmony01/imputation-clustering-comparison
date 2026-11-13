# Methodology Restructure Plan

Source of truth for the Methodology rewrite. Built from the agreed restructure plus the
teacher's 8 comments (inst.md). Implement phase by phase, pause after each for review.

---

## Style rules (apply to EVERY new or edited sentence, whole paper)
- **No colons in prose.** Split into two sentences instead.
- **No em-dashes (`---`) or ` -- ` dashes in prose.** Use commas, full stops, or parentheses.
- **No semicolons.** Use short separate sentences.
- **Short, fluent, human sentences.** No long mechanical clauses, no overly general filler.
- **Be specific.** Describe what we actually did, not generic method descriptions.
- **Cite each method once**, right after its name. Never repeat a citation across sections.

---

## Target Methodology structure
```
\section{Methodology}
  (short generic intro paragraph, 1-2 sentences)

  \subsection{Data Description and Preprocessing}      <- A  (paragraphs only, no sub-sub)
      data -> missingness (Fig 1 here) -> conditional filling -> encoding
      -> categorical rationalization (TRIMMED) -> drop-vs-impute design + Table 1

  \subsection{Methodological Pipeline}                 <- B  (teacher's exact name)
      \subsubsection{Imputation}
      \subsubsection{Clustering}
      \subsubsection{Score}      (composite + balance equations kept, prose trimmed)
      (Fig 2 pipeline at the very end, placed BEFORE its description paragraph)

  \subsection{Algorithm}                               <- C  (new, pseudocode)
```

### Figure / table numbering after restructure
- **Figure 1** = missingness (in A). Short caption.
- **Figure 2** = pipeline / intro.png (end of B). Placed first, then described.
- **Figure 3** = clusters (Results, unchanged).
- **Table 1** = design / `tbl:design` (in A). Short caption, full column width.
- **Table 2** = `tbl:rankdist` (Results, unchanged).
- **Algorithm 1** = pseudocode (in C).

### Old -> new mapping
| Current subsection | Goes to |
|---|---|
| (intro paragraph "The pipeline proceeds...") | trimmed to a generic 1-2 sentence intro |
| Dataset and Missingness | A |
| Categorical Schema Rationalization | A (trimmed hard) |
| Deterministic Recovery and Drop-versus-Impute Design | A (end, with Table 1) |
| Imputation Methods | B > Imputation |
| Clustering Algorithms | B > Clustering |
| Composite Cluster-Validity Score | B > Score |
| (none) | C > Algorithm (new) |

---

## Phase 0 — Preamble + figure re-enable (no prose changes)
- Re-add `\usepackage{algorithm}` and `\usepackage{algpseudocode}` (removed earlier; needed for pseudocode).
- Un-comment the pipeline figure block (delete the `\begin{comment}` / `\end{comment}` wrapper). It will be physically moved to the end of B in Phase 3.
- Nothing else.

## Phase 1 — Section skeleton
- Add a short generic intro paragraph after `\section{Methodology}` (no stage-by-stage detail; that lives in the subsections).
- Insert the three new subsection headings (A, B with three subsubsections, C). Content reflows in later phases.

## Phase 2 — A. Data Description and Preprocessing
Merge the three current preprocessing subsections into one, paragraphs only. Order:
1. **Data description.** 1,617 cases, source outlets, 29 retained features (13 categorical, 16 numerical). Dataset citation stays here (single, `alom2020bangladesh`).
2. **Missingness.** Severity, the band spread, 3.5% row-complete, listwise not viable. **Figure 1 (missingness) placed BEFORE this paragraph**, then described in the text. **Shorten the caption** (comment 2) to one plain line, move the omitted-fields / recovery / abbreviation detail into the paragraph.
3. **Conditional filling (deterministic recovery).** Geocoding for lat/long, timestamp, Meteostat weather. Keep the "these are retrieved not estimated" point briefly.
4. **Encoding.** 29 features. One-hot expands 3 nominal fields to 11 columns, giving 37 for KNN/MICE. 29 label-encoded for MissForest. Keep the `29-3+11` explanation (it fixed a real confusion).
5. **Categorical rationalization (TRIMMED HARD, comment 4).** Operations-first, 2-3 short sentences on what we did (spelling normalization, place->district, verbose->canonical, minority-category preservation). One short sentence of LLM disclosure. Fix the grammar on the Chakma/Marma/Santal line (comment 6). Keep the AutoDCWorkflow contrast only if it survives the trim; otherwise drop.
6. **Drop-vs-impute design + Table 1.** The shared-recovery-base controlled-comparison point. **Table 1 caption shortened** (comment 5), move the "MICE 1,613 rows" note to text. **Table full column width** (comment 5): switch to `tabular*{\columnwidth}` or widen columns so it fills the column instead of sitting narrow.

## Phase 3 — B. Methodological Pipeline
Write each subsubsection as sequential steps that follow the pipeline diagram, citations after the method name (comment 3).
- **Imputation.** Trim the current paragraph (comment 7). Combine, remove repetition. Keep the specifics: three imputers, no-context predictors, MissForest 100 trees on 29 label cols, KNN k=5 Euclidean on 37 one-hot, MICE per-variable BayesianRidge single pass, residual <=0.25%. Citations once each (already single now).
- **Clustering.** Standardise + PCA, then K-Means (grid over k, init, n_init, max_iter) and Agglomerative (linkage, metric). Short sentences. Keep the "different paradigms guard against artefacts" point in one line.
- **Score.** Keep BOTH equations exactly (balance eq and composite eq). **Shorten the surrounding prose** (comment 8) to a compact walkthrough. Keep enough to read the equations (what p_k, K, r_m, omega_m, n are; best gets 10 points down to 1). Keep the weight-free pointer to Results (we do not fix the weights). Trim the longer explanation we added earlier.
- **End of B.** Re-add **Figure 2 (pipeline)**. Place the figure, then a short paragraph that walks the diagram left to right (comment 1 and 4: figure before description).

## Phase 4 — C. Algorithm (new)
- `\subsection{Algorithm}` with one compact `algorithm` block (~15-18 lines) summarising the whole procedure. Rough shape:
  ```
  Input: raw newspaper records
  1  clean and harmonise categories (design-time dictionaries)
  2  recover lat/long, time, weather from external sources
  3  encode -> 37-col (one-hot/freq) and 29-col (label) matrices
  4  build 5 datasets: 3 imputed (MissForest, KNN, MICE) + 2 drop baselines
  5  for each dataset: standardise, PCA
  6      run K-Means and Agglomerative (tuned)
  7      compute 6 validity metrics + balance term
  8  rank all pipelines under the composite over 100k weightings
  Output: weight-robust ranking + best cluster structure
  ```
- Keep it short. This is the first thing to shrink or cut if we go over 6 pages.

## Phase 5 — Style sweep + verify + page check
- Sweep all new/edited text for colons, em-dashes, semicolons. Replace with short sentences.
- Confirm the Chakma grammar fix landed.
- Verify: all `\ref`/`\cite` resolve, figures number 1/2/3, tables 1/2, algorithm 1, no dangling `fig:pipeline`.
- **Page count is Overleaf-only.** Figure 2 + algorithm add space, the trims offset. If over 6 pages, shrink then cut the pseudocode first, then the Score prose.

---

## Open decisions (confirm before/while implementing)
1. **Algorithm placement.** Own subsection C (this plan, your earlier note) vs inside B (teacher comment 4). Default here is own subsection C.
2. **AutoDCWorkflow citation** in the LLM part. Keep the one-clause contrast, or drop it in the trim. Default is drop if it does not fit in 2-3 sentences.
3. **How compact for Score.** Keep a 2-3 sentence walkthrough per equation, or go minimal (just name the terms). Default is compact walkthrough.

## Execution order
Phase 0 -> 1 -> 2 -> 3 -> 4 -> 5. Pause after each phase for review. Do not batch all at once.
