# Software Engineering Module 1 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

SE_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Software Process Models & Agile Methodologies</div>
  <div class="toc-grid">
    <div>1. The Software Crisis, Engineering Principles & The Dual Nature of Software</div>
    <div>2. Generic Software Process Framework (Communication, Planning, Modeling, Construction, Deployment)</div>
    <div>3. Classical Waterfall Model: Sequential Phases, Feedback Loops & Major Inherent Flaws</div>
    <div>4. The V-Model: Verification vs. Validation Cross-Phase Association</div>
    <div>5. Prototyping Paradigm: Throwaway vs. Evolutionary Prototyping Mechanics</div>
    <div>6. Boehm's Spiral Model: 4 Quadrants & Explicit Risk-Driven Iterations</div>
    <div>7. The Agile Manifesto: 4 Core Core Values & 12 Guiding Principles</div>
    <div>8. The Scrum Framework: Roles (PO, Scrum Master, Team) & Ceremonies</div>
    <div>9. Scrum Artifacts: Product Backlog, Sprint Backlog & Sprint Burndown Charts</div>
    <div>10. Extreme Programming (XP): Pair Programming, Test-Driven Development (TDD) & CI</div>
    <div>11. Process Model Selection Decision Matrix for Diverse Engineering Constraints</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 – 4: Traditional Prescriptive Process Models</h2>
<p>
  A <strong>Software Process Model</strong> is an abstract representation of the lifecycle activities, actions, tasks, milestones, and work products required to build high-quality software.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Process Model</th>
      <th style="width: 40%;">Core Operational Philosophy</th>
      <th>Ideal Project Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Classical Waterfall</strong></td>
      <td>Strictly linear sequential progression. Downstream phases only begin once upstream deliverables are frozen.</td>
      <td>Requirements are 100% clear, stable, and well-understood; safety-critical systems with rigid standards.</td>
    </tr>
    <tr>
      <td><strong>2. V-Model</strong></td>
      <td>Pairs each development phase on the left descending arm with its corresponding testing verification phase on the right ascending arm.</td>
      <td>High-reliability systems where test plan generation occurs early in parallel with requirements.</td>
    </tr>
    <tr>
      <td><strong>3. Prototyping</strong></td>
      <td>Builds a quick mock-up interface to elicit, clarify, and validate ambiguous user requirements.</td>
      <td>High user interaction systems where clients cannot articulate exact requirements upfront.</td>
    </tr>
    <tr>
      <td><strong>4. Boehm's Spiral Model</strong></td>
      <td>Risk-driven iterative model combining iterative prototyping with Waterfall systematic control. Evaluates risk in 4 quadrants per cycle.</td>
      <td>Large-scale, expensive, high-risk enterprise systems with emerging requirements.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 6: Boehm's Spiral Model (4 Quadrants of Iteration)</h2>

<div class="callout callout-info">
  <div class="callout-title">The 4 Quadrants of the Spiral Model Cycle</div>
  <ol>
    <li><strong>Quadrant 1: Determine Objectives, Alternatives & Constraints:</strong> Identify specific phase goals, alternative architectural options, and operational constraints (cost, schedule).</li>
    <li><strong>Quadrant 2: Identify & Resolve Risks (Risk Analysis):</strong> Detailed risk evaluation; create simulations, benchmarks, or prototypes to mitigate technical and project risks.</li>
    <li><strong>Quadrant 3: Develop & Verify Next-Level Product:</strong> Engineering design, coding, and verification testing of the release increment.</li>
    <li><strong>Quadrant 4: Review & Plan Next Phase:</strong> Customer evaluation of the increment, review progress, and plan the next spiral loop.</li>
  </ol>
</div>

<h2 class="section-title">Topic 7 – 9: Agile Methodologies & The Scrum Framework</h2>

<div class="formula-card">
  <strong>The 4 Values of the Agile Manifesto (2001):</strong>
  1. <strong>Individuals and interactions</strong> over processes and tools.
  2. <strong>Working software</strong> over comprehensive documentation.
  3. <strong>Customer collaboration</strong> over contract negotiation.
  4. <strong>Responding to change</strong> over following a rigid plan.
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Scrum Component</th>
      <th style="width: 45%;">Definition & Purpose</th>
      <th>Key Responsibility / Invariant</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Product Owner (PO)</strong></td>
      <td>Represents business stakeholders and customers; defines vision.</td>
      <td>Owns and prioritizes the Product Backlog.</td>
    </tr>
    <tr>
      <td><strong>Scrum Master</strong></td>
      <td>Servant-leader; removes organizational impediments and ensures adherence to Scrum.</td>
      <td>Facilitates Daily Standups, Sprint Planning, and Retrospectives.</td>
    </tr>
    <tr>
      <td><strong>Sprint Backlog</strong></td>
      <td>Subset of Product Backlog user stories selected for delivery in current 2–4 week Sprint.</td>
      <td>Estimated by developers using Story Points (Planning Poker).</td>
    </tr>
    <tr>
      <td><strong>Burndown Chart</strong></td>
      <td>Visual graph plotting remaining work (story points) against time (days of the sprint).</td>
      <td>Tracks velocity and predicts whether sprint goals will be met on time.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module I)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare the Waterfall Model and the Spiral Model across 4 engineering parameters. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Risk Management:</strong> Waterfall has zero explicit risk management mechanisms; Spiral is fundamentally driven by continuous risk analysis in every cycle.<br>
    2. <strong>Handling Changing Requirements:</strong> Waterfall resists changes after requirements freeze; Spiral accommodates evolving requirements in subsequent spiral loops.<br>
    3. <strong>Customer Involvement:</strong> In Waterfall, customer interaction happens only at the beginning (requirements) and end (delivery); in Spiral, customer evaluates prototypes after every loop.<br>
    4. <strong>Project Cost & Complexity:</strong> Waterfall is suitable for small, simple projects; Spiral is designed for large-scale, complex, mission-critical systems.
  </div>
</div>
"""
