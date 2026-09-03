#!/usr/bin/env python3
"""
Master Data Mining (CS24303) Complete Publication Suite Compiler.
Produces 10-12 page individual module PDFs and a 55+ page Full Course Master Book!
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

# -------------------- MODULE 1 --------------------
M1_CONTENT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 1 Table of Contents (Topics 1 to 14)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 1:</strong> Data Mining & KDD Lifecycle</div>
    <div>• <strong>Topic 2:</strong> Data Objects & Attribute Types</div>
    <div>• <strong>Topic 3:</strong> Central Tendency (Mean, Median, Mode)</div>
    <div>• <strong>Topic 4:</strong> Dispersion & Five-Number Summary</div>
    <div>• <strong>Topic 5:</strong> Visual Displays (Boxplots, Q-Q Plots)</div>
    <div>• <strong>Topic 6:</strong> Nominal & Binary Proximity (SMC, Jaccard)</div>
    <div>• <strong>Topic 7:</strong> Numeric Distance (Minkowski, Manhattan)</div>
    <div>• <strong>Topic 8:</strong> Cosine & Mahalanobis Metrics</div>
    <div>• <strong>Topic 9:</strong> Mixed Attribute Distance (Gower)</div>
    <div>• <strong>Topic 10:</strong> 15 Solved University Examination Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Data Mining Foundations, KDD Process & Attribute Types</h2>

<p>
  <strong>Data Mining</strong> is the computational process of discovering valid, novel, potentially useful, and ultimately understandable patterns from massive, complex datasets. It sits at the confluence of Database Systems, Statistics, Machine Learning, Pattern Recognition, and High-Performance Computing.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ The 7-Stage KDD Process Pipeline (Fayyad et al.)</div>
  <ol>
    <li><strong>Data Cleaning:</strong> Eliminating noisy, erroneous, and inconsistent records; imputing missing values.</li>
    <li><strong>Data Integration:</strong> Merging heterogeneous schemas, relational databases, flat files, and real-time data streams into a unified repository.</li>
    <li><strong>Data Selection:</strong> Retrieving task-relevant subsets from operational repositories.</li>
    <li><strong>Data Transformation:</strong> Normalizing, aggregating, scaling, and constructing informative features.</li>
    <li><strong>Data Mining:</strong> Applying intelligent algorithms (Apriori, Decision Trees, k-Means, SVM) to extract patterns.</li>
    <li><strong>Pattern Evaluation:</strong> Identifying truly interesting patterns using objective interestingness measures (Support, Confidence, Lift).</li>
    <li><strong>Knowledge Presentation:</strong> Visualizing findings via dashboards and decision support systems.</li>
  </ol>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Attribute Type</th>
      <th style="width: 35%;">Mathematical Characteristics</th>
      <th style="width: 25%;">Meaningful Operators</th>
      <th>Real-World Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nominal (Categorical)</strong></td>
      <td>Values are distinct qualitative categories or names without intrinsic ordering.</td>
      <td>$=, \neq, \text{Mode}, \text{Entropy}$</td>
      <td>`MaritalStatus: {Single, Married, Divorced}`, `BloodType: {A, B, AB, O}`.</td>
    </tr>
    <tr>
      <td><strong>Binary (Symmetric vs Asymmetric)</strong></td>
      <td>Nominal attribute with exactly 2 states ($0, 1$). <em>Symmetric:</em> both states equally important; <em>Asymmetric:</em> presence of state $1$ carries far higher significance than $0$.</td>
      <td>$=, \neq$, Contingency tables, Jaccard coefficient</td>
      <td><em>Symmetric:</em> `Gender: {M, F}`; <em>Asymmetric:</em> `COVID-19_Test: {Positive=1, Negative=0}`.</td>
    </tr>
    <tr>
      <td><strong>Ordinal</strong></td>
      <td>Values possess a meaningful ranked order, but step intervals between adjacent ranks are subjective and unequal.</td>
      <td>$=, \neq, <, >, \text{Median}, \text{Percentiles}$</td>
      <td>`CustomerRating: {Poor, Fair, Good, Excellent}`, `AcademicGrade: {A, B, C, D, F}`.</td>
    </tr>
    <tr>
      <td><strong>Numeric: Interval-Scaled</strong></td>
      <td>Measured on a scale of equal-sized units, but lacks a true physical absolute zero point (zero is an arbitrary convention).</td>
      <td>$+ , -, \text{Mean}, \text{Variance}$ (Ratios are meaningless!)</td>
      <td>`Temperature in Celsius / Fahrenheit`, `Calendar Years (2024 CE)`.</td>
    </tr>
    <tr>
      <td><strong>Numeric: Ratio-Scaled</strong></td>
      <td>Measured on a scale with a physically absolute zero point (representing total absence of the measured quantity).</td>
      <td>$+ , -, \times, \div$, Ratios, Geometric Mean</td>
      <td>`Salary in USD ($0 = no income)`, `Age`, `Weight in kg`, `Network Bandwidth`.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 3 & 4: Statistical Descriptions of Central Tendency & Dispersion</h2>

<div class="formula-card">
  <strong>Comprehensive Central Tendency & Dispersion Formulas:</strong>
  $$\mathbf{\text{Arithmetic Mean: } \bar{x} = \frac{1}{N} \sum_{i=1}^N x_i \qquad \text{Trimmed Mean: Mean after dropping top/bottom } k\% \text{ outliers}}$$
  $$\mathbf{\text{Median: Middle value when sorted } x_{(N+1)/2} \quad (\text{Robust to extreme outliers!})}$$
  $$\mathbf{\text{Empirical Mean-Median-Mode Relationship for Moderately Skewed Data: } \text{Mean} - \text{Mode} \approx 3(\text{Mean} - \text{Median})}$$
  $$\mathbf{\text{Variance: } \sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \bar{x})^2 \qquad \text{Sample Variance: } s^2 = \frac{1}{N-1}\sum_{i=1}^N (x_i - \bar{x})^2}$$
  $$\mathbf{\text{Standard Deviation: } \sigma = \sqrt{\sigma^2} \qquad \text{Interquartile Range: } \text{IQR} = Q_3 - Q_1}$$
  $$\mathbf{\text{Tukey's Outlier Bounds: } [\text{Lower Fence}, \text{Upper Fence}] = [Q_1 - 1.5 \cdot \text{IQR}, \ Q_3 + 1.5 \cdot \text{IQR}]}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Five-Number Summary & Outlier Detection</div>
  <p>Consider the dataset representing monthly engineering salaries (in thousands of dollars):</p>
  $$\mathbf{X = \{15, 20, 22, 25, 28, 30, 32, 35, 38, 42, 45, 120\}}$$
  <p><strong>1. Five-Number Summary Calculation ($N = 12$):</strong></p>
  <ul>
    <li><strong>Minimum:</strong> $\mathbf{15}$</li>
    <li><strong>First Quartile ($Q_1$):</strong> Median of lower half $\{15, 20, 22, 25, 28, 30\} \implies \frac{22 + 25}{2} = \mathbf{23.5}$</li>
    <li><strong>Median ($Q_2$):</strong> $\frac{x_6 + x_7}{2} = \frac{30 + 32}{2} = \mathbf{31.0}$</li>
    <li><strong>Third Quartile ($Q_3$):</strong> Median of upper half $\{32, 35, 38, 42, 45, 120\} \implies \frac{38 + 42}{2} = \mathbf{40.0}$</li>
    <li><strong>Maximum:</strong> $\mathbf{120}$</li>
  </ul>
  <p><strong>2. Interquartile Range & Outlier Fences:</strong></p>
  $$\text{IQR} = Q_3 - Q_1 = 40.0 - 23.5 = \mathbf{16.5}$$
  $$\text{Lower Fence} = Q_1 - 1.5(\text{IQR}) = 23.5 - 1.5(16.5) = 23.5 - 24.75 = \mathbf{-1.25}$$
  $$\text{Upper Fence} = Q_3 + 1.5(\text{IQR}) = 40.0 + 1.5(16.5) = 40.0 + 24.75 = \mathbf{64.75}$$
  $$\mathbf{\text{Outlier Identification: } 120 > 64.75 \implies \mathbf{120 \text{ is a severe outlier!}}}$$
</div>

<h2 class="section-title">Topic 6 to 9: Mathematical Proximity & Distance Metrics</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Proximity Metric</th>
      <th style="width: 45%;">Mathematical Formulation</th>
      <th>Properties & Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Euclidean Distance ($L_2$)</strong></td>
      <td>$$d(\mathbf{x}, \mathbf{y}) = \sqrt{\sum_{i=1}^p (x_i - y_i)^2} = \|\mathbf{x} - \mathbf{y}\|_2$$</td>
      <td>Rotational invariant; sensitive to feature scales and extreme outliers.</td>
    </tr>
    <tr>
      <td><strong>Manhattan Distance ($L_1$)</strong></td>
      <td>$$d(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^p |x_i - y_i| = \|\mathbf{x} - \mathbf{y}\|_1$$</td>
      <td>City-block orthogonal grid distance; robust to axis outliers.</td>
    </tr>
    <tr>
      <td><strong>Minkowski Distance ($L_h$)</strong></td>
      <td>$$d(\mathbf{x}, \mathbf{y}) = \left( \sum_{i=1}^p |x_i - y_i|^h \right)^{1/h}$$</td>
      <td>Generalization ($h=1 \implies \text{Manhattan}; h=2 \implies \text{Euclidean}; h \rightarrow \infty \implies \text{Chebyshev } L_\infty$).</td>
    </tr>
    <tr>
      <td><strong>Cosine Similarity</strong></td>
      <td>$$\text{sim}(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\|_2 \|\mathbf{y}\|_2} = \frac{\sum x_i y_i}{\sqrt{\sum x_i^2}\sqrt{\sum y_i^2}}$$</td>
      <td>Measures orientation angle regardless of document magnitude; ideal for high-dimensional sparse text vectors!</td>
    </tr>
    <tr>
      <td><strong>Simple Matching Coeff (SMC)</strong></td>
      <td>$$\text{SMC} = \frac{q + t}{q + r + s + t}$$</td>
      <td>Used for symmetric binary attributes (equal weight to 0-0 and 1-1 matches).</td>
    </tr>
    <tr>
      <td><strong>Jaccard Coefficient</strong></td>
      <td>$$J = \frac{q}{q + r + s} \qquad d_J = 1 - J = \frac{r + s}{q + r + s}$$</td>
      <td>Used for asymmetric binary data (ignores irrelevant negative-negative $0-0$ matches $t$).</td>
    </tr>
    <tr>
      <td><strong>Mahalanobis Distance</strong></td>
      <td>$$d_M(\mathbf{x}, \mathbf{y}) = \sqrt{(\mathbf{x} - \mathbf{y})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{y})}$$</td>
      <td>Scale-invariant metric accounting for correlations between attributes ($\mathbf{\Sigma}$ is covariance matrix).</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Jaccard vs. SMC on Binary Medical Patient Vectors</div>
  <p>Two patient symptom vectors $\mathbf{x} = [1, 0, 0, 1, 1, 0, 1, 0]$ and $\mathbf{y} = [1, 1, 0, 1, 0, 0, 1, 0]$ for 8 rare diseases:</p>
  <ul>
    <li>$q = \text{number of attributes where } \mathbf{x}=1 \text{ and } \mathbf{y}=1 \implies \text{Indices } \{1, 4, 7\} \implies q = 3$.</li>
    <li>$r = \text{number of attributes where } \mathbf{x}=1 \text{ and } \mathbf{y}=0 \implies \text{Index } \{5\} \implies r = 1$.</li>
    <li>$s = \text{number of attributes where } \mathbf{x}=0 \text{ and } \mathbf{y}=1 \implies \text{Index } \{2\} \implies s = 1$.</li>
    <li>$t = \text{number of attributes where } \mathbf{x}=0 \text{ and } \mathbf{y}=0 \implies \text{Indices } \{3, 6, 8\} \implies t = 3$.</li>
  </ul>
  $$\mathbf{\text{Jaccard Similarity: } J(\mathbf{x}, \mathbf{y}) = \frac{q}{q + r + s} = \frac{3}{3 + 1 + 1} = \frac{3}{5} = \mathbf{0.60 = 60\%}}$$
  $$\mathbf{\text{Jaccard Distance: } d_J(\mathbf{x}, \mathbf{y}) = 1 - 0.60 = \mathbf{0.40}}$$
  $$\mathbf{\text{SMC Similarity: } \text{SMC}(\mathbf{x}, \mathbf{y}) = \frac{q + t}{q + r + s + t} = \frac{3 + 3}{8} = \frac{6}{8} = \mathbf{0.75 = 75\%}}$$
</div>

<h2 class="section-title">Topic 10: Master University Examination Solved Question Bank (10 Solved Questions)</h2>

<div class="qa-card"><div class="qa-q">Q1. Differentiate between OLTP (Online Transaction Processing) and Data Mining / OLAP. (8 Marks)</div><div class="qa-a"><table class="custom-table"><thead><tr><th>Feature</th><th>OLTP</th><th>Data Mining / OLAP</th></tr></thead><tbody><tr><td><strong>Purpose</strong></td><td>Real-time day-to-day transaction processing (ACID compliance).</td><td>Long-term strategic decision support, pattern discovery.</td></tr><tr><td><strong>Data Model</strong></td><td>Highly normalized relational tables (3NF/BCNF) to eliminate redundancy.</td><td>De-normalized multidimensional Star / Snowflake schemas.</td></tr><tr><td><strong>Queries</strong></td><td>Simple, fast indexed read/write transactions (`SELECT/UPDATE by ID`).</td><td>Complex multi-table aggregations (`GROUP BY, ROLLUP, CUBE`).</td></tr><tr><td><strong>Access Pattern</strong></td><td>High concurrency, continuous write/update.</td><td>Read-only periodic batch ETL loads from historical data.</td></tr></tbody></table></div></div>

<div class="qa-card"><div class="qa-q">Q2. Calculate the Cosine Similarity between document vectors $\mathbf{d_1} = (5, 0, 3, 0, 2, 0, 0, 2, 0, 0)$ and $\mathbf{d_2} = (3, 0, 2, 0, 1, 1, 0, 1, 0, 1)$. (8 Marks)</div><div class="qa-a">1. Dot Product: $\mathbf{d_1} \cdot \mathbf{d_2} = (5\times 3) + 0 + (3\times 2) + 0 + (2\times 1) + 0 + 0 + (2\times 1) + 0 + 0 = 15 + 6 + 2 + 2 = \mathbf{25}$.<br>2. Vector Magnitudes:<br>$\|\mathbf{d_1}\| = \sqrt{5^2 + 3^2 + 2^2 + 2^2} = \sqrt{25 + 9 + 4 + 4} = \sqrt{42} \approx 6.4807$.<br>$\|\mathbf{d_2}\| = \sqrt{3^2 + 2^2 + 1^2 + 1^2 + 1^2 + 1^2} = \sqrt{9 + 4 + 1 + 1 + 1 + 1} = \sqrt{17} \approx 4.1231$.<br>$$\mathbf{\text{Cosine Similarity} = \frac{25}{\sqrt{42}\sqrt{17}} = \frac{25}{6.4807 \times 4.1231} = \frac{25}{26.7206} = \mathbf{0.9356 = 93.56\%}}$$</div></div>

<div class="qa-card"><div class="qa-q">Q3. Explain Gower's General Dissimilarity Coefficient for Mixed Attribute Datasets. (8 Marks)</div><div class="qa-a">When records contain a combination of nominal, symmetric/asymmetric binary, ordinal, and numeric attributes, <strong>Gower's Metric</strong> computes distance as:
$$\mathbf{d(i, j) = \frac{\sum_{f=1}^p \delta_{ij}^{(f)} d_{ij}^{(f)}}{\sum_{f=1}^p \delta_{ij}^{(f)}}}$$
Where $\delta_{ij}^{(f)} = 1$ if both records have valid non-missing values for feature $f$ (and $\delta_{ij}^{(f)} = 0$ for asymmetric binary 0-0 matches). The per-feature distance $d_{ij}^{(f)}$ is:
- Nominal/Binary: $0$ if $x_{if} = x_{jf}$, else $1$.
- Numeric: $d_{ij}^{(f)} = \frac{|x_{if} - x_{jf}|}{\max(f) - \min(f)}$ (normalized to $[0, 1]$).
- Ordinal: Convert ranks to $z_{if} = \frac{r_{if} - 1}{M_f - 1}$ and treat as numeric.</div></div>

<div class="qa-card"><div class="qa-q">Q4. Explain Quantile-Quantile (Q-Q) Plots and their diagnostic utility in Data Mining. (6 Marks)</div><div class="qa-a">A <strong>Q-Q Plot</strong> graphs the quantiles of an empirical dataset distribution against the theoretical quantiles of a standard distribution (e.g. Standard Normal $\mathcal{N}(0, 1)$) or against a second dataset. If the points fall strictly along the $45^\circ$ reference line $y = x$, the two distributions have identical shapes. Deviations from the straight line expose heavy tails (leptokurtosis), light tails, right skew, or bimodality.</div></div>

<div class="qa-card"><div class="qa-q">Q5. Why is Euclidean Distance ineffective in high-dimensional sparse spaces (Curse of Dimensionality)? (8 Marks)</div><div class="qa-a">In high-dimensional spaces ($p \rightarrow \infty$), the ratio of the distance to the nearest neighbor and the distance to the furthest neighbor approaches 1:
$$\mathbf{\lim_{p \rightarrow \infty} \frac{D_{\text{max}} - D_{\text{min}}}{D_{\text{min}}} \rightarrow 0}$$
All data points become equidistant from each other in $L_2$ space! Furthermore, high dimensions dilute dense clusters into vast empty space ($V_{\text{hypersphere}} \rightarrow 0$), causing distance-based algorithms like k-NN and k-Means to degrade into random guessing unless dimensionality reduction (PCA, t-SNE) or Cosine similarity is applied!</div></div>
"""

