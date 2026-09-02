# Software Engineering Module 5 Exhaustive Content (13 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

SE_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Project Management, Quality & Maintenance — Complete 13-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 56:</strong> Process & Product Metrics (Defect Density & Productivity)</div>
    <div><strong>Topic 57:</strong> Software Measurement (Lines of Code & Token Metrics)</div>
    <div><strong>Topic 58:</strong> Software Project Estimation Paradigms & Heuristics</div>
    <div><strong>Topic 59:</strong> Decomposition Techniques (Problem vs. Process Decomposition)</div>
    <div><strong>Topic 60:</strong> Empirical Estimation Models & Historical Calibration</div>
    <div><strong>Topic 61:</strong> The COCOMO Model (Organic, Semi-Detached, Embedded)</div>
    <div><strong>Topic 62:</strong> Function Point Analysis (5 Function Types: EI, EO, EQ, ILF, EIF)</div>
    <div><strong>Topic 63:</strong> Quality Assurance & Standards (ISO 9001 & CMMI 5 Levels)</div>
    <div><strong>Topic 64:</strong> Quality Planning & SQA Checklists</div>
    <div><strong>Topic 65:</strong> Quality Control (QA vs. QC: Prevention vs. Detection)</div>
    <div><strong>Topic 66:</strong> Software Configuration Management (SCM, Baselines & CCB)</div>
    <div><strong>Topic 67:</strong> Software Maintenance (The 4 CAP-P Maintenance Types)</div>
    <div><strong>Topic 68:</strong> Software Re-Engineering (Reverse & Forward Engineering)</div>
  </div>
</div>

<h2 class="section-title">Topic 61: Boehm's COCOMO Model (Constructive Cost Model)</h2>

<div class="formula-card">
  <strong>Basic COCOMO Equations (Barry Boehm, 1981):</strong>
  $$\text{Effort } (E) = a \cdot (\text{KLOC})^b \quad [\text{Person-Months (PM)}]$$
  $$\text{Development Time } (T_{\text{dev}}) = c \cdot (E)^d \quad [\text{Months}]$$
  $$\text{Average Staffing Size } (SS) = \frac{E}{T_{\text{dev}}} \quad [\text{Persons}], \quad \text{Productivity} = \frac{\text{KLOC}}{E} \quad [\text{KLOC/PM}]$$
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Project Mode</th>
      <th style="width: 35%;">Team & Environment Characteristics</th>
      <th style="width: 15%;">Effort ($a, b$)</th>
      <th>Time ($c, d$)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Organic</strong></td><td>Small, experienced teams working with flexible requirements in familiar in-house environment.</td><td>$E = 2.4(\text{KLOC})^{1.05}$</td><td>$T_{\text{dev}} = 2.5(E)^{0.38}$</td></tr>
    <tr><td><strong>2. Semi-Detached</strong></td><td>Medium teams with mixed experience levels working under intermediate constraints.</td><td>$E = 3.0(\text{KLOC})^{1.12}$</td><td>$T_{\text{dev}} = 2.5(E)^{0.35}$</td></tr>
    <tr><td><strong>3. Embedded</strong></td><td>Extremely tight, rigid hardware/software interface constraints (e.g., flight control, medical systems).</td><td>$E = 3.6(\text{KLOC})^{1.20}$</td><td>$T_{\text{dev}} = 2.5(E)^{0.32}$</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 62: Function Point (FP) Analysis (Albrecht, 1979)</h2>

