# i-COSTE 2026 Conference Paper — Writing Plan

**Compiled:** 2026-06-26 — to be handed to a fresh conversation that will focus exclusively on writing this paper.

**How to use this document:** Read this top-to-bottom before opening any source file. It is self-contained: it captures the project context, the locked scope, the section-by-section content plan, the reusable assets from the thesis, and the pre-writing checklist. After reading, work from the sections in order and check off the pre-writing checklist before drafting.

---

## 1. Project context (one-page brief)

**Source project:** BUBT (Bangladesh University of Business and Technology) CSE undergraduate capstone — *Comparing Imputation and Clustering Methods on Incomplete Bangladeshi Suicide News Data: An Exploratory Study*.

**Thesis state:** Complete, 89-page LaTeX report in `/home/mhmd1/Music/capstone/latex/`, current PDF at `latex/main.pdf`. Defended; teachers' feedback addressed in the post-defense reframe pass (2026-06-23).

**Dataset:** 1,617 suicide cases scraped from Bangladeshi newspapers (2017–2025), 34 analytical columns, severe missingness (50–90% on many columns).

**Methodology (full thesis):** 32-pipeline factorial benchmark = (3 imputation methods × 2 predictor strategies × 4 clustering algorithms = 24 imputed pipelines) + 8 no-imputation baselines (2 baseline datasets × 4 algorithms). Six-component composite score with 35% balance penalty.

**Headline result:** Best pipeline `agg_rf_no_context` (Agglomerative + MissForest, no-context strategy) = composite 27.30/32, two-cluster solution (759 vs 858 records).

**Key load-bearing claims (from MEMORY.md):**
- 8 of 32 pipelines are no-imputation baselines occupying bottom-third ranks
- Pre-imputation missingness audit in §3.2.2 of thesis (Table 3.1) — four bands (77–96%, 45–53%, 24–38%, 0.4–19%)
- Source-cohort confound: cluster boundary aligns with Kaggle 2020 vs manual 2017–19+2021–25 collection cohort
- Temperature unit caveat: Kelvin in Cluster 0 vs Celsius in Cluster 1
- Score margin caveat: top 4 pipelines within 1.7 composite points (do not claim statistical separability)
- Headline imputation lift number: MissForest 23.27 vs baseline 10.90

---

## 2. Conference target — i-COSTE 2026

- **Full name:** 12th IEEE International Conference on Sustainable Technology and Engineering
- **Host:** Bangladesh University of Business and Technology (BUBT) — your own institution; supervisor has a connection
- **Date:** 1–3 November 2026
- **Indexing:** Scopus-indexed IEEE proceedings
- **Page limit:** 6 pages, IEEE two-column conference format
- **Scope fit:** Weak on paper (sustainability/AI conference). We bridge via SDG-3 (good health and well-being) and LMIC public-health surveillance framing. Realistic acceptance edge comes from supervisor connection + Scopus venue + reasonable methodology.

---

## 3. Locked scope decisions (do not re-litigate)

These were settled in the planning conversation on 2026-06-26.

### Title (LOCKED 2026-06-26)
> **Handling Severe Missingness in Newspaper-Reported Suicide Data: An Imputation and Clustering Study for SDG-3 in Bangladesh**

Rationale for this choice over earlier candidates: the title's promise (we handled missingness; does imputation help?) equals our most defensible result, so the title-to-outcome sentence needs no caveat. Candidates that led with "patterns"/"benchmark" were set aside — "patterns" front-loads the source-cohort caveat, and "benchmark/comparative" framing is reserved for the journal extension to keep the two titles cleanly distinct.

### What is IN the conference paper
1. **10-cell pipeline subset:** 3 imputers (MissForest, KNN, MICE) × 2 algos (K-Means, Agglomerative) × no-context strategy (= 6 imputed cells) + 2 baselines (df_encoded_20, df_encoded_40) × the same 2 algos (= 4 baseline cells). Framed as "a focused subset of our 32-pipeline benchmark." **NOTE: this is 10 cells, not 8** — the earlier "8-cell" wording was wrong; there are 4 baseline cells (2 datasets × 2 algos), not 2. All exact values are in §3.5 below.
2. **LLM-assisted categorical schema rationalization** as the AI methodology contribution. Source: `llm_preprocessing_methodology.md` at project root. Use the 230-word block in §9 of that file verbatim or close to it.
3. **Headline imputation lift (IN-SCOPE numbers, recomputed for the 2 algorithms shown — use these, NOT the thesis 23.27/10.90 which averages over 4 algorithms):** all-imputed mean **19.71** vs baseline mean **8.09** (2.4×); MissForest alone **25.30** vs **8.09** (3.1×). See §3.5.
4. **Interaction finding ("the combination matters"):** imputation helps, but the imputer×algorithm pairing decides the gain — with K-Means all three imputers are strong (avg 23.98); with Agglomerative only MissForest survives (27.30) while MICE/KNN collapse below a baseline. MissForest is the only imputer robust across both algorithms. This is the conference's distinctive framing AND the forward-pointer that motivates the 32-pipeline journal grid.
5. **Two-cluster solution** with summary-statistic interpretation.
6. **Cardinality reduction table** (raw 918 → consolidated 156, 83% reduction).
7. **Brief mention of balance-penalty score component** (one sentence in methods describing the 6-component composite).
8. **Single-sentence caveats** in Limitations: source-cohort confound + score-margin warning.
9. **SDG-3 framing** in abstract, intro, conclusion.

