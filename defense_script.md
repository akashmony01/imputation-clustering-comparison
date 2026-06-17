# Defense Script — Short Lines to Memorize

Two lines max per slide. Simple words. Speak slow.

---

## Slide 1 — Title
Good morning everyone. Today we will present our work on comparing imputation and clustering pipelines on incomplete newspaper suicide data from Bangladesh.

## Slide 2 — The Team
We are a team of five from the CSE department of BUBT.
Our names and IDs are shown on the screen.

## Slide 3 — Overview
Our presentation has six sections.
Background, literature, research question, methodology, results, and findings with limitations.

## Slide 4 — Section: Background
Let me start with the background.

## Slide 5 — Suicide in Bangladesh
Suicide in Bangladesh is a serious public-health crisis.
But the country has no national surveillance system to track it.

## Slide 6 — The numbers
Bangladesh Police recorded 73,597 suicide deaths between 2020 and 2024.
That is about 14,719 deaths per year, or 40 deaths every single day.

## Slide 7 — The true figure is higher
But the real number is even higher than this.
Because of stigma, cultural barriers, and no surveillance system, many cases are never reported.

## Slide 8 — Section: The Data Problem
Now let me explain the data problem we faced.

## Slide 9 — Newspapers are the only source
In Bangladesh, newspapers are the only public source of suicide case data.
There is no hospital or government dataset available.

## Slide 10 — 50 to 90 percent missing
But newspaper data is broken. Around 50 to 90 percent of critical fields are missing.
Fields like age, occupation, mental health, location, and weather are often empty.

## Slide 11 — Standard ML cannot run
Because of this, standard machine learning cannot run on this data.
Dropping rows wastes most of the dataset, and simple mean filling creates bias.

## Slide 12 — Section: Literature Review
Now I will discuss the literature review and the research gap.

## Slide 13 — Bangladeshi research
Two important studies by Arafat and team looked at Bangladeshi newspaper data.
But they only did manual grouping or aggregate statistics. No algorithm was used.

## Slide 14 — Global research
Globally, Xiao and Wong applied machine learning and clustering on suicide data.
But their work was on the US and Hong Kong, not on Bangladesh.

## Slide 15 — The Research Gap
We found five gaps in the literature.
No clustering on Bangladeshi news data, no multi-method imputation, only single algorithm used, weak metrics, and no comparison of predictor strategies.

## Slide 16 — Section: Research Framing
This brings us to our research framing.

## Slide 17 — Research Question
Our research question is simple.
Which combination of missing-data handling and unsupervised learning gives the most stable and interpretable cluster structure from this data?

## Slide 18 — Objectives
We had four objectives.
Build the dataset, benchmark 32 pipelines, design a balance-aware score, and find the best pipeline with honest caveats.

## Slide 19 — Section: Methodology
Now let me walk you through the methodology.

## Slide 20 — End-to-end pipeline
This figure shows our full pipeline at a high level.
It goes from data collection to preprocessing, encoding, imputation, clustering, and evaluation.

## Slide 21 — Dataset
We built a dataset of 1,617 records covering 2017 to 2025.
760 came from a public Kaggle dataset and 857 we collected manually.

## Slide 22 — New attributes
We added nine new attributes to enrich the data.
These cover family, profession, financial condition, and mental-health history.

## Slide 23 — External API enrichment
We used two APIs to fill in missing context.
Geopy gave us geocoding, and Meteostat gave us weather data.

## Slide 24 — Encoding strategy
We used different encoding for different feature types.
Frequency for ordinal, one-hot for low-cardinality, and label encoding for MissForest.

## Slide 25 — Imputation workflow
This diagram shows the full imputation workflow.
We used three methods and two predictor strategies, giving six imputed datasets.

## Slide 26 — Three imputation methods
The three methods are MICE, KNN, and MissForest.
Each one uses a different statistical approach to fill missing values.

