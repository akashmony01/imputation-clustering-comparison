# Capstone Project Memory

## Project Overview
- **Topic**: Discovering suicide patterns from incomplete newspaper-reported data in Bangladesh using imputation + clustering pipelines
- **University**: BUBT (Bangladesh University of Business and Technology), Dept. of CSE
- **Dataset**: 1,617 suicide cases, 36 columns, scraped from Bangladeshi news
- **Pipeline**: 12 Colab notebooks (0-11), preprocessing → imputation → clustering → evaluation
- **Combinations**: 3 imputation methods × 2 predictor strategies × 4 clustering algorithms + 2 baselines = 32 pipelines
- **Best result**: agg_rf_no_context (Agglomerative + MissForest, no context) = score 27.30

## Report Structure
- Format: BUBT CSE capstone report (6 chapters + front/back matter)
- File: `my_report/newly formated capstone report 2025.docx`
- Ch 1 (Intro): structurally complete, rough draft
- Ch 2 (Lit Review): structurally complete, rough draft
- Ch 3 (Methodology): COMPLETE, detailed (~5500 words)
- Ch 4 (Results): COMPLETE, thorough (~5000 words)
- Ch 5 (Standards/Constraints): very thin (~800 words), needs expansion
- Ch 6 (Conclusion): present but has factual errors and informal tone
- **Missing front matter**: abstract, title page, declaration, approval, dedication, acknowledgment, ToC, list of figures/tables, abbreviations

## Known Issues
- Only 11 references listed but many more cited in text
- Factual discrepancy in Ch 6 (says "six clusters, 27.65" but Ch 4 shows 2 clusters, 27.30)
- Informal closing "Thank you. That concludes the entire thesis!"
- Spelling: "missForrest" inconsistent, "Supplimetary" misspelled
- Figure 4.6.2(b) caption wrong (says "age" should be "feels_like")
- Figure 4.4.1.6 caption wrong (says "Davies-Bouldin" should be "Xie-Beni")
- Stray blank in Ch 1: "highly fragmented,  , and inconsistent"

## Key Files
- `super_pdf.pdf`: PDF of last notebook run (full pipeline reference)
- `datasets/`: intermediate and final datasets by step and clustering algorithm
- `report_format/report_format.docx`: expected format template
- `example_report/`: 2 example PDFs of past capstone reports
