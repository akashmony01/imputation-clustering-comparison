# BUBT CSE Capstone — LaTeX Project

This directory contains the LaTeX port of `my_report/my_report_so_far.docx`,
scaffolded against the formatting of `example_report/report_example_2.pdf` and
`report_format/report_format.docx`.

## Project layout

```
latex/
├── main.tex                     # Top-level document — compile this
├── preamble.tex                 # Packages, page setup, heading styles
├── references.bib               # 42 references (extracted, need cleanup — see below)
├── chapters/
│   ├── ch1_introduction.tex
│   ├── ch2_literature.tex
│   ├── ch3_methodology.tex
│   ├── ch4_results.tex
│   ├── ch5_standards.tex
│   ├── ch6_conclusion.tex
│   └── appendix.tex
├── frontmatter/
│   ├── titlepage.tex
│   ├── declaration.tex
│   ├── approval.tex
│   ├── dedication.tex
│   ├── acknowledgment.tex
│   ├── abstract.tex
│   └── abbreviations.tex
├── figures/                     # 37 PNGs (17 from docx + 23 from images/)
└── assets/                      # place bubt_logo.png here
```

## How to compile

### Option A: Tectonic (recommended, lightweight)
```bash
sudo apt install tectonic
cd latex
tectonic main.tex
```

Tectonic auto-fetches needed packages on first run.

### Option B: TeX Live (full)
```bash
sudo apt install texlive-full biber
cd latex
pdflatex main && biber main && pdflatex main && pdflatex main
```

### Option C: Overleaf
Upload the entire `latex/` directory as a project, set the main document to
`main.tex`, set the compiler to **pdfLaTeX** with **Biber** for biblatex.

## What still needs your input

Search the `.tex` files for `<...>` placeholders. They mark every spot that
needs your real info before final compile:

| File | Placeholders |
|---|---|
| `frontmatter/titlepage.tex` | 5 student names + IDs, submission month/year |
| `frontmatter/declaration.tex` | Same student names + IDs |
| `frontmatter/approval.tex` | Supervisor name, designation; Chairman name, designation |
| `frontmatter/acknowledgment.tex` | Supervisor name + designation |
| `assets/bubt_logo.png` | Place the BUBT logo image here (extract from any official source) |

Quick sanity check from the shell:

```bash
grep -nR "<.*>" frontmatter/ chapters/
```

## Known TODOs in the converted content

These were flagged during the docx → LaTeX conversion. Search the chapters
for `% TODO` or `FIGURE PLACEHOLDER` to find them:

1. **Figure floats are placeholders.** Each `\begin{figure}` block has a
   `FIGURE PLACEHOLDER` framed box instead of `\includegraphics`. You need
   to replace each with the correct image filename from `figures/`. The
   docx had ~30 figure captions but only 17 embedded images (the rest were
   linked from `images/`). All of them are now in `figures/`.

2. **Appendix table (Table S1).** The 32-case full results table got
   flattened into a long list of paragraphs in `chapters/appendix.tex`.
   You'll want to rebuild it as a proper `\begin{tabular}` block.

3. **References.bib uses `@misc` placeholders.** All 42 entries were
   imported with raw text in the `note` field. To get proper IEEE
   formatting, convert each to `@article`, `@inproceedings`, `@book`,
   `@online`, etc. with `author`, `title`, `journal`, `year`, etc. fields.
   Alternatively, switch the bib style in `preamble.tex` from
   `style=ieee` to a numeric style that just prints the `note` field.

4. **Inline citations still use `[1]`, `[12, 13]` raw text.** These were
   preserved as-is from the docx. To get proper biblatex cross-referencing,
   replace each with `\cite{ref1}`, `\cite{ref12,ref13}`, etc. (the bib
   keys are `ref1` through `ref42`, in the same order as the docx
   reference list).

5. **Tables in Ch2/Ch3/Ch4/Ch5.** The docx had 13 table captions; the
   converter didn't reconstruct the table grids. Each table's content
   appears as a paragraph block — you'll need to wrap them in proper
   `tabular` environments. See chapters for `Table N:` markers.

## Fixes already applied during conversion

- `missForrest` → `MissForest` (8 occurrences fixed)
- `Supplimetary` → `Supplementary` (1 occurrence fixed)
- `teh` → `the` (1 typo fixed)
- Stray `,  ,` removed from Ch 1
- Smart quotes → straight quotes
- En-dashes → `--`, em-dashes → `---`
- Figure 4.6.2(b) caption: "age" → "feels\_like"
- Figure 4.6.3(b) caption: "reason" → "workplace"
- Figure 4.4.1.6 caption: "Davies-Bouldin" → "Xie-Beni"
- Heading hierarchy normalised: chapter / section / subsection / subsubsection
- Wrong Heading4-styled mid-paragraph sentences in Ch3 demoted to body text

## Next steps (in order)

1. Replace `<...>` placeholders in the 5 frontmatter files
2. Drop `bubt_logo.png` into `assets/`
3. Install Tectonic and run a first compile to see any LaTeX errors
4. Map the figure placeholders to real `figures/*.png` files (Ch3-Ch6)
5. Rebuild Table S1 in the appendix and the body-chapter tables
6. Convert `references.bib` from `@misc{note=...}` to proper structured entries
7. Replace inline `[N]` citation strings with `\cite{refN}`
# imputation-clustering-comparison
