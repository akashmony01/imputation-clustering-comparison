# Camera-Ready Revision Plan — IEEE CSDE 2026 (Paper ieee-csde_4087)

**Status:** Accepted. Camera-ready + signed IEEE copyright form due **30 September 2026**.
**Paper:** `final_overleaf/main.tex` (currently exactly 6 pages, 20 refs).

## Working constraints (agreed)
- **No pipeline re-runs.** Post-hoc arithmetic on saved data is allowed; re-clustering / re-imputation is not.
- **Writing-first.** Every reviewer point is addressed through prose and honest scoping, not new experiments.
- **Style unchanged.** No prose colons, semicolons, or em-dashes. Short, human sentences.
- **Structure:** extend existing paragraphs in place. No new "Threats to Validity" heading.
- **Space:** add everything first, then re-read the whole paper and decide trims (Related Works is the likely trim source). We are at the 6-page ceiling, so expect an overflow to resolve at the end.

## Global decisions (from the interview)
- The four experiment requests (masking test, bootstrap, mapping-sensitivity, full distribution comparison) are **deferred to Future Work** with explicit, honest reasons.
- **Source naming corrected for accuracy.** Real process = Google keyword search across Bangladeshi online news portals, not four fixed outlets. We will write "Bangladeshi online newspapers and news portals, such as Prothom Alo, The Daily Star, Jugantor, and Ittefaq."
- **No formal inter-rater agreement exists** (teammates split the work by year, no double-coding). We state the real quality control honestly and name the absence of formal double-coding as a limitation. We do NOT invent a kappa.
- Selection-bias concession = **brief** (one clear sentence).
- LLM-mapping validation = **counts only** (918 to 156, all reviewed, 3 overridden).
- A **response-to-reviewers document** will be produced from this plan.

## Locked facts for the edits
- **Collection process:** team searched Google with suicide-related keywords ("suicide in bangladesh", "bangladesh suicide", "suicide bangladesh 2021", etc.), filtered by year (sometimes month), often restricted to the News tab, opened each link, read the report, and extracted fields. Bangladesh-only. Included **confirmed completed suicides** only.
- **Team + dedup:** multiple collectors partitioned the years among themselves and worked month by month in sequence (so no two people covered the same period). One author then reviewed every case end to end, checking name, place, and date by eye, to remove duplicates and inconsistencies.
- **Cohort split:** ~760 from the public 2020 collection (`alom2020bangladesh`), essentially all reported in 2020; ~857 collected manually for 2017 to 2019 and 2021 to 2025.
- **Per-year counts (reported year):** 2020 = 762, 2022 = 313, 2024 = 235, 2021 = 152, 2019 = 88, 2018 = 14, 2023 = 12, 2017 = 1, 2025 = 1; reported year is itself missing for a small number of cases.

---

# Issue-by-issue: what we change, what we do not

Tags: **CHANGE** = new/edited prose · **ALREADY** = present, we make it explicit · **DEFER** = future work with stated reason.

## Reviewer 2 — "acceptable as exploratory if conclusions stay bounded"

### 2.1 Explain the LLM mapping and give manual-validation stats — ALREADY (tighten)
- Already in §III-A: 918 raw values to 156 canonical categories, GPT-4 proposed, authors validated all, 3 overridden.
- **Edit:** make the validation counts explicit in one sentence. No new claim.

### 2.2 Compare imputed vs observed marginal/joint distributions — DEFER
- **Reason:** a proper marginal-and-joint distribution check is a validation study in its own right and belongs with the masking test. Not doable inside the camera-ready window without a re-run.
- **Edit:** add to the Future Work sentence ("compare imputed against observed distributions").

### 2.3 Cluster-profile uncertainty; do not treat imputed values as observed — CHANGE
- **Edit:** in the Results interpretation, add one sentence that the cluster profiles rest on imputed values, so they carry imputation uncertainty and are read as structure, not as observed fact. Reinforces the existing "structure recovery, not epidemiological discovery."

### 2.4 Analyze source, year, and collection-method effects — ALREADY + CHANGE
- The source-cohort confound is already the central caveat. The new provenance paragraph (see 4.2/4.3) adds per-year counts and the two-cohort origin explicitly.
- **Edit:** covered by the provenance paragraph plus the existing confound discussion.

### 2.5 No population denominator; cannot estimate incidence/prevalence — CHANGE
- **Edit:** one prominent sentence in the limitations that the corpus has no population denominator, so it cannot estimate suicide incidence or prevalence and is not an epidemiological sample.

### 2.6 Responsible-reporting safeguards — CHANGE (strengthen Ethics)
- **Edit:** add to the Ethics section that we report only aggregate structure, publish no individual-level identifying details, and describe no methods of suicide at a level that could sensationalize or instruct, following responsible-reporting guidance.

## Reviewer 3 — "methodologically thoughtful"

