# List → Inline Conversion Pass — Change Log (for undo)

Date: 2026-06-07
Baseline PDF: **88 pages** (state after the tightening pass)
After this pass: **87 pages** (−1 page, plus all itemize blocks in Ch3 eliminated)
User constraint: BUBT capstone format; no content lost; every feature name preserved verbatim in inline form.

To undo, restore the multi-paragraph or itemize-block form shown in the "Old" column.

---

## Applied conversions (all `latex/chapters/ch3_methodology.tex`)

All conversions preserve every feature/column/attribute name verbatim. Only the vertical layout changes from one-line-per-item to comma-separated within the surrounding sentence.

### L7 — §3.2.1 source/size/coverage

| Old | New |
|---|---|
| `The base dataset was obtained from Kaggle \cite{ref3}, containing suicide-related records from Bangladesh:` + 3 paragraph-style items (Source / Initial size / Coverage) | Single sentence: `…containing suicide-related records from Bangladesh: the Kaggle Bangladesh Suicide Dataset with an initial size of 760 records × 27 columns, covering the year 2020.` |

### L1 + L8 — §3.2.1 nine new attributes + final dataset statistics

| Old | New |
|---|---|
| Lead-in + `\begin{itemize}` block with 9 `\texttt{}` items + post-stats with `Total records:` / `Total columns:` as paragraph items | Single paragraph: `…nine new attributes were introduced: family_members, position_in_siblings, marital_status, duration_of_separation, profession_description, workplace, financial_condition, previous_health_condition, and previous_suicide_attempt. After expansion, the final dataset contained 1,617 records and 36 columns…` |

### L9 — §3.2.2 column removals

| Old | New |
|---|---|
| Lead-in + 2 paragraph items (`full_name:` / `data_source:`) | Single sentence: `…two columns were permanently removed: full_name (to avoid PII) and data_source (the news URL did not contribute…).` |

### L10 — §3.3.1 column standardisation

| Old | New |
|---|---|
| `…corrective actions were applied:` + 3 paragraph-style steps | Single sentence: `Three corrective actions were applied: all column names were converted to snake_case; spelling errors were corrected (e.g., maritual_status → marital_status); and numerical values stored as strings were converted to appropriate integer or float types.` |

### L2 + L11 — §3.3.2 date/time standardisation + 5 derived features

| Old | New |
|---|---|
| `…To ensure consistency:` + 2 paragraph items + `Five temporal features were derived:` + 5 paragraph items | Single short paragraph: `…To ensure consistency, all dates were standardized to DD/MM/YYYY format and categorical time values were mapped to representative hours (0–23). Five temporal features were then derived: suicide_day, suicide_month, suicide_year, suicide_week, and suicide_weekday.` |

### L12 — §3.3.3 categorical value harmonisation steps

| Old | New |
|---|---|
| `A column-wise iterative cleaning process was applied:` + 3 paragraph items | Single sentence with `;`-separated steps |

### L6 — §3.4 Feature Engineering steps

| Old | New |
|---|---|
| `The following steps were applied before encoding:` + 3 paragraph items | Single sentence: `Before encoding, three final steps were applied: long free-text columns (profession_description, reason_description) were dropped; suicide_date and unix_time were removed after feature extraction; and the final feature set contained 29 columns…` |

### L3 — §3.5.1 Ordinal Encoding features

| Old | New |
|---|---|
| `…applied to the following features:` + 4 paragraph items | Inline: `…applied to age_group, financial_condition, weather_main, and suicide_weekday.` |

### L4 — §3.5.2 One-Hot Encoding features

| Old | New |
|---|---|
| `…applied to the following features:` + 3 paragraph items | Inline: `…applied to gender, workplace, and Religion.` |

### L5 — §3.5.3 Frequency Encoding features

| Old | New |
|---|---|
| `This method was applied to:` + 6 paragraph items | Inline: `This method was applied to profession_group, hometown, reason, method, weather_description, and marital_status.` |

---

## Verification

- [x] Clean build (`./build.sh`, 6.15 MiB, no errors)
- [x] Page count: **87** (was 88; net −1)
- [x] `grep -c '\begin{itemize}' chapters/ch3_methodology.tex` returns **0** (all itemize blocks eliminated from Ch3)
- [x] All feature names spot-checked present in inline form
- [x] No orphan `\item` / `\begin{itemize}` / `\end{itemize}` lingering

## Honest reflection on the modest 1-page saving

The plan projected ~2 pages reclaimed. We landed at 1. Why:

- The vertical-line savings (~50 lines reclaimed) accumulated mostly in mid-Ch3 prose flow, where the gains pushed content earlier within the chapter without quite reaching the next page-boundary trigger.
- Page boundaries are quantised — saving 35 lines reorganises content within existing page allocations; saving 38+ lines typically triggers a full-page shift. We landed just under the threshold.
- The build's auto-rerun with `\widowpenalty=10000` + `\clubpenalty=10000` may also have absorbed some gain into improved widow/orphan avoidance rather than page reduction.

## Cumulative page history across all sessions

| Pass | Result |
|---|---|
| Original PDF | 104 pages |
| Page-reduction (font + spacing) | 85 pages (−19) |
| Orphan-figure appendix added | 93 pages (+8) |
| Title swap + methodology reframe | 93 pages (=) |
| Factual fixes (F1-F5, F3 v2) | 93 pages (=) |
| Tightening (S + A + B + C6) | 88 pages (−5) |
| **List → inline (this pass)** | **87 pages (−1)** |

Total reduction vs. the original 104-page baseline: **−17 pages** (~16%).

## What's left as a lever to reach 80

Per honest assessment, the remaining bigger levers all cross a previously stated boundary:
- Drop appendix sub-figures (~7 pages, but loses per-feature comparison plots)
- Cut §1.7 (Washington Accord) or §6.3 (Achievement table) — violates BUBT format
- Cut chapter intro paragraphs — violates "don't shorten things that need detailed explanation"

Recommend stopping at 87 unless one of those boundaries is open to revisit.

## Rollback

Restore the multi-paragraph or itemize form shown in the "Old" column of each section.
