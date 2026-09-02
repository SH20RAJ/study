# Data Mining Module 2 Exhaustive Content (6 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DM_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Data Preprocessing — Complete 6-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 15:</strong> Data Cleaning (Handling Missing Values & Noisy Data Smoothing)</div>
    <div><strong>Topic 16:</strong> Data Integration (Schema Matching & Redundancy Correlation)</div>
    <div><strong>Topic 17:</strong> Data Transformation (Min-Max & Z-Score Normalizations)</div>
    <div><strong>Topic 18:</strong> Data Reduction (Dimensionality, Numerosity & Compression)</div>
    <div><strong>Topic 19:</strong> Data Discretization (Unsupervised Binning & Supervised Trees)</div>
    <div><strong>Topic 20:</strong> Concept Hierarchy Generation for Nominal & Numeric Data</div>
  </div>
</div>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: C-I-T-R-D-H Preprocessing Pipeline</div>
  <strong>C</strong>lean $\rightarrow$ <strong>I</strong>ntegrate $\rightarrow$ <strong>T</strong>ransform $\rightarrow$ <strong>R</strong>educe $\rightarrow$ <strong>D</strong>iscretize $\rightarrow$ <strong>H</strong>ierarchy
</div>

<h2 class="section-title">Topic 15: Data Cleaning Techniques</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Missing Data Strategy</th>
      <th style="width: 45%;">Operational Mechanism</th>
      <th>Tradeoffs & Constraints</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Ignore Tuple</strong></td><td>Discard the entire row containing missing values.</td><td>Simple; highly wasteful if tuple contains other valuable attributes.</td></tr>
    <tr><td><strong>2. Global Constant</strong></td><td>Fill missing values with a label like `"Unknown"` or $-\infty$.</td><td>May mislead data mining classifiers into treating `"Unknown"` as a true category.</td></tr>
    <tr><td><strong>3. Attribute Mean / Median</strong></td><td>Replace missing numeric value with mean (symmetric distribution) or median (skewed data).</td><td>Preserves overall sample mean; reduces natural variance.</td></tr>
    <tr><td><strong>4. Most Probable Value</strong></td><td>Estimate using regression, decision tree inference, or Bayesian expectation maximization.</td><td>Statistically soundest; computationally intensive.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 17: Data Transformation & Normalization [UPLOADED PYQ]</h2>

<div class="formula-card">
  <strong>1. Min-Max Normalization Formula [UPLOADED PYQ]:</strong>
  $$v' = \frac{v - \min_A}{\max_A - \min_A} (\text{new\_max}_A - \text{new\_min}_A) + \text{new\_min}_A$$
  Maps values into designated target range $[\text{new\_min}_A, \text{new\_max}_A]$ (commonly $[0.0, 1.0]$).
</div>

<div class="formula-card">
  <strong>2. Z-Score (Zero-Mean) Normalization Formula:</strong>
  $$v' = \frac{v - \bar{A}}{\sigma_A}$$
  Where $\bar{A}$ is the mean and $\sigma_A$ is the standard deviation. Essential when actual minimum and maximum are unknown or outliers dominate.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ [UPLOADED PYQ] Solved Problem: Min-Max Normalization of Value $400$ in Range $[200, 1000]$ to Target $[10, 20]$</div>
  <p>Given: $v = 400, \min = 200, \max = 1000, \text{new\_min} = 10, \text{new\_max} = 20$.</p>
  $$v' = \frac{400 - 200}{1000 - 200} \times (20 - 10) + 10 = \frac{200}{800} \times 10 + 10 = 0.25 \times 10 + 10 = 2.5 + 10 = \mathbf{12.5}$$
</div>

<h2 class="section-title">Topic 18 & 19: Data Reduction & Discretization</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Reduction Approach</th>
      <th style="width: 45%;">Core Mathematical / Statistical Techniques</th>
      <th>Key Benefits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Dimensionality Reduction</strong></td>
      <td><strong>Principal Component Analysis (PCA):</strong> Projects $d$-dimensional space onto $k$ orthogonal eigenvectors ($k \ll d$) maximizing variance. Wavelet transforms.</td>
      <td>Removes irrelevant features; mitigates Curse of Dimensionality.</td>
    </tr>
    <tr>
      <td><strong>2. Numerosity Reduction</strong></td>
      <td>Parametric: Linear regression models ($y = mx + c$), Log-linear models.<br>Non-parametric: Histograms, Clustering, Random Sampling without replacement.</td>
      <td>Replaces massive raw dataset with compact mathematical surrogate models.</td>
    </tr>
    <tr>
      <td><strong>3. Discretization (Binning)</strong></td>
      <td>• <strong>Equal-Width (Distance) Partitioning:</strong> Divides range into $k$ equal intervals: $W = \frac{\max - \min}{k}$.<br>• <strong>Equal-Frequency (Depth) Partitioning:</strong> Divides sorted values such that each bin contains $N / k$ samples.</td>
      <td>Converts continuous attributes into discrete intervals for Decision Trees and Association Mining.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 20: Concept Hierarchy Generation [UPLOADED PYQ]</h2>

<div class="callout callout-info">
  <div class="callout-title">[UPLOADED PYQ — IT426 End] Concept Hierarchy Generation for Nominal Data</div>
  A <strong>Concept Hierarchy</strong> defines a sequence of mappings from a set of low-level concepts to higher-level, more general concepts:
  $$\text{Street} \longrightarrow \text{City} \longrightarrow \text{State} \longrightarrow \text{Country}$$
  <strong>Two Primary Methods of Generation:</strong>
  <ol>
    <li><strong>Specification of Partial Ordering by Users / Experts at Schema Level:</strong> Explicitly defined by database administrators (e.g., `street < city < state < country`).</li>
    <li><strong>Data-Driven Automatic Generation Based on Attribute Value Counts (Distinct Cardinality):</strong> The attribute with the largest number of distinct values is placed at the lowest level of the hierarchy, while the attribute with the fewest distinct values is placed at the top (e.g., `Country` (10 values) $>$ `State` (50 values) $>$ `City` (500 values) $>$ `Street` (50,000 values)).</li>
  </ol>
</div>

<h2 class="section-title">🧠 M2 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Explain Equal-Width vs. Equal-Frequency Binning for data smoothing on sorted data: `4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34`. (8 Marks)</div>
  <div class="qa-a">
    Dataset size $N = 12$, target bins $k = 3$:<br>
    - <strong>Equal-Frequency (Depth) Partitioning (4 elements per bin):</strong><br>
      • Bin 1: `4, 8, 9, 15` $\rightarrow$ Smoothed by bin mean: `9, 9, 9, 9`<br>
      • Bin 2: `21, 21, 24, 25` $\rightarrow$ Smoothed by bin mean: `23, 23, 23, 23`<br>
      • Bin 3: `26, 28, 29, 34` $\rightarrow$ Smoothed by bin mean: `29, 29, 29, 29`<br>
    - <strong>Equal-Width Partitioning:</strong> Width $W = \frac{34 - 4}{3} = 10$.<br>
      • Bin 1 $[4, 14)$: `4, 8, 9`<br>
      • Bin 2 $[14, 24)$: `15, 21, 21`<br>
      • Bin 3 $[24, 34]$: `24, 25, 26, 28, 29, 34`
  </div>
</div>
"""
