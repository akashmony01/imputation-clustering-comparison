# Response to Reviewers — IEEE CSDE 2026

**Paper ID:** ieee-csde_4087
**Title:** Addressing Extensive Missingness in Newspaper-Reported Suicide Data Through Imputation and Clustering Techniques

We thank the reviewers for their careful and constructive comments. The camera-ready version has been revised throughout to keep the conclusions carefully bounded, to describe the data collection in full, and to strengthen the ethical safeguards. Every reviewer point is addressed below with a pointer to where the change appears. Comments that call for additional experiments are addressed as explicit, scoped future work, because re-running the imputation and clustering pipeline was outside the camera-ready window. The paper remains six pages.

*Reviewer 1 submitted no comments.*

---

## Reviewer 2 — "acceptable as an exploratory methodological study if conclusions remain carefully bounded"

**2.1 Explain the deterministic LLM-derived category mapping and provide manual-validation statistics.**
Addressed in Section III-A (Data Description and Preprocessing). We now state that 918 raw values across 11 fields were consolidated to 156 canonical categories (an 83% reduction), that all 156 mappings were reviewed and validated by the authors, and that the model (GPT-4) was overridden in three cases. The model was used only at design time, and the validated mappings ship as deterministic dictionaries, so the runtime pipeline is reproducible.

**2.2 Compare imputed marginal and joint distributions with observed-data distributions.**
Added as an explicit future-work item in Section V. A full marginal-and-joint distribution comparison is a validation study in its own right and requires re-running the imputation, so we scoped it as future work rather than reporting a partial check.

**2.3 Add cluster-profile uncertainty and avoid interpreting imputed variables as observed facts.**
Addressed in Section IV (Results and Analysis). We now state that the cluster profiles rest on imputed values, so they carry imputation uncertainty and describe structure rather than observed fact.

**2.4 Analyze newspaper-source, year, and collection-method effects explicitly.**
Addressed in Section III-A and Section IV. The new data-provenance paragraph reports the two-cohort origin and the per-year case counts (2020 dominates with 762 cases, followed by 2022, 2024, 2021, and 2019). Section IV states that the recovered two-cluster boundary most likely reflects a change in collection method rather than epidemiological structure.

**2.5 The absence of a population denominator means the dataset cannot estimate incidence or prevalence; state this prominently.**
Addressed in Section V. We now state plainly that the corpus has no population denominator and therefore cannot estimate suicide incidence or prevalence.

**2.6 Preserve responsible-reporting safeguards.**
Addressed in the Ethics and Data Availability section. We report only aggregate cluster structure, personal names are removed during cleaning so the released analytical dataset carries no direct identifiers, and we do not describe methods of suicide in any way that could sensationalise them.

---

## Reviewer 3 — "methodologically thoughtful"

**3.1 Because missingness is likely not at random, discuss how each imputation method may distort sensitive variables (occupation, location, circumstances).**
Addressed in Section V. We now state that the imputers assume the missingness is ignorable, and that under a missing-not-at-random mechanism (likely here) they can distort the least-reported fields such as occupation and circumstances, so we treat those imputed fields as support for structure and not as reliable values.

**3.2 Validate imputation quality through artificial masking experiments.**
Added as an explicit future-work item in Section V, described as a mask-and-recover test that hides observed values and measures how well each imputer restores them. This requires re-running the imputation and is therefore scoped as future work.

**3.3 Examine whether the two-cluster structure reflects collection-process changes rather than meaningful epidemiological structure.**
Addressed in Section IV. We state directly that the boundary most likely marks a change in how the data were gathered (the 2020 public collection against the later manual collection) rather than a real epidemiological divide, consistent with the source-cohort analysis the paper reports.

**3.4 Report stability under bootstrap resampling and alternative numbers of clusters.**
Partly addressed and partly scoped. The number of clusters was selected by the grid search rather than fixed in advance, and Section IV now states this. Bootstrap resampling for cluster-stability confidence intervals is added as a future-work item in Section V, since it requires re-clustering.

**3.5 Keep internal clustering indices separate from evidence of substantive public-health validity.**
Addressed in Section IV. We now state that the internal validity indices measure only the geometric quality of the clusters and are not evidence of public-health or epidemiological validity.

**3.6 Provide sensitivity analysis to the 918-to-156 category-consolidation mapping.**
Added as an explicit future-work item in Section V. Testing alternative mappings requires re-deriving them and re-running the pipeline, so it is scoped as future work.

---

## Reviewer 4 — data validity, missing-data assumptions, evaluation, interpretability, and ethics

**4.1 Newspaper-reported cases are not representative, and imputation cannot correct this selection bias.**
Addressed in Section V. We now state plainly that newspaper reports are a selection-biased sample, that reporting depends on factors such as location, gender, age, and method, and that imputation cannot correct that selection bias.

**4.2 Explain how the 1,617 cases were identified, screened, deduplicated, and verified (search terms, sources, inclusion criteria, inter-rater agreement, conflicting reports).**
Addressed with a new data-provenance paragraph in Section III-A. It describes the web keyword search (with example terms), filtering by year and by news, the Bangladesh-only and confirmed-completed-suicide inclusion criteria, the sources (Bangladeshi online newspapers and news portals such as Prothom Alo, The Daily Star, Jugantor, and Ittefaq), the year-partitioned collection by several team members working month by month, and a final single-author end-to-end review by reported name, date, and location to remove duplicates and fix inconsistencies. We also state that no formal inter-rater agreement statistic was computed, because the years were divided between collectors rather than double-coded.

**4.3 Distinguish newly collected from public data; report cases per source and year; assess distributional differences.**
Addressed in Section III-A. We report the split of about 760 public 2020 cases and about 857 manually collected cases for 2017 to 2019 and 2021 to 2025, together with the per-year counts. The distributional difference between the cohorts is exactly the source-cohort confound the paper analyzes in Section IV.

**4.4 Missingness reaching 90% raises recoverability concerns; report field-specific rates and the proportion affected.**
Addressed in Section III-A. Figure 1 reports the per-field missing rates. We now state explicitly that fields above 70% missingness are dropped rather than imputed, so imputation never runs on the sparsest fields and operates only on the fields that remain below that threshold.

**4.5 The missing-data mechanism is not examined; MissForest, MICE, and KNN are not valid under MNAR.**
Addressed in Section V. We concede that the three imputers assume ignorable (MAR) missingness and do not guarantee valid estimates under a missing-not-at-random mechanism, which is plausible here, so we claim usable structure rather than accurate per-cell reconstruction.

---

## Summary of camera-ready changes
- New data-provenance paragraph in Section III-A (collection method, inclusion criteria, sources, deduplication, cohort split, per-year counts).
- Strengthened limitations in Section V (selection bias, MNAR invalidity, no population denominator).
- Strengthened interpretation caveats in Section IV (imputed values are not observed facts; internal indices are not public-health validity; the split likely reflects a collection-process change; k was selected by grid search).
- Expanded future work in Section V (mask-and-recover test, imputed-versus-observed distribution comparison, bootstrap resampling, category-mapping sensitivity).
- Strengthened Ethics section (aggregate-only reporting, no direct identifiers, no sensationalising of methods).
- A factual correction: the small ethnic-religious groups (Chakma, Marma, Santal) are described as merged into a single indigenous category, and the data sources are described accurately as online newspapers and portals.
- The paper remains six pages, and all references are retained.
