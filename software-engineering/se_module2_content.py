# Software Engineering Module 2 Exhaustive Content (12 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

SE_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Software Requirements Engineering — Complete 12-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 15:</strong> Functional Requirements (Core Behavioral Capabilities)</div>
    <div><strong>Topic 16:</strong> Non-Functional Requirements (Quality Constraints & Performance)</div>
    <div><strong>Topic 17:</strong> User Requirements (High-Level Natural Language Statements)</div>
    <div><strong>Topic 18:</strong> System Requirements (Detailed Technical Specifications)</div>
    <div><strong>Topic 19:</strong> The Software Requirements Specification (SRS) Document</div>
    <div><strong>Topic 20:</strong> IEEE 830 Standard Format for SRS Organization</div>
    <div><strong>Topic 21:</strong> 9 Characteristics of a Good SRS (C-U-C-C-V-F-T-P-M)</div>
    <div><strong>Topic 22:</strong> Feasibility Study (The TELOS Analytical Framework)</div>
    <div><strong>Topic 23:</strong> Requirements Elicitation Techniques (Interviews, JAD, Prototyping)</div>
    <div><strong>Topic 24:</strong> Requirements Analysis & Conflict Negotiation</div>
    <div><strong>Topic 25:</strong> Requirements Validation & Formal Inspection Reviews</div>
    <div><strong>Topic 26:</strong> Requirements Management & Traceability Matrices (RTM)</div>
  </div>
</div>

<h2 class="section-title">Topic 15 – 18: Functional vs. Non-Functional & User vs. System Requirements</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Requirement Class</th>
      <th style="width: 45%;">Formal Definition & Scope</th>
      <th>Concrete Illustrative Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Functional</strong></td>
      <td>Specifies <strong>WHAT</strong> services, computations, and transformations the software must perform in response to specific inputs.</td>
      <td>"The banking system shall transfer funds between accounts and send SMS confirmation within 5 seconds."</td>
    </tr>
    <tr>
      <td><strong>2. Non-Functional</strong></td>
      <td>Specifies <strong>HOW WELL</strong> the system operates, defining constraints on quality attributes: Performance, Security, Availability, Usability.</td>
      <td>"The system shall maintain $99.99\%$ annual availability and encrypt database records using AES-256."</td>
    </tr>
    <tr>
      <td><strong>3. User Requirements</strong></td>
      <td>High-level natural language statements + informal diagrams intended for non-technical clients and executive sponsors.</td>
      <td>"Patients should be able to book doctor consultations online."</td>
    </tr>
    <tr>
      <td><strong>4. System Requirements</strong></td>
      <td>Structured, unambiguous technical contracts detailing software services, inputs, outputs, exceptions, and DB schemas for developers.</td>
      <td>"The API endpoint `POST /api/v1/appointments` shall validate doctor availability locks via Redis mutexes."</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 19 – 21: The SRS Document & IEEE 830 Standard</h2>

<div class="callout callout-info">
  <div class="callout-title">🧠 The 9 Characteristics of a High-Quality SRS (C-U-C-C-V-F-T-P-M)</div>
  <ol>
    <li><strong>Correct:</strong> Every requirement accurately reflects actual customer needs.</li>
    <li><strong>Unambiguous:</strong> Every requirement has exactly ONE possible interpretation by developers and testers.</li>
    <li><strong>Complete:</strong> All critical functional capabilities, responses to errors, and constraints are specified.</li>
    <li><strong>Consistent:</strong> Zero contradictions between individual requirements or interface definitions.</li>
    <li><strong>Verifiable (Testable):</strong> A finite, cost-effective test case can prove whether the software satisfies the requirement.</li>
    <li><strong>Feasible:</strong> The requirement is achievable within project budget, timeline, and technology constraints.</li>
    <li><strong>Traceable:</strong> Each requirement has a unique identifier linked backward to user needs and forward to code/tests.</li>
    <li><strong>Prioritized:</strong> Requirements are ranked by business importance (Essential, Desirable, Optional).</li>
    <li><strong>Modifiable:</strong> Organized with a clear table of contents and cross-references for easy updates.</li>
  </ol>
</div>

<h2 class="section-title">Topic 22 – 26: Requirements Engineering Process (TELOS to Traceability)</h2>

<div class="formula-card">
  <strong>The TELOS Feasibility Analysis Framework:</strong>
  - <strong>T — Technical:</strong> Do we have the hardware, software tools, and developer expertise?
  - <strong>E — Economic:</strong> Is the Return on Investment (ROI) and Cost-Benefit Analysis positive?
  - <strong>L — Legal:</strong> Does the product comply with GDPR, HIPAA, copyright, and regional labor laws?
  - <strong>O — Operational:</strong> Will end-users and the organizational structure accept the system?
  - <strong>S — Schedule:</strong> Can the product be delivered before the critical market deadline?
</div>

<div class="worked-box">
  <div class="worked-title">Requirements Traceability Matrix (RTM) Sample Architecture</div>
  <table class="custom-table">
    <thead><tr><th>Req ID</th><th>Requirement Description</th><th>Source</th><th>Design Module</th><th>Code File</th><th>Test Case ID</th></tr></thead>
    <tbody>
      <tr><td>`REQ-01`</td><td>User OTP Authentication</td><td>Client Specs §2.1</td><td>`AuthModule`</td><td>`auth_service.py`</td><td>`TC-AUTH-001`</td></tr>
      <tr><td>`REQ-02`</td><td>Payment Gateway Checkout</td><td>Client Specs §3.4</td><td>`PaymentEngine`</td><td>`payment_gateway.py`</td><td>`TC-PAY-014`</td></tr>
    </tbody>
  </table>
</div>

<h2 class="section-title">🧠 M2 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the IEEE 830 standard structure for a Software Requirements Specification (SRS). (8 Marks)</div>
  <div class="qa-a">
    The IEEE 830 standard organizes an SRS into 3 primary sections:<br>
    1. <strong>Section 1: Introduction:</strong> Purpose, Scope, Definitions, Acronyms, References, and Document Overview.<br>
    2. <strong>Section 2: Overall Description:</strong> Product Perspective, Product Functions, User Classes & Characteristics, Operating Environment, Design Constraints, Assumptions & Dependencies.<br>
    3. <strong>Section 3: Specific Requirements:</strong> Detailed Functional Requirements, External Interface Requirements (User, Hardware, Software, Comm), Performance Requirements, Security & Safety Attributes, and Verification Criteria.
  </div>
</div>
"""
