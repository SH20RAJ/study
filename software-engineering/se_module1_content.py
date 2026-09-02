# Software Engineering Module 1 Exhaustive Content (14 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

SE_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Introduction & Process Models — Complete 14-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> What is Software Engineering? (Systematic Discipline)</div>
    <div><strong>Topic 2:</strong> Why Software Engineering? (Software Crisis & Complexity)</div>
    <div><strong>Topic 3:</strong> The Evolving Role of Software (Product, Service & System)</div>
    <div><strong>Topic 4:</strong> Software Process Framework (Core Generic Activities)</div>
    <div><strong>Topic 5:</strong> Classical Waterfall Model (Linear Sequential Lifecycle)</div>
    <div><strong>Topic 6:</strong> Prototyping Model (Requirement Discovery & User Feedback)</div>
    <div><strong>Topic 7:</strong> Boehm's Spiral Model (Risk-Driven Iterative Cycles)</div>
    <div><strong>Topic 8:</strong> Rapid Application Development (RAD Component Reuse)</div>
    <div><strong>Topic 9:</strong> Incremental Process Model (Progressive Feature Delivery)</div>
    <div><strong>Topic 10:</strong> Agile Models (Agile Manifesto & Sprint Feedback Loops)</div>
    <div><strong>Topic 11:</strong> Software Management Activities (The 4 P's Framework)</div>
    <div><strong>Topic 12:</strong> Project Planning (Scope, Cost & Resource Allocation)</div>
    <div><strong>Topic 13:</strong> Project Scheduling (WBS, Gantt Charts & PERT/CPM)</div>
    <div><strong>Topic 14:</strong> Risk Management (I-A-P-M-M Risk Assessment Cycle)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 – 3: What is Software Engineering & The Software Crisis?</h2>
<p>
  <strong>Software Engineering (IEEE 610.12)</strong> is the systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering principles to software.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Ad-Hoc Programming</th>
      <th>Software Engineering Discipline</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Individual developer writing code without formal specifications.</td><td>Multi-person, multi-team systematic engineering development lifecycle.</td></tr>
    <tr><td>No formal documentation; maintainability ignored.</td><td>Comprehensive SRS, architectural designs, test plans, and version control.</td></tr>
    <tr><td>Massive budget overruns, missed deadlines, high defect rates.</td><td>Predictable cost estimation (COCOMO), scheduling (PERT/Gantt), and QA/QC.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 4 – 10: Software Development Process Models</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Process Model</th>
      <th style="width: 45%;">Core Lifecycle Mechanism & Characteristics</th>
      <th>Ideal Project Suitability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Waterfall Model</strong></td>
      <td>Strict linear sequential phases (Requirements $\rightarrow$ Design $\rightarrow$ Code $\rightarrow$ Test $\rightarrow$ Deploy). Each phase produces sign-off deliverables before the next begins.</td>
      <td>Well-understood, stable requirements with mature technology stacks (e.g., Space flight software, banking backends).</td>
    </tr>
    <tr>
      <td><strong>2. Prototyping</strong></td>
      <td>Builds an early disposable mock-up interface to elicit feedback, refine ambiguous user requirements, and discard/re-engineer.</td>
      <td>High user interaction systems where clients have unclear or fuzzy initial requirements.</td>
    </tr>
    <tr>
      <td><strong>3. Spiral Model (Boehm)</strong></td>
      <td>Risk-driven iterative model structured in 4 quadrants: (1) Objective Determination, (2) <strong>Risk Analysis</strong>, (3) Engineering, (4) Customer Evaluation.</td>
      <td>Large-scale, expensive, mission-critical, high-risk enterprise projects.</td>
    </tr>
    <tr>
      <td><strong>4. RAD Model</strong></td>
      <td>Rapid Application Development ($60\text{–}90$ days) utilizing component-based construction, GUI builders, and automated code generators.</td>
      <td>Well-modularized information systems with short delivery deadlines and high component reuse.</td>
    </tr>
    <tr>
      <td><strong>5. Incremental Model</strong></td>
      <td>System is decomposed into modular release increments. Increment 1 delivers core functionality; subsequent releases add peripheral features.</td>
      <td>Projects requiring early partial operational software release to capture market share.</td>
    </tr>
    <tr>
      <td><strong>6. Agile (Scrum / XP)</strong></td>
      <td>Iterative 2–4 week <strong>Sprints</strong> emphasizing working software over documentation, customer collaboration, and adaptive response to changing requirements.</td>
      <td>Dynamic web/mobile products with volatile, continuously evolving market requirements.</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: Process Model Selection Strategy</div>
  • Stable requirements $\rightarrow$ <strong>Waterfall</strong><br>
  • Unclear user requirements $\rightarrow$ <strong>Prototyping</strong><br>
  • High financial/technical risk $\rightarrow$ <strong>Spiral</strong><br>
  • Rapid component delivery $\rightarrow$ <strong>RAD / Incremental</strong><br>
  • Changing, dynamic requirements $\rightarrow$ <strong>Agile</strong>
</div>

<h2 class="section-title">Topic 11 – 14: Project Planning, Scheduling & Risk Management</h2>

<div class="callout callout-warning">
  <div class="callout-title">The 5-Stage Risk Management Cycle (I-A-P-M-M)</div>
  <ol>
    <li><strong>Risk Identification:</strong> Identify project, product, and business risks (e.g., staff turnover, scope creep).</li>
    <li><strong>Risk Analysis (Estimation):</strong> Quantify Risk Probability ($P$) and Risk Impact / Severity ($I$). $\text{Risk Exposure } (RE) = P \times I$.</li>
    <li><strong>Risk Prioritization:</strong> Rank risks in a Risk Matrix to focus engineering resources on top hazards.</li>
    <li><strong>Risk Mitigation (RMMM Plan):</strong> Develop Risk Mitigation, Monitoring, and Management strategies to minimize impact.</li>
    <li><strong>Risk Monitoring:</strong> Continuously track risk indicators throughout the project lifecycle.</li>
  </ol>
</div>

<h2 class="section-title">🧠 M1 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare Waterfall, Prototyping, Spiral, and Agile models across 5 engineering parameters. (10 Marks)</div>
  <div class="qa-a">
    1. <strong>Requirement Flexibility:</strong> Waterfall is rigid; Prototyping clarifies fuzzy needs; Spiral adapts per cycle; Agile welcomes changes at any stage.<br>
    2. <strong>Risk Management:</strong> Spiral explicitly incorporates formal Risk Analysis in every cycle; Waterfall and Prototyping have zero built-in risk analysis; Agile manages risk via short sprint iterations.<br>
    3. <strong>Customer Involvement:</strong> Waterfall involves customer only at start and end; Agile and Prototyping require continuous customer collaboration.<br>
    4. <strong>Delivery Schedule:</strong> Waterfall delivers product only at the very end; Incremental/Agile delivers functional software increments every few weeks.<br>
    5. <strong>Cost & Documentation:</strong> Waterfall is documentation-heavy; Spiral is expensive due to risk experts; Agile prioritizes working software over extensive documentation.
  </div>
</div>
"""