### 3.1 MNAR may distort sensitive variables (occupation, location, circumstances) — CHANGE
- **Edit:** in limitations, state that under the likely MNAR mechanism the imputers may systematically distort exactly the sensitive, least-reported fields, so those imputed fields are treated as support for structure, not as reliable per-field values.

### 3.2 Validate imputation via artificial masking — DEFER
- **Reason:** requires re-imputing masked data (a re-run). Already named in Future Work.
- **Edit:** keep and sharpen the existing mask-and-recover Future Work item.

### 3.3 Is the two-cluster split a collection artifact? — ALREADY (foreground)
- We already show both leaders split on the 2020 cohort vs the rest and say the split is confounded with collection source.
- **Edit:** add one explicit clause that the boundary likely reflects a collection-process change (the 2020 public dump vs later manual collection) rather than epidemiological structure. This is what the reviewer asked and we already believe it.

### 3.4 Bootstrap stability and alternative cluster counts — DEFER (bootstrap) + ALREADY (k)
- Alternative k: the number of clusters was already grid-searched (2 to 20 for K-Means, 2 to 10 for Agglomerative) and k=2 was selected. **Edit:** state in Results that k=2 emerged from the sweep, so it is a selected value, not an assumption.
- Bootstrap: **DEFER** (needs re-clustering). **Edit:** add "bootstrap resampling for cluster-stability confidence intervals" to Future Work.

### 3.5 Keep internal indices separate from public-health validity — CHANGE
- **Edit:** one sentence that internal validity indices measure geometric cluster quality only and are not evidence of substantive public-health or epidemiological validity.

### 3.6 Sensitivity to the 918 to 156 mapping — DEFER
- **Reason:** re-deriving alternative mappings and re-running imputation and clustering is a re-run.
- **Edit:** add "sensitivity of results to the category-consolidation mapping" to Future Work.

## Reviewer 4 — "serious concerns" (addressed by bounding + provenance)

### 4.1 Non-representativeness and selection bias — CHANGE (brief concession)
- **Edit:** one clear sentence in limitations that newspaper-reported cases are a non-representative, selection-biased sample (driven by geography, gender, age, method, and media access) and that imputation cannot correct this selection bias.

### 4.2 How the 1,617 cases were identified, screened, deduplicated, verified — CHANGE (new provenance paragraph)
- **Edit:** expand the opening of §III-A into a short data-provenance paragraph using the locked facts: keyword search, News-tab filtering, Bangladesh-only, confirmed-completed-suicide inclusion, year-partitioned collection by multiple collectors, month-by-month sequencing, and a final single-author end-to-end consistency and duplicate review. State plainly that no formal inter-rater agreement statistic was computed.

### 4.3 Distinguish new vs public data; per-source/year counts; distributional differences — CHANGE
- **Edit:** in the same provenance paragraph, give the cohort split (~760 public 2020 vs ~857 manual 2017 to 2025) and the per-year counts, and note the distributional difference between the cohorts is exactly the source-cohort confound the paper analyzes. Per-outlet counts were not separately tracked (Google-sourced), stated honestly.

### 4.4 90% missingness recoverability; field-specific rates — ALREADY (emphasize)
- Fig. 1 already gives per-field rates. The key rebuttal: fields above 70% missing are **dropped, never imputed**, so the 90% fields (prior attempt 91.7%, separation 96.2%) are removed, not reconstructed.
- **Edit:** add one sentence making explicit that the highest-missingness fields are dropped rather than imputed, so imputation operates only on moderately incomplete fields.

### 4.5 Missing-data mechanism not examined; methods invalid under MNAR — CHANGE
- **Edit:** concede that MissForest, MICE, and KNN assume ignorable (MAR) missingness and do not guarantee valid estimates under MNAR, which is plausible here, so we claim usable structure rather than accurate per-cell reconstruction. (Merges with 3.1 and 4.1 in the limitations paragraph.)

---

# Where each edit lands in main.tex
- **§III-A Data Description and Preprocessing:** provenance paragraph (4.2, 4.3, 2.4), drop-not-impute sentence (4.4), tighten LLM counts (2.1).
- **§IV Results and Analysis:** k=2-from-sweep sentence (3.4), imputed-not-observed and indices-not-validity caveats (2.3, 3.5), collection-process-change clause (3.3).
- **§V Conclusion / limitations:** selection bias (4.1), MNAR invalidity (4.5, 3.1), no denominator (2.5).
- **§V Future Work:** expand deferral list (2.2, 3.2, 3.4-bootstrap, 3.6).
- **Ethics and Data Availability:** responsible-reporting sentence (2.6).

# Space plan
Additions are roughly one new paragraph plus 6 to 8 sentences spread across sections. This will push past 6 pages. After all edits land, re-read the whole paper and trim, most likely from Related Works, until it returns to 6 pages. Do not trim any reviewer-driven addition.

# Deliverables
1. Edited `final_overleaf/main.tex` (this plan applied).
2. `final_overleaf/response_to_reviewers.md` derived from the issue-by-issue section above.
