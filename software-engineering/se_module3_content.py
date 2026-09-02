# Software Engineering Module 3 Exhaustive Content (13 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

SE_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Software Design Engineering & UML — Complete 13-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 27:</strong> Design Engineering (Architecture vs. Detailed Component Design)</div>
    <div><strong>Topic 28:</strong> The Software Design Process (Iterative Model Transformations)</div>
    <div><strong>Topic 29:</strong> Software Design Quality Attributes (Modularity & Maintainability)</div>
    <div><strong>Topic 30:</strong> Fundamental Design Concepts (Abstraction & Information Hiding)</div>
    <div><strong>Topic 31:</strong> Design Models (Data, Architectural, Interface & Component)</div>
    <div><strong>Topic 32:</strong> Object-Oriented Design Principles (SOLID Design Principles)</div>
    <div><strong>Topic 33:</strong> Cohesion (7 Levels: Coincidental to Functional Cohesion)</div>
    <div><strong>Topic 34:</strong> Coupling (5 Levels: Content to Data Coupling)</div>
    <div><strong>Topic 35:</strong> UML Use Case Diagrams (Actors, Systems & Include/Extend)</div>
    <div><strong>Topic 36:</strong> UML Class Diagrams (Attributes, Methods, Visibility & Relations)</div>
    <div><strong>Topic 37:</strong> UML Activity Diagrams (Workflows, Swimlanes & Fork/Join)</div>
    <div><strong>Topic 38:</strong> UML Sequence Diagrams (Lifelines, Messages & Time Sequence)</div>
    <div><strong>Topic 39:</strong> UML Collaboration / Communication Diagrams</div>
  </div>
</div>

<h2 class="section-title">Topic 27 – 30: Fundamental Software Design Concepts</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Design Concept</th>
      <th style="width: 45%;">Engineering Principle & Definition</th>
      <th>Key Benefit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Abstraction</strong></td><td>Suppressing low-level implementation details to focus on high-level essential characteristics.</td><td>Reduces cognitive complexity for system architects.</td></tr>
    <tr><td><strong>2. Modularity</strong></td><td>Decomposing software into discrete, independently testable, naming-addressable modules.</td><td>Enables parallel team development and isolated debugging.</td></tr>
    <tr><td><strong>3. Information Hiding</strong></td><td>Modules are designed so that internal algorithms and data structures are inaccessible from outside (Parnas, 1972).</td><td>Prevents cascading bug propagation when internal code changes.</td></tr>
    <tr><td><strong>4. Functional Independence</strong></td><td>Achieved by designing modules with <strong>High Cohesion</strong> and <strong>Low Coupling</strong>.</td><td>Maximizes code reusability and minimizes side-effect bugs.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 33 & 34: Cohesion vs. Coupling (The Cornerstone of Modular Design)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Cohesion Level (Internal Focus)</th>
      <th style="width: 45%;">Operating Semantics</th>
      <th>Quality Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Functional Cohesion</strong></td><td>Every instruction in the module contributes to executing <strong>exactly ONE single mathematical/business function</strong> (e.g., `calculate_tax()`).</td><td>⭐⭐⭐⭐⭐ <strong>BEST</strong></td></tr>
    <tr><td><strong>2. Sequential Cohesion</strong></td><td>Output data from one operation serves as direct input to the next operation in the module.</td><td>⭐⭐⭐⭐ Very Good</td></tr>
    <tr><td><strong>3. Communicational Cohesion</strong></td><td>Functions operate on the exact same input data structure (e.g., `print_student_record()` and `save_student_record()`).</td><td>⭐⭐⭐ Good</td></tr>
    <tr><td><strong>4. Procedural / Temporal</strong></td><td>Functions executed in a sequence or executed at the same time (e.g., `startup_initialization()`).</td><td>⭐⭐ Moderate</td></tr>
    <tr><td><strong>5. Coincidental Cohesion</strong></td><td>Arbitrary unrelated tasks grouped together in a `utils.py` file with no logical relationship.</td><td>⭐ <strong>WORST</strong></td></tr>
  </tbody>
</table>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Coupling Level (Inter-Dependency)</th>
      <th style="width: 45%;">Operating Semantics</th>
      <th>Quality Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Data Coupling</strong></td><td>Modules communicate strictly by passing necessary simple primitive data parameters ($x, y$).</td><td>⭐⭐⭐⭐⭐ <strong>BEST</strong></td></tr>
    <tr><td><strong>2. Stamp Coupling</strong></td><td>Modules pass entire complex data structures when only a single field is actually needed.</td><td>⭐⭐⭐⭐ Good</td></tr>
    <tr><td><strong>3. Control Coupling</strong></td><td>One module passes a control flag (`bool is_admin`) that dictates the internal execution path of another.</td><td>⭐⭐ Moderate</td></tr>
    <tr><td><strong>4. Common Coupling</strong></td><td>Multiple modules read and write to shared global variables.</td><td>⭐ Poor</td></tr>
    <tr><td><strong>5. Content Coupling</strong></td><td>One module directly accesses, modifies, or branches into the internal memory/code of another module.</td><td>💥 <strong>WORST</strong></td></tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">🧠 Golden Rule of Software Design</div>
  <strong>HIGH COHESION (Functional) + LOW COUPLING (Data) = Publication-Grade Software Architecture!</strong>
</div>

<h2 class="section-title">Topic 35 – 39: Unified Modeling Language (UML) Diagrams</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">UML Diagram</th>
      <th style="width: 25%;">Structural / Behavioral</th>
      <th>Key Modeling Elements & Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Use Case Diagram</strong></td><td>Behavioral</td><td>Actors (stick figures), Use Cases (ovals), System boundary, `<<include>>` (mandatory) and `<<extend>>` (optional).</td></tr>
    <tr><td><strong>2. Class Diagram</strong></td><td>Structural</td><td>Classes with 3 compartments: Name, Attributes (`- private`, `+ public`, `# protected`), Operations. Inheritance ($\triangle$), Association, Composition ($\blacklozenge$).</td></tr>
    <tr><td><strong>3. Activity Diagram</strong></td><td>Behavioral</td><td>Initial/Final nodes, Action states, Decision diamonds, Swimlanes, Fork/Join synchronization bars.</td></tr>
    <tr><td><strong>4. Sequence Diagram</strong></td><td>Behavioral (Dynamic)</td><td>Lifelines (vertical dashed lines), Activation boxes, Synchronous solid-arrow calls, Asynchronous open-arrow calls, Return dashed arrows.</td></tr>
    <tr><td><strong>5. Collaboration Diagram</strong></td><td>Behavioral (Dynamic)</td><td>Emphasizes structural organization of objects with numbered message arrows ($1.0, 1.1$) rather than a vertical time axis.</td></tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M3 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Differentiate between `<<include>>` and `<<extend>>` relationships in UML Use Case Diagrams with examples. (8 Marks)</div>
  <div class="qa-a">
    - <strong>`<<include>>` Relationship:</strong> Represents mandatory common functionality unconditionally shared across multiple use cases. The base use case <em>cannot execute</em> without invoking the included use case.<br>
      <em>Example:</em> `PlaceOrder` $\xrightarrow{<<include>>}$ `AuthenticateUser`.<br>
    - <strong>`<<extend>>` Relationship:</strong> Represents optional, conditional behavior that executes only when a specific extension point condition is met at runtime.<br>
      <em>Example:</em> `CalculateTotal` $\xleftarrow{<<extend>>}$ `ApplyDiscountCoupon` (executed only if the customer possesses a valid coupon code).
  </div>
</div>
"""
