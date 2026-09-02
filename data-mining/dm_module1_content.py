# Data Mining Module 1 Exhaustive Content (14 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DM_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Introduction to Data Mining — Complete 14-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Introduction to Data Mining (Knowledge Discovery Process)</div>
    <div><strong>Topic 2:</strong> Relational Databases (Tables, Tuples & Schemas)</div>
    <div><strong>Topic 3:</strong> Data Warehouses (SITN Characteristics & OLAP)</div>
    <div><strong>Topic 4:</strong> Transactional Databases (Transaction Sets & Market Basket)</div>
    <div><strong>Topic 5:</strong> Advanced Database Systems & Applications</div>
    <div><strong>Topic 6:</strong> Data Mining Functionalities (Characterization vs. Discrimination)</div>
    <div><strong>Topic 7:</strong> Classification of Data Mining Systems</div>
    <div><strong>Topic 8:</strong> Major Issues in Data Mining (Quality, Scalability, Privacy)</div>
    <div><strong>Topic 9:</strong> Data Concepts (Objects, Attributes & Datasets)</div>
    <div><strong>Topic 10:</strong> Data Objects & Attribute Types (Nominal, Binary, Ordinal, Numeric)</div>
    <div><strong>Topic 11:</strong> Basic Statistical Descriptions (Mean, Median, Mode, IQR, Box Plots)</div>
    <div><strong>Topic 12:</strong> Data Visualization (Histograms, Scatter Plots, Quantile Plots)</div>
    <div><strong>Topic 13:</strong> Measuring Data Similarity (Cosine Similarity & Dot Products)</div>
    <div><strong>Topic 14:</strong> Measuring Data Dissimilarity (Euclidean & Manhattan Distances)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Introduction to Data Mining & Relational Databases</h2>