### What is OUT of the conference paper (hold for journal extension)
1. DBSCAN and Spectral clustering algorithms.
2. Context-aware predictor strategy.
3. Full 32-pipeline ranking.
4. **Full source-cohort forensic analysis** — this is the journal's headline novelty; do not spend it here.
5. **Balance-penalty design rationale** — only mentioned in passing here; the journal version makes it a co-contribution.
6. Per-component composite heatmap.
7. Temperature-unit caveat depth.
8. Full limitations matrix.
9. LLM-assisted cluster interpretation (treated as Grammarly-class writing aid; not disclosed as methodology — disclosing it would weaken the paper).
10. Colab AI code-completion mention (standard tooling, not a contribution).

### Why this split is defensible (≥30% novel material rule)
The journal extension adds: 2 algos + 1 strategy + 24 cells + source-cohort forensic + balance-penalty design + per-component breakdown + extended limitations. Well past the conference-to-journal differentiation threshold.

---

## 3.5 Verified numbers, final 10-cell selection & framing (LOCKED 2026-06-26, checked against `latex/main.pdf` + notebooks)

Everything in this section was read directly out of `latex/chapters/ch4_results.tex` (Tables 4.1, 4.3, the §4.2 group analysis, §4.6 profiling) and `latex/chapters/appendix.tex` (`tbl:full_per_case_results_across_a`, the raw per-metric table for all 32 cases). **These supersede any TBD/estimated numbers elsewhere in this plan.**

### 3.5.1 The 10 conference cells — full metrics (drop straight into Table 1)

Sorted by composite. Balance/silhouette/composite are exact from the annex; `k` from the ranking table's optimal params.

| Pipeline | Imputer | Algorithm | Balance | Silhouette | Composite (/32) | k |
|---|---|---|---|---|---|---|
| agg_rf_no_context | MissForest | Agglomerative | 0.685 | 0.756 | **27.30** | 2 |
| kmeans_mice_no_context | MICE | K-Means | 0.674 | 0.792 | **26.60** | 2 |
| kmeans_rf_no_context | MissForest | K-Means | 0.685 | 0.755 | **23.30** | 2 |
| kmeans_knn_no_context | KNN | K-Means | 0.542 | 0.785 | **22.05** | 2 |
| agg_encoded_40 | none (baseline) | Agglomerative | 0.355 | 0.157 | 10.35 | 2 |
| agg_mice_no_context | MICE | Agglomerative | 0.356 | −0.078 | 9.65 | 2 |
| agg_knn_no_context | KNN | Agglomerative | 0.361 | −0.020 | 9.35 | 2 |
| kmeans_encoded_40 | none (baseline) | K-Means | 0.315 | −0.072 | 9.15 | 8 |
| kmeans_encoded_20 | none (baseline) | K-Means | 0.289 | −0.213 | 7.20 | 10 |
| agg_encoded_20 | none (baseline) | Agglomerative | 0.258 | −0.317 | 5.65 | 6 |

### 3.5.2 Recomputed in-scope aggregate numbers (USE THESE in abstract/results)

The thesis "23.27 vs 10.90" averages over **four** algorithms (K-Means, Agglomerative, DBSCAN, Spectral). The conference shows only **two**, so we must report the 2-algorithm means to stay internally consistent. All derived by hand from the table above (arithmetic only, no code):

- **By imputer (no-context, K-Means + Agglomerative):** MissForest **25.30** · MICE **18.13** · KNN **15.70** · Baselines (4 cells) **8.09** · all-imputed (6 cells) **19.71**.
- **Headline lift:** all-imputed 19.71 vs baseline 8.09 = **2.4×**; MissForest 25.30 vs 8.09 = **3.1×**. "More than doubles" holds honestly on exactly the shown cells.
- **By algorithm (imputed only, no-context) — the interaction story:** K-Means **23.98** (all three imputers 22–27, tight) vs Agglomerative **15.43** (MissForest 27.30, but MICE 9.65 / KNN 9.35 collapse).

