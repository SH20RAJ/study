# Data Mining Module 3 Exhaustive Content (9 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DM_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Data Warehouse & OLAP Technology — Complete 9-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 21:</strong> Basic Concepts of Data Warehouse & ETL Pipelines</div>
    <div><strong>Topic 22:</strong> Data Warehouse Modeling (Star, Snowflake, Fact Constellation)</div>
    <div><strong>Topic 23:</strong> Data Cube Multidimensional Views (Base to Apex Cuboids)</div>
    <div><strong>Topic 24:</strong> OLAP Operations (Roll-Up, Drill-Down, Slice, Dice, Pivot)</div>
    <div><strong>Topic 25:</strong> Data Warehouse Design & 4 Architecture Views [UPLOADED PYQ]</div>
    <div><strong>Topic 26:</strong> Data Warehouse Implementation (Materialized Views & Indexing)</div>
    <div><strong>Topic 27:</strong> Attribute-Oriented Induction (AOI Generalization Algorithm)</div>
    <div><strong>Topic 28:</strong> Data Cube Computation & Materialization Choices [UPLOADED PYQ]</div>
    <div><strong>Topic 29:</strong> Preliminary Warehouse Concepts (Fact vs. Dimension Tables)</div>
  </div>
</div>

<h2 class="section-title">Topic 21 & 22: Data Warehouse Modeling Schemas [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Dimensional Schema</th>
      <th style="width: 45%;">Structural Layout & Normalization</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Star Schema</strong></td>
      <td>Single central Fact Table connected radially to completely <strong>denormalized Dimension Tables</strong> (1-join query topology).</td>
      <td>Simplest structure; blazing fast OLAP query response times. Contains data redundancy in dimension tables.</td>
    </tr>
    <tr>
      <td><strong>2. Snowflake Schema [UPLOADED PYQ]</strong></td>
      <td>Dimension tables are <strong>normalized</strong> into multiple hierarchical sub-tables (e.g., `Product` splits into `Product_Category` and `Supplier`).</td>
      <td>Zero data redundancy; saves storage space. Slower query execution due to expensive multi-table relational joins.</td>
    </tr>
    <tr>
      <td><strong>3. Fact Constellation (Galaxy)</strong></td>
      <td>Multiple Fact Tables (e.g., `Sales_Fact` and `Shipping_Fact`) sharing common conformed Dimension Tables (`Time`, `Item`).</td>
      <td>Models sophisticated enterprise-wide business operations across multiple departments.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 23 & 24: Data Cube & OLAP Operations [UPLOADED PYQ]</h2>

<div class="callout callout-info">
  <div class="callout-title">The 5 Canonical OLAP Operations</div>
  <ol>
    <li><strong>Roll-Up (Drill-Up):</strong> Aggregates data by climbing up a concept hierarchy or reducing dimensions (e.g., from `Day` $\rightarrow$ `Month` $\rightarrow$ `Quarter` $\rightarrow$ `Year`).</li>
    <li><strong>Drill-Down:</strong> Navigates from summarized high-level data to detailed granular data (e.g., from `Country` $\rightarrow$ `State` $\rightarrow$ `City`).</li>
    <li><strong>Slice:</strong> Performs a selection on a single dimension, producing a 2D sub-cube (e.g., `Time = "Q1 2026"`).</li>
    <li><strong>Dice:</strong> Defines a sub-cube by performing a selection on two or more dimensions (e.g., `Location = {"Ranchi", "Patna"}` AND `Item = {"Laptop", "Phone"}`).</li>
    <li><strong>Pivot (Rotate):</strong> Rotates the data axes in visualization to provide alternative multidimensional viewing angles.</li>
  </ol>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">OLTP (Online Transaction Processing)</th>
      <th>OLAP (Online Analytical Processing) [UPLOADED PYQ]</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Primary Focus</strong></td><td>Day-to-day transaction processing and CRUD operations.</td><td>Complex multidimensional decision support and data mining.</td></tr>
    <tr><td><strong>Data Content</strong></td><td>Current, real-time snapshot; highly detailed.</td><td>Historical, consolidated, multi-year summarized aggregates.</td></tr>
    <tr><td><strong>Database Design</strong></td><td>Highly normalized entity-relationship (ER) models (3NF).</td><td>Denormalized multidimensional Star / Snowflake schemas.</td></tr>
    <tr><td><strong>Access Pattern</strong></td><td>High frequency, short, deterministic atomic transactions.</td><td>Low frequency, complex analytical aggregation queries.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 25 – 28: Warehouse Design Views & Cube Materialization [UPLOADED PYQ]</h2>

<div class="callout callout-warning">
  <div class="callout-title">[UPLOADED PYQ — IT426 Mid] The 4 Essential Design Views for a Data Warehouse</div>
  <ol>
    <li><strong>Top-Down View:</strong> Defines the overall information requirements of decision makers and enterprise business goals.</li>
    <li><strong>Data Source View:</strong> Models the operational schemas, data types, and access protocols of legacy source systems.</li>
    <li><strong>Data Warehouse View:</strong> Defines the dimensional Star/Snowflake schemas, fact measures, dimensions, and aggregation granularities.</li>
    <li><strong>Business Query View:</strong> Analyzes user query patterns, analytical workloads, and reporting requirements to guide index design and cube materialization.</li>
  </ol>
</div>

<h3 class="subsection-title">Data Cube Materialization Choices ($2^n$ Cuboids) [UPLOADED PYQ]:</h3>
<ul>
  <li><strong>1. No Materialization:</strong> Compute cuboids on-the-fly when requested. Zero disk overhead; extremely slow query latency.</li>
  <li><strong>2. Full Materialization:</strong> Precompute all $2^n$ possible cuboids in the lattice. Fast query response; massive storage overhead.</li>
  <li><strong>3. Partial Materialization (Optimal Industry Standard):</strong> Precomputes a carefully selected subset of high-frequency cuboids based on query workload and storage constraints (Greedy algorithm / PBS).</li>
</ul>

<h2 class="section-title">🧠 M3 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Compare Star Schema and Snowflake Schema across 4 architectural parameters. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Normalization Level:</strong> Star schema uses denormalized dimension tables; Snowflake schema normalizes dimension tables into 3NF hierarchies.<br>
    2. <strong>Query Performance:</strong> Star schema provides faster query execution because queries require only simple single-level joins with the central fact table; Snowflake requires multiple expensive joins across normalized dimension sub-tables.<br>
    3. <strong>Storage Overhead:</strong> Star schema contains data redundancy (e.g., repeated city/state names); Snowflake eliminates redundancy, saving disk space.<br>
    4. <strong>Maintenance Complexity:</strong> Star schema is easier to understand and maintain for business analysts; Snowflake has complex structural dependencies.
  </div>
</div>
"""
