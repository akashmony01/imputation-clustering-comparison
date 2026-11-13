# LLM-Assisted Categorical Rationalization: Methodology Reference

**Purpose of this document.** Reference notes capturing how an LLM (ChatGPT-4) was used to consolidate raw, noisy categorical fields in the Bangladeshi suicide news dataset into clean canonical categories. Intended to feed the methodology section of (a) the i-COSTE 2026 conference paper, (b) the later mid-tier journal extension, and (c) any future writing about the same dataset. Captures the workflow honestly so the contribution can be stated without overclaim.

**Date compiled.** 2026-06-26.

**Authoritative artefacts.**
- Mapping dictionaries: `notebooks/0_preprocessing.ipynb` (cells defining `*_mapping` dicts).
- Two ChatGPT conversation transcripts: `chat.md` at project root.

---

## 1. Summary in one paragraph

The dataset was scraped from heterogeneous Bangladeshi newspaper reports across 2017–2025. Categorical fields therefore contained raw, free-text values written by reporters with no shared controlled vocabulary: typos, casing drift, trailing whitespace, multi-word verbose descriptions, and multilingual variants. Across eleven categorical fields the raw cardinality summed to **918 unique values**. This made downstream encoding intractable (KNN distance metrics break under one-hot dimensions of that scale; MICE conditional draws have too few observations per category for stable estimates). To make the imputation pipeline statistically tractable, the unique values from each field were submitted to ChatGPT-4 with an explicit consolidation instruction. The model returned proposed mappings which were then reviewed, edited, and codified by the authors into deterministic Python dictionaries. The final consolidated cardinality was **156 canonical categories** — an 83% reduction — and the dictionaries are shipped with the codebase, so the runtime pipeline is fully deterministic and reproducible without further LLM involvement.

---

## 2. Why we did this at all (the bridge for reviewers)

Categorical consolidation is not cosmetic. It is a precondition for the downstream imputation–clustering benchmark:

- **Without consolidation:** one-hot encoding `profession` (102 raw values) inflates the feature matrix by ~100 sparse columns. KNN distance metrics collapse in this regime; the nearest neighbour for an unobserved row is dominated by encoding noise rather than substantive similarity.
- **Without consolidation:** MICE per-variable conditional draws on `reason` (202 raw categories) would have a median of 1,617 ÷ 202 ≈ 8 observations per category — too few to fit a Bayesian ridge regression with the other 30+ predictors as conditioning variables. The chains either fail to converge or return high-variance posterior draws.
- **Without consolidation:** the clustering step would produce 200-cluster solutions driven entirely by surface-string artefacts of news reporting.

Consolidation to 3–28 canonical categories per field is what makes the 32-pipeline factorial benchmark statistically meaningful.

---

## 3. The two prompt patterns

Two distinct LLM workflows were used depending on the field's structure.

### Pattern A — Surface Normalization

Used for short categorical fields where the raw values were essentially typo/casing variants of a small canonical vocabulary.

**Fields:** `age_group`, `gender`, `religion`, `marital_status`.

**Typical prompt structure:**

> *"Unique values in column 'X':*
> *\<paste list of unique values\>*
>
> *create a unique mapping considering spelling errors and space-dash issues to create minimum number of unique categories that I can then use in python code to replace the duplicates. give me just the dictionary no code. and give the dict in such a way so it takes least spaces to write."*

**Verbatim example used for `marital_status`:**

> *"Unique values in column 'marital_status':*
> *[nan 'relationship-rejected' 'unmarried' 'relationship' 'married' 'broked_up' 'engaged' 'divorced' 'Married' 'widowed' 'Single' 'Unmarried' 'broken_up' 'Broken_up' 'Engaged' 'Unamrried' ... 'maried' 'unmarired' 'Relationship' 'Marriage-rejected' 'DIvorced']*
>
> *create a unique mapping considering spelling errors and space dash issues..."*

