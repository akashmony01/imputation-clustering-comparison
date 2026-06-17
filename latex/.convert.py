"""Convert structured docx (paras + images + tables) to per-chapter .tex files."""
import json, os, re

with open('latex/.docx_extract2.json') as f:
    items = json.load(f)

# Load crop map (image, l,t,r,b) -> cropped filename
crop_map = {}
if os.path.exists('latex/.crop_map.json'):
    with open('latex/.crop_map.json') as f:
        raw = json.load(f)
    for k, v in raw.items():
        parts = k.split('|')
        crop_map[(parts[0], int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]))] = v

# ---------- Text fixes ----------
def fix_text(t):
    if not t:
        return t
    t = t.replace('missForrest', 'MissForest')
    t = t.replace('Supplimetary', 'Supplementary')
    t = re.sub(r'\bteh\b', 'the', t)
    t = t.replace('‘', "`").replace('’', "'")
    t = t.replace('“', '``').replace('”', "''")
    t = t.replace('–', '--').replace('—', '---')
    t = t.replace(' ', ' ')
    # Replace common Unicode math/symbol chars with LaTeX equivalents
    sym_map = {
        '×': r'$\times$', '±': r'$\pm$',
        '≤': r'$\leq$', '≥': r'$\geq$',
        '≠': r'$\neq$', '≈': r'$\approx$',
        '∞': r'$\infty$', '∑': r'$\sum$', '∏': r'$\prod$',
        '∈': r'$\in$', '∉': r'$\notin$', '∀': r'$\forall$', '∃': r'$\exists$',
        '∩': r'$\cap$', '∪': r'$\cup$',
        '→': r'$\to$', '←': r'$\leftarrow$', '↔': r'$\leftrightarrow$',
        '⇒': r'$\Rightarrow$', '⇐': r'$\Leftarrow$',
        '√': r'$\sqrt{\,}$', '∝': r'$\propto$', '∂': r'$\partial$',
        '·': r'$\cdot$', '∘': r'$\circ$',
        'α': r'$\alpha$', 'β': r'$\beta$', 'γ': r'$\gamma$', 'δ': r'$\delta$',
        'ε': r'$\varepsilon$', 'θ': r'$\theta$', 'λ': r'$\lambda$',
        'μ': r'$\mu$', 'π': r'$\pi$', 'σ': r'$\sigma$', 'τ': r'$\tau$',
        'φ': r'$\varphi$', 'ω': r'$\omega$', 'Δ': r'$\Delta$', 'Σ': r'$\Sigma$',
        '°': r'$^{\circ}$',
    }
    for src_ch, repl in sym_map.items():
        t = t.replace(src_ch, repl)
    # Strip zero-width / bidi / other invisible chars
    for ch in ('​','‌','‍','‎','‏','‪','‫','‬','‭','‮','﻿'):
        t = t.replace(ch, '')
    t = re.sub(r',\s*,', ',', t)
    return t

def latex_escape(t):
    """Escape LaTeX-special chars BUT preserve already-inserted math snippets like $\times$."""
    if not t:
        return t
    # Protect existing math segments
    placeholders = {}
    def stash(m):
        key = f'\x00MATH{len(placeholders)}\x00'
        placeholders[key] = m.group(0)
        return key
    t = re.sub(r'\$[^$]*\$', stash, t)

    t = t.replace('\\', r'\textbackslash{}')
    t = t.replace('&', r'\&')
    t = t.replace('%', r'\%')
    t = t.replace('$', r'\$')
    t = t.replace('#', r'\#')
    t = t.replace('_', r'\_')
    t = t.replace('{', r'\{')
    t = t.replace('}', r'\}')
    t = t.replace('~', r'\textasciitilde{}')
    t = t.replace('^', r'\textasciicircum{}')

    for key, val in placeholders.items():
        t = t.replace(key, val)
    return t

SECTION_RE = re.compile(r'^(\d+)\.(\d+)(?:\.(\d+))?(?:\.(\d+))?\s+([A-Za-z].*)$')

def parse_heading(text):
    m = SECTION_RE.match(text.strip())
    if not m:
        return None, None
    chnum = int(m.group(1))
    if chnum > 9:
        return None, None
    nums = [m.group(i) for i in range(1, 5) if m.group(i) is not None]
    title = m.group(5).strip()
    level = len(nums) - 1
    return level, title

