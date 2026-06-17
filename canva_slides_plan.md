# Capstone Defense — Canva Slide Plan

**Title:** Comparing Imputation and Clustering Pipelines on Incomplete Newspaper-Reported Suicide Data from Bangladesh
**Team:** 5 members · BUBT CSE
**Total slides:** 55
**Target duration:** 18–22 minutes

This file is content-only. Style, font, colour, and layout choices are left for you to apply in Canva later.

Each slide includes:
- **Title** — what goes at the top of the slide
- **Body** — exact text content
- **Figure / Image** — file from `/images/` or chart to draw
- **Numbers / Facts** — the precise data points (so nothing gets fabricated)
- **Source** — where the data comes from
- **Note** — short layout hint

---

# SECTION 1 — OPENING

## Slide 1 — Title

**Title:** Comparing Imputation and Clustering Pipelines on Incomplete Newspaper-Reported Suicide Data from Bangladesh

**Body:**
- Subtitle: *A 32-pipeline factorial benchmark with a balance-aware composite score*
- Footer: BUBT · Department of Computer Science and Engineering · Capstone Defense · June 2026

**Image:** BUBT logo (top centre) — `images/bubt-logo.png`

**Note:** Cover slide — keep clean. Logo small at top, then large title, subtitle below in muted weight, footer at bottom in small caps.

---

## Slide 2 — The Team

**Title:** The Team

**Body:** Five members in one row, each with photo, name, and role.

| Member | Role |
|---|---|
| [Name 1] | Project Lead / Pipeline Architecture |
| [Name 2] | Data Collection and Curation |
| [Name 3] | Imputation and Clustering Pipeline |
| [Name 4] | Evaluation Framework and Composite Scoring |
| [Name 5] | Documentation and Visualisation |