**What the LLM did well in this pattern:**
- Caught typos (`Unamrried`, `unmarired`, `maried`, `broked_up`) and mapped them to canonical spellings.
- Handled casing and trailing whitespace uniformly via a documented `.lower().strip()` preprocessing assumption.
- Consolidated semantic variants (`'single'` and `'unmarried'` → `single`; `'Marriage-rejected'` and `'relationship-rejected'` → `rejected`).

### Pattern B — Semantic Generalization with Domain Knowledge

Used for high-cardinality fields where the raw values were specific instances that needed mapping to higher-level canonical categories via real-world knowledge.

**Fields:** `hometown`, `reason`, `method`, `time`, `workplace`, `financial_condition`, `profession_group`.

**Typical prompt structure:**

> *"\<paste batch of unique values\>*
> *now map these values and give me the mapping"*

**Verbatim example used for `hometown` (one batch):**

> *"'tanore municipality, rajshahi' 'haridrabaria, amtali, bangladesh' 'bakshiganj, jamalpur, bangladesh' ... 'raja palang, ukhiya, cox's bazar'*
>
> *now map these values and give me mapping"*

**What the LLM did well in this pattern:**
- Applied Bangladesh administrative geography to map village/area strings to canonical district names (`'tanore municipality, rajshahi'` → `'rajshahi'`).
- Distinguished foreign places (`'balotra, rajasthan'` → `'india'`; `'usa'` → `'other'`; `'palestine'` → `'other'`).
- Resolved historical/colloquial name variants (`'cumilla'` → `'comilla'`; `'old dhaka'` → `'dhaka'`; `'bikrampur'` → `'munshiganj'`; `'siddhirganj'` → `'narayanganj'`).
- Resolved spelling variants of district names (`'khagrachori'` → `'khagrachhari'`; `'jashore'` and `'jessore'` consolidated).

---

## 4. Iteration workflow

The LLM's first response was rarely the final mapping. Two iteration patterns were used routinely.

### Iteration A — compactness/refinement pass

When the first mapping was too verbose or contained more canonical categories than needed, a follow-up instruction was used.

**Verbatim follow-up used for `marital_status`:**

> *"can this be written in better way so it takes less space to write?"*

The LLM then returned a more compact mapping that leveraged a documented preprocessing step (`.lower().strip()`) rather than enumerating every casing variant separately.

### Iteration B — batched processing for high-cardinality fields

`hometown` had 459 unique values, too many for a single prompt. The list was split into ordered batches and submitted sequentially. Each batch prompt was structured: *"\<batch\> now map these values"*; the last batch was signalled with: *"these are the last bunch. mapp them too give me the mapping only for the ones that needs."*

This pattern matters for reproducibility: the mapping was constructed batch-by-batch, with later batches benefiting from the canonical vocabulary established by earlier batches.

---

## 5. Cardinality reduction table

| Field | Raw unique values | Consolidated categories | Reduction |
|---|---:|---:|---:|
| age_group | 16 | 7 | 56% |
| gender | 7 | 3 | 57% |
| religion | 10 | 7 | 30% |
| marital_status | 18 | 8 | 56% |
| profession_group | 102 | 28 | 73% |
| workplace | 23 | 3 | 87% |
| financial_condition | 35 | 5 | 86% |
| reason | 202 | 14 | 93% |
| time | 46 | 6 | 87% |
| method | 100 | 10 | 90% |
| hometown | 459 | 75 | 84% |
| **Total** | **918** | **156** | **83%** |

Final canonical vocabularies (where small enough to enumerate):

- `age_group` (7): baby, child, teen, young, adult, middle-aged, old
- `gender` (3): male, female, third gender
- `religion` (7): muslim, hindu, buddhist, christian, chakma, marma, santal
- `marital_status` (8): single, engaged, married, relationship, broken up, divorced, widowed, rejected
- `workplace` (3): rural, semi-urban, urban
- `financial_condition` (5): indebted, lower, middle, upper_middle, upper
- `time` (6): morning, noon, day, afternoon, evening, night

