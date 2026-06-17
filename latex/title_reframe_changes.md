# Title Swap + Methodology Reframe — Change Log (for undo)

Date: 2026-06-07
Baseline PDF: **93 pages** (state after the page-reduction + orphan-figure passes documented in `page_reduction_changes.md`)
Goal: Align front-matter and framing with a methodology-first claim, without touching code, experiments, figures, tables, equations, or references.

**Old title (in 4 places before this pass):**
> "Discovering Suicide Patterns from Incomplete Newspaper-Reported Data in Bangladesh using Imputation and Clustering Pipelines"

**New title (verbatim):**
> "Comparing Imputation and Clustering Pipelines on Incomplete Newspaper-Reported Suicide Data from Bangladesh: An Exploratory Study"

To undo any single change, restore the Old value listed.

---

## Tier T — Title swap (4 files)

| # | File | Anchor | Status |
|---|---|---|---|
| T1 | `latex/main.tex` | header comment lines 3–5 | pending |
| T2 | `latex/frontmatter/titlepage.tex` | `\LARGE\bfseries` title block, lines 12–14 | pending |
| T3 | `latex/frontmatter/declaration.tex` | quoted title, lines 11–12 | pending |
| T4 | `latex/frontmatter/approval.tex` | quoted title, lines 8–9 | pending |

## Tier A — Abstract reframe

| # | File | Anchor | Change |
|---|---|---|---|
| A1 | `latex/frontmatter/abstract.tex` | opening sentence (lines 11–18) | Replace public-health-first opener with methodology-first opener |

Middle (32 pipelines / composite score / balance penalty), source-confound caveat (lines 32–37), and keywords line are **unchanged**.

## Tier C1 — Ch1 reframe

| # | File | Anchor | Change |
|---|---|---|---|
| C1.1 | `latex/chapters/ch1_introduction.tex` | §1.2 Problem Statement | Reframe goal from "discover hidden patterns" → "what does standard imputation+clustering recover from heterogeneous, severely-incomplete newspaper data, and how do we evaluate that?" |
| C1.2 | `latex/chapters/ch1_introduction.tex` | §1.3 Motivation (line 22) | "interpretable pattern discovery" → "interpretable exploratory subgroup analysis" |
| C1.3 | `latex/chapters/ch1_introduction.tex` | §1.5 Scope (line 50) | "unsupervised pattern discovery" → "unsupervised exploratory subgroup analysis" |
| C1.4 | `latex/chapters/ch1_introduction.tex` | §1.6 Contributions | Reorder so framework is contribution #1; source-cohort observation is contribution #2; dataset expansion is contribution #3 |

## Tier C4 — Ch4 audit

| # | File | Anchor | Change |
|---|---|---|---|
| C4.1 | `latex/chapters/ch4_results.tex` | §4.7 upstream of line 400 | Audit only. Edit only if a stronger "discovery" claim exists upstream that contradicts the line-400 hedge. |

## Tier C6 — Ch6 reframe

| # | File | Anchor | Change |
|---|---|---|---|
| C6.1 | `latex/chapters/ch6_conclusion.tex` | §6.1 line 6 | Reframe opening goal from "rigorous analysis of suicide patterns" → "systematic, methodologically transparent framework for imputation+clustering on severely-incomplete, multi-source social data, demonstrated on Bangladeshi newspaper-reported suicide cases" |
| C6.2 | `latex/chapters/ch6_conclusion.tex` | §6.2 (between Finding 3 and Finding 4) | **Insert a new finding** that promotes the source-cohort observation from Limitation 7 to a result-level methodological observation. ~2 sentences. |
| C6.3 | `latex/chapters/ch6_conclusion.tex` | §6.4 Limitation 7 (line 71) | Shorten — keep the limitation framing but redirect to the new §6.2 finding |

## Tier W — Word-level soften (≤5 occurrences)

| # | File | Anchor | Change |
|---|---|---|---|
| W1 | `latex/chapters/ch3_methodology.tex` | line 556 | "low-noise clusters suitable for suicide data pattern analysis" — keep wording (already neutral; remove the word "discovery" if present) |
| W2 | `latex/chapters/ch3_methodology.tex` | line 583 | "real-world pattern discovery" → "real-world exploratory subgroup analysis" |
| W3 | `latex/chapters/ch5_standards.tex` | line 96 | "unsupervised pattern discovery" → "unsupervised exploratory subgroup analysis" |
| W4 | `latex/chapters/ch6_conclusion.tex` | line 83 | "discovery of more nuanced patterns" → "characterisation of more nuanced patterns" |
| W5 | `latex/chapters/ch6_conclusion.tex` | line 85 (heading) | "pattern discovery to causal understanding" → "descriptive subgroup analysis to causal understanding" |
| W6 | `latex/chapters/ch6_conclusion.tex` | line 89 | "generalisable toolkit for pattern discovery from incomplete social data" → "generalisable toolkit for exploratory subgroup analysis on incomplete social data" |

**Do not** edit `ch3_methodology.tex` line 371 ("discover hidden patterns") — that describes what clustering generically does and is fine in a methods chapter.

---

## Undo procedure

Either:
- Reverse each row in the tables above individually, OR
- Restore the listed files from version control if available.

No equations, figures, tables, references, citations, or numerical results were changed in this pass.

## Verification log (executed 2026-06-07)

- [x] Clean build (`./build.sh` — wrote `main.pdf` 6.16 MiB, no errors)
- [x] Page count: **93** (unchanged from baseline; prose-length delta absorbed)
- [x] `grep -rn -i "discovering suicide" *.tex chapters/ frontmatter/` returns zero hits in `.tex` files
- [x] `grep -rn "Comparing Imputation" *.tex chapters/ frontmatter/` returns expected 4 hits (`main.tex:3`, `frontmatter/titlepage.tex:12`, `frontmatter/declaration.tex:11`, `frontmatter/approval.tex:8`)
- [x] All title swaps applied
- [x] Abstract reframed (methodology-first opener; middle + caveat + keywords preserved)
- [x] Ch1 §1.2/§1.3/§1.5 softened; §1.6 contributions reordered (framework #1, composite #2, source-cohort observation #3, dataset #4, profiles #5)
- [x] Ch4 audit: no edits needed — §4.6.5 line 400 and §4.7 line 415 already hedge correctly
- [x] Ch6 §6.1 opening reframed; §6.2 Finding 4 promoted to methodological observation with cohort details retained; §6.4 Limitation 7 shortened and redirected to Finding 4
- [x] Word-level soften applied: Ch3 lines 556 + 583, Ch5 line 96, Ch6 lines 83 + 85 + 89

**Items still recommended for eye-check on `main.pdf`** (the build doesn't catch these):
- Title page line-wrap at the 3-line split renders balanced
- Abstract reads coherently (no awkward sentence boundary at the splice point)
- Ch1 §1.6 contributions list order reads naturally
- Ch6 §6.2 Finding 4 heading + new methodological framing reads cleanly
- Ch6 §6.4 Limitation 7 redirects to Finding 4 without ambiguity
- ToC entries updated automatically
