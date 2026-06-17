# Presentation Brief

**Title:** Comparing Imputation and Clustering Pipelines on Incomplete Newspaper-Reported Suicide Data from Bangladesh
**Subtitle:** A 32-pipeline factorial benchmark with a balance-aware composite score
**Authors:** Five-member capstone team, BUBT Department of Computer Science and Engineering
**Audience:** Capstone defense panel — university faculty in CSE / data science
**Duration target:** 15–18 minutes
**Total cards:** 53

## Tone

Sober, respectful, academic. This is research on suicide. Do not make it light, playful, or motivational. Do not use stock imagery of sad faces, candles, broken hearts, or "depression" symbolism. Do not use emojis. Use plain declarative language. Let the numbers carry the weight.

## Visual direction

- Dark theme. Charcoal background (#1A1A1F). Off-white body text (#EAEAEA).
- Type-driven design. The visual element on most cards is the typography itself.
- Minimal ornament. No swoops, no gradients, no decorative shapes.
- One idea per card. Generous empty space — at least 40 percent of each card should be unused.
- Use large numbers as visual anchors. Numbers like 40, 73,597, 27.30, 1,617 should dominate their cards.
- Accent palette, used sparingly:
  - Cyan (#5EEAD4) for technical terms and section markers
  - Soft green (#34D399) for contributions and future work
  - Muted amber (#FBBF24) for caveats and honest findings
  - Restrained red (#F87171) used exactly once, on card 11, for the headline death-rate number — nowhere else
- Headlines: a heavy condensed sans like Anton, Bebas Neue, or Archivo Black
- Body: Inter or Manrope, regular weight

## Imagery

- Allowed: team-member portraits, Bangladesh map, pipeline flowchart, QR code, statistical charts derived from the actual data
- Forbidden: stock photos of grief, candles, mental-health symbolism, dramatic word-art, Bangla "suicide" text rendered in dramatic styles

---

# Card 1

One question, before we begin.

---

# Card 2

How do you study a public-health crisis when the data is broken?

*Visual: italic centered statement, no other elements.*

---

# Card 3

Suicide in Bangladesh.

*Visual: heavy weight, centered, dominates the card. The subject of the work.*

---

# Card 4

No national registry.

No structured surveillance.

Only newspaper reports.

*Visual: three short lines stacked, each given its own breathing room.*

---

# Card 5 — Title card

Comparing Imputation and Clustering Pipelines on Incomplete Newspaper-Reported Suicide Data from Bangladesh

A 32-pipeline factorial benchmark with a balance-aware composite score

BUBT Department of Computer Science and Engineering · Capstone Defense, June 2026

---

# Card 6 — Team Member 1

[Photo placeholder — team member 1]

[Name]

Project Lead and Pipeline Architecture

---

# Card 7 — Team Member 2

[Photo placeholder — team member 2]

[Name]

Data Collection and Curation

---

# Card 8 — Team Member 3

[Photo placeholder — team member 3]

[Name]

Imputation and Clustering Pipeline

---

# Card 9 — Team Member 4

[Photo placeholder — team member 4]

[Name]

Evaluation Framework and Composite Scoring

---

# Card 10 — Team Member 5

[Photo placeholder — team member 5]

[Name]

Documentation, Visualisation, and Caveats

---

# Card 11

40

suicides per day in Bangladesh

*Visual: the number 40 in massive type, restrained red (#F87171). Caption beneath in off-white. This is the only card that uses red.*

---

# Card 12

73,597

Bangladesh Police records, 2020 to 2024

Average: 14,719 per year

*Visual: large central number, two muted caption lines below.*

---

# Card 13

Stigma.

Cultural barriers.

No surveillance system.

*Visual: three single words on three lines, each given equal weight. The true rate is almost certainly higher than recorded for these reasons.*

---

# Card 14

High-income countries: structured registries.

Bangladesh: newspaper clippings.

*Visual: two contrasting pairs of lines. A thin horizontal rule between them. The contrast is the message.*

---

# Card 15

Newspaper reports are the only data we have.

*Visual: single declarative sentence, centered.*

---

# Card 16

50 to 90 percent

of fields are missing

*Visual: range as the dominant number, caption below.*

---

# Card 17

Age. Occupation. Location.

Mental-health history.

Socio-economic status.

*Visual: three short lines of period-separated phrases, listing what is systematically absent from newspaper reports.*

---

# Card 18

Standard machine learning cannot run on data this broken.

*Visual: two-line declarative statement.*

---

# Card 19 — Research Question

RESEARCH QUESTION

Which combination of missing-data handling and unsupervised learning produces the most stable, interpretable cluster structure from Bangladeshi newspaper suicide records?

*Visual: small cyan label above, italic question below, generous empty space around.*

---

# Card 20

What we built.

*Section divider. Cyan heading.*

---

# Card 21

1,617

records

*Visual: single number plus one-word caption. The size of the curated dataset.*

---

# Card 22

760 records from a public 2020 Kaggle dataset.

857 records manually collected, 2017 to 2025.

9 new socio-economic and clinical attributes added during expansion.

---

# Card 23

A factorial benchmark.

*Visual: single statement, centered, period included.*

---

# Card 24

3 × 2 × 4 = 32 pipelines

*Visual: equation centered. Numbers in cyan, equals sign and operators in off-white. Result emphasised.*

---

# Card 25 — Imputation methods

MICE — per-variable BayesianRidge regression

KNN — k = 5 nearest-neighbour averaging

MissForest — random forest per variable

Each method ran twice: once with correlation-filtered predictors (context-aware), once with all available predictors (no-context).

---

# Card 26 — Clustering algorithms

K-Means — centroid

Agglomerative — hierarchical

DBSCAN — density

Spectral — graph

One representative from each major paradigm, because no algorithm dominates when cluster geometry is unknown.

---

# Card 27

Standard scores reward degenerate solutions.

*Visual: two-line statement, amber accent.*

---

# Card 28

DBSCAN can label 99 percent of cases as noise and still score well on Silhouette.

*Visual: declarative example, centered.*

---

# Card 29 — The composite

Balance penalty — 35 percent

Silhouette — 25 percent

Calinski-Harabasz — 20 percent

Dunn — 10 percent

Davies-Bouldin — 5 percent

Xie-Beni — 5 percent

Six components. Maximum possible score: 32.

*Visual: weighted breakdown with percentages right-aligned. Closing summary below.*

---

# Card 30

Results.

*Section divider. Cyan heading.*

---

# Card 31

Agglomerative + MissForest

no-context

*Visual: pipeline name on two lines, centered. The top-ranked combination.*

---

# Card 32

27.30

out of 32

*Visual: massive composite score number, muted denominator below.*

---

# Card 33

Two clusters.

*Visual: declarative two-word statement, centered.*

---

# Card 34

Cluster 0 — 759 records

Cluster 1 — 858 records

*Visual: two horizontal lines or a balanced bar comparison. The split is near-balanced.*

---

# Card 35 — Cluster 0 profile

Cluster 0

Semi-urban workplaces.

Hometowns dispersed across mid-sized provincial cities.

Bogura. Rajshahi. Mymensingh.

---

# Card 36 — Cluster 1 profile

Cluster 1

Rural workplaces.

Hometowns concentrated at the two largest cities.

Dhaka (9.1 percent). Chattogram (7.7 percent).

---

# Card 37 — Workplace contrast

Cluster 0 modal workplace: semi-urban (54.5 percent)

Cluster 1 modal workplace: rural (50.0 percent)

*Visual: two-pair comparison, percentages prominent.*

---

# Card 38

An honest finding.

*Section divider. Amber heading.*

---

# Card 39

The two clusters align with the data-collection boundary, not with two distinct epidemiological groups.

*Visual: declarative statement, amber accent on the operative phrase.*

---

# Card 40

Cluster 0 = all 2020 (the Kaggle subset)

Cluster 1 = 2017 to 2019 + 2021 to 2025 (manually collected)

*Visual: two stacked equations showing how the cluster split aligns with the data origin.*

---

# Card 41

The algorithm never saw the year.

The split is emergent.

*Visual: two-line statement, centered. The clustering input contained no temporal or source attribute.*

---

# Card 42

An internal consistency check.

The pipeline preserves cohort structure under heavy missingness.

Not a substantive epidemiological finding.

*Visual: positive read above in soft green, negative read below in amber. Two contrasting interpretations of the same result.*

---

# Card 43

Caveat one: Source-cohort confound.

The cluster split coincides with data origin, not with epidemiology.

*Visual: amber accent on caveat number, statement below in off-white.*

---

# Card 44

Caveat two: Temperature units differ.

Kelvin in Cluster 0. Celsius in Cluster 1.

Disclosed, not hidden — documented in Chapter 6 and the abstract.

*Visual: amber accent on caveat number.*

---

# Card 45

Caveat three: De-identified, not anonymised.

District plus date plus age plus method could theoretically permit re-identification.

The dataset is released under a research-use licence with explicit non-re-identification terms.

*Visual: amber accent.*

---

# Card 46 — Limitations

Newspaper bias toward newsworthy cases.

Small sample by machine-learning standards.

No external ground-truth labels.

Bangla NLP excluded — no project-tier resources for free-text fields.

Weather data sparse for rural locations.

---

# Card 47

What's next.

*Section divider. Soft green heading.*

---

# Card 48 — Future work

Causal modelling beyond descriptive clustering.

BanglaBERT for free-text reason and profession fields.

Real-time alerting for high-risk demographic and geographic profiles.

Extension of the framework to other LMIC newspaper datasets.

---

# Card 49

What this thesis contributes.

*Section divider. Soft green heading.*

---

# Card 50 — Four contributions

The largest curated Bangladeshi newspaper-derived suicide dataset to date.

A reproducible 32-pipeline benchmark on severely incomplete social data.

A balance-aware composite metric that demotes degenerate cluster solutions.

Open-source release of code, data, and the full 12-notebook pipeline.

*Visual: four short blocks, soft green accent on the lead phrase of each.*

---

# Card 51 — Repository

github.com/akashmony01/imputation-clustering-comparison

Code released under MIT License.

Data released under CC-BY 4.0.

12 Colab notebooks, intermediate datasets, and cached external API responses.

*Visual: URL prominent in monospace on left. QR code linking to the URL on right. Licence details below.*

---

# Card 52 — Summary

The dataset is broken.

The method is honest.

The framework is reusable.

*Visual: three short declarative lines, equal weight, centered.*

---

# Card 53 — Closing

Thank you.

Questions?

*Visual: large "Thank you" centered. "Questions?" smaller below in cyan. Maximum empty space.*
