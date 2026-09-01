# Software Engineering Module 4 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

SE_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Software Project Estimation, Metrics & Scheduling</div>
  <div class="toc-grid">
    <div>1. Software Project Management Dimensions (People, Product, Process, Project — 4 P's)</div>
    <div>2. Size-Oriented Metrics (Lines of Code — LOC) & Inherent Productivity Pitfalls</div>
    <div>3. Function-Oriented Metrics: Albrecht's Function Point (FP) Analysis Formulations</div>
    <div>4. Unadjusted Function Count (UFC) across 5 Information Domain Characteristics</div>
    <div>5. 14 General System Characteristics & Value Adjustment Factor (VAF) Math</div>
    <div>6. Boehm's COCOMO I Model: Organic, Semi-Detached & Embedded Project Modes</div>
    <div>7. Basic, Intermediate (Cost Drivers / EAF) & Detailed COCOMO Equations</div>
    <div>8. Project Scheduling: Work Breakdown Structure (WBS) & Activity Networks</div>
    <div>9. Critical Path Method (CPM): Earliest Start/Finish & Latest Start/Finish Slack Times</div>
    <div>10. Program Evaluation and Review Technique (PERT) Expected Duration ($T_e$) & Variance</div>
    <div>11. Risk Management Framework: Identification, Projection, Assessment & RMMM Plans</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 3 – 5: Function Point (FP) Analysis</h2>

<div class="formula-card">
  <strong>1. Function Point Formula (Albrecht, 1979):</strong>
  $$\text{FP} = \text{UFC} \times \text{VAF} = \text{UFC} \times \left( 0.65 + 0.01 \times \sum_{i=1}^{14} F_i \right)$$
  Where $\text{UFC}$ is Unadjusted Function Count, and $F_i \in [0, 5]$ are ratings for 14 General System Characteristics (yielding $\text{VAF} \in [0.65, 1.35]$).
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 30%;">Information Domain Element</th>
      <th style="width: 20%;">Low Complexity</th>
      <th style="width: 20%;">Average Complexity</th>
      <th>High Complexity</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. External Inputs (EI)</strong></td><td>3</td><td>4</td><td>6</td></tr>
    <tr><td><strong>2. External Outputs (EO)</strong></td><td>4</td><td>5</td><td>7</td></tr>
    <tr><td><strong>3. External Inquiries (EQ)</strong></td><td>3</td><td>4</td><td>6</td></tr>
    <tr><td><strong>4. Internal Logical Files (ILF)</strong></td><td>7</td><td>10</td><td>15</td></tr>
    <tr><td><strong>5. External Interface Files (EIF)</strong></td><td>5</td><td>7</td><td>10</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 6 & 7: Boehm's COCOMO (Constructive Cost Model)</h2>

<div class="formula-card">
  <strong>Basic COCOMO Effort & Schedule Equations:</strong>
  $$\text{Effort } (E) = a \times (\text{KLOC})^b \quad \text{Person-Months (PM)}$$
  $$\text{Development Time } (T_{\text{dev}}) = c \times (E)^d \quad \text{Months}$$
  $$\text{Average Staffing } (\text{Staff}) = \frac{E}{T_{\text{dev}}} \quad \text{Persons}$$
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Project Mode</th>
      <th style="width: 30%;">Characteristics</th>
      <th style="width: 12%;">$a$</th>
      <th style="width: 12%;">$b$</th>
      <th style="width: 12%;">$c$</th>
      <th>$d$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Organic</strong></td>
      <td>Small teams, familiar in-house domain, relaxed constraints.</td>
      <td>2.4</td>
      <td>1.05</td>
      <td>2.5</td>
      <td>0.38</td>
    </tr>
    <tr>
      <td><strong>2. Semi-Detached</strong></td>
      <td>Medium teams, mixed experience levels, medium constraints.</td>
      <td>3.0</td>
      <td>1.12</td>
      <td>2.5</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td><strong>3. Embedded</strong></td>
      <td>Tight hardware/software constraints, complex safety-critical systems.</td>
      <td>3.6</td>
      <td>1.20</td>
      <td>2.5</td>
      <td>0.32</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Basic COCOMO Estimation for a 30 KLOC Semi-Detached Project</div>
  <ol>
    <li>
      <strong>Step 1: Compute Effort ($E$):</strong>
      $$E = 3.0 \times (30)^{1.12} = 3.0 \times 44.91 = \mathbf{134.73} \text{ Person-Months}$$
    </li>
    <li>
      <strong>Step 2: Compute Development Time ($T_{\text{dev}}$):</strong>
      $$T_{\text{dev}} = 2.5 \times (134.73)^{0.35} = 2.5 \times 5.54 = \mathbf{13.85} \text{ Months}$$
    </li>
    <li>
      <strong>Step 3: Compute Average Staffing Size:</strong>
      $$\text{Staff} = \frac{E}{T_{\text{dev}}} = \frac{134.73}{13.85} \approx \mathbf{9.7} \implies \mathbf{10} \text{ Engineers}$$
    </li>
  </ol>
</div>

<h2 class="section-title">Topic 9 & 10: Project Scheduling (CPM & PERT Calculations)</h2>

<div class="formula-card">
  <strong>PERT Three-Point Estimation Formulas:</strong>
  - Optimistic time ($a$), Most likely time ($m$), Pessimistic time ($b$).
  $$\text{Expected Duration } (T_e) = \frac{a + 4m + b}{6}$$
  $$\text{Standard Deviation } (\sigma) = \frac{b - a}{6}, \quad \text{Variance } (\sigma^2) = \left( \frac{b - a}{6} \right)^2$$
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module IV)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. State the components of an RMMM (Risk Mitigation, Monitoring, and Management) plan. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Risk Mitigation (Proactive Prevention):</strong> Developing actionable strategy to reduce the probability of risk occurrence.<br>
       <em>Example:</em> High developer turnover risk $\rightarrow$ cross-training team members and establishing thorough documentation standards.<br>
    2. <strong>Risk Monitoring (Tracking):</strong> Continuously observing warning indicators to detect when a risk is transitioning from potential threat to reality.<br>
       <em>Example:</em> Monitoring team morale, overtime hours, and unresolved bug counts.<br>
    3. <strong>Risk Management (Contingency Action):</strong> Executing contingency plans when mitigation fails and the risk actually occurs.<br>
       <em>Example:</em> Activating backup external contractors if a key developer departs.
  </div>
</div>
"""