<p>
  <strong>Data Mining (Knowledge Discovery in Databases — KDD)</strong> is the computational process of discovering non-trivial, implicit, previously unknown, and potentially actionable patterns and models from massive datasets.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Database Query (SQL / OLTP)</th>
      <th>Data Mining (KDD / Discovery)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Retrieves exact known records matching user-specified criteria (e.g., "Find all students with $\text{CGPA} > 8.0$").</td>
      <td>Discovers hidden, inductive relationships and associations (e.g., "Students who score high in Algorithms also excel in Compiler Design").</td>
    </tr>
    <tr>
      <td>Deductive, exact, deterministic SQL responses.</td>
      <td>Inductive, statistical, pattern-based models with probabilistic confidence.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 3 – 5: Data Warehouses & Advanced Databases [UPLOADED PYQ]</h2>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: SITN Characteristics of Data Warehouses (Inmon)</div>
  <ul>
    <li><strong>S — Subject-Oriented:</strong> Organized around major business subjects (Customers, Products, Sales) rather than transactional operations.</li>
    <li><strong>I — Integrated:</strong> Data from diverse operational sources is standardized into consistent naming, units, and encoding schemes.</li>
    <li><strong>T — Time-Variant:</strong> Maintains historical data spanning 5–10 years with explicit timestamp attributes for trend analysis.</li>
    <li><strong>N — Non-Volatile:</strong> Read-only analytical storage; historical snapshots are loaded and not updated in-place.</li>
  </ul>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Operational Database (OLTP)</th>
      <th>Data Warehouse (OLAP) [UPLOADED PYQ — IT335 Mid]</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Supports day-to-day operational transactions (e.g., bank ATM withdrawal).</td><td>Supports long-term executive decision making, reporting, and predictive analytics.</td></tr>
    <tr><td>Stores current, real-time up-to-the-second data.</td><td>Stores historical snapshots over long multi-year horizons.</td></tr>
    <tr><td>Highly normalized tables (3NF/BCNF) to eliminate update anomalies.</td><td>Denormalized dimensional schemas (Star / Snowflake) to optimize complex query joins.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 6: Data Mining Functionalities [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Functionality</th>
      <th style="width: 45%;">Core Algorithmic Objective</th>
      <th>Illustrative Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Characterization [UPLOADED PYQ]</strong></td>
      <td>Summarizes the general properties of a target class into compact descriptions (Attribute-Oriented Induction).</td>
      <td>"Summarize the demographic profile of customers who spent $> ₹1,00,000$ last year."</td>
    </tr>
    <tr>
      <td><strong>2. Discrimination [UPLOADED PYQ]</strong></td>
      <td>Compares the target class against one or a set of contrasting comparative classes.</td>
      <td>"Compare customers who buy gaming laptops vs. customers who buy standard business laptops."</td>
    </tr>
    <tr>
      <td><strong>3. Association & Correlation</strong></td>
      <td>Finds frequent itemsets and conditional dependency rules ($X \implies Y$).</td>
      <td>"Customers purchasing Milk and Bread also buy Butter with 80% confidence."</td>
    </tr>
    <tr>
      <td><strong>4. Classification</strong></td>
      <td>Supervised learning predicting discrete categorical class labels.</td>
      <td>"Classifying credit card transactions as Fraudulent or Legitimate."</td>
    </tr>
    <tr>
      <td><strong>5. Prediction (Regression)</strong></td>
      <td>Predicts continuous real-valued numeric values.</td>
      <td>"Predicting real-estate house prices based on square footage and location."</td>
    </tr>
    <tr>
      <td><strong>6. Clustering</strong></td>
      <td>Unsupervised grouping of unlabeled data points based on geometric similarity.</td>
      <td>"Customer market segmentation into 5 distinct spending behavioral clusters."</td>
    </tr>
    <tr>
      <td><strong>7. Outlier Analysis</strong></td>
      <td>Detects anomalous objects that deviate significantly from normal baseline distributions.</td>
      <td>"Network intrusion detection and credit card fraud surveillance."</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 8 – 10: Data Objects & Attribute Types</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Attribute Type</th>
      <th style="width: 45%;">Mathematical Characteristics & Valid Operations</th>
      <th>Representative Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Nominal</strong></td>
      <td>Categorical labels, names, or codes with <strong>no meaningful rank or ordering</strong> ($=, \neq$).</td>
      <td>`Marital_Status` (Single, Married), `Color` (Red, Blue).</td>
    </tr>
    <tr>
      <td><strong>2. Binary</strong></td>
      <td>Nominal attribute with exactly 2 states (`0` and `1`). Symmetric (Gender) vs. Asymmetric (Medical test positive/negative).</td>
      <td>`Smoker` (Yes/No), `COVID_Positive` (0/1).</td>
    </tr>
    <tr>
      <td><strong>3. Ordinal</strong></td>
      <td>Categorical values with a <strong>meaningful ranking / order</strong>, but intervals between values cannot be measured ($<, >, =, \neq$).</td>
      <td>`Customer_Rating` (Poor < Fair < Good < Excellent), `Academic_Grade` (A, B, C, D, F).</td>
    </tr>
    <tr>
      <td><strong>4. Numeric (Interval)</strong></td>
      <td>Measured on a scale of equal units; <strong>zero is arbitrary</strong> (no true zero point; addition and subtraction meaningful, ratios meaningless).</td>
      <td>Temperature in $^\circ\text{C}$ or $^\circ\text{F}$, Calendar Years.</td>
    </tr>
    <tr>
      <td><strong>5. Numeric (Ratio)</strong></td>
      <td>Inherent <strong>absolute zero point</strong> (both differences and ratios are mathematically meaningful: $y = 2x$).</td>
      <td>`Salary` ($₹50,000$), `Age` (20 years), `Weight`, `Length`.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 11 & 12: Basic Statistical Descriptions & Visualization</h2>

<div class="formula-card">
  <strong>Five-Number Summary & Box-Plot Formulations:</strong>
  $$\text{Five-Number Summary} = \langle \text{Minimum}, \ Q_1 \ (25\%), \ \text{Median} \ (Q_2), \ Q_3 \ (75\%), \ \text{Maximum} \rangle$$
  $$\text{Interquartile Range } (\text{IQR}) = Q_3 - Q_1$$
  $$\text{Outlier Cutoff Boundaries: Lower} = Q_1 - 1.5 \times \text{IQR}, \quad \text{Upper} = Q_3 + 1.5 \times \text{IQR}$$
</div>

<h2 class="section-title">Topic 13 & 14: Data Similarity & Dissimilarity Measures</h2>

<div class="formula-card">
  <strong>1. Cosine Similarity (For Sparse Document/Text Vectors $\mathbf{x}, \mathbf{y}$):</strong>
  $$\text{sim}(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\|_2 \|\mathbf{y}\|_2} = \frac{\sum_{i=1}^n x_i y_i}{\sqrt{\sum_{i=1}^n x_i^2} \sqrt{\sum_{i=1}^n y_i^2}}$$
</div>

<div class="formula-card">
  <strong>2. Minkowski Distance Metric ($L_p$ Norm):</strong>
  $$d(\mathbf{x}, \mathbf{y}) = \left( \sum_{i=1}^n |x_i - y_i|^p \right)^{\frac{1}{p}}$$
  - For $p = 1$: <strong>Manhattan ($L_1$) Distance:</strong> $d(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^n |x_i - y_i|$
  - For $p = 2$: <strong>Euclidean ($L_2$) Distance:</strong> $d(\mathbf{x}, \mathbf{y}) = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$
</div>

<h2 class="section-title">🧠 M1 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ — IT426 Mid] Differentiate between Data Characterization and Data Discrimination with concrete examples. (8 Marks)</div>
  <div class="qa-a">
    - <strong>Data Characterization:</strong> A summarization of the general characteristics or features of a target class of data. The output can be represented as pie charts, bar charts, multidimensional data cubes, or generalized relations.<br>
      <em>Example:</em> Characterizing customers who purchased items worth over ₹1,00,000 at an electronics store to find their average age, income, and city.<br>
    - <strong>Data Discrimination:</strong> A comparative analysis of the general features of the target class objects against one or more contrasting comparative classes.<br>
      <em>Example:</em> Comparing software engineers who remained at a company for over 5 years against those who left within 1 year to identify key turnover drivers.
  </div>
</div>
"""