# ---------- Find chapter boundaries (in items array) ----------
chapters = []
for i, it in enumerate(items):
    if it['kind'] != 'p':
        continue
    txt = it['text'].strip()
    if it['style'] == 'Heading1' and txt.lower().startswith('chapter '):
        m = re.match(r'chapter\s+(\d+)', txt, re.I)
        cnum = int(m.group(1)) if m else None
        # Find next H2 for title
        title = ''
        for j in range(i+1, min(i+5, len(items))):
            if items[j]['kind']=='p' and items[j]['style']=='Heading2' and items[j]['text'].strip():
                title = items[j]['text'].strip()
                start = j + 1
                break
        else:
            start = i + 1
        chapters.append({'num':cnum, 'title':title, 'start':start})

# Set ends
for k in range(len(chapters)-1):
    chapters[k]['end'] = next(
        i for i in range(chapters[k]['start'], chapters[k+1]['start'])
        if items[i]['kind']=='p' and items[i]['style']=='Heading1'
        and items[i]['text'].strip().lower().startswith('chapter ')
    )

# Find references / appendix in last chapter
last = chapters[-1]
last['end'] = len(items)
ref_idx = appendix_idx = None
for i in range(last['start'], len(items)):
    if items[i]['kind'] != 'p':
        continue
    txt = items[i]['text'].strip().lower().rstrip(':')
    if txt == 'references' and ref_idx is None:
        ref_idx = i
    if (txt.startswith('appendix') or 'supplementary' in txt) and appendix_idx is None and i > (ref_idx or 0):
        appendix_idx = i
if ref_idx:
    last['end'] = ref_idx

print('Chapters:')
for c in chapters:
    print(f"  Ch{c['num']} [{c['start']}..{c['end']}] {c['title']}")
print(f'References at item {ref_idx}, appendix at {appendix_idx}')

# ---------- Caption fixes (run on RAW caption text including "(b)" markers) ----------
def fix_raw_caption(raw):
    """Apply known caption corrections based on (b) markers — must run BEFORE prefix-strip."""
    rl = raw.lower()
    # 4.6.2(b) — original wrongly says "age", should be "feels_like"
    if '(b)' in rl and 'comparing age for two clusters' in rl:
        return raw.replace('Comparing age for two clusters', 'Comparing feels_like for two clusters')
    # 4.6.3(b) — original wrongly says "reason", should be "workplace"
    if '(b)' in rl and 'comparing reason for two clusters' in rl:
        return raw.replace('Comparing reason for two clusters', 'Comparing workplace for two clusters')
    # 4.4.1.6 — Davies-Bouldin caption mistakenly used; should be Xie-Beni
    if '4.4.1.6' in rl and 'davies' in rl:
        return re.sub(r'davies[–\-]+bouldin', 'Xie--Beni', raw, flags=re.I)
    return raw

def fix_caption(cap):  # left for compatibility, no-op
    return cap

# ---------- Render table ----------
def compute_col_weights(rows, ncols):
    """Compute relative column widths from content length."""
    import math
    # Per-column avg length of cells (skip empty)
    col_max = [1] * ncols
    col_avg = [1] * ncols
    for ci in range(ncols):
        lens = []
        for r in rows:
            cell = (r[ci] if ci < len(r) else '') or ''
            cell = cell.replace('\n', ' ')
            if cell.strip():
                lens.append(len(cell))
        if lens:
            col_max[ci] = max(lens)
            col_avg[ci] = sum(lens) / len(lens)
    # Weight = sqrt(0.5*max + 0.5*avg) to dampen extremes
    raw = [math.sqrt(0.5*col_max[i] + 0.5*col_avg[i]) for i in range(ncols)]
    total = sum(raw)
    # Normalize to ncols; clamp each weight to [0.4, 3.0]
    weights = [max(0.4, min(3.0, w / total * ncols)) for w in raw]
    # Re-normalize after clamp so they sum to ncols
    s = sum(weights)
    weights = [w / s * ncols for w in weights]
    return weights

