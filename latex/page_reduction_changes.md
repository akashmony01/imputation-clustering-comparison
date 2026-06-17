# Page-Reduction Pass — Change Log (for undo)

Date: 2026-05-23
Baseline PDF: **104 pages**
After this pass: **85 pages** (−19 pages, ~18% reduction)
Goal: reduce page count without removing/condensing any content.

To undo any single change, reverse the value in the file/line listed.

---

## Tier A — font + line spacing (BUBT-compliance fix)

| # | File | Line | Old | New |
|---|---|---|---|---|
| A1 | `latex/main.tex` | 9 | `\documentclass[12pt,a4paper,oneside]{report}` | `\documentclass[11pt,a4paper,oneside]{report}` |
| A2 | `latex/preamble.tex` | 21 | `\onehalfspacing` | `\setstretch{1.15}` |

## Tier B — global whitespace tightening

| # | File | Line | Old | New |
|---|---|---|---|---|
| B1 | `latex/preamble.tex` | 41 | `\titlespacing*{\chapter}{0pt}{40pt}{30pt}` | `\titlespacing*{\chapter}{0pt}{20pt}{18pt}` |
| B2 | `latex/preamble.tex` | 51 | `\titlespacing*{name=\chapter,numberless}{0pt}{40pt}{30pt}` | `\titlespacing*{name=\chapter,numberless}{0pt}{20pt}{18pt}` |
| B3 | `latex/preamble.tex` | 62 | `\setlength{\parskip}{0.5\baselineskip plus 1pt minus 1pt}` | `\setlength{\parskip}{0.35\baselineskip plus 1pt minus 1pt}` |
| B4 | `latex/preamble.tex` | after captionsetup block | (none) | `\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}` + 4 more float/caption skip lines |

## Tier C — frontmatter local trims

| # | File | Line | Old | New |
|---|---|---|---|---|
| C1 | `latex/frontmatter/dedication.tex` | 7 | `\vspace*{2in}` | `\vspace*{1.4in}` |
| C2 | `latex/frontmatter/acknowledgment.tex` | 10, 18, 24, 31 | `\vspace{0.1in}` (4×) | (removed) |
| C3 | `latex/frontmatter/abstract.tex` | 4 | `\titlespacing*{name=\chapter,numberless}{0pt}{-30pt}{20pt}` | (removed — no longer needed) |
| C4 | `latex/frontmatter/abstract.tex` | 50 | `\titlespacing*{name=\chapter,numberless}{0pt}{40pt}{30pt}` | (removed — paired restore no longer needed) |

---

## Orphan-figure fix (appendix + ch4)

| # | File | Change |
|---|---|---|
| O1 | `images/all_numerical_comparison.png` → `latex/figures/` | Copied |
| O2 | `images/all_categoricaL_comparsion.png` → `latex/figures/` | Copied (filename has typo; kept as-is to match disk) |
| O3 | `latex/figures/all_numerical_comparison_p1.png … _p4.png` | Generated 4 vertical splits via Python/PIL (originals are 1489×8779 — too tall for a single page at readable width). **Splits align to whitespace gaps between subplot rows** (detected as contiguous bands of mostly-white rows ≥ 30px long) so no chart is cut through. Closest qualifying gap to each quartile boundary is used. Same for categorical → 4 part files. |
| O4 | `appendix.tex` | Added 8 `\begin{figure}[H]` blocks (4 numerical + 4 categorical). Each part renders at full text-width on its own page. `\ContinuedFloat` keeps them as one logical figure each (Figure S3 = numerical, Figure S4 = categorical). Short caption `[]` on parts 2–4 suppresses extra List-of-Figures entries. Labels `fig:appendix_numerical_all` and `fig:appendix_categorical_all` placed on Part 1 of each. |
| O5 | `ch4_results.tex:333` | `Figure S4` → `Figure~\ref{fig:appendix_numerical_all}` (resolves to S3) |
| O6 | `ch4_results.tex:381` | `Figure S5` → `Figure~\ref{fig:appendix_categorical_all}` (resolves to S4) |

Page count: 85 → **93** (+8 for the 8 sub-figure pages). Trade-off: +6 pages over the squashed-but-unreadable version, but every plot now legible at full text-width.

## Follow-up equation fixes (ch3_methodology.tex)

| # | File | Line | Old | New |
|---|---|---|---|---|
| E1 | `ch3_methodology.tex` | 512 | `...similar to Davies-Bouldin but with a focus on fuzzy partitioning (adapted for crisp clusters). Formula:` | `...similar to Davies-Bouldin but originally formulated for fuzzy partitioning; the crisp-clustering form is used here. Formula:` |
| E2 | `ch3_methodology.tex` | 513–515 | `XB = (Σᵢ Σₖ (xᵢ−cₖ)²/n) / minᵢ≠ⱼ ‖cᵢ−cⱼ‖²` (sums every point to every centroid — incorrect) | `XB = (Σₖ Σ_{xᵢ∈Cₖ} ‖xᵢ−cₖ‖²) / (n · minᵢ≠ⱼ ‖cᵢ−cⱼ‖²)` (each point contributes only to its own cluster centroid — correct hard-clustering form) |
| E3 | `ch3_methodology.tex` | 552 | `where ωₘ is the weight of metric m, and rₘ is its rank (0 for NaN).` | `where ωₘ is the weight of metric m, and rₘ ∈ {0,1,…,n−1} is its zero-indexed rank (best = 0). NaN values contribute 0 points directly, bypassing the formula.` |

## Undo procedure

Either:
- Reverse each row in the table above individually, OR
- Delete this change log + re-apply the values listed in the "Old" column for every row.

No content, references, figures, tables, or chapter prose was changed.