**Image:** 5 circular team-member photos (you'll upload these)

**Note:** Single row across the slide. Each member: photo (circular, ~150px) + name + 1-line role. Equal spacing.

---

## Slide 3 — Outline

**Title:** Outline

**Body:**
1. Background and the data problem
2. Literature review and the research gap
3. Research question and objectives
4. Methodology — the 32-pipeline benchmark
5. Results, cluster profiles, feature comparisons
6. Honest findings, limitations, what's next

**Note:** Numbered list, big numbers in accent colour next to each section name.

---

# SECTION 2 — BACKGROUND

## Slide 4 — Section divider

**Title:** SECTION 01 — Background

**Body:** Just the section number and section title. Visual break.

**Note:** Full-screen section divider. Large section title.

---

## Slide 5 — Suicide in Bangladesh

**Title:** Suicide in Bangladesh

**Body:** A public-health crisis without a national surveillance system.

**Note:** Statement slide. Just the heading and one sub-line.

---

## Slide 6 — 40 deaths per day

**Title:** (no title — just the number)

**Body:**
- Massive number: **40**
- Caption: suicides per day in Bangladesh
- Source: Bangladesh Police (AIG Ashraful Islam), reported by Prothom Alo, 2025

**Numbers:** 40 (per day)

**Source:** Bangladesh Police nationwide data, reported in Prothom Alo, January 2025

**Note:** Big-number slide. 40 in very large type. Small source line beneath caption.

---

## Slide 7 — 73,597 deaths over five years

**Title:** (no title — just the number)

**Body:**
- Massive number: **73,597**
- Sub-line: Bangladesh Police records, 2020 – 2024
- Sub-line: Average — **14,719 per year**
- Source: Bangladesh Police nationwide data, 2025

**Numbers:**
- 73,597 total deaths
- 14,719/year average
- Period: 2020–2024

**Note:** Big-number slide. Same template as Slide 6.

---

## Slide 8 — The true figure is higher

**Title:** The true figure is higher.

**Body:**
Three reasons stacked vertically:
- Stigma
- Cultural barriers
- No surveillance system

**Source:** WHO; Arafat et al., 2025 (Health Science Reports)

**Note:** Three single words on separate lines. Each in equal weight.

---

# SECTION 3 — THE DATA PROBLEM

## Slide 9 — Section divider

**Title:** SECTION 02 — The Data Problem

**Note:** Section divider.

---

## Slide 10 — Newspapers are the only source

**Title:** (no title)

**Body:** Newspaper reports are the only structured data we have.

**Note:** One declarative sentence centered. The single most important framing in the whole talk.

---

## Slide 11 — 50–90% missingness

**Title:** (no title — just the number)

**Body:**
- Big number range: **50–90%**
- Caption: of critical fields are missing across the dataset
- Source: measured directly on the curated dataset (this study)

**Numbers:** 50% to 90% (range across fields)

**Note:** Big-number slide. Show a horizontal bar with the 50–90% range highlighted to give visual scale.

---

## Slide 12 — What is systematically missing

**Title:** What is systematically missing

**Body:** Bulleted list:
- Age, occupation, marital status
- Mental-health history
- Socio-economic indicators
- Latitude and longitude
- Weather and environmental context

**Note:** Left-aligned list. Plain bullets.

---

## Slide 13 — Standard machine learning fails

**Title:** Standard machine learning cannot run on data this broken.

**Body:**
- Complete-case analysis discards most of the dataset.
- Naïve mean substitution introduces distributional bias.

**Source:** Garmdareh/Shadbahr et al., 2023 (Communications Medicine); Jäger et al., 2021 (Frontiers in Big Data)

**Note:** Two-line declarative statement at top, two consequence lines beneath.

---

# SECTION 4 — LITERATURE REVIEW

## Slide 14 — Section divider

**Title:** SECTION 03 — Literature Review

**Note:** Section divider.

---

## Slide 15 — Bangladeshi newspaper suicide research

**Title:** Bangladeshi newspaper suicide research

**Body:** Two paper cards:

**Card 1 — Arafat et al. (2018)**
- Journal: Asian Journal of Psychiatry
- Title: Demography and risk factors of suicidal behavior in Bangladesh — retrospective online news content analysis
- Finding: Manual grouping only · no algorithmic clustering applied

**Card 2 — Arafat et al. (2025)**
- Journal: Health Science Reports
- Title: Prevalence of suicidal behavior in Bangladesh — systematic review and meta-analysis
- Finding: Aggregate epidemiology · no case-level subgroup analysis

**Note:** Two card-style boxes vertically stacked. Each card: author + year on top line, title in muted, key finding in stronger emphasis.

---

## Slide 16 — Global algorithmic clustering on suicide data

**Title:** Global algorithmic clustering on suicide data

**Body:** Three paper cards:

**Card 1 — Wong et al. (2022)**
- Journal: BMC Public Health
- Title: *From the hidden to the obvious — classification of primary and secondary school student suicides using cluster analysis*
- Context: Hong Kong primary and secondary school student suicides
- Method: cluster analysis (K-Means)
- Gap: Single algorithm · no imputation comparison

**Card 2 — Xiao et al. (2025)**
- Journal: Nature Mental Health
- Title: *Machine learning to investigate policy-relevant social determinants of health and suicide rates in the United States*
- Context: United States, community-level suicide rates
- Method: ML on social determinants of health
- Gap: Administrative data · not severely incomplete

**Card 3 — Sanz-Gomez et al. (2025)**
- Journal: European Psychiatry
- Title: *Delineating impulsivity-based pathways to suicide deaths — a cluster analysis*
- Context: Spain, autopsy data
- Method: K-Means + Agglomerative clustering
- Gap: No LMIC newspaper context

**Note:** Three cards. Same template as Slide 15.

---

## Slide 17 — The research gap

**Title:** Five gaps in prior work

**Body:**
1. No algorithmic clustering on Bangladeshi newspaper suicide data
2. No multi-method imputation benchmark in this domain
3. Prior studies use a single clustering algorithm — we use four
4. Standard validity indices fail on imbalanced social data
5. No prior work compares predictor-selection strategies during imputation

**Note:** Numbered list, big numbers in accent colour.

---

# SECTION 5 — RESEARCH FRAMING

## Slide 18 — Section divider

**Title:** SECTION 04 — Research Question

**Note:** Section divider.

---

## Slide 19 — Research question

**Title:** Research Question

**Body:** *Which combination of missing-data handling and unsupervised learning produces the most stable, interpretable cluster structure from Bangladeshi newspaper suicide records?*

**Note:** Italic, centered. One sentence. Plenty of space.

---

## Slide 20 — Objectives

**Title:** Objectives

**Body:**
1. Expand and curate a Bangladeshi newspaper-reported suicide dataset spanning 2017–2025.
2. Benchmark three imputation methods × two predictor strategies × four clustering algorithms.
3. Design a balance-aware composite metric that demotes degenerate cluster solutions.
4. Identify and interpret the top-ranked pipeline — and surface its caveats openly.

**Note:** Four numbered objectives, left-aligned.

---

# SECTION 6 — METHODOLOGY

## Slide 21 — Section divider

**Title:** SECTION 05 — Methodology

**Note:** Section divider.

---

## Slide 22 — End-to-end pipeline

**Title:** End-to-end pipeline

**Image:** `images/intro.png` (full pipeline diagram)

**Body:** Caption beneath: *From newspaper scraping through cleaning, enrichment, imputation, clustering, and composite evaluation.*

**Note:** Image takes up ~70% of slide. Caption below.

---

## Slide 23 — Dataset construction

**Title:** Dataset · 1,617 records · 2017–2025

**Body:**
| | |
|---|---|
| 760 records | Public 2020 Kaggle dataset |
| 857 records | Manually collected, 2017–2025 |
| 9 new attributes | Socio-economic and clinical fields added |
| 36 columns | Raw |
| 34 columns | After ethical removals (full_name, data_source) |
| 29 columns | Final analytical feature set (13 categorical + 16 numerical) |

**Numbers:** 1617, 760, 857, 9, 36, 34, 29, 13, 16

**Source:** This study · github.com/akashmony01/imputation-clustering-comparison

**Note:** Two-column table. Numbers on left in big type, descriptions on right.

---

## Slide 24 — New attributes added

**Title:** Nine new attributes

**Body:**
- family_members
- position_in_siblings
- marital_status (new variant)
- duration_of_separation
- profession_description
- workplace (new variant)
- financial_condition
- previous_health_condition
- previous_suicide_attempt

**Note:** Two-column list. These are the 9 new attributes added during dataset expansion.

---

## Slide 25 — External API enrichment

**Title:** External API enrichment

**Body:**
- **Geopy** — geocoding service · reduced lat/lon missingness from ~53% to **6.49%**
- **Meteostat** — historical weather API · added feels_like, temp_min/max, humidity, wind, clouds, weather descriptions

**Numbers:**
- 53% → 6.49% (lat/lon missingness reduction)
- 11 weather columns added

**Source:** This study (notebook 1_filling-lat-lon, notebook 2_filling-weather)

**Note:** Two enrichment blocks. Show the missingness reduction as a small visual bar.

---

## Slide 26 — Encoding strategy

**Title:** Encoding strategy

**Body:**
| Variable type | Strategy |
|---|---|
| Ordinal categoricals | Frequency encoding |
| Low-cardinality nominals (gender, workplace, religion) | One-hot |
| High-cardinality nominals (hometown, profession_group) | Frequency / label encoding |
| MissForest input | Label encoding (tree-native) |

**Note:** Four-row mapping table.

---

## Slide 27 — Imputation workflow

**Title:** Imputation workflow

**Image:** `images/imputation.png`

**Body:** Caption: *Three methods · two predictor strategies · six imputed datasets · post-imputation residual missingness ≤ 0.25%.*

**Numbers:** 6 variants · ≤0.25% residual missingness

**Note:** Image takes ~70% of slide.

---

## Slide 28 — Three imputation methods

**Title:** Three imputation methods

**Body:**
- **MICE** — per-variable BayesianRidge regression · single-pass MICE-style imputation
- **KNN** — k = 5 nearest-neighbour averaging
- **MissForest** — random forest per variable, 100 trees, iterated to Stekhoven convergence

**Numbers:** k=5 (KNN) · 100 trees (MissForest)

**Source:**
- MICE: Van Buuren & Groothuis-Oudshoorn, 2011
- KNN: Troyanskaya et al., 2001
- MissForest: Stekhoven & Bühlmann, 2012

**Note:** Three method blocks with one-line description each.

---

## Slide 29 — Two predictor strategies

**Title:** Two predictor strategies

**Body:**
- **Context-aware** — for each target column, predictors are the columns with non-zero Pearson/Cramér's V correlation to the target
- **No-context** — all available columns serve as predictors

**Note:** Two definition cards. Use a small comparison icon or split layout.

---

## Slide 30 — Clustering workflow

**Title:** Clustering workflow

**Image:** `images/cluster_flow.png`

**Body:** Caption: *Standardisation · PCA · per-algorithm grid search · composite ranking across all 32 pipelines.*

**Note:** Image takes ~70% of slide.

---

## Slide 31 — Four clustering algorithms

**Title:** Four clustering algorithms across paradigms

**Body:**
| Algorithm | Paradigm | Reference |
|---|---|---|
| K-Means | Centroid | MacQueen, 1967 |
| Agglomerative | Hierarchical | Ward Jr., 1963 |
| DBSCAN | Density | Ester et al., 1996 |
| Spectral | Graph | Ng, Jordan, Weiss, 2001 |

**Note:** Four-row table.

---

## Slide 32 — Hyperparameter search ranges

**Title:** Hyperparameter search ranges

**Body:**
- **K-Means:** k ∈ [2, 20] · init ∈ {k-means++, random} · n_init ∈ {10, 20, 50} · max_iter ∈ {300, 500}
- **Agglomerative:** k ∈ [2, 10] · linkage ∈ {ward, complete, average, single}
- **DBSCAN:** eps ∈ grid · min_samples ∈ grid
- **Spectral:** k ∈ [2, 10] · affinity = nearest_neighbors · labels = kmeans
- **PCA:** 99% variance (K-Means) · 10 components (Agg, DBSCAN) · 20 components (Spectral)

**Note:** Five blocks with searched parameter ranges.

---

## Slide 33 — The scoring problem

**Title:** Standard scores reward degenerate solutions.

**Body:** Example: DBSCAN can label **99%** of cases as noise and still score "high" on Silhouette.

**Numbers:** 99% noise possible while scoring high

**Source:** Ikotun et al., 2025 (Heliyon · cluster validity indices review)

**Note:** Statement + one example line below.

---

## Slide 34 — Our six-component composite

**Title:** Our six-component composite score

**Body:**
| Metric | Weight |
|---|---|
| Balance penalty | 35% |
| Silhouette | 25% |
| Calinski–Harabasz | 20% |
| Dunn | 10% |
| Davies–Bouldin (inverted) | 5% |
| Xie–Beni (inverted) | 5% |

Closing line: *Maximum possible score: **32***

**Note:** Six-row table with horizontal bars showing weight visually. Total at bottom.

---

## Slide 35 — Methodology recap · here is everything we did

**Title:** Here is what we built · the full pipeline

**Image:** `images/overall.png` (detailed end-to-end pipeline figure from Chapter 3 of the report)

**Body:** Caption beneath: *From newspaper scraping through cleaning, geocoding (Geopy), weather enrichment (Meteostat), encoding (frequency, one-hot, label), six imputation variants (MICE / KNN / MissForest × context-aware / no-context), four clustering algorithms across 8 input datasets (= 32 pipelines), and the balance-aware composite scoring framework — visualised end-to-end.*

**Numbers visible in the figure:** 1,617 records · 36 raw columns · 6 imputed datasets · 32 pipelines · 6-component composite

**Note:** This is a "here's everything we just walked through" recap slide. Use it to consolidate the Methodology section before transitioning into Results. The image should dominate the slide — keep the caption short. Speaker should say something like "to summarise the methodology section, this is the full pipeline we built — and now we'll move into what came out of it."

---

# SECTION 7 — RESULTS

## Slide 35 — Section divider

**Title:** SECTION 06 — Results

**Note:** Section divider.

---

## Slide 36 — All 32 pipelines ranked

**Title:** All 32 pipelines ranked by composite score

**Image:** `images/all_cases_sorted_with_combined_score.png`

**Body:** Caption: *The full ranking. Agglomerative + MissForest no-context leads the field at 27.30.*

**Note:** Image fills ~70% of slide. Caption below.

---

## Slide 37 — Composite-score heatmap

**Title:** Composite scores · all 32 pipelines, all 6 metrics

**Image:** `images/all_values_heat_map.png.png`

**Body:** Caption: *Per-pipeline, per-metric heatmap. Higher values are darker.*

**Note:** Image fills ~70% of slide.

---

## Slide 38 — Group averages

**Title:** Group averages

**Body:**
| Group | Average composite |
|---|---|
| MissForest variants | **23.27** |
| MICE variants | 16.91 |
| KNN variants | 14.92 |
| Non-imputed baselines | 10.90 |

**Body 2 (algorithm averages):**
| Algorithm | Average composite |
|---|---|
| Spectral | **22.18** |
| K-Means | 18.80 |
| Agglomerative | 13.28 |

**Numbers:** all values above

**Note:** Two stacked tables — imputation groups on top, algorithm groups below.

---

## Slide 39 — The winner

**Title:** The top-ranked pipeline

**Body:**
- **Agglomerative + MissForest** (no-context)
- Composite score: **27.30 / 32**
- Cluster count: **2**

**Note:** Pipeline name large, score large beneath, cluster count small.

---

## Slide 40 — 27.30 / 32

**Title:** (no title — just the number)

**Body:**
- Massive number: **27.30**
- Caption: out of 32
- Source: This study · composite score across 32 pipelines

**Note:** Big-number slide.

---

## Slide 41 — Two clusters

**Title:** Two clusters

**Body:**
- **Cluster 0** — 759 records
- **Cluster 1** — 858 records
- Caption: Near-balanced partition from 1,617 records

**Numbers:** 759, 858, 1617

**Note:** Two circles (proportional sizes) side by side or two large numbers.

---

## Slide 42 — Cluster 0 geographic distribution

**Title:** Cluster 0 · geographic distribution

**Image:** `images/cluster_0_bangladesh.png`

**Body:** Caption: *Cluster 0 hometowns mapped across Bangladesh.*

**Note:** Map image dominates the slide.

---

## Slide 43 — Cluster 1 geographic distribution

**Title:** Cluster 1 · geographic distribution

**Image:** `images/cluster_1_bangladesh.png`

**Body:** Caption: *Cluster 1 hometowns mapped across Bangladesh.*

**Note:** Map image dominates the slide.

---

## Slide 44 — Cluster 0 profile

**Title:** Cluster 0 profile

**Body:**
- **Workplace:** semi-urban (54.5%) · rural (35.7%) · urban (9.7%)
- **Top hometowns:** Bogura (4.0%) · Rajshahi (3.6%) · Dhaka (3.4%) · Mymensingh (3.0%)
- **Year coverage:** 2020 only
- **Source cohort:** Kaggle 2020

**Numbers:** all percentages above

**Source:** This study · agg_rf_no_context output

**Note:** Four-line profile block.

---

## Slide 45 — Cluster 1 profile

**Title:** Cluster 1 profile

**Body:**
- **Workplace:** rural (50.0%) · urban (26.6%) · semi-urban (23.4%)
- **Top hometowns:** Dhaka (9.1%) · Chattogram (7.7%) · Barishal (2.6%) · Jessore (2.4%)
- **Year coverage:** 2017–2019 + 2021–2025 (with small 2020 residue)
- **Source cohort:** manual collection

**Numbers:** all percentages above

**Source:** This study · agg_rf_no_context output

**Note:** Four-line profile block matching Slide 44.

---

## Slide 46 — Feature-by-feature contrast

**Title:** Feature-by-feature contrast

**Body:**
| Feature | Cluster 0 | Cluster 1 |
|---|---|---|
| Modal workplace | Semi-urban (54.5%) | Rural (50.0%) |
| Top hometown | Bogura (4.0%) | Dhaka (9.1%) |
| Top reason | Family conflict | Family conflict |
| Year coverage | 2020 only | 2017–2025 |
| Cluster size | 759 | 858 |
| Source cohort | Kaggle 2020 | Manual collection |
| Temperature unit | Kelvin | Celsius |

**Note:** Compact comparison table.

---

## Slide 47 — Age distribution

**Title:** Age distribution by cluster

**Image:** `images/age_cpmaring.png`

**Body:** Caption: *Both clusters concentrate in the 16–35 high-risk window. Cluster 1 skews slightly older.*

**Note:** Figure dominates slide.

---

## Slide 48 — Reason for suicide

**Title:** Reason for suicide · by cluster

**Image:** `images/reason_comparing.png`

**Body:** Caption: *Family conflict and relationship-related distress dominate in both clusters; the weighting differs.*

**Note:** Figure dominates slide.

---

## Slide 49 — Geographic comparison

**Title:** Location patterns by cluster

**Image:** `images/location_comparing.png`

**Body:** Caption: *Cluster 1 concentrates at major urban hometowns (Dhaka, Chattogram); Cluster 0 spreads across mid-sized cities.*

**Note:** Figure dominates slide.

---

## Slide 50 — Weather comparison

**Title:** Weather context · feels_like by cluster

**Image:** `images/feels_like_comparing.png`

**Body:** Caption: *Cluster 0 feels_like values appear in Kelvin (artefact of the Kaggle subset's encoding); Cluster 1 in Celsius. See caveats.*

**Note:** Figure dominates slide. Important to flag the Kelvin/Celsius issue right here.

---

# SECTION 8 — HONEST FINDINGS

## Slide 51 — Section divider

**Title:** SECTION 07 — Honest Findings

**Note:** Section divider (use caveat colour).

---

## Slide 52 — The honest finding

**Title:** An honest finding

**Body:** The two clusters align with the **data-collection boundary**, not with two distinct epidemiological groups.

**Note:** Single declarative sentence centered. Caveat colour.

---

## Slide 53 — How the cohorts map

**Title:** How the cohorts map to the clusters

**Body:**
- **Cluster 0** = all 2020 (Kaggle subset)
- **Cluster 1** = 2017–2019 + 2021–2025 (manually collected)
- Note: the algorithm never saw the year — the split is **emergent**
- Reading: an internal consistency check, not a substantive epidemiological finding

**Note:** Two equation lines on top, two reading lines below.

---

## Slide 54 — Three caveats

**Title:** Three caveats — disclosed in the abstract

**Body:**
1. **Source-cohort confound** — cluster split coincides with data origin
2. **Temperature units differ** — Kelvin in Cluster 0 · Celsius in Cluster 1
3. **De-identified, not anonymised** — district + date + age + method could permit re-identification

**Note:** Three numbered caveats. Caveat colour for emphasis.

---

# SECTION 9 — STANDARDS AND CONSTRAINTS

## Slide 55 — Section divider

**Title:** SECTION 08 — Standards, Ethics, Sustainability

**Note:** Section divider.

---

## Slide 56 — SDG alignment

**Title:** UN Sustainable Development Goal alignment

**Body:**
- **SDG 3.4 / 3.4.2** — Suicide mortality rate (per 100,000 population)
- **SDG 5.2** — Eliminate violence against women and girls
- **SDG 10** — Reduce inequalities within and among countries

**Source:** UN SDG indicator framework; WHO Global Health Observatory

**Note:** Three SDG cards. Cite the indicator number.

---

## Slide 57 — Ethical safeguards

**Title:** Ethical safeguards

**Body:**
- full_name column removed at preprocessing
- Address coarsened to district level (no street/exact location)
- data_source URLs removed to prevent traceback to articles
- Suicide method retained only in encoded form, never reproduced at case level
- Source: publicly available Bangladeshi news outlets only
- Dataset released as **de-identified**, not formally anonymised

**Note:** Bulleted ethical-measures list.

---

## Slide 58 — Project timeline

**Title:** Project timeline · 25 weeks

**Image:** `images/gantt_timeline.png`

**Body:** Caption: *Literature review · base data collection · manual case expansion · cleaning · API filling · feature engineering · six-variant imputation · four-algorithm clustering · composite scoring · report writing.*

**Numbers:** 25 weeks · 9 task groups

**Note:** Gantt chart dominates slide.

---

# SECTION 10 — CLOSING

## Slide 59 — Limitations

**Title:** Limitations

**Body:**
- Newspaper bias toward newsworthy cases
- 1,617 records — small by ML standards
- No external ground-truth labels
- Bangla NLP excluded from free-text fields
- Weather data sparse in rural areas
- Pipeline search space bounded by compute budget

**Note:** Six short lines.

---

## Slide 60 — Future work

**Title:** Future work

**Body:**
1. SHAP / feature-importance analysis to surface cluster drivers
2. Data expansion via more newspaper sources and other LMIC outlets
3. Causal modelling — propensity-score matching, structural equation models
4. BanglaBERT for free-text reason and profession fields
5. Real-time alerting framework for high-risk demographic profiles
6. Extension of the framework to other LMIC newspaper-derived datasets

**Note:** Six-line numbered list. Future-work colour.

---

## Slide 61 — Contribution

**Title:** Contribution

**Body:**
1. The **largest curated** Bangladeshi newspaper suicide dataset to date
2. A **reproducible** 32-pipeline factorial benchmark
3. A **balance-aware composite** metric that demotes degenerate clusters
4. **Open-source** release: code + data + 12 Colab notebooks

**Note:** Four contribution blocks. Highlight the bold phrase in each.

---

## Slide 62 — Repository

**Title:** Repository and licences

**Body:**
- URL: `github.com/akashmony01/imputation-clustering-comparison`
- Code licence: **MIT**
- Data licence: **CC-BY 4.0**
- Contents: 12 Colab notebooks · intermediate datasets · cached external API responses

**Image:** QR code (Canva generates from the URL)

**Note:** URL in monospace, QR code on the right.

---

## Slide 63 — Thank you

**Title:** Thank you

**Body:** Questions?

**Note:** Two-line closing slide.

---

# APPENDIX OF FACTS USED IN THIS DECK

A reference list of every number and fact that appears in the slides, so you can double-check any claim during the talk.

## Dataset facts
- Total records: 1,617
- Raw columns: 36
- Analytical columns: 34 (after ethical removals)
- Final feature set: 29 (13 categorical + 16 numerical)
- Post-encoding for MICE/KNN: 37 numerical columns
- Post-encoding for MissForest: 29 label-encoded columns
- Kaggle subset: 760 records (all year 2020)
- Manual collection: 857 records (2017–2025)
- New attributes added: 9
- Date range: 2017–2025

## Imputation facts
- MICE retains: 1,613 rows × 37 columns (4 rows dropped — insufficient predictors)
- KNN retains: 1,617 rows × 37 columns
- MissForest retains: 1,617 rows × 29 columns
- MissForest trees: 100
- KNN neighbours: k = 5
- Residual missingness post-imputation: ≤ 0.25%
- Lat/lon missingness reduction: ~53% → 6.49% (via Geopy)

## Pipeline facts
- Total pipelines: 32 = 4 algorithms × 8 input datasets
- 6 imputed datasets + 2 encoded baselines = 8 inputs
- Notebook count: 12 (0_preprocessing through 11_comparing_clustering)

## Composite score facts
- Components: 6
- Weights: balance 35% · silhouette 25% · CH 20% · Dunn 10% · DB 5% · XB 5%
- Maximum score: 32
- Minimum score: 1

## Result facts
- Winning pipeline: agg_rf_no_context (Agglomerative + MissForest, no-context)
- Winning score: 27.30 / 32
- Number of clusters: 2
- Cluster 0 size: 759
- Cluster 1 size: 858
- Cluster 0 modal workplace: semi-urban (54.5%)
- Cluster 1 modal workplace: rural (50.0%)
- Cluster 0 hometown top: Bogura (4.0%)
- Cluster 1 hometown top: Dhaka (9.1%), Chattogram (7.7%)
- Cluster 0 year coverage: 2020 only
- Cluster 1 year coverage: 2017–2025 (predominantly 2017–2019 + 2021–2025)

## Group-average facts
- MissForest variants average: 23.27
- MICE variants average: 16.91
- KNN variants average: 14.92
- Non-imputed baselines average: 10.90
- Spectral algorithm average: 22.18
- K-Means algorithm average: 18.80
- Agglomerative algorithm average: 13.28

## External facts
- Bangladesh suicides per day: 40 (Bangladesh Police, 2025)
- 2020–2024 total: 73,597 deaths (Bangladesh Police, 2025)
- Annual average: 14,719 per year
- Older WHO estimate: ~10,000 per year

## Caveats
- Source-cohort confound: cluster split aligns with Kaggle 2020 vs manual 2017–2025 cohort
- Temperature unit issue: Kelvin in Cluster 0, Celsius in Cluster 1
- De-identification, not anonymisation: residual re-identification risk

## Available figures in /images/
- bubt-logo.png
- intro.png — overall pipeline
- imputation.png — imputation workflow
- cluster_flow.png — clustering workflow
- all_cases_sorted_with_combined_score.png — ranked composite scores
- all_values_heat_map.png — composite heatmap (per-pipeline, per-metric)
- cluster_0_bangladesh.png — Cluster 0 geographic
- cluster_1_bangladesh.png — Cluster 1 geographic
- cluster_visualization_of_all_cases.png — cluster visualisation
- cluster_number_and_cluster_items_for_all_cases.png — cluster size distribution
- comparing_clustering_algo_bar_chart.png — algorithm comparison
- comparing_context_vs_no_context_bar_cart.png — context comparison
- compraing_imputaion_bar_chart.png — imputation comparison
- comparing_all_cases_for _individual_metrics.png — per-metric comparison
- feels_like_comparing.png — feels_like (weather) comparison
- age_cpmaring.png — age comparison
- reason_comparing.png — reason comparison
- location_comparing.png — location comparison
- all_numerical_comparison.png — all numerical features
- all_categoricaL_comparsion.png — all categorical features
- gantt_timeline.png — 25-week project timeline

## Sources / references used in deck
- Bangladesh Police data, 2025 (via Prothom Alo, Daily Star)
- WHO Global Health Observatory (suicide mortality, SDG 3.4.2)
- UN Sustainable Development Goals framework
- Arafat et al., 2018 (Asian Journal of Psychiatry)
- Arafat et al., 2025 (Health Science Reports)
- Wong et al., 2022 (BMC Public Health)
- Xiao et al., 2025 (Nature Mental Health)
- Sanz-Gomez et al., 2025 (European Psychiatry)
- Boyce / Moniri et al., 2026 (Journal of Affective Disorders)
- Van Buuren & Groothuis-Oudshoorn, 2011 (MICE — JSS)
- Troyanskaya et al., 2001 (KNN — Bioinformatics)
- Stekhoven & Bühlmann, 2012 (MissForest — Bioinformatics)
- MacQueen, 1967 (K-Means)
- Ward Jr., 1963 (Hierarchical clustering)
- Ester et al., 1996 (DBSCAN)
- Ng, Jordan, Weiss, 2001 (Spectral clustering)
- Ikotun et al., 2025 (Heliyon — cluster validity review)
- Shadbahr / Garmdareh et al., 2023 (Communications Medicine — imputation quality)
- Jäger et al., 2021 (Frontiers in Big Data — imputation benchmark)