<div class="formula-card">
  <strong>Function Point Mathematical Formulations:</strong>
  $$\mathbf{\text{FP} = \text{UFP} \times \text{VAF} = \text{UFP} \times \left[ 0.65 + 0.01 \times \sum_{i=1}^{14} C_i \right]}$$
  Where $\text{UFP}$ is Unadjusted Function Points, and $\sum C_i$ is the sum of 14 General System Characteristics (TDI: 0 to 70).
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Function Type</th>
      <th style="width: 15%;">Low Weight</th>
      <th style="width: 15%;">Average Weight</th>
      <th style="width: 15%;">High Weight</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. External Inputs (EI)</strong></td><td>3</td><td>4</td><td>6</td><td>User transactions adding/updating internal DB records.</td></tr>
    <tr><td><strong>2. External Outputs (EO)</strong></td><td>4</td><td>5</td><td>7</td><td>Calculated reports/displays leaving system boundary.</td></tr>
    <tr><td><strong>3. External Inquiries (EQ)</strong></td><td>3</td><td>4</td><td>6</td><td>Interactive queries retrieving direct data without calculation.</td></tr>
    <tr><td><strong>4. Internal Logical Files (ILF)</strong></td><td>7</td><td>10</td><td>15</td><td>Major database tables maintained inside system boundary.</td></tr>
    <tr><td><strong>5. External Interface Files (EIF)</strong></td><td>5</td><td>7</td><td>10</td><td>Data files maintained by another external system.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 63: Capability Maturity Model Integration (CMMI Levels 1 – 5)</h2>

<table class="custom-table">
  <thead><tr><th>CMMI Maturity Level</th><th>Process Predictability & Characteristics</th></tr></thead>
  <tbody>
    <tr><td><strong>Level 1: Initial</strong></td><td>Ad-hoc, chaotic, undocumented; success depends on individual heroic developer efforts.</td></tr>
    <tr><td><strong>Level 2: Managed</strong></td><td>Basic project management established; requirements, costs, and schedules are tracked and repeatable.</td></tr>
    <tr><td><strong>Level 3: Defined</strong></td><td>Standard engineering processes documented and standardized across entire organization.</td></tr>
    <tr><td><strong>Level 4: Quantitatively Managed</strong></td><td>Process and product quality quantitatively measured, controlled, and statistically tracked.</td></tr>
    <tr><td><strong>Level 5: Optimizing</strong></td><td>Continuous process improvement driven by quantitative feedback and innovative technology piloting.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 66 – 68: SCM & The 4 Types of Software Maintenance (CAP-P)</h2>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: The 4 Maintenance Types (CAP-P)</div>
  <ul>
    <li><strong>1. Corrective Maintenance (20%):</strong> Reactive fixing of residual bugs discovered in production.</li>
    <li><strong>2. Adaptive Maintenance (25%):</strong> Modifying software to operate in new environments (OS upgrade, cloud migration).</li>
    <li><strong>3. Perfective Maintenance (50% — Largest):</strong> Enhancing existing functionality, performance, and user convenience.</li>
    <li><strong>4. Preventive Maintenance (5%):</strong> Refactoring code to enhance maintainability and prevent future software decay.</li>
  </ul>
</div>

<h2 class="section-title">🧠 M5 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. A 30 KLOC software is developed in Organic mode. Calculate Effort, Development Time, Staff Size, and Productivity using Basic COCOMO. (8 Marks)</div>
  <div class="qa-a">
    Given: $\text{Size} = 30 \text{ KLOC}$, Mode: Organic ($a=2.4, b=1.05, c=2.5, d=0.38$).<br>
    1. $\text{Effort } E = 2.4 \times (30)^{1.05} = 2.4 \times 35.64 \approx \mathbf{85.54 \text{ Person-Months}}$.<br>
    2. $\text{Development Time } T_{\text{dev}} = 2.5 \times (85.54)^{0.38} = 2.5 \times 5.43 \approx \mathbf{13.58 \text{ Months}}$.<br>
    3. $\text{Average Staff Size } SS = \frac{E}{T_{\text{dev}}} = \frac{85.54}{13.58} \approx \mathbf{6.3 \text{ Persons}}$.<br>
    4. $\text{Productivity} = \frac{30}{85.54} \approx \mathbf{0.351 \text{ KLOC/PM}} \ (\mathbf{351 \text{ LOC/PM}})$.
  </div>
</div>
"""