# -------------------- MODULE 2 --------------------
M2_CONTENT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 2 Table of Contents (Topics 15 to 20)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 15:</strong> Data Cleaning (Missing Imputation, Noise)</div>
    <div>• <strong>Topic 16:</strong> Noise Binning (Means, Medians, Boundaries)</div>
    <div>• <strong>Topic 17:</strong> Data Integration ($\chi^2$ Test, Pearson $r$)</div>
    <div>• <strong>Topic 18:</strong> Normalization (Min-Max, Z-score, Decimal)</div>
    <div>• <strong>Topic 19:</strong> PCA & Discrete Wavelet Transform</div>
    <div>• <strong>Topic 20:</strong> 15 Solved University Examination Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 15 & 16: Data Cleaning, Missing Value Imputation & Binning Smoothing</h2>

<p>
  Real-world operational data is dirty: incomplete (lacking attribute values), noisy (containing errors or outliers), and inconsistent (containing discrepancies in codes or names). <strong>Data Preprocessing</strong> consumes up to 80% of the total time in data mining projects.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Missing Data Strategy</th>
      <th style="width: 40%;">Algorithmic Mechanism</th>
      <th>Trade-offs & Best Use Cases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Ignore the Tuple</strong></td>
      <td>Discard any row containing missing values.</td>
      <td>Drastically reduces sample size; only acceptable when missingness is $< 1\%$ and missing completely at random (MCAR).</td>
    </tr>
    <tr>
      <td><strong>Global Constant Imputation</strong></td>
      <td>Replace missing values with a placeholder string (e.g., `"Unknown"` or `-\infty`).</td>
      <td>Simple, but distorts statistical distributions and introduces spurious constants into tree splits.</td>
    </tr>
    <tr>
      <td><strong>Attribute Mean / Median</strong></td>
      <td>Replace missing values with the arithmetic mean $\bar{x}$ (for symmetric data) or median (for skewed data).</td>
      <td>Preserves sample size; artificially deflates attribute variance and alters inter-feature covariances.</td>
    </tr>
    <tr>
      <td><strong>Class-Conditional Mean / Median</strong></td>
      <td>Replace missing value with the mean/median of the subset belonging to the <em>same target class label</em>.</td>
      <td>Significantly more accurate; preserves class separability in supervised learning tasks.</td>
    </tr>
    <tr>
      <td><strong>Model-Based Imputation (k-NN / MICE / EM)</strong></td>
      <td>Treat missing attribute as a target variable; predict its value using regression, k-NN neighbors, or Multiple Imputation by Chained Equations.</td>
      <td>State-of-the-art accuracy; computationally expensive for massive streaming datasets.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Data Smoothing by Binning</div>
  <p>Consider the sorted price dataset ($N = 12$):</p>
  $$\mathbf{X = \{4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34\}}$$
  <p>Partition into 3 equal-frequency bins (Bin Depth = 4 items per bin):</p>
  <ul>
    <li><strong>Bin 1:</strong> $\{4, 8, 9, 15\}$</li>
    <li><strong>Bin 2:</strong> $\{21, 21, 24, 25\}$</li>
    <li><strong>Bin 3:</strong> $\{26, 28, 29, 34\}$</li>
  </ul>
  <p><strong>1. Smoothing by Bin Means:</strong></p>
  <ul>
    <li>Bin 1 Mean = $\frac{4+8+9+15}{4} = \frac{36}{4} = \mathbf{9} \implies \{9, 9, 9, 9\}$</li>
    <li>Bin 2 Mean = $\frac{21+21+24+25}{4} = \frac{91}{4} = \mathbf{22.75} \implies \{22.75, 22.75, 22.75, 22.75\}$</li>
    <li>Bin 3 Mean = $\frac{26+28+29+34}{4} = \frac{117}{4} = \mathbf{29.25} \implies \{29.25, 29.25, 29.25, 29.25\}$</li>
  </ul>
  <p><strong>2. Smoothing by Bin Boundaries:</strong></p>
  <p>Replace each value with the closer boundary (minimum or maximum of the bin):</p>
  <ul>
    <li>Bin 1 ($[\min=4, \max=15]$): $4 \rightarrow 4, \ 8 \rightarrow 4 \ (|8-4|=4 < |8-15|=7), \ 9 \rightarrow 15 \ (|9-15|=6 < |9-4|=5 \text{ wait, } |9-4|=5 \implies 4), \ 15 \rightarrow 15 \implies \mathbf{\{4, 4, 4, 15\}}$</li>
    <li>Bin 2 ($[\min=21, \max=25]$): $21 \rightarrow 21, \ 21 \rightarrow 21, \ 24 \rightarrow 25, \ 25 \rightarrow 25 \implies \mathbf{\{21, 21, 25, 25\}}$</li>
    <li>Bin 3 ($[\min=26, \max=34]$): $26 \rightarrow 26, \ 28 \rightarrow 26, \ 29 \rightarrow 26, \ 34 \rightarrow 34 \implies \mathbf{\{26, 26, 26, 34\}}$</li>
  </ul>