def render_table_fixed(tbl):
    """Render plain tabular with NATURAL widths — to be wrapped in \\resizebox.
    \\resizebox auto-scales to \\linewidth so we don't constrain widths here."""
    rows = tbl['rows']
    if not rows:
        return ''
    ncols = max(len(r) for r in rows)
    rows = [r + ['']*(ncols-len(r)) for r in rows]

    # Detect mostly-numeric columns → center; text → left
    def is_num_col(ci):
        n = total = 0
        for r in rows[1:]:
            cell = (r[ci] if ci < len(r) else '').strip()
            if not cell:
                continue
            total += 1
            if re.match(r'^-?[\d,.\s%]+$', cell.replace('\n','')):
                n += 1
        return total > 0 and n / total > 0.7

    cols = []
    for ci in range(ncols):
        cols.append('c' if is_num_col(ci) else 'l')
    colspec = '|' + '|'.join(cols) + '|'

    out = [f'\\begin{{tabular}}{{{colspec}}}', '\\hline']
    for ri, row in enumerate(rows):
        cells = []
        for c in row:
            c = fix_text(c).replace('\n', ' ').strip()
            cells.append(latex_escape(c))
        if ri == 0:
            cells = [f'\\textbf{{{c}}}' for c in cells]
        out.append(' & '.join(cells) + ' \\\\ \\hline')
    out.append('\\end{tabular}')
    return '\n'.join(out)

def render_table(tbl):
    rows = tbl['rows']
    if not rows:
        return ''
    ncols = max(len(r) for r in rows)
    rows = [r + ['']*(ncols-len(r)) for r in rows]
    nrows = len(rows)

    weights = compute_col_weights(rows, ncols)

    # tabularx col spec — variable widths via \hsize
    just = '>{\\raggedright\\arraybackslash\\hangindent=0pt}'
    cols = []
    for w in weights:
        cols.append(f'>{{\\hsize={w:.3f}\\hsize\\linewidth=\\hsize\\raggedright\\arraybackslash}}X')
    colspec = '|' + '|'.join(cols) + '|'

    # Pick font size based on table dimensions
    font_size = ''
    if ncols >= 8 or nrows >= 25:
        font_size = '\\scriptsize'
    elif ncols >= 6 or nrows >= 15:
        font_size = '\\footnotesize'
    elif ncols >= 4:
        font_size = '\\small'

    out = []
    if font_size:
        out.append(font_size)
    out.append(f'\\begin{{tabularx}}{{\\textwidth}}{{{colspec}}}')
    out.append('\\hline')
    for ri, row in enumerate(rows):
        cells = []
        for c in row:
            c = fix_text(c).replace('\n', ' \\newline ').strip()
            esc = latex_escape(c).replace('\\textbackslash{}newline', '\\newline')
            # Allow line breaks at \_ inside long compound words (e.g., agg\_rf\_no\_context)
            esc = re.sub(r'(\\_)(?=[A-Za-z0-9])', r'\1\\hspace{0pt}', esc)
            cells.append(esc)
        if ri == 0:
            cells = [f'\\textbf{{{c}}}' for c in cells]
        out.append(' & '.join(cells) + ' \\\\ \\hline')
    out.append('\\end{tabularx}')
    return '\n'.join(out)

def render_table_with_caption(tbl, caption_text=None):
    rows = tbl['rows']
    ncols = max(len(r) for r in rows) if rows else 0
    nrows = len(rows)
    # All tables stay in portrait; wide ones use \resizebox + small font
    is_wide = ncols >= 5 or (ncols >= 4 and nrows >= 15)
    is_long = nrows >= 20

    out = []
    out.append('\\begin{table}[H]')
    out.append('\\centering')
    out.append('\\renewcommand{\\arraystretch}{1.05}')
    # Pick font for wide / long tables
    if is_long and ncols >= 6:
        out.append('\\scriptsize')
    elif is_long or ncols >= 6:
        out.append('\\footnotesize')
    elif ncols >= 4:
        out.append('\\small')

    if is_wide:
        out.append('\\resizebox{\\textwidth}{!}{%')
        out.append(render_table_fixed(tbl))
        out.append('}')
    else:
        out.append(render_table(tbl))
    if caption_text:
        cap = fix_text(caption_text).strip()
        cap = re.sub(r'^table\s+\d+(\.\d+)*(\s*\([a-z]\))?\s*[:.\-]?\s+', '', cap, flags=re.I).strip()
        label = re.sub(r'[^a-z0-9]+','_', cap.lower())[:30].strip('_') or 'tbl'
        out.append(f'\\caption{{{latex_escape(cap)}}}')
        out.append(f'\\label{{tbl:{label}}}')
    out.append('\\end{table}')
    return '\n'.join(out)