### 3.5.3 Two honesty flags (FEATURE them, don't hide them)

1. **Two imputed cells lose to a baseline:** `agg_mice` (9.65) and `agg_knn` (9.35) score below `agg_encoded_40` (10.35), with **negative silhouettes** (−0.078, −0.020) = genuinely failed clusterings. This is the proof that "imputation always helps" is false → motivates the "combination matters" framing instead of a blanket claim.
2. **Baselines fragment under K-Means:** no imputation forced k=8 and k=10 (and agg_encoded_20 → k=6); every imputed pipeline gave a clean k=2. Free, vivid "imputation stabilizes structure" point.

### 3.5.4 The data-prep framing — recovery waterfall + two-arm experiment (REPLACES the earlier L0/L1/L2 three-arm idea)

There is **no "nothing-filled" clustering arm** — confirmed in notebook 3: the baselines start from `df_weather` (L1 deterministic filling already applied), then drop columns above a missingness threshold AND drop incomplete rows. So:
- **Part A — Recovery waterfall (descriptive, not a result):** raw missingness (L0) → deterministic recovery (L1: Geopy geocoding 53%→6.5%; Meteostat weather API, Table 3.2; in **% terms**, no cell counts exist) → residual severe missingness. Applies to every pipeline equally; motivates the experiment.
- **Part B — The experiment is a controlled TWO-arm comparison on the same L1 base**, differing in ONE decision — what to do with still-incomplete columns: **DROP them** (baseline: `df_encoded_20` = 853 rows × 22 cols; `df_encoded_40` = 403 rows × 30 cols) vs **IMPUTE them** (MissForest/MICE/KNN, retaining ~1,617 rows × 29–37 cols). Holding L1 constant means the downstream difference is cleanly attributable to impute-vs-drop. Frame this control as a strength. The baselines lose both columns AND rows — quantifiable feature/row loss, numbers above.

### 3.5.5 The "no ground truth" defense (organic missingness) — 4 parts, ALL no-code

Asked at the thesis defense; bake the answer into Methodology/Limitations:
1. **Reframe:** we validate imputation by its **downstream** effect (cluster validity), not per-cell reconstruction — the accepted approach when missingness is organic.
2. **Much of the filling isn't guessed:** geocoding + weather API are verifiable true values, not statistical estimates (the L1 layer).
3. **Convergence:** three independent imputers agree structure exists (all strong with K-Means), an internal consistency signal.
4. **Name the real reason it's hard — MNAR:** newspaper missingness is likely Missing Not At Random; stating this is a strength and justifies keeping all cluster claims exploratory.
- **NOT available (disclose as limitation, do not fabricate):** MissForest OOB/NRMSE error (never instrumented); cross-imputer ARI agreement (never computed); masking experiment (excluded by choice — no new code).

### 3.5.6 "Why only 2 algorithms?" — prepared answer

"We present the two most widely used clustering families — centroid-based (K-Means) and hierarchical (Agglomerative); density- and graph-based methods (DBSCAN, Spectral) are in the extended factorial (in preparation)." Legitimate scoping. Internal note: keep the conference claim scoped to "these two algorithms" + "combination matters" — do NOT claim "imputation always wins everywhere," because the full grid has a no-imputation Spectral baseline (spc_encoded_40 = 22.80) beating several imputed pipelines. Scoped claim = fully consistent with the journal, no exposure.

---

## 4. Section-by-section content plan (6-page IEEE 2-column target)

Use the example template at `/home/mhmd1/Music/capstone/example-i-coste-template/main.tex` as the LaTeX skeleton. Same preamble, same author block format, same section structure.

### 4.1 Title and Author Block

- **Title:** as above.
- **Authors (same five as the thesis declaration page, BUBT CSE):**
  - Mohammed Akash (ID 21221203019)
  - Sajedul Islam (ID 21221203022)
  - Md Arifuzzan (ID 21221203034)
  - Komol Chandra Devnath (ID 21221203028)
  - Anisul Haque Bhuiyan (ID 20211203010)
  - Supervisor (per thesis approval page — confirm name and add as senior author)