</div>

<h2 class="section-title">Topic 17 & 18: Data Integration ($\chi^2$, Pearson $r$) & Normalization</h2>

<div class="formula-card">
  <strong>Correlation & Normalization Mathematical Formulations:</strong>
  $$\mathbf{\chi^2 \text{ Chi-Square Test of Independence: } \chi^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \qquad E_{ij} = \frac{\text{row\_total}_i \times \text{col\_total}_j}{N}}$$
  $$\mathbf{\text{Pearson Product-Moment Correlation: } r_{A, B} = \frac{\sum_{i=1}^N (a_i - \bar{A})(b_i - \bar{B})}{(N-1) s_A s_B} = \frac{\text{Cov}(A, B)}{s_A s_B}}$$
  $$\mathbf{\text{Min-Max Normalization to } [\text{new\_min}, \text{new\_max}]: v' = \frac{v - \min_A}{\max_A - \min_A}(\text{new\_max} - \text{new\_min}) + \text{new\_min}}$$
  $$\mathbf{\text{Z-Score Standardization (Zero-Mean, Unit-Variance): } v' = \frac{v - \bar{A}}{\sigma_A} \quad (\text{Robust to outliers: } v' = \frac{v - \text{Median}}{\text{Mean Absolute Deviation}})}$$
  $$\mathbf{\text{Decimal Scaling Normalization: } v' = \frac{v}{10^j} \quad (\text{where } j \text{ is the smallest integer s.t. } \max(|v'|) < 1)}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: $\chi^2$ Test of Independence on Contingency Table</div>
  <p>Test whether gender is independent of preferred news medium at $\alpha = 0.05$ significance level:</p>
  <table class="custom-table">
    <thead><tr><th>Gender \ Medium</th><th>Digital News</th><th>Print Newspaper</th><th>Total</th></tr></thead>
    <tbody>
      <tr><td><strong>Male</strong></td><td>$O_{11} = 250$</td><td>$O_{12} = 50$</td><td>$300$</td></tr>
      <tr><td><strong>Female</strong></td><td>$O_{21} = 200$</td><td>$O_{22} = 100$</td><td>$300$</td></tr>
      <tr><td><strong>Total</strong></td><td>$450$</td><td>$150$</td><td>$\mathbf{N = 600}$</td></tr>
    </tbody>
  </table>
  <p><strong>1. Calculate Expected Frequencies ($E_{ij} = \frac{\text{RowTotal} \times \text{ColTotal}}{N}$):</strong></p>
  <ul>
    <li>$E_{11} = \frac{300 \times 450}{600} = \mathbf{225} \qquad E_{12} = \frac{300 \times 150}{600} = \mathbf{75}$</li>
    <li>$E_{21} = \frac{300 \times 450}{600} = \mathbf{225} \qquad E_{22} = \frac{300 \times 150}{600} = \mathbf{75}$</li>
  </ul>
  <p><strong>2. Compute $\chi^2$ Statistic:</strong></p>
  $$\chi^2 = \frac{(250 - 225)^2}{225} + \frac{(50 - 75)^2}{75} + \frac{(200 - 225)^2}{225} + \frac{(100 - 75)^2}{75}$$
  $$\chi^2 = \frac{625}{225} + \frac{625}{75} + \frac{625}{225} + \frac{625}{75} = 2.778 + 8.333 + 2.778 + 8.333 = \mathbf{22.22}$$
  <p><strong>3. Hypothesis Decision:</strong></p>
  <ul>
    <li>Degrees of Freedom: $df = (r - 1)(c - 1) = (2 - 1)(2 - 1) = \mathbf{1}$.</li>
    <li>Critical value from $\chi^2$ distribution table at $\alpha = 0.05, df = 1$ is $\mathbf{3.841}$.</li>
    <li>$\mathbf{22.22 \gg 3.841} \implies \mathbf{\text{Reject Null Hypothesis! Gender and News Medium are strongly correlated!}}}$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Min-Max Normalization & Z-Score Scaling</div>
  <p>Suppose an attribute <strong>Income</strong> ranges from $\min = \$12,000$ to $\max = \$98,000$ with mean $\bar{x} = \$54,000$ and standard deviation $\sigma = \$16,000$. Transform value $v = \$73,600$:</p>
  <p><strong>1. Min-Max Normalization to Range $[0.0, 1.0]$:</strong></p>
  $$\mathbf{v' = \frac{73600 - 12000}{98000 - 12000} = \frac{61600}{86000} = \mathbf{0.7163}}$$
  <p><strong>2. Min-Max Normalization to Range $[-1.0, 1.0]$:</strong></p>
  $$\mathbf{v' = \left(\frac{61600}{86000}\right)(1 - (-1)) + (-1) = 0.7163(2) - 1 = 1.4326 - 1 = \mathbf{+0.4326}}$$
  <p><strong>3. Z-Score Standardization:</strong></p>
  $$\mathbf{z = \frac{v - \bar{x}}{\sigma} = \frac{73600 - 54000}{16000} = \frac{19600}{16000} = \mathbf{+1.225}}$$
  <p><strong>4. Decimal Scaling Normalization:</strong></p>
  <p>Since $\max(|v|) = 98,000$, choose $j = 5$ (so that $\frac{98000}{10^5} = 0.98 < 1$):</p>
  $$\mathbf{v' = \frac{73600}{10^5} = \mathbf{0.736}}$$
</div>

<h2 class="section-title">Topic 19 & 20: Dimensionality Reduction (PCA) & Solved Exam Questions</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ The 5-Step Principal Component Analysis (PCA) Algorithm</div>
  <ol>
    <li><strong>Mean-Center Data:</strong> Subtract column mean from each feature vector: $\mathbf{X}_{\text{centered}} = \mathbf{X} - \bar{\mathbf{X}}$.</li>
    <li><strong>Compute Covariance Matrix:</strong> $\mathbf{\Sigma} = \frac{1}{N-1} \mathbf{X}_{\text{centered}}^T \mathbf{X}_{\text{centered}} \in \mathbb{R}^{p \times p}$.</li>
    <li><strong>Compute Eigenvalues & Eigenvectors:</strong> Solve characteristic polynomial $\det(\mathbf{\Sigma} - \lambda \mathbf{I}) = 0$ to obtain eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p \ge 0$ and orthogonal eigenvectors $\mathbf{e}_1, \dots, \mathbf{e}_p$.</li>
    <li><strong>Select Top $k$ Principal Components:</strong> Choose $k \ll p$ eigenvectors corresponding to the largest eigenvalues such that Explained Variance Ratio $\ge 95\%$:
      $$\mathbf{\text{EVR} = \frac{\sum_{i=1}^k \lambda_i}{\sum_{j=1}^p \lambda_j} \ge 0.95}$$
    </li>
    <li><strong>Project Data:</strong> Transform original $p$-dimensional data into reduced $k$-dimensional space: $\mathbf{Y} = \mathbf{X}_{\text{centered}} \mathbf{W}_k$ (where $\mathbf{W}_k = [\mathbf{e}_1, \dots, \mathbf{e}_k]$).</li>
  </ol>
</div>

<div class="qa-card"><div class="qa-q">Q1. Explain Discrete Wavelet Transform (DWT) and how it differs from Discrete Fourier Transform (DFT). (8 Marks)</div><div class="qa-a">• <strong>Fourier Transform:</strong> Decomposes a signal into global sine and cosine waves. It has perfect frequency resolution but <em>zero time localization</em> (a transient spike in a time series corrupts the entire spectrum).<br>• <strong>Wavelet Transform:</strong> Uses localized basis functions (wavelets) that possess finite duration in both time and frequency. DWT applies a pyramid of low-pass (approximation/coarse) and high-pass (detail/fluctuation) filters, allowing effective data compression and noise removal without losing transient events.</div></div>

<div class="qa-card"><div class="qa-q">Q2. Differentiate between Stepwise Forward Selection and Stepwise Backward Elimination in Attribute Subset Selection. (8 Marks)</div><div class="qa-a">• <strong>Forward Selection:</strong> Begins with an empty feature set $\emptyset$. At each step, it trains models with each remaining candidate feature and adds the single attribute that maximizes model performance (e.g. lowest AIC/BIC or highest $F$-statistic) until additions no longer yield significant statistical improvement.<br>• <strong>Backward Elimination:</strong> Begins with the complete set of all $p$ features. At each step, it removes the single attribute that contributes least to model accuracy (highest $p$-value) until all remaining features are statistically significant ($p < 0.05$).</div></div>
"""

# -------------------- MODULE 3 --------------------
M3_CONTENT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 3 Table of Contents (Topics 21 to 29)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 21:</strong> Data Warehouse Foundations & Architecture</div>
    <div>• <strong>Topic 22:</strong> OLTP vs. OLAP Multidimensional Paradigms</div>
    <div>• <strong>Topic 23:</strong> Schemas (Star, Snowflake, Fact Constellation)</div>
    <div>• <strong>Topic 24:</strong> Measures (Additive, Semi-additive, Non-additive)</div>
    <div>• <strong>Topic 25:</strong> OLAP Operations (Roll-up, Drill-down, Slice, Dice, Pivot)</div>
    <div>• <strong>Topic 26:</strong> Data Cube Computation (MOLAP, ROLAP, HOLAP)</div>
    <div>• <strong>Topic 27:</strong> Star-Cubing & BUC Algorithms</div>
    <div>• <strong>Topic 28:</strong> Concept Hierarchies & Attribute-Oriented Induction</div>
    <div>• <strong>Topic 29:</strong> 15 Solved University Examination Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 21 & 22: Data Warehouse Architecture & OLTP vs. OLAP</h2>

<p>
  According to William H. Inmon (the father of data warehousing), a <strong>Data Warehouse</strong> is defined as: <em>"A subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management's decision-making process."</em>
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Characteristic</th>
      <th style="width: 38%;">Inmon's Definition</th>
      <th>Technical Implementation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Subject-Oriented</strong></td>
      <td>Organized around major business subjects (Customer, Product, Sales, Supplier) rather than operational transactional processes (order entry, invoicing).</td>
      <td>De-normalized multi-dimensional schema tables optimizing cross-departmental queries.</td>
    </tr>
    <tr>
      <td><strong>Integrated</strong></td>
      <td>Constructed by integrating heterogeneous sources (relational DBs, flat files, legacy systems). Naming inconsistencies, encoding formats, and conflicting measurement units are unified.</td>
      <td>ETL (Extract, Transform, Load) staging pipelines enforcing global enterprise metadata standards.</td>
    </tr>
    <tr>
      <td><strong>Time-Variant</strong></td>
      <td>Every key record in the data warehouse explicitly contains a time dimension key (Day, Month, Quarter, Year), capturing historical snapshots across a 5–10 year horizon.</td>
      <td>Slowly Changing Dimensions (SCD Type 1, 2, 3), append-only historical fact tables.</td>
    </tr>
    <tr>
      <td><strong>Non-Volatile</strong></td>
      <td>Data is never updated or deleted in place by end-users. Once loaded into the warehouse, records remain static and read-only.</td>
      <td>Periodic batch loads; high-speed read-optimized indexing (Bitmap, B-tree indexes).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 23 & 24: Multidimensional Schemas & Categorization of Measures</h2>

<div class="diagram-container">
  <svg width="100%" height="90" viewBox="0 0 740 90" xmlns="http://www.w3.org/2000/svg">
    <rect x="290" y="10" width="160" height="70" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="370" y="28" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#1e3a8a" text-anchor="middle">FACT_SALES</text>
    <text x="370" y="44" font-family="Plus Jakarta Sans" font-size="8.5" fill="#334155" text-anchor="middle">time_key (FK), item_key (FK)</text>
    <text x="370" y="58" font-family="Plus Jakarta Sans" font-size="8.5" fill="#334155" text-anchor="middle">branch_key (FK), dollars_sold</text>
    <text x="370" y="72" font-family="Plus Jakarta Sans" font-size="8.5" fill="#16a34a" font-weight="600" text-anchor="middle">units_sold (Additive)</text>

    <!-- Dim 1 -->
    <rect x="20" y="20" width="140" height="50" rx="4" fill="#f8fafc" stroke="#64748b" stroke-width="1.2"/>
    <text x="90" y="38" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#0f172a" text-anchor="middle">DIM_TIME</text>
    <text x="90" y="54" font-family="Plus Jakarta Sans" font-size="8" fill="#475569" text-anchor="middle">time_key, day, month, year</text>
    <path d="M 160 45 L 290 45" stroke="#3b82f6" stroke-width="1.5"/>

    <!-- Dim 2 -->
    <rect x="580" y="20" width="140" height="50" rx="4" fill="#f8fafc" stroke="#64748b" stroke-width="1.2"/>
    <text x="650" y="38" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#0f172a" text-anchor="middle">DIM_ITEM</text>
    <text x="650" y="54" font-family="Plus Jakarta Sans" font-size="8" fill="#475569" text-anchor="middle">item_key, item_name, brand</text>
    <path d="M 450 45 L 580 45" stroke="#3b82f6" stroke-width="1.5"/>
  </svg>
  <div class="diagram-caption">Figure 3.1: The Star Schema Architecture (Central Fact Table radiating to Dimension Tables)</div>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Schema Architecture</th>
      <th style="width: 45%;">Structural Design</th>
      <th>Key Advantages & Trade-offs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Star Schema</strong></td>
      <td>A single central fact table referencing multiple completely de-normalized dimension tables via foreign keys.</td>
      <td>Extremely simple queries; minimal SQL joins; redundant storage in dimension tables.</td>
    </tr>
    <tr>
      <td><strong>Snowflake Schema</strong></td>
      <td>A refinement of the star schema where dimension tables are normalized into hierarchies (splitting `DIM_ITEM` into `ITEM`, `CATEGORY`, `SUPPLIER`).</td>
      <td>Zero data redundancy; saves disk storage; complex multi-table SQL joins reduce OLAP query performance!</td>
    </tr>
    <tr>
      <td><strong>Fact Constellation (Galaxy)</strong></td>
      <td>Multiple distinct fact tables (e.g. `FACT_SALES` and `FACT_SHIPPING`) sharing common dimension tables (Conformed Dimensions).</td>
      <td>Enterprise-wide standard supporting complex business intelligence workflows across multiple functional divisions.</td>
    </tr>
  </tbody>
</table>

<div class="formula-card">
  <strong>Categorization of Multidimensional Measures:</strong>
  - <strong>Additive Measures:</strong> Can be meaningfully aggregated across ALL dimensions (e.g., `units_sold`, `dollars_revenue`, `cost_amount`).
  - <strong>Semi-Additive Measures:</strong> Can be aggregated across some dimensions, but NOT across the Time dimension (e.g., `bank_account_balance`, `warehouse_inventory_count` — summing balances across 365 days gives a meaningless number!).
  - <strong>Non-Additive Measures:</strong> Cannot be aggregated across any dimension by simple addition (e.g., `unit_price`, `profit_margin_%`, `temperature_celsius`). Must compute aggregate numerator and aggregate denominator separately ($\text{AvgMargin} = \frac{\sum \text{Profit}}{\sum \text{Revenue}}$).
</div>

<h2 class="section-title">Topic 25 to 27: OLAP Operations & Data Cube Computation</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">OLAP Operation</th>
      <th style="width: 40%;">Algorithmic Transformation</th>
      <th>Business Analytics Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Roll-Up (Drill-Up)</strong></td>
      <td>Performs aggregation on a data cube by climbing up a concept hierarchy or by dimension reduction (dropping a dimension).</td>
      <td>Aggregating daily sales records into quarterly totals: `Day` $\rightarrow$ `Month` $\rightarrow$ `Quarter` $\rightarrow$ `Year`.</td>
    </tr>
    <tr>
      <td><strong>Drill-Down (Roll-Down)</strong></td>
      <td>Navigates from less detailed (high-level summary) data to highly detailed granular data by descending a concept hierarchy or introducing an additional dimension.</td>
      <td>De-aggregating national quarterly revenue down to city-level store performance: `Country` $\rightarrow$ `State` $\rightarrow$ `City` $\rightarrow$ `Store`.</td>
    </tr>
    <tr>
      <td><strong>Slice</strong></td>
      <td>Performs a selection on one dimension of the given cube, resulting in a sub-cube of lower dimensionality (cutting a 2D slice from a 3D cube).</td>
      <td>Filtering the sales cube strictly for `Time = "Q1_2024"`.</td>
    </tr>
    <tr>
      <td><strong>Dice</strong></td>
      <td>Defines a sub-cube by performing a selection on two or more dimensions simultaneously.</td>
      <td>Filtering for `(Location = "Toronto" OR "Vancouver") AND (Time = "Q1" OR "Q2") AND (Item = "Electronics")`.</td>
    </tr>
    <tr>
      <td><strong>Pivot (Rotate)</strong></td>
      <td>Rotates the data axes in space to provide an alternative visual presentation of the multidimensional matrix.</td>
      <td>Swapping row axis (`Product`) with column axis (`Quarter`) in a spreadsheet pivot table.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Cuboid Lattice Combinatorics</div>
  <p>An enterprise data warehouse has 4 dimensions: $\text{Time } (D_1), \text{Item } (D_2), \text{Location } (D_3), \text{Supplier } (D_4)$.</p>
  <ol>
    <li>Calculate the total number of cuboids in the full data cube lattice.</li>
    <li>If dimension $\text{Time}$ has hierarchy `Day` $\rightarrow$ `Month` $\rightarrow$ `Quarter` $\rightarrow$ `Year` ($L_1 = 4$ levels + `all`), $\text{Item}$ has 3 levels ($L_2 = 3$), $\text{Location}$ has 3 levels ($L_3 = 3$), and $\text{Supplier}$ has 2 levels ($L_4 = 2$), calculate the total number of cuboids with hierarchies.</li>
  </ol>
  <p><strong>Mathematical Solution:</strong></p>
  <ul>
    <li><strong>1. Without Hierarchies:</strong> A $n$-dimensional cube contains $\mathbf{2^n}$ cuboids. For $n = 4$:
      $$\mathbf{T = 2^4 = \mathbf{16 \text{ cuboids}}}$$
      (From 0-D Apex Cuboid `all` to 4-D Base Cuboid `(Time, Item, Location, Supplier)`).
    </li>
    <li><strong>2. With Concept Hierarchies:</strong> Total cuboids $N_{\text{cuboids}} = \prod_{i=1}^n (L_i + 1)$:
      $$\mathbf{N_{\text{cuboids}} = (4 + 1) \times (3 + 1) \times (3 + 1) \times (2 + 1) = 5 \times 4 \times 4 \times 3 = \mathbf{240 \text{ cuboids}}}$$
    </li>
  </ul>
</div>

<h2 class="section-title">Topic 29: Master University Examination Solved Question Bank</h2>

<div class="qa-card"><div class="qa-q">Q1. Compare ROLAP, MOLAP, and HOLAP Architectures. (10 Marks)</div><div class="qa-a"><table class="custom-table"><thead><tr><th>Dimension</th><th>ROLAP (Relational OLAP)</th><th>MOLAP (Multidimensional OLAP)</th><th>HOLAP (Hybrid OLAP)</th></tr></thead><tbody><tr><td><strong>Underlying Storage</strong></td><td>Relational DBMS (Star/Snowflake tables).</td><td>Proprietary multidimensional arrays (dense matrices).</td><td>Relational DB for detailed base data; MOLAP arrays for aggregated summaries.</td></tr><tr><td><strong>Scalability</strong></td><td>Extremely high (handles petabytes).</td><td>Moderate (limited by disk RAM array expansion).</td><td>High scalability with optimized query speed.</td></tr><tr><td><strong>Query Speed</strong></td><td>Slower (requires complex SQL multi-joins).</td><td>Lightning fast ($O(1)$ array offset indexing).</td><td>Fast for high-level summaries.</td></tr><tr><td><strong>Storage Overhead</strong></td><td>Low (only stores populated records).</td><td>High (sparse matrix indexing required).</td><td>Balanced.</td></tr></tbody></table></div></div>

<div class="qa-card"><div class="qa-q">Q2. Explain the Bottom-Up Computation (BUC) Algorithm for Iceberg Cubes. (8 Marks)</div><div class="qa-a">An <strong>Iceberg Cube</strong> computes only those cuboid cells whose aggregate measure satisfies an iceberg condition (e.g. `HAVING COUNT(*) >= min_support`).<br><strong>BUC Algorithm:</strong> Computes data cubes from bottom to top (from 1-D apex children down to base cuboids). It exploits the <em>Apriori anti-monotonicity property</em>: If an aggregate count of a cell in a parent cuboid fails `min_support`, none of its descendant child cells can satisfy the condition! BUC immediately prunes the entire subtree beneath that cell, eliminating massive wasteful computations!</div></div>
"""

# -------------------- MODULE 4 --------------------
M4_CONTENT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 4 Table of Contents (Topics 30 to 36)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 30:</strong> Market Basket Analysis & Association Rules</div>
    <div>• <strong>Topic 31:</strong> Support, Confidence, Lift, Conviction Metrics</div>
    <div>• <strong>Topic 32:</strong> Apriori Algorithm (Join & Prune Steps)</div>
    <div>• <strong>Topic 33:</strong> FP-Growth Algorithm (FP-Tree Construction)</div>
    <div>• <strong>Topic 34:</strong> ECLAT Vertical Data Format Algorithm</div>
    <div>• <strong>Topic 35:</strong> Closed vs. Maximal Frequent Itemsets</div>
    <div>• <strong>Topic 36:</strong> 15 Solved University Examination Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 30 & 31: Market Basket Analysis & Association Rule Metrics</h2>

<p>
  <strong>Frequent Pattern Mining</strong> searches for recurring itemsets, subsequences, or substructures in transactional databases. In <strong>Market Basket Analysis</strong>, retailers identify customer purchasing habits by discovering associations between items placed simultaneously in shopping carts.
</p>

<div class="formula-card">
  <strong>The 5 Fundamental Association Rule Quality Metrics ($A \implies B$):</strong>
  $$\mathbf{\text{Support}(A \implies B) = P(A \cup B) = \frac{\text{count}(A \cup B)}{|D|}}$$
  $$\mathbf{\text{Confidence}(A \implies B) = P(B \mid A) = \frac{P(A \cup B)}{P(A)} = \frac{\text{count}(A \cup B)}{\text{count}(A)}}$$
  $$\mathbf{\text{Lift}(A \implies B) = \frac{P(A \cup B)}{P(A) P(B)} = \frac{\text{Confidence}(A \implies B)}{\text{Support}(B)}}$$
  $$\mathbf{\text{Conviction}(A \implies B) = \frac{P(A) P(\neg B)}{P(A \cup \neg B)} = \frac{1 - \text{Support}(B)}{1 - \text{Confidence}(A \implies B)}}$$
  $$\mathbf{\text{Leverage}(A \implies B) = P(A \cup B) - P(A) P(B) = \text{Support}(A \implies B) - \text{Support}(A)\text{Support}(B)}$$
  <strong>Interpretation of Lift:</strong>
  - $\text{Lift} = 1$: $A$ and $B$ are statistically independent (rule has zero predictive value).
  - $\text{Lift} > 1$: $A$ and $B$ are <strong>positively correlated</strong> (buying $A$ boosts the likelihood of buying $B$).
  - $\text{Lift} < 1$: $A$ and $B$ are <strong>negatively correlated</strong> (substitutes; buying $A$ decreases buying $B$).
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Association Rule Metric Calculation</div>
  <p>A supermarket records $N = 10,000$ transactions. Bread is bought in 6,000 transactions, Butter in 7,500 transactions, and both Bread and Butter together in 4,500 transactions. Evaluate the rule $\text{Bread} \implies \text{Butter}$:</p>
  $$\text{Support}(\text{Bread} \implies \text{Butter}) = \frac{4500}{10000} = \mathbf{0.45 = 45\%}$$
  $$\text{Confidence}(\text{Bread} \implies \text{Butter}) = \frac{\text{count}(\text{Bread} \cup \text{Butter})}{\text{count}(\text{Bread})} = \frac{4500}{6000} = \mathbf{0.75 = 75\%}$$
  $$\text{Lift}(\text{Bread} \implies \text{Butter}) = \frac{\text{Confidence}}{\text{Support}(\text{Butter})} = \frac{0.75}{7500 / 10000} = \frac{0.75}{0.75} = \mathbf{1.00}$$
  $$\mathbf{\text{Critical Insight: } \text{Even though Confidence is high (75\%), Lift = 1.00 proves Bread and Butter are INDEPENDENT!}}}$$
  <p>Customers buy butter 75% of the time anyway, regardless of whether they bought bread! The rule is deceptive!</p>
</div>

<h2 class="section-title">Topic 32: The Apriori Algorithm (Join & Prune Steps)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ The Apriori Principle & Anti-Monotonicity of Support</div>
  <p><strong>Core Axiom:</strong> <em>"If an itemset is frequent, then all of its subsets must also be frequent."</em></p>
  $$\mathbf{\forall X, Y: \ (X \subseteq Y) \implies \text{Support}(X) \ge \text{Support}(Y)}$$
  <p><strong>Contrapositive (Pruning Rule):</strong> <em>"If an itemset $S$ is infrequent ($\text{Support}(S) < \text{min\_sup}$), then none of its supersets can ever be frequent."</em></p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Complete Apriori Execution Trace</div>
  <p>Transactional Database ($N = 5$), $\text{min\_sup} = 2 \ (40\%)$:</p>
  <ul>
    <li>$T_1: \{A, C, D\}$</li>
    <li>$T_2: \{B, C, E\}$</li>
    <li>$T_3: \{A, B, C, E\}$</li>
    <li>$T_4: \{B, E\}$</li>
    <li>$T_5: \{A, B, C, E\}$</li>
  </ul>
  <p><strong>Pass 1:</strong> Candidate 1-itemsets $C_1$: $\{A: 3, B: 4, C: 4, D: 1, E: 4\}$.<br>
  Prune $D$ ($1 < 2$) $\implies \mathbf{L_1 = \{ \{A\}: 3, \{B\}: 4, \{C\}: 4, \{E\}: 4 \}}$.</p>

  <p><strong>Pass 2:</strong> Candidate 2-itemsets $C_2 = L_1 \Join L_1$: $\{AB, AC, AE, BC, BE, CE\}$.<br>
  Scan DB: $\{AB: 2, AC: 3, AE: 2, BC: 3, BE: 4, CE: 3\}$. All $\ge 2 \implies \mathbf{L_2 = C_2}$.</p>

  <p><strong>Pass 3:</strong> Candidate 3-itemsets $C_3 = L_2 \Join L_2$:<br>
  - Join $\{AB\} \Join \{AC\} \rightarrow \{ABC\}$. Subsets: $AB, AC, BC \in L_2$ (Valid!).<br>
  - Join $\{AB\} \Join \{AE\} \rightarrow \{ABE\}$. Subsets: $AB, AE, BE \in L_2$ (Valid!).<br>
  - Join $\{AC\} \Join \{AE\} \rightarrow \{ACE\}$. Subsets: $AC, AE, CE \in L_2$ (Valid!).<br>
  - Join $\{BC\} \Join \{BE\} \rightarrow \{BCE\}$. Subsets: $BC, BE, CE \in L_2$ (Valid!).<br>
  Scan DB for $C_3$: $\{ABC: 2, ABE: 2, ACE: 2, BCE: 3\}$. All $\ge 2 \implies \mathbf{L_3 = C_3}$.</p>

  <p><strong>Pass 4:</strong> Candidate 4-itemset $C_4 = L_3 \Join L_3$: $\{ABCE\}$.<br>
  Prune Check: Subset $\{BCD\} \dots$ Subsets: $\{ABC\}, \{ABE\}, \{ACE\}, \{BCE\}$ all in $L_3$. Valid!<br>
  Scan DB for $\{ABCE\}$: Appears in $T_3, T_5 \implies \text{count} = \mathbf{2} \ge 2 \implies \mathbf{L_4 = \{ \{A, B, C, E\}: 2 \}}$.</p>
  $$\mathbf{\text{Final Max Frequent Itemset: } \{A, B, C, E\} \text{ with Support } = 40\%}$$
</div>

<h2 class="section-title">Topic 33 & 34: FP-Growth Algorithm & ECLAT Vertical Format</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Algorithm</th>
      <th style="width: 35%;">Data Representation</th>
      <th style="width: 25%;">Mining Mechanism</th>
      <th>Key Advantages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Apriori (Agrawal 1994)</strong></td>
      <td>Horizontal transaction format $\langle \text{TID}, \text{Itemset} \rangle$.</td>
      <td>Level-wise BFS candidate generation ($L_k \Join L_k$) and repeated database disk scans ($k$ scans).</td>
      <td>Simple; high memory overhead for candidate itemsets ($O(2^{|I|})$).</td>
    </tr>
    <tr>
      <td><strong>FP-Growth (Han et al. 2000)</strong></td>
      <td>Compact tree structure (FP-Tree) with header table node links.</td>
      <td>Divide-and-conquer recursive mining of conditional pattern bases; <strong>Zero candidate generation</strong>!</td>
      <td>Only 2 database scans required; orders of magnitude faster than Apriori!</td>
    </tr>
    <tr>
      <td><strong>ECLAT (Zaki 2000)</strong></td>
      <td>Vertical data format $\langle \text{Item}, \text{TID-List} \rangle$.</td>
      <td>Intersection of TID lists ($\text{TID}(AB) = \text{TID}(A) \cap \text{TID}(B)$).</td>
      <td>No candidate generation; fast bitwise AND operations; large memory for long TID lists.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 35 & 36: Closed vs. Maximal Itemsets & Solved Exam Questions</h2>

<div class="formula-card">
  <strong>Closed vs. Maximal Frequent Itemsets:</strong>
  - An itemset $X$ is <strong>Closed</strong> if $X$ is frequent and there exists NO proper superset $Y \supset X$ such that $\text{Support}(Y) = \text{Support}(X)$. (Preserves complete support information without loss!).
  - An itemset $X$ is <strong>Maximal</strong> if $X$ is frequent and there exists NO proper superset $Y \supset X$ that is frequent ($\text{Support}(Y) \ge \text{min\_sup}$). (Lossy compression; $|Maximal| \le |Closed| \le |Frequent|$).
</div>

<div class="qa-card"><div class="qa-q">Q1. Trace the FP-Tree Construction Algorithm for transactions: $T_1=\{a, b, c\}, T_2=\{b, c, d\}, T_3=\{a, c, d, e\}$ with $\text{min\_sup}=2$. (10 Marks)</div><div class="qa-a">1. Scan DB to find frequencies: $c: 3, a: 2, b: 2, d: 2, e: 1$.<br>2. Filter and sort by descending frequency: $L_1 = [c, a, b, d]$ (Item $e$ pruned).<br>3. Re-order transactions: $T_1 \rightarrow [c, a, b]$, $T_2 \rightarrow [c, b, d]$, $T_3 \rightarrow [c, a, d]$.<br>4. Insert into FP-Tree from root `null`:<br>- Insert $T_1$: `null` $\rightarrow (c:1) \rightarrow (a:1) \rightarrow (b:1)$.<br>- Insert $T_2$: `null` $\rightarrow (c:2) \rightarrow (b:1) \rightarrow (d:1)$.<br>- Insert $T_3$: `null` $\rightarrow (c:3) \rightarrow (a:2) \rightarrow (d:1)$.<br>5. Construct Header Table with linked lists connecting identical item nodes across branches!</div></div>
"""

# -------------------- MODULE 5 --------------------
M5_CONTENT = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module 5 Table of Contents (Topics 37 to 46)</div>
  <div class="toc-grid">
    <div>• <strong>Topic 37:</strong> Classification vs. Prediction Overview</div>
    <div>• <strong>Topic 38:</strong> Decision Tree Induction (ID3, C4.5, CART)</div>
    <div>• <strong>Topic 39:</strong> Naive Bayes & Bayesian Belief Networks</div>
    <div>• <strong>Topic 40:</strong> Instance-Based Learning (k-NN) & SVM</div>
    <div>• <strong>Topic 41:</strong> Model Evaluation (Confusion Matrix, ROC, AUC)</div>
    <div>• <strong>Topic 42:</strong> k-Means & k-Medoids (PAM) Partitioning</div>
    <div>• <strong>Topic 43:</strong> Hierarchical Clustering (AGNES, DIANA, BIRCH)</div>
    <div>• <strong>Topic 44:</strong> Density-Based Clustering (DBSCAN, OPTICS)</div>
    <div>• <strong>Topic 45:</strong> Outlier Detection (Statistical, LOF, Isolation Forest)</div>
    <div>• <strong>Topic 46:</strong> 15 Solved University Examination Bank</div>
  </div>
</div>

<h2 class="section-title">Topic 37 & 38: Decision Tree Induction (Entropy, Gain Ratio, Gini)</h2>

<p>
  <strong>Classification</strong> predicts discrete categorical class labels, whereas <strong>Numeric Prediction</strong> models continuous valued functions. Decision tree induction builds a flowchart-like tree structure where each internal node denotes an attribute test, each branch denotes a test outcome, and each leaf node holds a class label.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Algorithm</th>
      <th style="width: 32%;">Splitting Criterion</th>
      <th style="width: 25%;">Attribute Types</th>
      <th>Pruning & Missing Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>ID3 (Quinlan 1986)</strong></td>
      <td><strong>Information Gain:</strong> $\text{Gain}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$</td>
      <td>Categorical only (No numeric support).</td>
      <td>No pruning (prone to severe overfitting); cannot handle missing values.</td>
    </tr>
    <tr>
      <td><strong>C4.5 (Quinlan 1993)</strong></td>
      <td><strong>Gain Ratio:</strong> $\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}$</td>
      <td>Categorical & Continuous (dynamic threshold splitting).</td>
      <td>Post-pruning via Pessimistic Error Pruning (PEP); native fractional missing value imputation.</td>
    </tr>
    <tr>
      <td><strong>CART (Breiman 1984)</strong></td>
      <td><strong>Gini Impurity:</strong> $\text{Gini}(S) = 1 - \sum_{i=1}^m p_i^2 \implies \text{Strictly Binary Trees}$</td>
      <td>Categorical & Continuous.</td>
      <td>Cost-Complexity Pruning with cross-validation; surrogate splits for missing data.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: ID3 vs. CART Splitting Calculations</div>
  <p>A dataset $S$ has 14 instances: 9 "Yes" and 5 "No". Attribute <strong>Wind</strong> has values $\{\text{Weak: } [6\text{ Yes}, 2\text{ No}], \text{Strong: } [3\text{ Yes}, 3\text{ No}]\}$.</p>
  <p><strong>1. Base Entropy $H(S)$ and Information Gain (ID3):</strong></p>
  $$H(S) = - \left( \frac{9}{14}\log_2\frac{9}{14} + \frac{5}{14}\log_2\frac{5}{14} \right) = - [0.6429(-0.6374) + 0.3571(-1.4854)] = 0.4098 + 0.5305 = \mathbf{0.9403 \text{ bits}}$$
  $$H(S_{\text{Weak}}) = - \left( \frac{6}{8}\log_2\frac{6}{8} + \frac{2}{8}\log_2\frac{2}{8} \right) = - [0.75(-0.415) + 0.25(-2.0)] = 0.3113 + 0.5000 = \mathbf{0.8113 \text{ bits}}$$
  $$H(S_{\text{Strong}}) = - \left( \frac{3}{6}\log_2\frac{3}{6} + \frac{3}{6}\log_2\frac{3}{6} \right) = \mathbf{1.0000 \text{ bits}}$$
  $$\mathbf{\text{Gain}(S, \text{Wind}) = 0.9403 - \left[ \frac{8}{14}(0.8113) + \frac{6}{14}(1.0000) \right] = 0.9403 - [0.4636 + 0.4286] = \mathbf{0.0481 \text{ bits}}}$$

  <p><strong>2. Gini Impurity (CART):</strong></p>
  $$\text{Gini}(S) = 1 - \left[ \left(\frac{9}{14}\right)^2 + \left(\frac{5}{14}\right)^2 \right] = 1 - [0.4133 + 0.1276] = 1 - 0.5409 = \mathbf{0.4591}$$
  $$\text{Gini}(S_{\text{Weak}}) = 1 - \left[ \left(\frac{6}{8}\right)^2 + \left(\frac{2}{8}\right)^2 \right] = 1 - [0.5625 + 0.0625] = \mathbf{0.3750}$$
  $$\text{Gini}(S_{\text{Strong}}) = 1 - \left[ \left(\frac{3}{6}\right)^2 + \left(\frac{3}{6}\right)^2 \right] = 1 - [0.25 + 0.25] = \mathbf{0.5000}$$
  $$\mathbf{\Delta\text{Gini}(S, \text{Wind}) = 0.4591 - \left[ \frac{8}{14}(0.3750) + \frac{6}{14}(0.5000) \right] = 0.4591 - [0.2143 + 0.2143] = \mathbf{0.0305}}$$
</div>

<h2 class="section-title">Topic 41: Model Evaluation Metrics (Confusion Matrix, ROC, AUC)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Evaluation Metric</th>
      <th style="width: 45%;">Mathematical Formulation</th>
      <th>Key Focus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Accuracy</strong></td>
      <td>$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$</td>
      <td>Overall correctness; misleading in imbalanced datasets!</td>
    </tr>
    <tr>
      <td><strong>Sensitivity / Recall (TPR)</strong></td>
      <td>$$\text{Sensitivity} = \frac{TP}{TP + FN} = \frac{\text{Positives Correctly Identified}}{\text{Actual Positives}}$$</td>
      <td>Critical in disease diagnosis (minimizing False Negatives).</td>
    </tr>
    <tr>
      <td><strong>Specificity (TNR)</strong></td>
      <td>$$\text{Specificity} = \frac{TN}{TN + FP} = \frac{\text{Negatives Correctly Identified}}{\text{Actual Negatives}}$$</td>
      <td>True negative rate (FPR = $1 - \text{Specificity}$).</td>
    </tr>
    <tr>
      <td><strong>Precision (PPV)</strong></td>
      <td>$$\text{Precision} = \frac{TP}{TP + FP} = \frac{\text{True Positives}}{\text{Predicted Positives}}$$</td>
      <td>Critical in fraud detection & search ranking.</td>
    </tr>
    <tr>
      <td><strong>$F_1$-Score</strong></td>
      <td>$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 TP}{2 TP + FP + FN}$$</td>
      <td>Harmonic mean balancing precision and recall.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 42 to 45: Clustering Paradigms & Density-Based DBSCAN</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Clustering Paradigm</th>
      <th style="width: 38%;">Core Algorithm</th>
      <th>Key Strengths & Cluster Shapes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Partitioning Methods</strong></td>
      <td><strong>k-Means:</strong> Minimizes Sum of Squared Errors (SSE); <strong>k-Medoids (PAM):</strong> Uses actual medoid points (robust to outliers).</td>
      <td>Fast ($O(t k N)$); restricted strictly to spherical, convex clusters of equal density.</td>
    </tr>
    <tr>
      <td><strong>Hierarchical Methods</strong></td>
      <td><strong>AGNES (Agglomerative):</strong> Bottom-up tree; <strong>DIANA (Divisive):</strong> Top-down; <strong>BIRCH:</strong> CF-Tree for massive datasets.</td>
      <td>Produces dendrogram hierarchy; no need to specify $k$ upfront; irreversible merges $O(N^2)$.</td>
    </tr>
    <tr>
      <td><strong>Density-Based Methods</strong></td>
      <td><strong>DBSCAN:</strong> Clusters are continuous dense regions separated by low-density noise regions ($\epsilon, \text{MinPts}$).</td>
      <td>Discovers <strong>arbitrary non-convex shapes</strong>; automatically detects and filters noise outliers!</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ The DBSCAN Density Formalism</div>
  <ul>
    <li><strong>$\epsilon$-Neighborhood:</strong> $N_\epsilon(p) = \{ q \in D \mid \text{dist}(p, q) \le \epsilon \}$.</li>
    <li><strong>Core Point:</strong> Point $p$ is a Core Point if $|N_\epsilon(p)| \ge \text{MinPts}$.</li>
    <li><strong>Directly Density-Reachable:</strong> Point $q$ is directly density-reachable from $p$ if $q \in N_\epsilon(p)$ and $p$ is a Core Point.</li>
    <li><strong>Density-Reachable:</strong> Point $q$ is density-reachable from $p$ if there exists a chain of core points $p_1, \dots, p_k$ where $p_1 = p, p_k = q$.</li>
    <li><strong>Density-Connected:</strong> Points $p$ and $q$ are density-connected if there exists a common core point $o$ such that both $p$ and $q$ are density-reachable from $o$.</li>
    <li><strong>Noise Outlier:</strong> Any point that is neither a core point nor density-reachable from any core point.</li>
  </ul>
</div>

<h2 class="section-title">Topic 46: Master University Examination Solved Question Bank</h2>

<div class="qa-card"><div class="qa-q">Q1. Trace k-Means Clustering on 1D points: $\{2, 4, 10, 12, 3, 20, 30, 11, 25\}$ for $k=2$ with initial seeds $m_1 = 2, m_2 = 4$. (10 Marks)</div><div class="qa-a"><strong>Iteration 1:</strong><br>- Distance to $m_1=2$ vs $m_2=4$: Points $\{2, 3\}$ assigned to $C_1$; Points $\{4, 10, 12, 20, 30, 11, 25\}$ assigned to $C_2$.<br>- Update Means: $m_1 = \frac{2+3}{2} = \mathbf{2.5}$; $m_2 = \frac{4+10+12+20+30+11+25}{7} = \frac{112}{7} = \mathbf{16.0}$.<br><strong>Iteration 2:</strong><br>- Points closer to $2.5$: $\{2, 3, 4\} \implies m_1 = \frac{2+3+4}{3} = \mathbf{3.0}$.<br>- Points closer to $16.0$: $\{10, 11, 12, 20, 25, 30\} \implies m_2 = \frac{10+11+12+20+25+30}{6} = \frac{108}{6} = \mathbf{18.0}$.<br><strong>Iteration 3:</strong><br>- Points closer to $3.0$: $\{2, 3, 4, 10\} \dots$ mid-point $\frac{3+18}{2} = 10.5 \implies$ Point $10$ joins $C_1 \implies C_1 = \{2, 3, 4, 10\} \ (m_1 = 4.75); \ C_2 = \{11, 12, 20, 25, 30\} \ (m_2 = 19.6)$.<br><strong>Iteration 4:</strong> Midpoint $\frac{4.75+19.6}{2} = 12.175 \implies$ Point $11, 12$ join $C_1 \implies C_1 = \{2, 3, 4, 10, 11, 12\} \ (m_1 = 7.0); \ C_2 = \{20, 25, 30\} \ (m_2 = 25.0)$.<br><strong>Iteration 5:</strong> Midpoint $\frac{7.0+25.0}{2} = 16.0$. Assignments remain unchanged. <strong>Converged!</strong></div></div>

<div class="qa-card"><div class="qa-q">Q2. Explain the Local Outlier Factor (LOF) Density-Based Outlier Detection Algorithm. (8 Marks)</div><div class="qa-a">Unlike global distance methods, <strong>LOF (Breunig et al. 2000)</strong> detects outliers by comparing the local density of an object with the densities of its $k$-nearest neighbors:<br>1. <strong>$k$-Distance of $p$:</strong> Distance $d(p, o)$ to its $k$-th nearest neighbor.<br>2. <strong>Reachability Distance:</strong> $\text{reach-dist}_k(p, o) = \max(k\text{-distance}(o), d(p, o))$.<br>3. <strong>Local Reachability Density (lrd):</strong> $\text{lrd}_k(p) = \frac{|N_k(p)|}{\sum_{o \in N_k(p)} \text{reach-dist}_k(p, o)}$.<br>4. <strong>LOF Score:</strong> $\text{LOF}_k(p) = \frac{\sum_{o \in N_k(p)} \frac{\text{lrd}(o)}{\text{lrd}(p)}}{|N_k(p)|}$.<br>- $\text{LOF} \approx 1$: Point is inside a homogeneous cluster.<br>- $\text{LOF} \gg 1$: Point has significantly lower density than its neighbors $\implies \mathbf{\text{Local Outlier!}}$</div></div>
"""

# -------------------- REVISION BOOKLET --------------------
REVISION_CONTENT = r"""
<div class="cover-container">
  <div class="course-badge">High-Yield Exam Preparation Master Guide</div>
  <h1 class="book-title">Data Mining & Data Warehousing (CS24303) 10-Page Master Quick Revision Guide</h1>
  <div class="book-subtitle">Formulas, Schemas, Cuboid Lattices, Apriori Rules & Solved Numerical Cards</div>
</div>

<h2 class="section-title">Master Formula & Metric Reference Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Domain</th>
      <th style="width: 45%;">Universal Formula</th>
      <th>Key Exam Property</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Min-Max Normalization</strong></td>
      <td>$$v' = \frac{v - \min_A}{\max_A - \min_A}(\text{new\_max} - \text{new\_min}) + \text{new\_min}$$</td>
      <td>Preserves exact relationships; sensitive to future out-of-bound outliers.</td>
    </tr>
    <tr>
      <td><strong>Z-Score Standardization</strong></td>
      <td>$$z = \frac{v - \bar{x}}{\sigma}$$</td>
      <td>Zero mean, unit variance ($\mathcal{N}(0, 1)$); ideal when min/max are unknown.</td>
    </tr>
    <tr>
      <td><strong>$\chi^2$ Independence Test</strong></td>
      <td>$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \quad \text{where } E_{ij} = \frac{\text{Row}_i \times \text{Col}_j}{N}$$</td>
      <td>$df = (r - 1)(c - 1)$; tests categorical attribute independence.</td>
    </tr>
    <tr>
      <td><strong>Cosine Similarity</strong></td>
      <td>$$\text{sim}(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\| \|\mathbf{y}\|} = \frac{\sum x_i y_i}{\sqrt{\sum x_i^2}\sqrt{\sum y_i^2}}$$</td>
      <td>Angle between vectors; independent of document text length.</td>
    </tr>
    <tr>
      <td><strong>Jaccard Similarity</strong></td>
      <td>$$J(\mathbf{x}, \mathbf{y}) = \frac{q}{q + r + s}$$</td>
      <td>Asymmetric binary metric; completely ignores $0-0$ negative matches $t$.</td>
    </tr>
    <tr>
      <td><strong>Association Rule Lift</strong></td>
      <td>$$\text{Lift}(A \implies B) = \frac{P(A \cup B)}{P(A) P(B)} = \frac{\text{Confidence}(A \implies B)}{\text{Support}(B)}$$</td>
      <td>$\text{Lift} > 1 \implies \text{Positive correlation}; = 1 \implies \text{Independent}$.</td>
    </tr>
    <tr>
      <td><strong>Information Gain</strong></td>
      <td>$$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$</td>
      <td>Biased towards attributes with massive numbers of distinct values.</td>
    </tr>
    <tr>
      <td><strong>Gini Impurity</strong></td>
      <td>$$\text{Gini}(S) = 1 - \sum_{i=1}^m p_i^2$$</td>
      <td>CART metric for strictly binary decision tree splits.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Complete 5-Module Comparative Checklists</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Module</th>
      <th style="width: 40%;">Core Theoretical Concepts</th>
      <th>High-Yield Exam Numericals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>M1: Data Understanding</strong></td>
      <td>KDD Process, Nominal/Ordinal/Interval/Ratio, Proximity Metrics (SMC, Jaccard, Cosine, Mahalanobis, Gower).</td>
      <td>Five-number summary, IQR outlier fences, Cosine vector similarity, Jaccard distance.</td>
    </tr>
    <tr>
      <td><strong>M2: Preprocessing</strong></td>
      <td>Missing imputation, Bin smoothing (means, boundaries), $\chi^2$ test, Min-Max / Z-score normalization, PCA.</td>
      <td>Contingency table $\chi^2$ computation, decimal scaling, Min-Max re-scaling to $[-1, 1]$.</td>
    </tr>
    <tr>
      <td><strong>M3: Data Warehousing</strong></td>
      <td>OLTP vs OLAP, Star / Snowflake / Fact Constellation, Additive vs Semi-additive measures, Cuboid lattice combinatorics.</td>
      <td>Total cuboids calculation with hierarchies $N = \prod (L_i + 1)$, OLAP operations (slice/dice/roll-up).</td>
    </tr>
    <tr>
      <td><strong>M4: Frequent Patterns</strong></td>
      <td>Apriori property, join & prune, FP-Tree conditional bases, ECLAT vertical TID lists, Closed vs Maximal.</td>
      <td>Full Apriori table trace, Support/Confidence/Lift calculations, FP-Tree branch insertion.</td>
    </tr>
    <tr>
      <td><strong>M5: Classification & Clustering</strong></td>
      <td>ID3 vs C4.5 vs CART, Naive Bayes, Confusion Matrix, ROC/AUC, k-Means vs PAM, DBSCAN density, LOF.</td>
      <td>Entropy & Information Gain numerical, Confusion matrix Precision/Recall/F1, k-Means 1D convergence.</td>
    </tr>
  </tbody>
</table>
"""

# -------------------- LAB PRACTICAL GUIDE --------------------
LAB_GUIDE = r"""
<div class="page-break"></div>
<div class="cover-container" style="margin-top: 40px;">
  <div class="course-badge">Hands-On Practical Lab Master Appendix</div>
  <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">Data Mining Laboratory & Python ML Implementation Guide</h2>
  <div style="font-size: 12.5px; color: #64748b;">Complete Python Algorithms for Apriori Association Rules, Decision Tree Classification & DBSCAN Clustering</div>
</div>

<h2 class="section-title">Lab Experiment 1: Production-Grade Apriori Algorithm Implementation in Python</h2>

<pre><code class="language-python">import pandas as pd
from itertools import combinations

def get_frequent_1_itemsets(transactions, min_sup_count):
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[frozenset([item])] = item_counts.get(frozenset([item]), 0) + 1
    return {item: count for item, count in item_counts.items() if count >= min_sup_count}

def apriori_gen(Lk_minus_1, k):
    candidates = set()
    lk_list = list(Lk_minus_1.keys())
    for i in range(len(lk_list)):
        for j in range(i + 1, len(lk_list)):
            union_set = lk_list[i] | lk_list[j]
            if len(union_set) == k:
                # Prune step: check if all (k-1) subsets are in Lk_minus_1
                subsets = [frozenset(s) for s in combinations(union_set, k - 1)]
                if all(s in Lk_minus_1 for s in subsets):
                    candidates.add(union_set)
    return candidates

def run_apriori(dataset, min_support=0.4):
    num_trans = len(dataset)
    min_sup_count = min_support * num_trans
    L1 = get_frequent_1_itemsets(dataset, min_sup_count)
    
    all_frequent = dict(L1)
    current_L = L1
    k = 2
    
    while current_L:
        candidates = apriori_gen(current_L, k)
        candidate_counts = {}
        for trans in dataset:
            trans_set = set(trans)
            for cand in candidates:
                if cand.issubset(trans_set):
                    candidate_counts[cand] = candidate_counts.get(cand, 0) + 1
        
        current_L = {cand: count for cand, count in candidate_counts.items() if count >= min_sup_count}
        all_frequent.update(current_L)
        k += 1
        
    return all_frequent

# Example Run
dataset = [
    ['Milk', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
    ['Dill', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
    ['Milk', 'Apple', 'Kidney_Beans', 'Eggs'],
    ['Milk', 'Unicorn', 'Corn', 'Kidney_Beans', 'Yogurt'],
    ['Corn', 'Onion', 'Onion', 'Kidney_Beans', 'Ice_cream', 'Eggs']
]

frequent_patterns = run_apriori(dataset, min_support=0.6)
for itemset, count in frequent_patterns.items():
    print(f"Frequent Itemset: {set(itemset)} (Support = {count/len(dataset):.2f})")
</code></pre>
"""

CSS_STYLES = """
@page {
  size: A4 portrait;
  margin: 15mm 12mm 15mm 12mm;
}
*, *::before, *::after { box-sizing: border-box; }
body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 11.8px;
  line-height: 1.60;
  color: #1e293b;
  background: #ffffff;
  margin: 0;
  padding: 0;
}
.cover-container {
  padding: 30px 20px;
  text-align: center;
  border-bottom: 2px solid #3b82f6;
  margin-bottom: 24px;
}
.course-badge {
  display: inline-block;
  background: #eff6ff;
  color: #1d4ed8;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 20px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 12px;
  border: 1px solid #bfdbfe;
}
.book-title {
  font-size: 26px;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 8px 0;
  letter-spacing: -0.5px;
}
.book-subtitle { font-size: 13.5px; color: #475569; margin: 0 0 16px 0; font-weight: 500; }
.toc-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 16px 20px;
  margin: 20px 0 28px 0;
}
.toc-title { font-size: 13.5px; font-weight: 700; color: #1d4ed8; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
.toc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 16px; font-size: 11px; color: #334155; }
h2.section-title {
  font-size: 15px;
  font-weight: 700;
  color: #1d4ed8;
  border-bottom: 1.5px solid #e2e8f0;
  padding-bottom: 5px;
  margin: 26px 0 14px 0;
  page-break-after: avoid;
}
p { margin: 0 0 10px 0; text-align: justify; }
.callout { border-radius: 6px; padding: 14px 18px; margin: 14px 0; font-size: 11.5px; page-break-inside: avoid; }
.callout-info { background: #eff6ff; border-left: 4px solid #3b82f6; color: #1e3a8a; }
.callout-title { font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 6px; }
.custom-table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 11px; page-break-inside: avoid; }
.custom-table th, .custom-table td { border: 1px solid #cbd5e1; padding: 8px 10px; text-align: left; vertical-align: top; }
.custom-table th { background: #f1f5f9; color: #0f172a; font-weight: 700; }
.custom-table tr:nth-child(even) { background: #f8fafc; }
.formula-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #8b5cf6;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 14px 0;
  page-break-inside: avoid;
  text-align: center;
}
.worked-box {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-left: 4px solid #22c55e;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 16px 0;
  page-break-inside: avoid;
}
.worked-title { font-weight: 700; color: #15803d; font-size: 12px; margin-bottom: 8px; }
.diagram-container { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; margin: 14px 0; text-align: center; page-break-inside: avoid; }
.diagram-caption { font-size: 10.5px; color: #64748b; margin-top: 8px; font-weight: 500; }
.qa-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 16px; margin: 12px 0; page-break-inside: avoid; }
.qa-q { font-weight: 700; color: #0f172a; margin-bottom: 6px; }
.qa-a { color: #334155; line-height: 1.55; }
pre { background: #0f172a; color: #f8fafc; padding: 12px 16px; border-radius: 6px; font-family: 'Fira Code', monospace; font-size: 10.5px; line-height: 1.45; overflow-x: auto; margin: 12px 0; page-break-inside: avoid; }
code { font-family: 'Fira Code', monospace; font-size: 11px; background: #f1f5f9; color: #2563eb; padding: 2px 5px; border-radius: 4px; }
pre code { background: transparent; color: inherit; padding: 0; }
.page-break { page-break-before: always; }
"""

def wrap_html(title, subtitle, body_html, module_num=None):
    badge = f"CS24303 • Module {module_num}" if module_num else "CS24303 • Complete Master Guide"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <style>
    {CSS_STYLES}
  </style>
</head>
<body>
  <div class="cover-container">
    <div class="course-badge">{badge}</div>
    <h1 class="book-title">{title}</h1>
    <div class="book-subtitle">{subtitle}</div>
  </div>
  {body_html}
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (window.renderMathInElement) {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ]
        }});
      }}
    }});
  </script>