# ---------- Render figure ----------
def render_figure(image_filename, caption_text, src_rect=None):
    # Map cropped instance via srcRect lookup
    if src_rect and any(src_rect.get(k,0) for k in ('l','t','r','b')):
        key = (image_filename, src_rect['l'], src_rect['t'], src_rect['r'], src_rect['b'])
        if key in crop_map:
            image_filename = crop_map[key]
    raw = caption_text or ''
    raw = fix_raw_caption(raw)  # fix BEFORE prefix strip so "(b)" still detectable
    cap = fix_text(raw).strip()
    # Strip "Figure N.N.N(b):" / "Figure 1:" / "Figure 4.2.3.2 " prefix — keep descriptive text
    cap = re.sub(r'^(figure|fig\.?)\s+\d+(\.\d+)*(\s*\([a-z]\))?\s*[:.\-]?\s+', '', cap, flags=re.I).strip()
    label = re.sub(r'[^a-z0-9]+','_', cap.lower())[:30].strip('_') or 'fig'
    out = ['\\begin{figure}[htbp]', '  \\centering',
           f'  \\includegraphics[width=0.85\\textwidth,keepaspectratio]{{{image_filename}}}',
           f'  \\caption{{{latex_escape(cap)}}}',
           f'  \\label{{fig:{label}}}',
           '\\end{figure}']
    return '\n'.join(out)

# ---------- Render chapter ----------
def render_chapter(ch):
    out = [f"% Chapter {ch['num']}: {ch['title']}", f"\\chapter{{{ch['title']}}}", '']
    i = ch['start']
    while i < ch['end']:
        it = items[i]
        if it['kind'] == 'table':
            # Look BACK or FORWARD for "Table N: ..." caption — usually right before or right after
            caption = None
            # Check next 2 paragraphs for caption
            for j in range(i+1, min(i+3, ch['end'])):
                if items[j]['kind'] != 'p':
                    continue
                t = items[j]['text'].strip()
                if re.match(r'^table[\s:]*\d', t, re.I):
                    caption = t
                    break
            # Check 2 paragraphs back
            if not caption:
                for j in range(i-1, max(i-3, ch['start']-1), -1):
                    if items[j]['kind'] != 'p':
                        continue
                    t = items[j]['text'].strip()
                    if re.match(r'^table[\s:]*\d', t, re.I):
                        caption = t
                        break
            out.append(render_table_with_caption(it, caption))
            out.append('')
            # Skip caption paragraph if found ahead
            if caption:
                for j in range(i+1, min(i+3, ch['end'])):
                    if items[j]['kind']=='p' and items[j]['text'].strip() == caption.strip():
                        i = j + 1
                        break
                else:
                    i += 1
            else:
                i += 1
            continue

        # Paragraph
        txt = fix_text(it['text']).strip()
        style = it['style']

        if it.get('image'):
            # Caption resolution priority:
            #  1) Paragraph IMMEDIATELY before image starting with "Figure N:" → real caption
            #  2) Paragraph IMMEDIATELY after image starting with "Figure N:" → real caption
            #  3) Most recent section heading before image → use heading as caption
            FIG_PREFIX = re.compile(r'^(figure|fig\.?|table)\s*[\dsS]', re.I)
            caption = ''
            skip_to = i + 1
            # 1) check before
            for j in range(i-1, max(i-4, ch['start']-1), -1):
                if items[j]['kind']!='p':
                    continue
                t = items[j]['text'].strip()
                if not t:
                    continue
                if FIG_PREFIX.match(t):
                    caption = t
                    # mark the index to skip rendering this caption again as body
                    # (we already pre-emptively skip Table-prefixed paras; we'll do same for Figure)
                break
            # 2) check after
            if not caption:
                for j in range(i+1, min(i+4, ch['end'])):
                    if items[j]['kind']!='p':
                        continue
                    t = items[j]['text'].strip()
                    if not t:
                        continue
                    if FIG_PREFIX.match(t):
                        caption = t
                        skip_to = j + 1
                    break
            # 3) walk back to nearest heading
            if not caption:
                for j in range(i-1, max(i-15, ch['start']-1), -1):
                    if items[j]['kind']!='p':
                        continue
                    t = items[j]['text'].strip()
                    if not t:
                        continue
                    style = items[j]['style']
                    is_heading = (
                        style in ('Heading2','Heading3','Heading4') or
                        SECTION_RE.match(t) or
                        (len(t) < 60 and not t.endswith('.') and not t.endswith(','))
                    )
                    if is_heading:
                        m = SECTION_RE.match(t)
                        caption = m.group(5).strip() if m else t.rstrip(':')
                        break
            out.append(render_figure(it['image'], caption, it.get('srcRect')))
            out.append('')
            i = skip_to
            continue

        if not txt:
            i += 1
            continue

        # Skip "Table N: ..." or "Figure N: ..." caption lines — already rendered with float
        if re.match(r'^(table|figure|fig\.?)[\s:]*\d', txt, re.I) and len(txt) < 300:
            i += 1
            continue

        # Heading detection
        is_word_heading = style in ('Heading2','Heading3','Heading4')
        looks_numbered = SECTION_RE.match(txt) and len(txt) < 100 and not txt.endswith('.')
        if is_word_heading or looks_numbered:
            level, title = parse_heading(txt)
            if level is not None:
                cmd = {1:'section',2:'subsection',3:'subsubsection',4:'paragraph'}[level]
                out.append(f'\\{cmd}{{{latex_escape(title)}}}')
                out.append('')
                i += 1
                continue
            elif is_word_heading and txt and len(txt) < 80 and not txt.endswith('.'):
                out.append(f'\\subsubsection*{{{latex_escape(txt)}}}')
                out.append('')
                i += 1
                continue

        out.append(latex_escape(txt))
        out.append('')
        i += 1
    return '\n'.join(out)

