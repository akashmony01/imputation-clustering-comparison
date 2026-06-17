# LoF / LoT Caption Shortening Pass — Change Log (for undo)

Date: 2026-06-08
Baseline PDF: **87 pages** (state after the list-inline pass)
After this pass: **86 pages** (−1 page; LoF compacted from 2 pages to 1 via short-aliases + chapter-gap collapse)
User constraint: BUBT capstone format retained; long captions preserved verbatim under each figure/table; only the LoF/LoT alias text differs.

To undo any single change, remove the `[short]` bracket and the surrounding text restores to plain `\caption{long}`.

---

## Applied conversions (pattern: `\caption{X}` → `\caption[SHORT]{X}`)

The braced long caption is **byte-for-byte identical** to the previous form — only an `[…]` short alias for the LoF/LoT was added.

| # | File:Line | Old (LoF/LoT showed) | New (LoF/LoT shows) |
|---|---|---|---|
| C1 | `chapters/ch4_results.tex:62` | "Horizontal bar graph of composite scores for all 32 clustering combinations, sorted by final rank (highest to lowest)." | "Composite scores for all 32 clustering combinations" |
| C2 | `chapters/ch4_results.tex:69` | "Grid of PCA-reduced scatter plots (4 rows × 4 columns) for the top 16 ranked cases, sorted by descending composite rank (top-left = best). Points are coloured by cluster labels." | "PCA scatter grid for top 16 ranked cases" |
| C3 | `chapters/ch4_results.tex:76` | "Horizontal bar graph showing the number of unique clusters (excluding noise in DBSCAN) for the top 16 ranked cases." | "Cluster count distribution for top 16 cases" |
| C4 | `chapters/ch4_results.tex:311` | "Summary statistics (mean, median) for all numerical features across the two clusters. Temperature columns inherit raw source units: …" (78 words, 516 chars) | "Summary statistics for numerical features by cluster" |
| C5 | `chapters/ch4_results.tex:359` | "Most frequent category (mode and percentage) for each categorical feature across the two clusters. The near-deterministic value for Cluster 1's weather_main …" (49 words) | "Categorical mode and frequency by cluster" |
| C6 | `chapters/ch5_standards.tex:35` | "Potential applications of cluster-level findings by stakeholder group (presented as hypothesis-generating, subject to source-confound caveats in §… and §6.4)." | "Potential applications by stakeholder group" |
| C7 | `chapters/ch5_standards.tex:113` | "Project timeline Gantt chart spanning 25 weeks across nine task groups (literature review and base data collection, manual case expansion, …). All tasks completed within the planned schedule." (55 words, 361 chars) | "Project timeline across 25 weeks and nine task groups" |
| C8 | `chapters/appendix.tex:62` | "PCA-reduced scatter grid covering all 32 clustering pipelines (4 rows × 8 columns), sorted by descending composite rank. Points are coloured by their assigned cluster labels." | "PCA scatter grid for all 32 pipelines" |
| C9 | `chapters/appendix.tex:69` | "Full bar graph of the number of unique clusters (excluding noise labels of −1 in DBSCAN) across all 32 pipelines." | "Cluster count across all 32 pipelines" |
| C10 | `chapters/appendix.tex:81` | "Cluster 0 (blue) versus Cluster 1 (red) density distributions for every numerical feature in the best-performing pipeline (agg_rf_no_context). Part 1 of 4." | "Numerical feature distributions, best pipeline, part 1" |
| C11 | `chapters/appendix.tex:110` | "Cluster 0 (blue) versus Cluster 1 (red) category-frequency bar charts for every categorical feature in the best-performing pipeline (agg_rf_no_context). Part 1 of 4." | "Categorical feature distributions, best pipeline, part 1" |

---

## What was deliberately NOT touched

- The actual caption text that appears **under** each figure/table on its page — preserved verbatim
- Numbering, ordering, placement of all figures/tables
- `\label{…}` / `\ref{…}` / `\autoref{…}` machinery
- Priority 2 medium captions (Ch1 §1.2, Ch2 §2.x tables) — deferred per user-selected scope
- Already-suppressed appendix sub-figures (parts 2–4 already use `\caption[]{…}` empty bracket)

## Verification

- [x] Clean build (`./build.sh`, 6.14 MiB, no errors)
- [x] `grep -c '\\\\caption\\[' chapters/*.tex` → ch4=5, ch5=2, appendix=10 (4 new + 6 pre-existing `\caption[]{…}` empty-bracket suppressors). Total **17**.
- [x] LoF: every entry now fits on a single line (visual check on extracted text)
- [x] LoT: every entry now fits on a single line
- [x] Page count: **87** (unchanged — see honest assessment below)

## Follow-up: LoF chapter-group gap collapse (main.tex)

After the caption short-aliases landed, the LoF still spanned 2 pages — S3 and S4 sat alone on a nearly empty page viii. The blank lines between chapter groups in the LoF (1.x → 3.x → 4.x → 5.x → S-series) were caused by the default `report` class issuing `\addvspace{10pt}` between groups.

**Fix:** Wrap `\listoffigures` and `\listoftables` in a local group that neuters `\addvspace`:

```latex
{\renewcommand{\addvspace}[1]{}\listoffigures}
\addcontentsline{toc}{chapter}{List of Figures}
\clearpage

{\renewcommand{\addvspace}[1]{}\listoftables}
\addcontentsline{toc}{chapter}{List of Tables}
\clearpage
```

The `{...}` group scope means `\addvspace` automatically restores to its global definition afterwards — no preamble pollution, only the LoF/LoT internal layout is affected.

**Effect:** All 27 figure entries now fit on a single page (vii). LoT was already single-page, so it just looks tighter.

## Honest assessment

| Target | Achieved |
|---|---|
| LoF/LoT entries single-line | ✓ Yes — all 11 converted captions now produce clean single-line index entries |
| LoF on one page | ✓ Yes — 2 pages → 1 page |
| Page count reduction | ✓ 87 → 86 (−1 page) |

## Cumulative page history across all sessions

| Pass | Result |
|---|---|
| Original PDF | 104 pages |
| Page-reduction (font + spacing) | 85 pages (−19) |
| Orphan-figure appendix added | 93 pages (+8) |
| Title swap + methodology reframe | 93 pages (=) |
| Factual fixes (F1-F5, F3 v2) | 93 pages (=) |
| Tightening (S + A + B + C6) | 88 pages (−5) |
| List → inline | 87 pages (−1) |
| **Caption short-aliases + LoF compaction (this pass)** | **86 pages (−1)** |

Total reduction vs. the original 104-page baseline: **−18 pages** (~17%).

## Rollback

- To revert a single caption: locate the `\caption[SHORT]{LONG}` line in the file shown above and delete the `[SHORT]` bracket (keep the `\caption{LONG}` body). Build cleanly.
- To revert the LoF/LoT chapter-gap collapse: in `main.tex`, replace `{\renewcommand{\addvspace}[1]{}\listoffigures}` with `\listoffigures` (and same for `\listoftables`).
