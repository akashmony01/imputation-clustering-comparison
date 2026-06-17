# Title Swap + Methodology Reframe — No Code, No Experiments

> Local mirror of the approved plan that lives at `~/.claude/plans/curried-hugging-pudding.md`.
> Previous plan in this slot (page-reduction pass) is **complete** and lives in `latex/page_reduction_changes.md`. This file tracks the next task: aligning the paper's framing with what it actually delivers.

## Context

The current title — *"Discovering Suicide Patterns from Incomplete Newspaper-Reported Data in Bangladesh using Imputation and Clustering Pipelines"* — overstates the empirical contribution. Ch4 §4.7 (line 400) and Ch6 Limitation 7 (line 71) both already concede that the best pipeline's two-cluster split is **partly confounded with data-collection source** (2020 Kaggle subset vs. manually added 2017–2019 + 2021–2025 cases). Reviewers at any methods-aware venue will flag this title-vs-content mismatch as overclaiming and reject on the first read.

The fix is to swap the title and align the front matter, Ch1 framing, and Ch6 framing to a methodology-first claim. **No code, no experiments, no figures, no tables, no equations change.** Ch3 and Ch4 already read as methodology work; this pass updates only the framing layer so the paper *claims* what it actually *delivers*.

**Expected publishing impact (honest estimate):** IEEE Access ~30–40% → ~55–65%; PLOS ONE ~35–45% → ~50–60%; BMC Med Research Methodology ~15–20% → ~30–35%. The reframe is *necessary and sufficient* for IEEE Access / PLOS ONE; *necessary but not sufficient* for A-tier journals (those still need a second-dataset validation, out of scope here).

## New title (canonical string, used verbatim everywhere)

> **Comparing Imputation and Clustering Pipelines on Incomplete Newspaper-Reported Suicide Data from Bangladesh: An Exploratory Study**

Properties:
- Methodology-forward verb ("Comparing")
- Keeps "Pipelines" — matches the actual contribution and the IEEE Access methods-track audience
- Defensible exploratory hedge ("An Exploratory Study") — consistent with how Ch4 §4.7 already characterises the result

## Touch-points (text-only)

1. **Title swap — 4 files:** `main.tex` (header comment), `frontmatter/titlepage.tex` (title block), `frontmatter/declaration.tex` (quoted string), `frontmatter/approval.tex` (quoted string).
2. **Abstract reframe** — replace public-health opener with methodology-first opener; keep middle, caveat, keywords unchanged.
3. **Ch1 reframe** — §1.2 problem statement, §1.3 motivation, §1.5 scope, §1.6 contributions (reorder).
4. **Ch4 audit** — verify upstream §4.7 doesn't promise stronger "discovery" claim than line 400 hedges against.
5. **Ch6 reframe** — §6.1 opening goal sentence, §6.2 promote source-cohort observation to a result-level finding, §6.4 shorten Limitation 7 + redirect.
6. **Minor word swaps** — change "pattern discovery" → "exploratory subgroup analysis" in Ch3/Ch5/Ch6 (≤5 occurrences). Skip the generic methods-chapter use at Ch3 line 371.

## Files that will be edited

- `latex/main.tex`
- `latex/frontmatter/titlepage.tex`
- `latex/frontmatter/declaration.tex`
- `latex/frontmatter/approval.tex`
- `latex/frontmatter/abstract.tex`
- `latex/chapters/ch1_introduction.tex`
- `latex/chapters/ch4_results.tex` (audit only; 0–1 sentence edit)
- `latex/chapters/ch6_conclusion.tex`
- `latex/chapters/ch3_methodology.tex` (1–2 word swaps; optional)
- `latex/chapters/ch5_standards.tex` (1 word swap; optional)
- `latex/title_reframe_changes.md` (new — undo log)

**No changes** to: `ch2_literature.tex`, references, tables, figures, equations, page geometry, font/spacing, build script, any `.py` code, any datasets.

## What this does NOT do

- Does not add or remove any experiment, figure, table, equation, or reference
- Does not change `main.pdf` page count meaningfully (~±2 pages from prose-length deltas)
- Does not change any results or numbers
- Does not change chapter/section structure

## Verification

1. Build: `cd latex && ./build.sh` — clean compile (no new errors/warnings beyond baseline).
2. Visual checks on `main.pdf`:
   - Title page renders new title cleanly
   - Declaration and Approval pages show new title in quotes
   - Abstract opener flows into the existing 32-pipeline / composite-score middle, then into the existing caveat
   - Ch1 §1.6 contributions list leads with the framework, not the dataset
   - Ch6 §6.2 contains the source-cohort observation as a result; §6.4 Limitation 7 redirects to it
3. `grep -rn -i "discovering suicide" latex/` returns zero hits in `.tex` files.
4. Page count delta within ±2 pages of current 93.

## Rollback

See `latex/title_reframe_changes.md` for every old-string → new-string pair.
