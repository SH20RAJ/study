# Software Engineering Module 3 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

SE_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Software Design Engineering, Modularity & Architecture</div>
  <div class="toc-grid">
    <div>1. The Software Design Process (Architectural Design, Interface Design, Component Design)</div>
    <div>2. Fundamental Design Principles (Abstraction, Information Hiding, Modularity, Refactoring)</div>
    <div>3. Module Cohesion Taxonomy: Functional (Best) to Coincidental (Worst) Complete Scale</div>
    <div>4. Module Coupling Taxonomy: Data (Best) to Content (Worst) Complete Scale</div>
    <div>5. Object-Oriented Design Principles (SOLID: Single Responsibility, Open-Closed, Liskov, Interface, Dependency)</div>
    <div>6. Unified Modeling Language (UML): Structural Diagrams (Class, Object, Component)</div>
    <div>7. UML Behavioral & Interaction Diagrams: Sequence, State Machine & Activity Diagrams</div>
    <div>8. Software Architectural Styles: Layered, Client-Server, Pipe-and-Filter, MVC, Microservices</div>
    <div>9. GoF Design Patterns Taxonomy: Creational, Structural & Behavioral Paradigms</div>
    <div>10. Creational Patterns: Singleton & Factory Method Implementations & UML</div>
    <div>11. Structural & Behavioral Patterns: Adapter, Decorator, Observer & Strategy Patterns</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 3 & 4: Modularity (Cohesion vs. Coupling)</h2>

<p>
  The primary objective of software modularization is to achieve <strong>High Cohesion (Single Responsibility within a module)</strong> and <strong>Low Coupling (Minimal Interdependence between modules)</strong>.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Cohesion Type (High to Low)</th>
      <th style="width: 50%;">Definition & Internal Binding Characteristics</th>
      <th>Quality Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Functional</strong></td><td>All elements of a module contribute to executing a single, well-defined mathematical task (e.g., `computeSquareRoot()`).</td><td>⭐⭐⭐⭐⭐ (Ideal)</td></tr>
    <tr><td><strong>2. Sequential</strong></td><td>The output data of one element serves as the direct input to the next element inside the module (e.g., `readRecordAndFormat()`).</td><td>⭐⭐⭐⭐ (High)</td></tr>
    <tr><td><strong>3. Communicational</strong></td><td>Elements operate on the exact same input data structure or produce the same output structure (e.g., `updateAndPrintCustomerReport()`).</td><td>⭐⭐⭐ (Medium)</td></tr>
    <tr><td><strong>4. Procedural</strong></td><td>Elements are grouped because they execute in a specific sequential algorithmic order (e.g., `readInputsThenValidate()`).</td><td>⭐⭐ (Fair)</td></tr>
    <tr><td><strong>5. Temporal</strong></td><td>Elements are grouped simply because they are executed at the same time (e.g., system `startupInit()` or `shutdown()`).</td><td>⭐ (Poor)</td></tr>
    <tr><td><strong>6. Logical</strong></td><td>Elements perform logically similar tasks selected by a control flag (e.g., a single function with a switch case for all math operations).</td><td>⭐ (Poor)</td></tr>
    <tr><td><strong>7. Coincidental</strong></td><td>Elements have zero meaningful relationship; grouped purely by accident or arbitrary convenience.</td><td>❌ (Worst)</td></tr>
  </tbody>
</table>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Coupling Type (Low to High)</th>
      <th style="width: 50%;">Definition & Inter-Module Communication</th>
      <th>Quality Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Data Coupling</strong></td><td>Modules communicate strictly by passing elementary primitive data parameters (e.g., `int`, `float`).</td><td>⭐⭐⭐⭐⭐ (Ideal)</td></tr>
    <tr><td><strong>2. Stamp Coupling</strong></td><td>Modules pass complex composite data structures (e.g., entire `CustomerRecord`), even when the callee only needs a few fields.</td><td>⭐⭐⭐⭐ (Good)</td></tr>
    <tr><td><strong>3. Control Coupling</strong></td><td>One module passes a control flag (`bool`, `enum`) that dictates the internal execution flow of the other module.</td><td>⭐⭐ (Poor)</td></tr>
    <tr><td><strong>4. Common Coupling</strong></td><td>Multiple modules share and mutate global variables or shared global memory blocks.</td><td>⭐ (Very Poor)</td></tr>
    <tr><td><strong>5. Content Coupling</strong></td><td>One module directly accesses, modifies, or branches into the internal private code/memory of another module (e.g., modifying private memory).</td><td>❌ (Worst)</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 8: Software Architectural Styles</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Architectural Style</th>
      <th style="width: 45%;">Structural Organization & Communication</th>
      <th>Primary Use Cases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Layered (N-Tier)</strong></td>
      <td>Organized hierarchically into horizontal layers (UI $\rightarrow$ Business Logic $\rightarrow$ Data Access $\rightarrow$ Database). Upper layers invoke lower layers.</td>
      <td>Enterprise web applications, OS architectures.</td>
    </tr>
    <tr>
      <td><strong>2. Pipe-and-Filter</strong></td>
      <td>Data flows through a stream of discrete transformation filters connected by communication pipes.</td>
      <td>Unix pipelines, compilers, video processing engines.</td>
    </tr>
    <tr>
      <td><strong>3. Model-View-Controller</strong></td>
      <td>Decouples business data (Model), user interface presentation (View), and input handling (Controller).</td>
      <td>Interactive GUI applications (React, Angular, Django).</td>
    </tr>
    <tr>
      <td><strong>4. Microservices</strong></td>
      <td>Decomposes system into small, independently deployable services communicating via lightweight REST/gRPC APIs.</td>
      <td>Scalable cloud-native enterprise systems (Netflix, Uber).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module III)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the SOLID design principles in Object-Oriented Software Engineering. (10 Marks)</div>
  <div class="qa-a">
    - <strong>S (Single Responsibility Principle):</strong> A class should have only one reason to change, encapsulating a single responsibility.<br>
    - <strong>O (Open/Closed Principle):</strong> Software entities should be open for extension, but closed for modification (achieved via interfaces and polymorphism).<br>
    - <strong>L (Liskov Substitution Principle):</strong> Subtypes must be substitutable for their base types without altering program correctness.<br>
    - <strong>I (Interface Segregation Principle):</strong> Clients should not be forced to depend on interfaces they do not use (prefer small, client-specific interfaces over fat general ones).<br>
    - <strong>D (Dependency Inversion Principle):</strong> High-level modules should not depend on low-level modules; both should depend on abstractions.
  </div>
</div>
"""