- **Affiliation:** Department of Computer Science and Engineering, Bangladesh University of Business and Technology, Dhaka, Bangladesh.
- **Emails:** confirm with each author before submission. The thesis declaration page does not list emails.
- **Conference header:** update the `\lhead` block in the template to "12th IEEE International Conference on Sustainable Technology and Engineering, 01–03 November 2026, Bangladesh University of Business and Technology."
- **Copyright footer:** insert the 2026 IEEE copyright string once registration finalises the assigned DOI block.

### 4.2 Abstract — ~200 words

Structure: (1) problem in 1 sentence; (2) dataset in 1 sentence; (3) two-stage AI pipeline in 1 sentence; (4) experimental scope in 1 sentence; (5) headline result in 1 sentence; (6) implication for SDG-3 surveillance in 1 sentence.

Draft seed sentences:
- *"In countries without a centralised national suicide-surveillance registry, newspaper reports are the only public source of case-level data, yet they exhibit 50–90% missingness on key features."*
- *"We curate 1,617 newspaper-reported suicide cases from Bangladesh (2017–2025) — the largest publicly assembled record of its kind for a country lacking centralised surveillance."*
- *"We propose a two-stage AI pipeline combining LLM-assisted categorical schema rationalization with a benchmark over three imputation methods and two clustering algorithms under a six-component composite score."*
- *"On a focused 10-cell subset (3 imputers × 2 algorithms, no-context, plus baselines), MissForest imputation achieves a mean composite of 25.30 versus 8.09 for the no-imputation baseline — but the gain is conditional on the imputer–algorithm pairing."* (USE the §3.5.2 in-scope numbers, NOT the thesis 4-algo 23.27/10.90.)
- *"Results suggest that careful imputation methodology is a feasible foundation for SDG-3 (good health and well-being) surveillance in low-resource, news-derived public-health datasets."*

Keywords (6): *suicide surveillance; SDG-3; missing data imputation; MissForest; clustering; LMIC public health.*

### 4.3 Introduction — ~0.75 page

Structure (4 short paragraphs):
1. **Problem framing.** SDG-3 includes target 3.4 (reducing premature mortality including suicide). Many LMICs lack centralised suicide registries. Newspaper reports are the only public source. Bangladesh as concrete case.
2. **Why standard ML fails on this data.** 50–90% missingness on key features. Row-dropping eliminates 96.5% of records. Naive single-method imputation introduces unmeasured bias.
3. **Our approach.** Two-stage AI pipeline: LLM-assisted preprocessing + imputation-clustering benchmark with a balance-aware composite score. Designed to detect source-cohort artefacts that simpler workflows conceal.
4. **Contributions** (use `\begin{itemize}` like the template):
   - A reproducible LLM-assisted categorical rationalization workflow that reduces 918 raw unique values to 156 canonical categories across 11 fields.
   - A focused 8-cell imputation–clustering benchmark on 1,617 Bangladeshi newspaper-reported suicide cases.
   - Quantitative evidence that MissForest-based imputation more than doubles the composite cluster-validity score relative to the no-imputation baseline.
   - A two-cluster solution interpretable as case-cohort structure, with caveats supporting honest exploratory reporting in this data regime.

Research question (rendered as italics like the template):
> *"How well can a transparent imputation–clustering pipeline surface stable, interpretable structure in severely incomplete newspaper-reported suicide data, and how does it compare to a no-imputation baseline?"*

Close with a 1-sentence roadmap of the remaining sections, like the template does.

### 4.4 Related Works — ~0.75 page