filenames = {1:'ch1_introduction',2:'ch2_literature',3:'ch3_methodology',
             4:'ch4_results',5:'ch5_standards',6:'ch6_conclusion'}
os.makedirs('latex/chapters', exist_ok=True)
for ch in chapters:
    fn = filenames.get(ch['num'], f"ch{ch['num']}")
    out_path = f'latex/chapters/{fn}.tex'
    content = render_chapter(ch)
    with open(out_path, 'w') as f:
        f.write(content + '\n')
    print(f'Wrote {out_path}')

# ---------- Appendix (with the big Table S1) ----------
if appendix_idx is not None:
    out = ['% Appendix','\\appendix','\\chapter{Supplementary Materials}','']
    i = appendix_idx
    while i < len(items):
        it = items[i]
        if it['kind'] == 'table':
            out.append(render_table_with_caption(it, 'Full per-case results across all 32 pipelines'))
            out.append('')
            i += 1
            continue
        if it['kind'] == 'p':
            txt = fix_text(it['text']).strip()
            if it.get('image'):
                caption = ''
                for j in range(i+1, min(i+4, len(items))):
                    if items[j]['kind']=='p' and items[j]['text'].strip():
                        caption = items[j]['text'].strip()
                        break
                out.append(render_figure(it['image'], caption, it.get('srcRect')))
                out.append('')
                i += 2 if caption else 1
                continue
            if not txt:
                i += 1
                continue
            if re.match(r'^(supplementary\s+)?(figure|table)\s+s?\d', txt, re.I):
                # caption already rendered with float
                i += 1
                continue
            if it['style'].startswith('Heading') or len(txt)<60:
                out.append(f'\\section*{{{latex_escape(txt)}}}')
            else:
                out.append(latex_escape(txt))
            out.append('')
        i += 1
    with open('latex/chapters/appendix.tex','w') as f:
        f.write('\n'.join(out)+'\n')
    print('Wrote latex/chapters/appendix.tex')

# ---------- references.bib ----------
if ref_idx is not None:
    refs = []
    end = appendix_idx or len(items)
    for i in range(ref_idx+1, end):
        if items[i]['kind']!='p':
            continue
        t = fix_text(items[i]['text']).strip()
        if t:
            refs.append(t)
    with open('latex/references.bib','w') as f:
        f.write('% Auto-extracted refs as @misc placeholders. Convert to proper @article/@inproceedings later.\n\n')
        for k, raw in enumerate(refs, 1):
            clean = re.sub(r'^\[\d+\]\s*', '', raw).strip()
            esc = clean.replace('{','').replace('}','').replace('&','\\&')
            f.write(f'@misc{{ref{k},\n  note = {{{esc}}}\n}}\n\n')
    print(f'Wrote {len(refs)} refs to references.bib')

    # Also write a thebibliography .tex (bypasses bibtex — works everywhere)
    with open('latex/references.tex','w') as f:
        f.write('% Auto-generated thebibliography — used directly by main.tex (no bibtex required)\n')
        f.write('{\\raggedright\n')  # ragged right kills underfull-hbox in refs
        f.write('\\begin{thebibliography}{99}\n')
        f.write('\\setlength{\\itemsep}{4pt}\n')
        for k, raw in enumerate(refs, 1):
            clean = re.sub(r'^\[\d+\]\s*', '', raw).strip()
            f.write(f'\\bibitem{{ref{k}}} {latex_escape(clean)}\n\n')
        f.write('\\end{thebibliography}\n')
        f.write('}\n')
    print(f'Wrote {len(refs)} bibitems to references.tex')

print('Done.')
