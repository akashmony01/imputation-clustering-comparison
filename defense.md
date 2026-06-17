---
marp: true
theme: default
paginate: false
backgroundColor: '#1A1A1F'
color: '#EAEAEA'
transition: fade
style: |
  @import url('https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400&display=swap');

  section {
    background: #1A1A1F;
    background-image:
      radial-gradient(circle at 1px 1px, rgba(255,255,255,0.025) 1px, transparent 0);
    background-size: 32px 32px;
    color: #EAEAEA;
    font-family: 'Inter', sans-serif;
    padding: 64px 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-size: 30px;
    line-height: 1.4;
    position: relative;
    overflow: hidden;
  }

  /* Decorative corner brackets on every slide */
  section::before, section::after {
    content: '';
    position: absolute;
    width: 36px;
    height: 36px;
    pointer-events: none;
  }
  section::before {
    top: 24px; left: 24px;
    border-top: 2px solid #5EEAD4;
    border-left: 2px solid #5EEAD4;
    opacity: 0.35;
  }
  section::after {
    bottom: 24px; right: 24px;
    border-bottom: 2px solid #5EEAD4;
    border-right: 2px solid #5EEAD4;
    opacity: 0.35;
  }

  section.left { align-items: flex-start; text-align: left; }

  /* Side accent line for left-aligned content slides */
  section.left .side-line {
    position: absolute;
    left: 60px;
    top: 50%;
    transform: translateY(-50%);
    width: 3px;
    height: 140px;
    background: linear-gradient(to bottom, transparent, #5EEAD4 30%, #5EEAD4 70%, transparent);
    opacity: 0.55;
  }

  h1, h2, h3 {
    font-family: 'Anton', 'Bebas Neue', sans-serif;
    font-weight: 400;
    letter-spacing: 0.5px;
    margin: 0;
    line-height: 1.05;
  }
  h1 { font-size: 82px; }
  h2 { font-size: 60px; }
  h3 { font-size: 42px; color: #5EEAD4; }
  p  { margin: 12px 0; }
  strong { font-weight: 800; }

  .huge   { font-family: 'Anton', sans-serif; font-size: 260px; font-weight: 900; line-height: 1; margin: 0; }
  .large  { font-family: 'Anton', sans-serif; font-size: 190px; font-weight: 900; line-height: 1; margin: 0; }
  .medium { font-family: 'Anton', sans-serif; font-size: 130px; font-weight: 900; line-height: 1; margin: 0; }

  .cyan  { color: #5EEAD4; }
  .green { color: #34D399; }
  .amber { color: #FBBF24; }
  .red   { color: #F87171; }
  .muted { color: #8A8A8F; font-size: 22px; }
  .source {
    color: #6A6A70; font-size: 16px; letter-spacing: 1.5px;
    text-transform: uppercase; margin-top: 16px;
  }

  .label {
    color: #5EEAD4; font-size: 20px;
    letter-spacing: 4px; text-transform: uppercase;
    margin-bottom: 28px;
  }

  .caption { color: #8A8A8F; font-size: 24px; margin-top: 18px; }
  .statement { font-size: 54px; line-height: 1.25; font-weight: 600; }
  .small-statement { font-size: 42px; line-height: 1.3; }

  /* === Title slide === */
  section.title-slide {
    padding: 80px;
    background-image:
      radial-gradient(circle at 1px 1px, rgba(255,255,255,0.025) 1px, transparent 0),
      radial-gradient(ellipse at center, rgba(94,234,212,0.04), transparent 60%);
    background-size: 32px 32px, cover;
  }
  .title-stack {
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    max-width: 1100px;
  }
  .bubt-logo { width: 80px; height: 80px; margin-bottom: 28px; opacity: 0.92; }
  .title-motif { margin-bottom: 28px; }
  section.title-slide h1 {
    font-size: 52px; font-family: 'Anton', sans-serif;
    line-height: 1.1; margin: 0 0 24px 0;
  }
  section.title-slide .subtitle {
    color: #8A8A8F; font-size: 24px; margin-bottom: 56px; max-width: 900px;
  }
  section.title-slide .footer { color: #6A6A70; font-size: 18px; letter-spacing: 1.5px; }

  /* === Team grid === */
  .team-grid {
    display: flex; justify-content: center; gap: 40px; margin-top: 36px;
    flex-wrap: wrap;
  }
  .team-member { display: flex; flex-direction: column; align-items: center; text-align: center; }
  .team-photo {
    width: 150px; height: 150px; border-radius: 50%;
    background: #2A2A30; border: 2px dashed #3A3A40;
    display: flex; align-items: center; justify-content: center;
    color: #5A5A60; font-size: 12px; margin-bottom: 16px;
  }
  .team-member-name { font-family: 'Anton', sans-serif; font-size: 26px; color: #EAEAEA; line-height: 1; margin-bottom: 4px; }
  .team-member-role { color: #8A8A8F; font-size: 14px; max-width: 170px; line-height: 1.35; }

  /* === Outline === */
  .outline { display: flex; flex-direction: column; gap: 14px; align-items: flex-start; margin-top: 18px; }
  .outline-item { display: flex; align-items: baseline; gap: 28px; font-size: 32px; }
  .outline-number {
    font-family: 'Anton', sans-serif; font-size: 48px;
    color: #5EEAD4; line-height: 1; min-width: 72px;
  }
  .outline-text { color: #EAEAEA; }

  /* === Section divider === */
  .section-divider-num {
    font-family: 'Anton', sans-serif; font-size: 26px;
    color: #5EEAD4; letter-spacing: 12px; margin-bottom: 18px;
  }
  .section-divider-title { font-family: 'Anton', sans-serif; font-size: 120px; line-height: 1; color: #EAEAEA; }
  .section-divider-rule { width: 180px; border: none; border-top: 2px solid #3A3A40; margin-top: 36px; }
  .section-divider-dots { display: flex; gap: 10px; margin-top: 28px; }
  .section-divider-dots span { width: 6px; height: 6px; border-radius: 50%; background: #5EEAD4; opacity: 0.4; }

  /* === Matrix (3×2×4 = 32) === */
  .matrix {
    display: grid; grid-template-columns: repeat(8, 34px);
    gap: 6px; margin: 32px auto;
  }
  .matrix-cell {
    width: 34px; height: 34px;
    background: rgba(94, 234, 212, 0.15);
    border: 1.5px solid #5EEAD4; border-radius: 4px;
  }
  .matrix-cell.baseline { background: rgba(251, 191, 36, 0.15); border-color: #FBBF24; }
  .matrix-legend { display: flex; gap: 28px; justify-content: center; font-size: 16px; color: #8A8A8F; margin-top: 12px; }
  .matrix-legend .swatch { display: inline-block; width: 12px; height: 12px; border-radius: 3px; margin-right: 6px; vertical-align: middle; }

  /* === Composite score bars === */
  .composite-bar { display: flex; flex-direction: column; gap: 10px; width: 78%; margin: 28px auto; }
  .composite-row { display: flex; align-items: center; gap: 14px; }
  .composite-label { font-size: 20px; min-width: 220px; text-align: right; color: #EAEAEA; }
  .composite-track { flex: 1; height: 20px; background: #2A2A30; border-radius: 4px; overflow: hidden; }
  .composite-fill { height: 100%; background: #5EEAD4; }
  .composite-percent { font-family: 'Anton', sans-serif; font-size: 24px; color: #5EEAD4; min-width: 56px; text-align: left; }

  /* === Cluster bubbles === */
  .cluster-bubbles { display: flex; justify-content: center; align-items: center; gap: 80px; margin: 36px 0; }
  .cluster-bubble {
    border-radius: 50%;
    background: rgba(94, 234, 212, 0.08);
    border: 2px solid #5EEAD4;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    font-family: 'Anton', sans-serif; color: #EAEAEA;
  }
  .cluster-bubble.c0 { width: 240px; height: 240px; }
  .cluster-bubble.c1 { width: 270px; height: 270px; }
  .cluster-bubble .bubble-num { font-size: 76px; line-height: 1; }
  .cluster-bubble .bubble-label { font-family: 'Inter', sans-serif; font-size: 16px; color: #8A8A8F; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 8px; }

  /* === Missingness bar === */
  .missing-bar { width: 70%; height: 28px; background: #2A2A30; border-radius: 4px; margin: 28px auto 8px; position: relative; overflow: hidden; }
  .missing-fill { position: absolute; left: 50%; top: 0; height: 100%; width: 40%; background: linear-gradient(90deg, #5EEAD4, #FBBF24); border-radius: 4px; }
  .missing-scale { display: flex; justify-content: space-between; width: 70%; margin: 0 auto; font-size: 14px; color: #8A8A8F; }

  hr.divider { width: 80px; border: none; border-top: 1px solid #3A3A40; margin: 28px 0; }

  /* === Abstract motifs === */
  .motif-dots { display: flex; gap: 12px; justify-content: center; margin-bottom: 28px; }
  .motif-dot { width: 9px; height: 9px; border-radius: 50%; background: #5EEAD4; opacity: 0.8; }
  .motif-dot.missing { background: transparent; border: 1.5px dashed #5A5A60; }

  /* === Comparison table === */
  .compare-table {
    width: 85%; margin: 32px auto; border-collapse: collapse;
    font-size: 22px;
  }
  .compare-table th {
    text-align: left; padding: 14px 18px; font-family: 'Anton', sans-serif;
    color: #5EEAD4; font-size: 18px; letter-spacing: 2px; text-transform: uppercase;
    border-bottom: 2px solid #3A3A40;
  }
  .compare-table td {
    padding: 14px 18px; color: #EAEAEA;
    border-bottom: 1px solid #2A2A30;
  }
  .compare-table td.feat { color: #8A8A8F; font-size: 18px; }
  .compare-table .c0 { color: #5EEAD4; }
  .compare-table .c1 { color: #34D399; }

  /* === Literature card === */
  .lit-card {
    border: 1px solid #2A2A30;
    border-left: 3px solid #5EEAD4;
    padding: 20px 26px;
    margin: 14px 0;
    background: rgba(255,255,255,0.015);
    width: 80%;
  }
  .lit-card .lit-author { font-family: 'Anton', sans-serif; font-size: 28px; color: #EAEAEA; }
  .lit-card .lit-year { color: #5EEAD4; font-size: 18px; margin-left: 12px; }
  .lit-card .lit-title { font-size: 18px; color: #8A8A8F; margin-top: 4px; max-width: 760px; }
  .lit-card .lit-finding { font-size: 20px; color: #EAEAEA; margin-top: 10px; }

  /* === Inline images === */
  .figure-frame {
    background: #FFFFFF;
    border: 1px solid #3A3A40;
    padding: 14px;
    border-radius: 6px;
    margin: 20px auto;
    max-width: 90%;
  }
  .figure-frame img { display: block; max-width: 100%; height: auto; }
  .figure-caption { font-size: 18px; color: #8A8A8F; margin-top: 12px; text-align: center; }

  /* === Animations === */
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes scaleIn {
    from { opacity: 0; transform: scale(0.78); }
    to   { opacity: 1; transform: scale(1); }
  }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
  @keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-24px); }
    to   { opacity: 1; transform: translateX(0); }
  }

  section > * { animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) both; }
  section > *:nth-child(1) { animation-delay: 0.05s; }
  section > *:nth-child(2) { animation-delay: 0.20s; }
  section > *:nth-child(3) { animation-delay: 0.35s; }
  section > *:nth-child(4) { animation-delay: 0.50s; }
  section > *:nth-child(5) { animation-delay: 0.65s; }
  section > *:nth-child(6) { animation-delay: 0.80s; }
  section > *:nth-child(7) { animation-delay: 0.95s; }
  section > *:nth-child(8) { animation-delay: 1.10s; }

  .huge, .large, .medium {
    animation: scaleIn 0.7s cubic-bezier(0.16, 1, 0.3, 1) both !important;
  }
  .huge.red { animation: scaleIn 1.0s cubic-bezier(0.16, 1, 0.3, 1) both !important; }
  .label { animation: fadeIn 0.4s ease-out both !important; animation-delay: 0s !important; }
  hr.divider { animation: fadeIn 0.5s ease-out both; }
  .cluster-bubble { animation: scaleIn 0.7s cubic-bezier(0.16, 1, 0.3, 1) both; }
  .side-line { animation: fadeIn 0.6s ease-out both; }
---

<!-- _class: title-slide -->

<div class="title-stack">

<img src="./images/bubt-logo.png" class="bubt-logo" alt="BUBT" />

<svg class="title-motif" width="180" height="60" viewBox="0 0 180 60">
  <circle cx="70" cy="30" r="20" fill="none" stroke="#5EEAD4" stroke-width="1.5" opacity="0.85"/>
  <circle cx="100" cy="30" r="22" fill="none" stroke="#34D399" stroke-width="1.5" opacity="0.85"/>
  <circle cx="15" cy="15" r="1.8" fill="#EAEAEA" opacity="0.55"/>
  <circle cx="30" cy="48" r="1.8" fill="#EAEAEA" opacity="0.45"/>
  <circle cx="158" cy="18" r="1.8" fill="#EAEAEA" opacity="0.55"/>
  <circle cx="168" cy="44" r="1.8" fill="#EAEAEA" opacity="0.45"/>
  <circle cx="45" cy="55" r="1.5" fill="#FBBF24" opacity="0.6"/>
  <circle cx="135" cy="8"  r="1.5" fill="#F87171" opacity="0.5"/>
</svg>

<h1>Comparing Imputation and Clustering Pipelines<br/>on Incomplete Newspaper-Reported<br/>Suicide Data from Bangladesh</h1>

<p class="subtitle">A 32-pipeline factorial benchmark with a balance-aware composite score</p>

<p class="footer">BUBT · DEPARTMENT OF CSE · CAPSTONE DEFENSE · JUNE 2026</p>

</div>

---

<h3 class="label">The Team</h3>

<div class="team-grid">
  <div class="team-member">
    <div class="team-photo">photo 1</div>
    <div class="team-member-name">[Name 1]</div>
    <div class="team-member-role">Project Lead<br/>Pipeline Architecture</div>
  </div>
  <div class="team-member">
    <div class="team-photo">photo 2</div>
    <div class="team-member-name">[Name 2]</div>
    <div class="team-member-role">Data Collection<br/>and Curation</div>
  </div>
  <div class="team-member">
    <div class="team-photo">photo 3</div>
    <div class="team-member-name">[Name 3]</div>
    <div class="team-member-role">Imputation and<br/>Clustering Pipeline</div>
  </div>
  <div class="team-member">
    <div class="team-photo">photo 4</div>
    <div class="team-member-name">[Name 4]</div>
    <div class="team-member-role">Evaluation Framework<br/>and Scoring</div>
  </div>
  <div class="team-member">
    <div class="team-photo">photo 5</div>
    <div class="team-member-name">[Name 5]</div>
    <div class="team-member-role">Documentation and<br/>Visualisation</div>
  </div>
</div>

---

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">Outline</h3>

<div class="outline">
  <div class="outline-item"><span class="outline-number">01</span><span class="outline-text">Background and the data problem</span></div>
  <div class="outline-item"><span class="outline-number">02</span><span class="outline-text">Literature review and the gap we fill</span></div>
  <div class="outline-item"><span class="outline-number">03</span><span class="outline-text">Research question and objectives</span></div>
  <div class="outline-item"><span class="outline-number">04</span><span class="outline-text">Methodology — the 32-pipeline benchmark</span></div>
  <div class="outline-item"><span class="outline-number">05</span><span class="outline-text">Results, cluster profiles, feature comparison</span></div>
  <div class="outline-item"><span class="outline-number">06</span><span class="outline-text">Honest findings, limitations, what's next</span></div>
</div>

---

<p class="section-divider-num">SECTION 01</p>

<h1 class="section-divider-title">Background</h1>

<hr class="section-divider-rule" />

<div class="section-divider-dots"><span></span><span></span><span></span><span></span><span></span></div>

---

<h1>Suicide in Bangladesh.</h1>

<p class="muted">A public-health crisis without<br/>a national surveillance system.</p>

---

<p class="huge red">40</p>

<p class="caption">suicides per day in Bangladesh</p>

<p class="source">Source · Bangladesh Police (AIG Ashraful Islam) · reported by Prothom Alo, 2025</p>

---

<p class="large">73,597</p>

<p class="caption">Bangladesh Police records, 2020 – 2024<br/>Average: <strong>14,719 per year</strong></p>

<p class="source">Source · Bangladesh Police nationwide data, 2025</p>

---

<h2 class="amber">The true figure is higher.</h2>

<hr class="divider" />

<p>Stigma. Cultural barriers. No surveillance system.</p>

<p class="source">Reasoning · WHO; Arafat et al., 2025</p>

---

<div class="motif-dots">
  <div class="motif-dot"></div>
  <div class="motif-dot missing"></div>
  <div class="motif-dot"></div>
  <div class="motif-dot missing"></div>
  <div class="motif-dot missing"></div>
  <div class="motif-dot"></div>
  <div class="motif-dot missing"></div>
</div>

<p class="statement">Newspaper reports are<br/>the only structured data we have.</p>

---

<p class="medium cyan">50–90%</p>

<p class="caption">of critical fields are missing</p>

<div class="missing-bar"><div class="missing-fill"></div></div>

<div class="missing-scale">
  <span>0%</span>
  <span>50%</span>
  <span>90%</span>
  <span>100%</span>
</div>

<p class="source">Measured directly on the curated dataset · this study</p>

---

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">What is systematically missing</h3>

<p style="font-size:32px;"><span class="cyan">·</span> Age, occupation, marital status</p>

<p style="font-size:32px;"><span class="cyan">·</span> Mental-health history</p>

<p style="font-size:32px;"><span class="cyan">·</span> Socio-economic indicators</p>

<p style="font-size:32px;"><span class="cyan">·</span> Latitude, longitude</p>

<p style="font-size:32px;"><span class="cyan">·</span> Weather and environmental context</p>

---

<h2 class="amber">Standard machine learning<br/>cannot run on data this broken.</h2>

<p class="muted" style="margin-top:32px;">Complete-case analysis discards most of the dataset.<br/>Naïve mean substitution introduces distributional bias.</p>

---

<p class="section-divider-num">SECTION 02</p>

<h1 class="section-divider-title">Literature</h1>

<hr class="section-divider-rule" />

<div class="section-divider-dots"><span></span><span></span><span></span><span></span><span></span></div>

---

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">Prior work — Bangladeshi newspaper suicide research</h3>

<div class="lit-card">
  <span class="lit-author">Arafat et al.</span><span class="lit-year">2018</span>
  <div class="lit-title">Demography and risk factors of suicidal behavior in Bangladesh: retrospective online news content analysis</div>
  <div class="lit-finding">Manual grouping only — <strong class="amber">no algorithmic clustering applied.</strong></div>
</div>

<div class="lit-card">
  <span class="lit-author">Arafat et al.</span><span class="lit-year">2025</span>
  <div class="lit-title">Prevalence of suicidal behavior in Bangladesh: A systematic review and meta-analysis</div>
  <div class="lit-finding">Aggregate epidemiology — <strong class="amber">no case-level subgroup analysis.</strong></div>
</div>

---

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">Prior work — algorithmic clustering on suicide data</h3>

<div class="lit-card">
  <span class="lit-author">Wong et al.</span><span class="lit-year">2022</span>
  <div class="lit-title">Classification of school student suicides using cluster analysis · Hong Kong</div>
  <div class="lit-finding">K-Means on structured records — <strong class="amber">single algorithm, no imputation comparison.</strong></div>
</div>

<div class="lit-card">
  <span class="lit-author">Xiao et al.</span><span class="lit-year">2025</span>
  <div class="lit-title">Machine learning on social determinants of suicide · United States</div>
  <div class="lit-finding">Community-level K-Means — <strong class="amber">administrative data, not severely incomplete.</strong></div>
</div>

<div class="lit-card">
  <span class="lit-author">Sanz-Gomez et al.</span><span class="lit-year">2025</span>
  <div class="lit-title">Impulsivity-based pathways to suicide deaths: cluster analysis · Spain</div>
  <div class="lit-finding">Autopsy data, K-Means + Agglomerative — <strong class="amber">no LMIC newspaper context.</strong></div>
</div>

---

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">The five gaps we fill</h3>

<p style="font-size:24px;"><strong class="cyan">01</strong> &nbsp; No algorithmic clustering on Bangladeshi newspaper suicide data</p>

<p style="font-size:24px;"><strong class="cyan">02</strong> &nbsp; No multi-method imputation benchmark in this domain</p>

<p style="font-size:24px;"><strong class="cyan">03</strong> &nbsp; Prior studies use a single clustering algorithm — we use four</p>

<p style="font-size:24px;"><strong class="cyan">04</strong> &nbsp; Standard validity indices fail on imbalanced social data — we propose a balance penalty</p>

<p style="font-size:24px;"><strong class="cyan">05</strong> &nbsp; No prior work compares predictor-selection strategies during imputation</p>

---

<p class="section-divider-num">SECTION 03</p>

<h1 class="section-divider-title">Research</h1>

<hr class="section-divider-rule" />

<div class="section-divider-dots"><span></span><span></span><span></span><span></span><span></span></div>

---

<h3 class="label">Research Question</h3>

<p class="small-statement"><em>Which combination of missing-data handling and unsupervised learning produces the most stable, interpretable cluster structure from Bangladeshi newspaper suicide records?</em></p>

---

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">Objectives</h3>

<p style="font-size:28px;"><strong class="cyan">01</strong> &nbsp; Expand and curate a Bangladeshi newspaper suicide dataset across 2017–2025.</p>

<p style="font-size:28px;"><strong class="cyan">02</strong> &nbsp; Benchmark three imputation methods × two predictor strategies × four clustering algorithms.</p>

<p style="font-size:28px;"><strong class="cyan">03</strong> &nbsp; Design a balance-aware composite metric that demotes degenerate cluster solutions.</p>

<p style="font-size:28px;"><strong class="cyan">04</strong> &nbsp; Identify and interpret the top pipeline — and surface its caveats openly.</p>

---

<p class="section-divider-num">SECTION 04</p>

<h1 class="section-divider-title">Methodology</h1>

<hr class="section-divider-rule" />

<div class="section-divider-dots"><span></span><span></span><span></span><span></span><span></span></div>

---

<h3 class="label">End-to-end pipeline</h3>

<div class="figure-frame">
  <img src="./images/intro.png" alt="Overall pipeline" />
</div>

<p class="figure-caption">From newspaper scraping through cleaning, enrichment, imputation, clustering, and composite evaluation.</p>

---

<p class="large">1,617</p>

<p class="caption">records · 36 columns · 2017 to 2025</p>

<hr class="divider" />

<p style="font-size:24px; color:#8A8A8F;"><strong class="cyan">760</strong> Kaggle 2020 &nbsp;·&nbsp; <strong class="cyan">857</strong> manually collected &nbsp;·&nbsp; <strong class="cyan">9</strong> new attributes</p>

<p class="source">Source · this study · github.com/akashmony01/imputation-clustering-comparison</p>

---

<h2>A factorial benchmark.</h2>

<p style="font-size:54px; margin-top:24px;"><span class="cyan">3</span> imputers &nbsp;×&nbsp; <span class="cyan">2</span> strategies &nbsp;×&nbsp; <span class="cyan">4</span> clusterers</p>

<div class="matrix">
  <div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell baseline"></div><div class="matrix-cell baseline"></div>
  <div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell baseline"></div><div class="matrix-cell baseline"></div>
  <div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell baseline"></div><div class="matrix-cell baseline"></div>
  <div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell"></div><div class="matrix-cell baseline"></div><div class="matrix-cell baseline"></div>
</div>

<div class="matrix-legend">
  <span><span class="swatch" style="background:rgba(94,234,212,0.4);border:1px solid #5EEAD4;"></span>24 imputed</span>
  <span><span class="swatch" style="background:rgba(251,191,36,0.4);border:1px solid #FBBF24;"></span>8 baseline</span>
  <span style="color:#EAEAEA;"><strong>= 32 pipelines</strong></span>
</div>

---

<h3 class="label">Imputation workflow</h3>

<div class="figure-frame">
  <img src="./images/imputation.png" alt="Imputation pipeline" />
</div>

<p class="figure-caption">MICE · KNN · MissForest, each under context-aware and no-context predictor strategies.</p>

---

<h3 class="label">Clustering workflow</h3>

<div class="figure-frame">
  <img src="./images/cluster_flow.png" alt="Clustering pipeline" />
</div>

<p class="figure-caption">Standardisation · PCA · per-algorithm grid search · composite ranking across all 32 pipelines.</p>

---

<h2 class="amber">Standard scores reward<br/>degenerate solutions.</h2>

<p class="caption" style="margin-top:40px;">DBSCAN can label <strong style="color:#FBBF24;">99%</strong> of cases as noise<br/>and still post a high Silhouette score.</p>

---

<h3 class="label">Our six-component composite</h3>

<div class="composite-bar">
  <div class="composite-row">
    <span class="composite-label">Balance penalty</span>
    <div class="composite-track"><div class="composite-fill" style="width:100%;"></div></div>
    <span class="composite-percent">35%</span>
  </div>
  <div class="composite-row">
    <span class="composite-label">Silhouette</span>
    <div class="composite-track"><div class="composite-fill" style="width:71%;"></div></div>
    <span class="composite-percent">25%</span>
  </div>
  <div class="composite-row">
    <span class="composite-label">Calinski–Harabasz</span>
    <div class="composite-track"><div class="composite-fill" style="width:57%;"></div></div>
    <span class="composite-percent">20%</span>
  </div>
  <div class="composite-row">
    <span class="composite-label">Dunn</span>
    <div class="composite-track"><div class="composite-fill" style="width:28%;"></div></div>
    <span class="composite-percent">10%</span>
  </div>
  <div class="composite-row">
    <span class="composite-label">Davies–Bouldin</span>
    <div class="composite-track"><div class="composite-fill" style="width:14%;"></div></div>
    <span class="composite-percent">5%</span>
  </div>
  <div class="composite-row">
    <span class="composite-label">Xie–Beni</span>
    <div class="composite-track"><div class="composite-fill" style="width:14%;"></div></div>
    <span class="composite-percent">5%</span>
  </div>
</div>

<p class="caption">Maximum possible score: <strong style="color:#EAEAEA;">32</strong></p>

---

<p class="section-divider-num">SECTION 05</p>

<h1 class="section-divider-title">Results</h1>

<hr class="section-divider-rule" />

<div class="section-divider-dots"><span></span><span></span><span></span><span></span><span></span></div>

---

<h3 class="label">All 32 pipelines · ranked by composite score</h3>

<div class="figure-frame">
  <img src="./images/all_cases_sorted_with_combined_score.png" alt="Ranked pipelines" />
</div>

<p class="figure-caption">The full ranking. Agglomerative + MissForest no-context leads the field.</p>

---

<h3 class="label">The top-ranked pipeline</h3>

<h2 class="cyan">Agglomerative + MissForest</h2>

<p class="small-statement" style="margin-top:14px;">no-context</p>

<p class="caption" style="margin-top:40px;">Ranked first among all 32 pipelines</p>

---

<p class="huge">27.30</p>

<p class="caption">out of <strong>32</strong></p>

<p class="source">Composite score · this study · across 32 pipelines</p>

---

<h2>Two clusters.</h2>

<div class="cluster-bubbles">
  <div class="cluster-bubble c0">
    <span class="bubble-label">Cluster 0</span>
    <span class="bubble-num">759</span>
  </div>
  <div class="cluster-bubble c1">
    <span class="bubble-label">Cluster 1</span>
    <span class="bubble-num">858</span>
  </div>
</div>

<p class="caption">Near-balanced partition from 1,617 records</p>

---

![bg right:38% opacity:.5](./images/cluster_0_bangladesh.png)

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">Cluster 0</h3>

<p style="font-size:38px;"><strong>Semi-urban workplaces</strong> (54.5%)</p>

<p style="font-size:24px; color:#8A8A8F;">Hometowns dispersed across mid-sized provincial cities.</p>

<p style="font-size:20px; color:#8A8A8F; margin-top:24px;">Bogura &nbsp;·&nbsp; Rajshahi &nbsp;·&nbsp; Mymensingh</p>

<p style="font-size:20px; color:#5EEAD4; margin-top:16px;">All records: year 2020 (Kaggle subset)</p>

---

![bg right:38% opacity:.5](./images/cluster_1_bangladesh.png)

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">Cluster 1</h3>

<p style="font-size:38px;"><strong>Rural workplaces</strong> (50.0%)</p>

<p style="font-size:24px; color:#8A8A8F;">Hometowns concentrated at the two largest cities.</p>

<p style="font-size:20px; color:#8A8A8F; margin-top:24px;">Dhaka (9.1%) &nbsp;·&nbsp; Chattogram (7.7%)</p>

<p style="font-size:20px; color:#34D399; margin-top:16px;">All records: 2017–2019 + 2021–2025 (manual)</p>

---

<h3 class="label">Feature-by-feature contrast</h3>

<table class="compare-table">
  <tr>
    <th>Feature</th>
    <th>Cluster 0</th>
    <th>Cluster 1</th>
  </tr>
  <tr>
    <td class="feat">Workplace (modal)</td>
    <td class="c0">Semi-urban · 54.5%</td>
    <td class="c1">Rural · 50.0%</td>
  </tr>
  <tr>
    <td class="feat">Hometown (top 1)</td>
    <td class="c0">Bogura · 4.0%</td>
    <td class="c1">Dhaka · 9.1%</td>
  </tr>
  <tr>
    <td class="feat">Year coverage</td>
    <td class="c0">2020 only</td>
    <td class="c1">2017–2025</td>
  </tr>
  <tr>
    <td class="feat">Cluster size</td>
    <td class="c0">759</td>
    <td class="c1">858</td>
  </tr>
  <tr>
    <td class="feat">Source cohort</td>
    <td class="c0">Kaggle 2020</td>
    <td class="c1">Manual collection</td>
  </tr>
</table>

---

<h3 class="label">Age distribution by cluster</h3>

<div class="figure-frame">
  <img src="./images/age_cpmaring.png" alt="Age comparison" />
</div>

<p class="figure-caption">Cluster 1 skews slightly older. Both clusters concentrate in the 16–35 high-risk window.</p>

---

<h3 class="label">Reason for suicide · cluster comparison</h3>

<div class="figure-frame">
  <img src="./images/reason_comparing.png" alt="Reason comparison" />
</div>

<p class="figure-caption">Family conflict and relationship-related distress dominate in both clusters; weighting differs across the two cohorts.</p>

---

<p class="section-divider-num" style="color:#FBBF24;">SECTION 06</p>

<h1 class="section-divider-title">Honest Findings</h1>

<hr class="section-divider-rule" />

<div class="section-divider-dots"><span></span><span></span><span></span><span></span><span></span></div>

---

<h3 class="label" style="color:#FBBF24;">An honest finding</h3>

<p class="small-statement">The two clusters align with the<br/><strong class="amber">data-collection boundary</strong>,<br/>not with two distinct epidemiological groups.</p>

---

<!-- _class: left -->

<div class="side-line" style="background: linear-gradient(to bottom, transparent, #FBBF24 30%, #FBBF24 70%, transparent);"></div>

<p style="font-size:32px;"><strong class="cyan">Cluster 0</strong> = all 2020 (Kaggle subset)</p>

<p style="font-size:32px;"><strong class="cyan">Cluster 1</strong> = 2017–2019 + 2021–2025 (manually collected)</p>

<hr class="divider" />

<p style="font-size:28px;">The algorithm never saw the year.<br/>The split is <strong>emergent</strong>.</p>

<p class="muted" style="margin-top:20px;">An internal consistency check — not a substantive epidemiological finding.</p>

---

<!-- _class: left -->

<div class="side-line" style="background: linear-gradient(to bottom, transparent, #FBBF24 30%, #FBBF24 70%, transparent);"></div>

<h3 class="label" style="color:#FBBF24;">Caveats — disclosed in the abstract</h3>

<p style="font-size:28px;"><strong class="amber">Source-cohort confound</strong><br/><span style="color:#8A8A8F; font-size:20px;">cluster split coincides with data origin</span></p>

<p style="font-size:28px; margin-top:20px;"><strong class="amber">Temperature units differ</strong><br/><span style="color:#8A8A8F; font-size:20px;">Kelvin in Cluster 0 · Celsius in Cluster 1</span></p>

<p style="font-size:28px; margin-top:20px;"><strong class="amber">De-identified, not anonymised</strong><br/><span style="color:#8A8A8F; font-size:20px;">residual re-identification risk acknowledged</span></p>

---

<!-- _class: left -->

<div class="side-line"></div>

<h3 class="label">Limitations</h3>

<p style="font-size:28px;">Newspaper bias toward newsworthy cases</p>

<p style="font-size:28px;">Small sample by ML standards</p>

<p style="font-size:28px;">No external ground-truth labels</p>

<p style="font-size:28px;">Bangla NLP excluded from free-text fields</p>

<p style="font-size:28px;">Weather data sparse in rural areas</p>

---

<p class="section-divider-num" style="color:#34D399;">SECTION 07</p>

<h1 class="section-divider-title">What's Next</h1>

<hr class="section-divider-rule" />

<div class="section-divider-dots"><span></span><span></span><span></span><span></span><span></span></div>

---

<!-- _class: left -->

<div class="side-line" style="background: linear-gradient(to bottom, transparent, #34D399 30%, #34D399 70%, transparent);"></div>

<h3 class="label" style="color:#34D399;">Future work</h3>

<p style="font-size:28px;"><strong class="green">·</strong> &nbsp; Causal modelling beyond descriptive clustering</p>

<p style="font-size:28px;"><strong class="green">·</strong> &nbsp; BanglaBERT for free-text reason and profession fields</p>

<p style="font-size:28px;"><strong class="green">·</strong> &nbsp; Real-time alerting for high-risk demographic profiles</p>

<p style="font-size:28px;"><strong class="green">·</strong> &nbsp; Extension to other LMIC newspaper datasets</p>

---

<!-- _class: left -->

<div class="side-line" style="background: linear-gradient(to bottom, transparent, #34D399 30%, #34D399 70%, transparent);"></div>

<h3 class="label" style="color:#34D399;">Contribution</h3>

<p style="font-size:28px;">The <strong class="green">largest curated</strong> Bangladeshi newspaper suicide dataset to date</p>

<p style="font-size:28px;">A <strong class="green">reproducible</strong> 32-pipeline benchmark</p>

<p style="font-size:28px;">A <strong class="green">balance-aware</strong> composite metric</p>

<p style="font-size:28px;"><strong class="green">Open-source</strong> release: code + data + 12 notebooks</p>

---

<h3 class="label" style="color:#34D399;">Repository</h3>

<p style="font-family:'JetBrains Mono', monospace; font-size:26px; color:#EAEAEA;">github.com/akashmony01/<br/>imputation-clustering-comparison</p>

<hr class="divider" />

<p class="caption">Code: <strong style="color:#EAEAEA;">MIT</strong> &nbsp;·&nbsp; Data: <strong style="color:#EAEAEA;">CC-BY 4.0</strong></p>

<p style="font-size:18px; color:#8A8A8F; margin-top:20px;">12 Colab notebooks · intermediate datasets · cached API responses</p>

---

<h2>Thank you.</h2>

<p class="cyan" style="font-size:42px; margin-top:36px;">Questions?</p>