Three short paragraphs + one comparison table (use `\begin{table*}` to span both columns, exactly like the template's `tab:related-comparison`).

- **Paragraph 1:** Prior work on newspaper-based suicide surveillance (LMIC focus). Cite WHO Mental Health Atlas, Vijayakumar's work, India-based newspaper studies.
- **Paragraph 2:** Imputation benchmarks on public-health data — MICE (van Buuren), MissForest (Stekhoven & Bühlmann), KNN imputation.
- **Paragraph 3:** Cluster-validity benchmarks for unsupervised structure discovery in mixed-type data.
- **Comparison table** with columns: Approach | Dataset Type | Imputation Coverage | Clustering Coverage | Reproducibility | Cohort Confound Awareness. Position our work in the bottom row with all-yes.

Source thesis chapter for content: Ch 2 (literature review). Compress the 5-gap analysis into the comparison table; do NOT carry over the full gap-by-gap discussion.

### 4.5 Methodology — ~1.5 pages

Five short subsections, each 1 short paragraph + at most one figure:

**4.5.1 Dataset**
- 1,617 cases, 34 analytical columns, 2017–2025 collection.
- Missingness summary: only 3.5% of rows are complete across all 37 retained columns; 52.8% complete at the easiest threshold. Report this number; do not include the full 4-band missingness table here.

**4.5.2 LLM-Assisted Categorical Schema Rationalization** (this is your AI methodology hook)
- Pull the 230-word block from `llm_preprocessing_methodology.md` §9.
- Include the cardinality reduction table — trim to the 6 most informative rows if space is tight (hometown, profession, reason, method, marital_status, religion).

**4.5.3 Imputation Methods**
- One sentence each on MICE (per-variable BayesianRidge, single-pass), KNN (k=5), MissForest (n_estimators=100, Stekhoven Δ-stop convergence).
- One sentence on the "no-context predictor strategy" (which columns each imputer is allowed to use as predictors).

**4.5.4 Clustering Algorithms**
- One sentence each on K-Means (n_clusters search, n_init=10) and Agglomerative (Ward linkage, n_clusters search).
- Briefly note that DBSCAN and Spectral are evaluated in the extended version (cite "in preparation").

**4.5.5 Composite Cluster Validity Score**
- Six-component composite: Silhouette, Calinski–Harabasz, Davies–Bouldin, Dunn, Xie–Beni, and a balance-penalty term.
- One sentence on the balance penalty: *"a penalty designed to discourage near-degenerate cluster assignments where one cluster contains nearly all records, given weight 0.35 in the composite."*
- Do NOT defend the weight choice in detail (that's for the journal).

Figures candidate (pick ONE for this section): the unified pipeline overview from thesis Ch 3 (`overall.png`) or a simpler bespoke flowchart created for this paper.

### 4.6 Results & Analysis — ~1.5 pages

Structure: one paragraph framing → one table → one figure → one paragraph interpretation.

**Paragraph 1 — framing.** "We report results on the 8-cell focused subset. The full 32-pipeline ranking is presented in the extended version (in preparation)."

**Table 1 — 10-cell ranking.** Columns: Pipeline | Imputation | Algorithm | Balance | Silhouette | Composite | k. Sort descending by composite. **All values are filled and verified in §3.5.1 — copy that table directly.** (Cluster-size split is only known for the winner, 759/858; report `k` for the rest, sizes only for the winner in §4.6.)

**Figure 1 — PCA scatter of the best pipeline.** Lift from thesis `image14_a.png` or render a fresh single-panel PCA for `agg_rf_no_context` showing the two-cluster structure.

**Paragraph 2 — interpretation.** Four short claims, each with one number (all from §3.5.2/3.5.3):
- Imputation more than doubles the composite vs baseline on the shown cells (all-imputed 19.71 vs 8.09; MissForest 25.30 vs 8.09).
- **But the combination matters:** with K-Means all three imputers are strong (avg 23.98); with Agglomerative only MissForest survives (27.30) — MICE (9.65) and KNN (9.35) fall *below* a baseline (agg_encoded_40 = 10.35) with negative silhouettes. MissForest is the only imputer robust across both algorithms.
- Imputation stabilizes structure: baselines fragment under K-Means (k=8, k=10) while every imputed pipeline gives a clean k=2.
- Best pipeline (agg_rf_no_context) yields a balanced two-cluster split (759 vs 858).
- Forward-pointer sentence: the full imputer×algorithm interaction surface (4 algos × 3 imputers × 2 strategies = 32 pipelines) is characterized in the extended version (in preparation).

Honest mini-table or sentence on cluster summary statistics: report the *top 3 distinguishing features* between the two clusters (e.g., gender ratio, urban/rural split, dominant reason category). Pull from thesis Ch 4 Table 4.3 — DO NOT include the full mean/median table; pick the 3 most striking contrasts.

### 4.7 Conclusion — ~0.3 page

One paragraph, ~100 words. Restate (1) the problem, (2) the contribution, (3) the headline result, (4) implications for SDG-3 surveillance.

Example structure:
> *"This study presents a two-stage AI pipeline for analysing incomplete newspaper-reported suicide data in low-resource settings. On 1,617 Bangladeshi cases from 2017–2025, LLM-assisted categorical rationalization reduced raw cardinality by 83%, enabling a downstream imputation–clustering benchmark in which MissForest-based imputation more than doubled the composite cluster-validity score over the no-imputation baseline. The framework supports honest, exploratory subgroup analysis in a data regime where standard machine-learning workflows fail outright."*

### 4.8 Limitations & Future Work — ~0.5 page

One paragraph for each:

**Limitations.** Three short sentences:
1. *Source-cohort caveat:* "The two-cluster boundary partly aligns with the dataset's collection-source split (a 2020 Kaggle subset versus 2017–19 and 2021–25 manually-collected reports); resulting cluster structure should be read as exploratory subgroup signal rather than discovery of distinct epidemiological categories."
2. *Score margin caveat:* "The top-ranked pipelines lie within 1.7 composite points of each other; we therefore do not claim statistical separability between leading methods."
3. *Newspaper sourcing caveat:* "Newspaper reports systematically under-report suicide and skew toward urban, working-age cases; our framework's conclusions inherit these representational biases."

**Future Work.** One paragraph noting the extended journal version covers the full 32-pipeline factorial, the complete source-cohort forensic analysis, and the balance-penalty design rationale; and that follow-on work will validate the framework on additional LMIC public-health datasets.

### 4.9 References

Use `\bibliography{ref}` with a BibTeX file. Required citation seeds (verify and complete):

- MICE: van Buuren & Groothuis-Oudshoorn, "mice: Multivariate Imputation by Chained Equations in R", *Journal of Statistical Software*, 2011.
- MissForest: Stekhoven & Bühlmann, "MissForest—non-parametric missing value imputation for mixed-type data", *Bioinformatics*, 2012.
- KNN imputation: Troyanskaya et al., "Missing value estimation methods for DNA microarrays", *Bioinformatics*, 2001.
- Silhouette: Rousseeuw, "Silhouettes: A graphical aid to the interpretation and validation of cluster analysis", *J. Computational and Applied Mathematics*, 1987.
- Calinski–Harabasz: Calinski & Harabasz, 1974.
- Davies–Bouldin: Davies & Bouldin, 1979.
- Dunn index: Dunn, 1974.
- Xie–Beni: Xie & Beni, 1991.
- Bangladesh suicide surveillance gap: Arafat et al. — "Suicide in Bangladesh" papers (any 2019–2023 review).
- Newspaper-based suicide surveillance methodology: Vijayakumar et al. or an Indian study using newspaper data for suicide patterns.
- WHO SDG-3 and mental-health surveillance: WHO Mental Health Atlas 2020 or 2024.
- Suicide reporting bias in news: Niederkrotenthaler or Pirkis review.
- LLM-assisted data curation: any 2023–2024 LLM-for-data-engineering paper (Narayan et al., or a Snorkel-style paper).

Use `IEEEtran` bibstyle. Convert thesis bibliography entries where reusable; trim aggressively — conference papers typically have 15–25 references.

---

## 5. Reusable assets from the thesis

### Figures that can be lifted directly (located in `latex/assets/images/`)
- `image14_a.png` — top-16 PCA scatter grid (use a single-panel crop for our chosen pipeline)
- `overall.png` — complete pipeline overview (optional for §4.5)
- `image7.png` — composite ranking bar chart (subset to 8 cells)

### Tables to derive from the thesis
- Cardinality reduction table → `llm_preprocessing_methodology.md` §5
- 8-cell results table → thesis Ch 4 (filter the 32-row ranking to the 8 cells we are reporting)
- Cluster summary contrast → thesis Ch 4 Table 4.3 (extract 3 most contrasting features)

### Content blocks to lift with minor edits
- Methodology subsection block: `llm_preprocessing_methodology.md` §9 (the 230-word LLM-preprocessing paragraph)
- Honest caveats: thesis Ch 6 §6.4 (the `lim:source_cohort` and the score-margin sentence)
- Composite score description: thesis Ch 3 (compress to ~50 words)

### Data files to consult while writing
- `notebooks/0_preprocessing.ipynb` — for the cardinality counts and the mapping dictionaries
- `notebooks/11_comparing-clustering.ipynb` — for the full ranking and metric values
- `datasets/` — for cluster size numbers and per-cluster summary statistics

---

## 6. Pre-writing checklist (do before opening the LaTeX file)

- [ ] Confirm supervisor name and authorship order for the conference paper (5 students + supervisor).
- [ ] Collect author emails (declaration page lists names + IDs only).
- [ ] Decide whether the supervisor is corresponding author (typical at this career stage).
- [ ] Confirm i-COSTE submission deadline (check call-for-papers; estimate is August–September 2026 based on November conference date).
- [ ] Pull the exact composite values for the 6 non-baseline cells from `notebooks/11_comparing-clustering.ipynb` so Table 1 is filled in correctly. (Currently only `agg_rf_no_context = 27.30` and the baseline mean `~10.90` are verified.)
- [ ] Pull the exact two-cluster size split for each of the 8 cells (the winner is 759/858).
- [ ] Re-export `image14_a.png` as a single-panel PCA for the chosen pipeline if you want a cleaner figure than the 16-panel grid.
- [ ] Decide on the bibliography seed list (Section 4.9) — confirm at least 15 references are findable in your existing thesis bibliography.

---

## 7. Drafting workflow (recommended)

Work in this order — each step is independent and unblocking:

1. **Set up scaffolding (15 min).** Copy `/home/mhmd1/Music/capstone/example-i-coste-template/` to a new directory (suggested: `/home/mhmd1/Music/capstone/conference-paper/`). Rename, update the title, update the author block, update the `\lhead` conference header, delete the example sections.
2. **Write Methodology subsection 4.5.2 first (30 min).** Drop in the 230-word LLM-preprocessing block + cardinality table. This is the most "done" part of the paper.
3. **Write Methodology subsections 4.5.1, 4.5.3, 4.5.4, 4.5.5 (60 min).** Short, factual, lift from thesis Ch 3.
4. **Write Results (90 min).** Look up the 8-cell numbers, build Table 1, prepare Figure 1, write 2 paragraphs.
5. **Write Limitations & Future Work (20 min).** Three caveat sentences + one future-work paragraph.
6. **Write Conclusion (15 min).** One paragraph.
7. **Write Related Works (60 min).** Three paragraphs + comparison table — slowest section because it needs care on citation choices.
8. **Write Introduction (45 min).** Hardest writing: needs to hook + frame + preview + commit.
9. **Write Abstract (30 min).** Last, when the rest is final.
10. **Bibliography pass (45 min).** Build `ref.bib`, run `bibtex`, fix missing entries.
11. **Format pass (30 min).** Check 6-page limit, balance columns with `\balance`, fix overflow tables.

Total drafting estimate: ~7.5 focused hours, spread across 4–6 sessions.

---

## 8. What to do if anything goes wrong

- **Paper exceeds 6 pages:** drop the dataset subsection figure first, then trim Related Works to two paragraphs, then trim the cardinality table to 4 rows, then collapse Conclusion + Limitations into one section.
- **Reviewer asks "why are DBSCAN and Spectral missing?":** answer factually — extended version with full 4-algorithm coverage is in preparation; the conference paper presents a focused subset.
- **Reviewer asks "what is the balance-penalty weight justification?":** answer briefly — empirical sensitivity analysis available in the extended version; the conference paper uses the value validated in our larger benchmark.
- **Reviewer challenges the source-cohort caveat as undermining the result:** point to the honesty as a methodological strength — frameworks that surface their own confounds are more trustworthy than those that don't.

---

## 9. Reference documents (read these before writing)

In recommended reading order:

1. **`MEMORY.md`** (auto-loaded into Claude sessions) — captures the project state, the publication plan, and the locked conference scope.
2. **`llm_preprocessing_methodology.md`** (project root) — full LLM-preprocessing reference. §5 has the cardinality table, §6 has the override examples, §9 has the drop-in 230-word methodology block.
3. **`chat.md`** (project root) — verbatim ChatGPT transcripts for the preprocessing prompts. Useful if the conference paper needs to quote a prompt directly.
4. **`latex/main.pdf`** — the full thesis. Reference for any factual claim or number.
5. **`latex/chapters/ch3_methodology.tex`** — for imputation/clustering descriptions.
6. **`latex/chapters/ch4_results.tex`** — for the 32-pipeline ranking and the §4.2.1 "Does Imputation Help at All?" content.
7. **`latex/chapters/ch6_conclusion.tex`** — for the source-cohort and score-margin caveat sentences.
8. **`notebooks/0_preprocessing.ipynb`** — for the mapping dictionaries.
9. **`notebooks/11_comparing-clustering.ipynb`** — for the 8-cell composite values and cluster sizes.
10. **`example-i-coste-template/main.tex`** — the IEEE conference template to copy and adapt.

---

## 10. What is intentionally NOT in this plan

- A complete LaTeX skeleton. Build it by copying the example template (step 1 of the drafting workflow above) — re-writing the preamble here would just duplicate `example-i-coste-template/main.tex`.
- Word-for-word section drafts. The plan deliberately stops at structure + content references so the actual writing benefits from your voice and the specific numbers you'll look up in step 4 of the drafting workflow.
- A schedule. Submission deadline is unknown (verify on i-COSTE site); back off from the deadline by 7.5 hours of drafting + 1 round of co-author review + 1 week of buffer for citation fixes.
- The journal extension plan. See MEMORY.md "Publication Plan" section — the journal version is a separate effort scheduled for Dec 2026 – Mar 2027.

---

## 11. One sentence to remember

The conference paper is the *seed* of the journal paper, not a separate work. Write it tight, leave room for the journal extension to differentiate cleanly, and resist the urge to over-claim now what you should keep for later.

---

## 12. Phased writing workflow (LOCKED 2026-06-26 — this is how we actually draft)

**Working directory:** all paper files live in a NEW directory `conference-latex/` (copied from `example-i-coste-template/`). Do not edit the template in place. Keep it clean: extract thesis assets (figures, tables, text blocks) into `conference-latex/` **phase by phase, only when that phase needs them** — never bulk-copy.

**Per-phase protocol (MANDATORY for every phase):**
1. **CHECKOUT FIRST** — before writing anything, re-read what was written in all previous phases (the current state of `conference-latex/main.tex` + any extracted assets) so the new phase stays consistent in voice, notation, terminology, and numbers.
2. **INTERVIEW** — ask the user the phase's open questions (listed below). Wait for answers. Do not start drafting until the user has responded.
3. **DRAFT** — write only that phase's content. Build/compile-check if LaTeX changed.
4. **PAUSE** — hand back for review before the next phase. User starts each phase explicitly.

**Source of truth for all numbers:** §3.5 of this plan (verified against the report). Never re-derive or use the thesis 4-algo numbers.

### Phase list

**Phase 0 — Scaffold.** Create `conference-latex/` from the template; set the locked title; author block; update the `\lhead` conference header to "12th IEEE International Conference on Sustainable Technology and Engineering, 01–03 November 2026, Bangladesh University of Business and Technology"; strip example sections to empty section stubs; confirm it compiles.
- *Interview:* (a) final author order + emails; (b) supervisor name and is the supervisor corresponding author?; (c) keep IEEEtran defaults (yes unless told otherwise).

**Phase 1 — Methodology** (write first; it's the most "done"). Subsections: Dataset; **LLM-assisted categorical rationalization** (230-word block from `llm_preprocessing_methodology.md` §9 + cardinality table §3.5/§5); Imputation methods; Clustering algorithms; Composite score (incl. one-sentence balance penalty); the **recovery-waterfall + two-arm drop-vs-impute** framing (§3.5.4).
- *Extract:* cardinality table; weather Table 3.2; pipeline figure (`overall.png` or bespoke).
- *Interview:* (a) use `overall.png` as-is or want a simpler bespoke pipeline flowchart?; (b) how much imputation algorithm detail (hyperparameters yes/no?).

**Phase 2 — Results & Analysis.** Table 1 (copy §3.5.1); in-scope numbers (§3.5.2); interaction story + 2 honesty flags (§3.5.3); top-pipeline two-cluster profiling (3 most striking contrasts from ch4 Tables 4.2/4.3 — e.g. gender 54.8%F vs 50.8%M, workplace semi-urban vs rural, reason family-issue vs mental); one PCA/figure.
- *Extract:* `image14_a.png` (PCA grid — may crop) or geographic cluster maps; optionally `image7.png` ranking bars subset.
- *Interview:* (a) which results figure — PCA grid crop, ranking bar, or a clean bespoke 2-cluster scatter?; (b) include the k=8/10 fragmentation point as a sentence or a small visual?

**Phase 3 — Limitations & Future Work + Conclusion.** Three caveat sentences (source-cohort §3.5; score-margin top-4 within 1.7; newspaper sourcing bias) + "no ground truth → downstream validation + MNAR" defense (§3.5.5) + future-work paragraph (journal extension) + ~100-word conclusion.
- *Extract:* none.
- *Interview:* confirm the MNAR sentence and the "in preparation" journal phrasing are acceptable.

**Phase 4 — Related Works.** 3 paragraphs (newspaper suicide surveillance in LMICs; imputation benchmarks; cluster-validity) + one `table*` comparison positioning our work bottom row. Slowest — citation care.
- *Interview:* confirm citation seeds from §4.9; any must-cite papers from the supervisor.

**Phase 5 — Introduction.** Problem framing (SDG-3 / indicator 3.4.2) → why standard ML fails (missingness, row/column loss) → our approach → contributions `itemize` → research question → roadmap sentence.
- *Interview:* confirm the 4 contribution bullets phrasing.

**Phase 6 — Abstract + Keywords.** ~200 words, 6-sentence structure; 6 keywords. Written last.
- *Interview:* none (derive from finished body); confirm keyword list.

**Phase 7 — Bibliography + format/length pass.** Build `ref.bib`; run bibtex; balance columns with `\balance`; enforce 6-page limit (fallback trims in §8); fix overflow tables.
- *Interview:* if over 6 pages, confirm which trims to apply.

End of plan.