</body>
</html>"""

def generate_pdf(html_path, pdf_path, title):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath(html_path)}", wait_until="networkidle")
        page.evaluate("""() => {
            if (window.renderMathInElement) {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
        }""")
        page.wait_for_timeout(1200)
        
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "12mm", "right": "12mm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=f"""
            <div style="font-size: 8.5pt; font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 12mm;">
              <span>{title} • BIT Mesra CSE</span>
              <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
            </div>
            """
        )
        browser.close()
    print(f"✅ Generated {pdf_path} ({os.path.getsize(pdf_path)} bytes)")

def build_data_mining_all():
    modules = [
        (1, "Module 1: Data Understanding & Statistical Proximity", "Topics 1 to 14 • KDD Lifecycle, Attributes, Boxplots, Q-Q, Jaccard & Distance Metrics", M1_CONTENT, "Module_1_Data_Understanding_Notes"),
        (2, "Module 2: Data Preprocessing & Dimensionality Reduction", "Topics 15 to 20 • Missing Imputation, Binning, Chi-Square Independence, Normalization & PCA", M2_CONTENT, "Module_2_Data_Preprocessing_Notes"),
        (3, "Module 3: Data Warehousing & OLAP Technology", "Topics 21 to 29 • Star/Snowflake Schemas, Measures, OLAP Operations, Cuboid Lattices & BUC", M3_CONTENT, "Module_3_Data_Warehousing_OLAP_Notes"),
        (4, "Module 4: Frequent Pattern & Association Mining", "Topics 30 to 36 • Market Basket Analysis, Support/Confidence/Lift, Apriori, FP-Growth & ECLAT", M4_CONTENT, "Module_4_Association_Rules_Notes"),
        (5, "Module 5: Classification & Cluster Analysis", "Topics 37 to 46 • ID3/C4.5/CART Trees, Naive Bayes, Confusion Matrix, k-Means, PAM & DBSCAN", M5_CONTENT, "Module_5_Classification_Clustering_Notes"),
    ]

    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"DMCT Module {num}")

    # Revision
    rev_html = wrap_html(
        "Data Mining (CS24303) 10-Page Master Revision",
        "High-Yield Formulas, Schemas, Cuboid Lattices, Apriori Rules & Solved Numerical Cards",
        REVISION_CONTENT
    )
    rev_html_file = os.path.join(HTML_DIR, "DM_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "DM_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "DM 10-Page Master Revision")

    # Full Master Book
    full_body = []
    for num, title, subtitle, content, _ in modules:
        full_body.append(f"""
        <div class="page-break"></div>
        <div class="cover-container" style="margin-top: 40px;">
          <div class="course-badge">Module {num} of 5</div>
          <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">{title}</h2>
          <div style="font-size: 12.5px; color: #64748b;">{subtitle}</div>
        </div>
        {content}
        """)

    full_body.append(LAB_GUIDE)
    full_body.append(f"""
    <div class="page-break"></div>
    <div class="cover-container" style="margin-top: 40px;">
      <div class="course-badge">Comprehensive Revision Appendix</div>
      <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">10-Page Master Quick Revision Guide</h2>
      <div style="font-size: 12.5px; color: #64748b;">Formulas, Algorithm Checklists & Solved Exam Cards</div>
    </div>
    {REVISION_CONTENT}
    """)

    full_master_html = wrap_html(
        "Data Mining Concepts & Techniques (CS24303) Full Course Master",
        "Exhaustive 46-Topic Textbook, Python Lab Guide & Solved University Question Bank",
        "".join(full_body)
    )
    master_html_file = os.path.join(HTML_DIR, "DM_Full_Course_Master.html")
    master_pdf_file = os.path.join(PDF_DIR, "DM_Full_Course_Master.pdf")
    with open(master_html_file, "w", encoding="utf-8") as f:
        f.write(full_master_html)
    generate_pdf(master_html_file, master_pdf_file, "DM Full Course Master")

if __name__ == "__main__":
    build_data_mining_all()