## Slide 27 — Two predictor strategies
We used two predictor strategies.
Context-aware uses only correlated columns, and no-context uses every available column.

## Slide 28 — Clustering workflow
This diagram shows the clustering workflow.
Every dataset goes through scaling, PCA, grid search, and final scoring.

## Slide 29 — Four clustering algorithms
We used four clustering algorithms from four different paradigms.
K-Means for centroid, Agglomerative for hierarchical, DBSCAN for density, and Spectral for graph.

## Slide 30 — Hyperparameter ranges
For each algorithm we tested a wide range of hyperparameters.
This made the comparison fair and reproducible.

## Slide 31 — Standard scores fail
Standard scores like Silhouette can reward bad solutions.
For example, DBSCAN can label 99 percent of cases as noise and still score high.

## Slide 32 — Six-component composite score
To fix this we built a six-component composite score.
The balance penalty has the biggest weight, so degenerate clusters are demoted.

## Slide 33 — Here is what we built
And this is the full detailed pipeline showing everything from start to finish.
Eight datasets times four algorithms equals 32 clustering pipelines.

## Slide 34 — Section: Results
Now let me share the results.

## Slide 35 — All 32 pipelines ranked
We ranked all 32 pipelines by composite score.
Agglomerative with MissForest no-context came first, with a score of 27.30 out of 32.

## Slide 36 — Composite heatmap
This heatmap shows how every pipeline performed on every metric.
Darker red means higher score.

## Slide 37 — Group averages
On average, MissForest imputation beat MICE and KNN.
And Spectral and K-Means did better than Agglomerative overall.

## Slide 38 — The top pipeline
The winning pipeline is Agglomerative with MissForest no-context.
It got 27.30 out of 32 and made two clear clusters.

## Slide 39 — Two clusters
The two clusters had 759 and 858 records.
This is a very balanced split.

## Slide 40 — Geographic distribution
This map shows where each cluster is located in Bangladesh.
Cluster 0 spreads across the country, while cluster 1 is more concentrated in big cities.

## Slide 41 — Cluster profiling
Cluster 0 is mostly semi-urban with hometowns like Bogura and Rajshahi.
Cluster 1 is more rural but with hometowns in Dhaka and Chattogram.

## Slide 42 — Reason and age comparison
The two clusters also differ in reason and age distribution.
Cluster 0 is wider in age, while cluster 1 peaks at younger adults.

## Slide 43 — Section: Honest Findings
Now I want to share an honest finding from our work.

## Slide 44 — An honest finding
The two clusters actually match the data-collection boundary.
Not two real epidemiological groups.

## Slide 45 — How the cohorts map
Cluster 0 is the 2020 Kaggle subset, and cluster 1 is our manually collected data.
But the algorithm never saw the year. So this split is emergent, and it works as an internal consistency check.

## Slide 46 — Section: Ethical Concern and Timeline
Next, I will cover our ethical safeguards and project timeline.

## Slide 47 — Ethical safeguards
We took several steps to protect privacy.
Names removed, addresses coarsened, URLs dropped, and methods stored only in encoded form.

## Slide 48 — Project timeline
The full project took 25 weeks.
You can see how each phase was done step by step.

## Slide 49 — Section: Closing
And now the closing part.

## Slide 50 — Limitations
We have some honest limitations.
Newspaper bias, small dataset, no ground truth, sparse weather data, and limited compute.

## Slide 51 — Future work
In future we want to add SHAP analysis, expand the data, and try causal modelling.
BanglaBERT for free text and a real-time alerting system are also next steps.

## Slide 52 — Contribution
Our main contributions are four.
The largest curated Bangladeshi suicide dataset, a reproducible benchmark, a balance-aware metric, and full open-source release.

## Slide 53 — Repository
You can find all our code, data, and notebooks on GitHub.
The QR code on the screen takes you to the repository.

## Slide 54 — Thank You
Thank you so much for listening.
We are happy to take your questions now.
