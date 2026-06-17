# Factual Fixes — Change Log (for undo)

Date: 2026-06-07
Baseline PDF: **93 pages** (state after the title-reframe pass documented in `title_reframe_changes.md`)
Goal: Apply factual corrections identified in the audit pass logged at `~/.claude/plans/curried-hugging-pudding.md`. Each fix was approved by the user via interview.

To undo a single change, restore the value in the "Old" column.

---

## Approved and applied

### F1 — BanglaBERT first-author initial

| File | Line | Old | New |
|---|---|---|---|
| `latex/references.tex` | 278 | `M.~Bhattacharjee {\em et~al.}, ``{BanglaBERT}: Language model pretraining and` | `A.~Bhattacharjee {\em et~al.}, ``{BanglaBERT}: Language model pretraining and` |

**Rationale:** First author of the BanglaBERT paper at the cited arXiv URL (https://arxiv.org/abs/2101.00204) is Abhik Bhattacharjee, not M. Bhattacharjee.

### F2 — ref28 journal name

| File | Line | Old | New |
|---|---|---|---|
| `latex/references.tex` | 127 | `{\em {BMC} Public Health}, 2024.` | `{\em Health Science Reports}, 2024.` |

**Rationale:** The paper at the cited URL (PMC11615682, DOI `10.1002/hsr2.70203`) was published in *Health Science Reports* by Wiley, not in *BMC Public Health*.

### F4 — Ch2 timeframe specificity

| File | Line | Old | New |
|---|---|---|---|
| `latex/chapters/ch2_literature.tex` | 18 | `984 student suicide cases were identified in the post-pandemic period, with females accounting for 61\% of these cases \cite{ref28}.` | `984 student suicide cases were identified between 2022 and 2023 (the post-pandemic period covered by the study), with females accounting for 61\% of these cases \cite{ref28}.` |

**Rationale:** The original "post-pandemic period" phrasing was vague. The Arafat et al. (2024) paper specifically covers 2022–2023; making the window explicit removes ambiguity without changing the claim.

### F5 — Ch3 line 575 prose cleanup

| File | Line | Old | New |
|---|---|---|---|
| `latex/chapters/ch3_methodology.tex` | 575 | `And this composite score, since we have all 32 cases, so 32 is the highest score one case can achieve while the lowest can be down to 1. So the cases closest to 32 is performing better and closest to 1 is performing worst.` | `Because all 32 cases are ranked, the highest achievable composite score is 32 and the lowest is 1; cases closer to 32 perform better, those closer to 1 worse.` |

**Rationale:** Original sentence was notebook drafting prose ("And…so…so…") with a subject-verb mismatch ("cases…is performing"). Rewritten in clean academic register; same factual content.

---

### F3 v2 — Ch1 10,000 deaths qualifier (revisited and applied)

**Status:** Applied with a peer-reviewed source (decision revised after follow-up web search).

**What changed:** After deferring F3 in the initial pass, a follow-up search uncovered Arafat (2025) *"Suicide is Criminal, Data is Silent: Reimagining Suicide Surveillance in Bangladesh — From Police Reports to Public Health Action"* in **International Journal of Mental Health and Addiction** (Springer, DOI 10.1007/s11469-025-01514-1). This paper is by an author already cited in the bibliography (S.M.Y. Arafat, also on ref12/28/29/30), is recent (2025), is peer-reviewed in a Springer journal, and is directly on point about the WHO-vs-police-records discrepancy. With a peer-reviewed source in hand, the trade-off that originally motivated the deferral no longer applies.

| File | Line | Old | New |
|---|---|---|---|
| `latex/chapters/ch1_introduction.tex` | 6 | `Estimates suggest that the country witnesses approximately 10,000 suicide deaths annually, though the true figure is likely far greater due to widespread social stigma, cultural barriers, and the near-total absence of a systematic national suicide surveillance registry \cite{ref12,ref13}.` | `Early epidemiological estimates placed the figure at approximately 10,000 suicide deaths annually \cite{ref12,ref13}, but more recent analyses of Bangladesh police records report an average of roughly 14,719 suicides per year across the 2020--2024 period (about 40 per day) \cite{ref48}, with the true figure likely higher still due to widespread social stigma, cultural barriers, and the near-total absence of a systematic national suicide surveillance registry.` |
| `latex/references.tex` | end of bibliography | (no `ref48` entry) | New `\bibitem{ref48}` for Arafat 2025 IJMHA appended after ref42 (Hernán & Robins) |

**New bibliography entry (`ref48`):**
```latex
\bibitem{ref48}
S.~M.~Y. Arafat, ``Suicide is criminal, data is silent: Reimagining suicide
  surveillance in {Bangladesh}---from police reports to public health action,''
  {\em International Journal of Mental Health and Addiction}, 2025.
\newblock \url{https://link.springer.com/article/10.1007/s11469-025-01514-1}.
```

**Verification after applying F3 v2:**
- [x] Clean build (`./build.sh` re-ran successfully)
- [x] `grep -c "ref48" chapters/ch1_introduction.tex` returns `1` (cite present)
- [x] `grep -c "14,719" chapters/ch1_introduction.tex` returns `1` (quantitative figure present)
- [x] `grep -c "Suicide is criminal" references.tex` returns `1` (bibitem present)
- [x] Page count: 93 (unchanged)

---

## Verification log

- [x] Clean build (`./build.sh` re-ran successfully, no new errors)
- [x] Page count delta within ±1 page
- [x] `grep -n "M.~Bhattacharjee" latex/references.tex` returns zero hits
- [x] `grep -n "BMC} Public Health" latex/references.tex` returns zero hits
- [x] `grep -n "in the post-pandemic period" latex/chapters/ch2_literature.tex` returns zero hits
- [x] `grep -n "And this composite score" latex/chapters/ch3_methodology.tex` returns zero hits

## Tightening opportunities — NOT applied this pass

Per user instruction, 10 tightening opportunities (T1–T10) catalogued in the audit plan at `~/.claude/plans/curried-hugging-pudding.md` were NOT touched. Aggregate potential savings: ~5–6 pages.

## Rollback

Either:
- Reverse each row in the tables above individually, OR
- Restore the listed files from version control.

No equations, figures, tables, numerical results, or chapter structure were changed in this pass.