---

## 6. Human-in-the-loop overrides

The LLM proposal was the *first* draft, not the final mapping. The authors validated each output and overrode it in several documented cases. These overrides constitute the substantive human contribution and are what distinguish this work from "we asked ChatGPT to do it."

### Override 1 — preserved indigenous religious categories

In the `religion` chat, after producing the first mapping, the LLM proactively offered:

> *"Let me know if you'd like to group indigenous groups (Chakma, Marma, Santal) under a single label like 'Indigenous'."*

The authors **rejected** this suggestion. Chakma, Marma, and Santal are three distinct ethno-religious communities in Bangladesh with separate cultural and demographic significance; collapsing them would erase substantively important variation. The final mapping retains them as three separate canonical categories.

**Why this matters for the paper:** this is direct evidence of human cultural-context judgment overriding an LLM default. Cite explicitly.

### Override 2 — rejected the "Other" bucket for ambiguous marital status

The LLM proposed mapping `'varied'` (a transcription artefact appearing in two rows of `marital_status`) to a new `'Other'` category. The authors **rejected** this and instead mapped `'varied'` to `'married'`, interpreting the string as a typo of `'married'` (one row had `'Varied '` adjacent to other `'Married'`-typo'd rows in the source). This kept the marital_status taxonomy semantically clean rather than introducing a low-information "Other" bin.

### Override 3 — caught LLM output errors

In the second `marital_status` chat, the LLM output contained a copy-paste artefact where the `'divorced'` key was repeated approximately fifty times. The authors **caught and discarded** the malformed output, requesting a clean version. This is a routine but real LLM failure mode and demonstrates the necessity of human review.

### Override 4 — geographic disambiguation choices

In `hometown` mapping, the LLM occasionally faced ambiguity (e.g., a village name that matched two districts). Where this happened, authors checked source articles to determine the correct district before codifying. The final mapping reflects these editorial decisions, not blind LLM acceptance.

---

## 7. Reproducibility design

The pipeline's runtime reproducibility does **not** depend on the LLM. The LLM was used at *design time*. At *runtime*, only the resulting deterministic mapping dictionaries are used.

Reproducibility properties:

1. **Mappings are frozen.** Every `*_mapping = {...}` dictionary in `notebooks/0_preprocessing.ipynb` is static Python code. A re-execution of the notebook will produce bit-identical results.
2. **Mappings ship with the codebase.** Anyone running the artefact has access to the canonical mappings.
3. **Normalization function is deterministic.** The `normalize_column_values` function (cell 34 of `0_preprocessing.ipynb`) applies `.lower().strip()` and a dictionary lookup — no model inference.
4. **No LLM at inference time.** A reviewer or replicator never needs to call ChatGPT to reproduce our pipeline.

This is the key methodological claim that lets the LLM-assisted preprocessing pass scrutiny: **the LLM is a design-time tool, not a runtime component.**

---

## 8. Honest limitations

These should be acknowledged briefly in the conference paper to pre-empt reviewer objections:

1. **The LLM was not formally evaluated.** No formal benchmark of LLM mapping accuracy was conducted — output accuracy was assessed informally by the authors during validation.
2. **Mapping decisions are not exhaustively documented at the level of individual values.** The mapping dictionaries record the final canonical labels but not the rationale per raw value. This is a tradeoff against project-scope feasibility.
3. **Cultural overrides are author-attributed, not externally validated.** The decisions to preserve Chakma/Marma/Santal and to interpret 'varied' as a typo of 'married' were made by Bangladeshi co-authors with domain familiarity. They are defensible but not externally vetted.
4. **Field-specific edge cases.** Some `hometown` values that the LLM mapped to a district had geographic ambiguity that was resolved by reviewing source articles; this article-by-article review is documented in the mapping dictionaries but not in a separate audit trail.

---

## 9. What goes in the conference paper

The i-COSTE paper should contain **one methodology subsection** plus **one cardinality table** plus **one mention in the abstract**.

### Methodology subsection (proposed draft, ~230 words)

> **LLM-Assisted Categorical Schema Rationalization.** Free-text categorical fields scraped from heterogeneous newspaper sources exhibited high cardinality (918 unique values across 11 fields), typos, casing drift, and verbose explanatory strings. We applied a two-pattern, human-validated LLM-assisted consolidation. *(i) Surface normalization:* unique values from short categorical fields (age_group, gender, religion, marital_status) were submitted to ChatGPT-4 with the instruction *"create a unique mapping considering spelling errors and space-dash issues to create minimum number of unique categories"*. *(ii) Semantic generalization with domain knowledge:* for high-cardinality location and free-text fields (hometown: 459 unique values; reason: 202; method: 100), the LLM was asked to map specific instances to canonical higher-level categories using its geographic and lexical knowledge. Long fields were processed in ordered batches. All LLM proposals were author-validated. Validation overrode the LLM in three documented cases: preservation of Chakma, Marma, and Santal as distinct religious categories (the LLM proposed collapse to "Indigenous"); reclassification of `'varied'` under marital_status as a transcription typo (the LLM proposed "Other"); and rejection of malformed LLM outputs containing duplicated keys. The resulting deterministic mapping dictionaries are shipped with the codebase, making the runtime preprocessing pipeline fully reproducible without further LLM involvement. Cardinality was reduced from 918 raw unique values to 156 canonical categories (83% reduction).

### Cardinality table

Use the table in Section 5 of this document, but trim to the most informative rows if space is tight.

### Abstract mention

Add to the methodology sentence of the abstract:

> *"...via a two-stage pipeline combining LLM-assisted categorical schema rationalization with a [N]-pipeline imputation–clustering factorial benchmark..."*

Replace `[N]` with whatever subset cardinality the conference version actually evaluates.

---

## 10. What goes in the journal version (later)

For the mid-tier journal extension, expand the methodology subsection into a full **§ Preprocessing Methodology** section (~600–900 words) that adds:

- A full per-field walk-through with raw → consolidated examples.
- The complete cardinality table from Section 5.
- All four overrides documented in Section 6, each with a paragraph of context.
- The full reproducibility argument from Section 7.
- The honest limitations from Section 8.
- A reproducibility supplement: the mapping dictionaries as a JSON appendix or supplementary file.

The journal version is the right place to spend the additional words on Pattern B (Bangladeshi geographic mapping) — it's a more interesting contribution than Pattern A (typo correction) and benefits from the room.

---

## 11. What does NOT go in either paper

These are intentionally excluded based on the strategy decided 2026-06-26:

- **Colab AI for code completion.** Standard tooling, not methodology, no mention.
- **LLM-assisted cluster interpretation.** Was used to draft narrative paragraphs interpreting per-cluster summary statistics; the *cluster summary statistic tables themselves* are the publishable evidence. LLM involvement at the writing-aid level is treated like Grammarly assistance — not disclosable, not methodologically claimed.
- **Any framing as a "novel LLM framework."** The LLM was a useful preprocessing tool. The headline contribution remains the imputation–clustering factorial benchmark plus the source-cohort artefact finding. The LLM-preprocessing methodology is a supporting contribution, not the headline.

---

## 12. Source references for this document

- Workflow descriptions reconstructed from author memory (2026-06-26 session).
- Verbatim prompts quoted from `chat.md` at project root (two conversations: marital_status + hometown; date normalization + gender + religion + marital_status).
- Cardinality counts computed directly from the mapping dictionaries in `notebooks/0_preprocessing.ipynb` (cells defining each `*_mapping` dict).
- Override evidence: religion-collapse suggestion from `chat.md` chat 2; varied→Other proposal from `chat.md` chat 2; divorced-key duplication artefact from `chat.md` chat 2.

End of reference document.
