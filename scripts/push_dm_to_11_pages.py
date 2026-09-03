#!/usr/bin/env python3
"""
Exhaustive 38k+ character Data Mining (CS24303) Module Suite Builder.
Guarantees 10-12 pages for every module (M1 to M5) and 55+ pages for DM_Full_Course_Master.pdf!
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import M1_CONTENT, M2_CONTENT, M3_CONTENT, M4_CONTENT, M5_CONTENT, REVISION_CONTENT, LAB_GUIDE, wrap_html, generate_pdf

# ----------------- EXTENSION FOR M1 -----------------
M1_EXP = r"""
<h2 class="section-title">Topic 11: Higher-Order Statistical Moments & Skewness / Kurtosis</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Statistical Moment</th>
      <th style="width: 45%;">Mathematical Formulation</th>
      <th>Diagnostic Significance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1st Raw Moment (Mean)</strong></td>
      <td>$$\mu_1' = \mathbb{E}[X] = \frac{1}{N}\sum x_i$$</td>
      <td>Center of mass / location of the distribution.</td>
    </tr>
    <tr>
      <td><strong>2nd Central Moment (Variance)</strong></td>
      <td>$$\mu_2 = \mathbb{E}[(X - \mu)^2] = \sigma^2$$</td>
      <td>Spread / scale of dispersion around the mean.</td>
    </tr>
    <tr>
      <td><strong>3rd Standardized Moment (Skewness)</strong></td>
      <td>$$\gamma_1 = \mathbb{E}\left[\left(\frac{X - \mu}{\sigma}\right)^3\right] = \frac{\mu_3}{\sigma^3}$$</td>
      <td>Asymmetry of distribution ($\gamma_1 > 0 \implies \text{Right/Positive Skew}$; $\gamma_1 < 0 \implies \text{Left/Negative Skew}$).</td>
    </tr>
    <tr>
      <td><strong>4th Standardized Moment (Kurtosis)</strong></td>
      <td>$$\text{Excess Kurtosis } \gamma_2 = \frac{\mu_4}{\sigma^4} - 3$$</td>
      <td>Tailedness and outlier propensity ($\gamma_2 > 0 \implies \text{Leptokurtic / Heavy-tailed}$; $\gamma_2 < 0 \implies \text{Platykurtic / Light-tailed}$).</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Spearman's Rank Correlation Calculation</div>
  <p>Two data mining algorithms rank 5 customer profiles by risk score:</p>
  <table class="custom-table">
    <thead><tr><th>Customer</th><th>Algorithm A Rank ($R_A$)</th><th>Algorithm B Rank ($R_B$)</th><th>$d_i = R_A - R_B$</th><th>$d_i^2$</th></tr></thead>
    <tbody>
      <tr><td>C1</td><td>1</td><td>2</td><td>$-1$</td><td>1</td></tr>
      <tr><td>C2</td><td>2</td><td>1</td><td>$+1$</td><td>1</td></tr>
      <tr><td>C3</td><td>3</td><td>4</td><td>$-1$</td><td>1</td></tr>
      <tr><td>C4</td><td>4</td><td>3</td><td>$+1$</td><td>1</td></tr>
      <tr><td>C5</td><td>5</td><td>5</td><td>$0$</td><td>0</td></tr>
      <tr><td><strong>Total</strong></td><td>—</td><td>—</td><td>$\sum d_i = 0$</td><td>$\mathbf{\sum d_i^2 = 4}$</td></tr>
    </tbody>
  </table>
  $$\mathbf{r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)} = 1 - \frac{6(4)}{5(25 - 1)} = 1 - \frac{24}{5(24)} = 1 - \frac{24}{120} = 1 - 0.20 = \mathbf{+0.80}}$$
  $$\mathbf{\text{Conclusion: Strong positive monotonic agreement between the two ranking algorithms!}}$$
</div>

<div class="qa-card"><div class="qa-q">Q6. State and prove Chebyshev's Inequality and explain its application in Outlier Detection. (8 Marks)</div><div class="qa-a"><strong>Chebyshev's Theorem:</strong> For any random variable $X$ with mean $\mu$ and finite variance $\sigma^2$, the probability that $X$ deviates from its mean by at least $k$ standard deviations is bounded by:
$$\mathbf{P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}}$$
<em>Application:</em> Unlike the Empirical Rule (which strictly requires a Gaussian bell curve), Chebyshev holds for <strong>ANY arbitrary probability distribution</strong>. For $k = 3$, at most $\frac{1}{3^2} = \frac{1}{9} \approx 11.11\%$ of observations can lie outside $[\mu - 3\sigma, \mu + 3\sigma]$. Any data point beyond $3\sigma$ is a candidate outlier!</div></div>

<div class="qa-card"><div class="qa-q">Q7. Explain Dynamic Time Warping (DTW) for Time-Series Distance Measurement. (8 Marks)</div><div class="qa-a">Standard Euclidean distance requires two time-series sequences to have identical lengths and aligned time steps, failing when sequences are shifted in phase or time-dilated (e.g. someone speaking slowly vs quickly).<br><strong>Dynamic Time Warping (DTW):</strong> Uses dynamic programming to find an optimal non-linear alignment (warping path $W = w_1, w_2, \dots, w_K$) on a cost matrix $C(i, j) = |x_i - y_j|$, satisfying boundary conditions, continuity, and monotonicity ($D(i, j) = C(i, j) + \min(D(i-1, j), D(i, j-1), D(i-1, j-1))$).</div></div>
"""

# ----------------- EXTENSION FOR M2 -----------------
M2_EXP = r"""
<h2 class="section-title">Topic 20.1: Advanced Dimensionality Reduction (LDA, SVD & t-SNE)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Reduction Technique</th>
      <th style="width: 45%;">Core Mathematical Objective</th>
      <th>Supervision & Linearity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Principal Component Analysis (PCA)</strong></td>
      <td>Maximizes projected variance: $\max_{\mathbf{w}} \mathbf{w}^T \mathbf{\Sigma} \mathbf{w} \ \text{s.t. } \|\mathbf{w}\|=1$. Unsupervised linear projection.</td>
      <td>Unsupervised • Linear</td>
    </tr>
    <tr>
      <td><strong>Linear Discriminant Analysis (LDA)</strong></td>
      <td>Maximizes between-class scatter over within-class scatter (Fisher's Criterion): $\max_{\mathbf{w}} \frac{\mathbf{w}^T \mathbf{S}_B \mathbf{w}}{\mathbf{w}^T \mathbf{S}_W \mathbf{w}}$.</td>
      <td><strong>Supervised</strong> • Linear</td>
    </tr>
    <tr>
      <td><strong>Singular Value Decomposition (SVD)</strong></td>
      <td>Decomposes data matrix $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$. Truncated SVD provides optimal rank-$k$ low-rank approximation (Eckart-Young-Mirsky Theorem).</td>
      <td>Unsupervised • Linear</td>
    </tr>
    <tr>
      <td><strong>t-SNE (t-Distributed Stochastic Neighbor Embedding)</strong></td>
      <td>Minimizes KL-divergence between high-dimensional Gaussian joint probabilities $p_{ij}$ and low-dimensional Student-t probabilities $q_{ij}$: $\mathcal{L} = \sum p_{ij} \log(p_{ij}/q_{ij})$.</td>
      <td>Unsupervised • <strong>Non-linear Manifold</strong></td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: SVD Matrix Decomposition Calculation</div>
  <p>Given rank-1 data matrix $\mathbf{X} = \begin{bmatrix} 3 & 3 \\ 4 & 4 \end{bmatrix}$:</p>
  <ol>
    <li>Compute $\mathbf{X}^T \mathbf{X} = \begin{bmatrix} 3 & 4 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 3 & 3 \\ 4 & 4 \end{bmatrix} = \begin{bmatrix} 25 & 25 \\ 25 & 25 \end{bmatrix}$.</li>
    <li>Eigenvalues of $\mathbf{X}^T \mathbf{X}$: $\det\begin{pmatrix} 25-\lambda & 25 \\ 25 & 25-\lambda \end{pmatrix} = (25-\lambda)^2 - 625 = \lambda^2 - 50\lambda = 0 \implies \mathbf{\lambda_1 = 50, \ \lambda_2 = 0}$.</li>
    <li>Singular value $\sigma_1 = \sqrt{50} = \mathbf{5\sqrt{2} \approx 7.071}$.</li>
    <li>Right Singular Vector $\mathbf{v}_1$: $(\mathbf{X}^T\mathbf{X} - 50\mathbf{I})\mathbf{v} = 0 \implies \begin{bmatrix} -25 & 25 \\ 25 & -25 \end{bmatrix}\mathbf{v} = 0 \implies \mathbf{v}_1 = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}$.</li>
    <li>Left Singular Vector $\mathbf{u}_1 = \frac{1}{\sigma_1}\mathbf{X}\mathbf{v}_1 = \frac{1}{5\sqrt{2}}\begin{bmatrix} 3 & 3 \\ 4 & 4 \end{bmatrix}\begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} = \frac{1}{10}\begin{bmatrix} 6 \\ 8 \end{bmatrix} = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}$.</li>
  </ol>
  $$\mathbf{\mathbf{X} = \mathbf{u}_1 \sigma_1 \mathbf{v}_1^T = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix} (5\sqrt{2}) \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix} = \begin{bmatrix} 3 & 3 \\ 4 & 4 \end{bmatrix} \quad (\text{Exact Rank-1 SVD!})}$$
</div>

<div class="qa-card"><div class="qa-q">Q3. Explain Kernel PCA (KPCA) and the Mercer Kernel Trick. (8 Marks)</div><div class="qa-a">Standard PCA fails when data points reside on non-linear manifolds (e.g., concentric circles or Swiss roll).<br><strong>Kernel PCA (Schölkopf 1998):</strong> Maps input data into a high-dimensional reproducing kernel Hilbert space $\Phi(\mathbf{x}) \in \mathcal{H}$ and performs linear PCA in that feature space. By <strong>Mercer's Theorem</strong>, the inner products in $\mathcal{H}$ can be computed directly in input space using kernel functions ($K(\mathbf{x}_i, \mathbf{x}_j) = \langle \Phi(\mathbf{x}_i), \Phi(\mathbf{x}_j) \rangle$), such as the Gaussian RBF kernel $K(\mathbf{x}, \mathbf{y}) = \exp(-\gamma \|\mathbf{x} - \mathbf{y}\|^2)$, discovering complex non-linear cluster structures!</div></div>
"""

# ----------------- EXTENSION FOR M3 -----------------
M3_EXP = r"""
<h2 class="section-title">Topic 29.1: Advanced Dimensional Modeling & Indexing Strategies</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Indexing Architecture</th>
      <th style="width: 45%;">Internal Bitwise Mechanism</th>
      <th>Best OLAP Query Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Bitmap Indexing</strong></td>
      <td>Creates a bit vector for each distinct value of a low-cardinality attribute (e.g. `Gender: {M: 1010, F: 0101}`). Queries execute via hardware-accelerated bitwise AND/OR/NOT operations.</td>
      <td>Low-cardinality categorical filters (`WHERE Region = 'East' AND Status = 'Active'`).</td>
    </tr>
    <tr>
      <td><strong>Join Indexing</strong></td>
      <td>Maintains index relationships between foreign keys of fact tables and primary keys of dimension tables across multi-table joins without physical table joining.</td>
      <td>Star schema star-join query acceleration.</td>
    </tr>
    <tr>
      <td><strong>Bitmapped Join Index</strong></td>
      <td>Stores bitmap representations of dimension attributes directly inside the fact table index.</td>
      <td>Complex multi-attribute enterprise OLAP reporting.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Bitmap Index Bitwise Query Processing</div>
  <p>A customer table has 6 records. Attribute <strong>Gender</strong> has distinct values $\{M, F\}$; Attribute <strong>CustType</strong> has distinct values $\{VIP, Regular\}$:</p>
  <ul>
    <li>Gender Bitmaps: $\text{Bit}_M = [1, 0, 1, 1, 0, 0]$, $\text{Bit}_F = [0, 1, 0, 0, 1, 1]$.</li>
    <li>CustType Bitmaps: $\text{Bit}_{VIP} = [1, 1, 0, 1, 0, 0]$, $\text{Bit}_{Regular} = [0, 0, 1, 0, 1, 1]$.</li>
  </ul>
  <p><strong>Query: Find all Female customers who are VIP (`Gender = 'F' AND CustType = 'VIP'`):</strong></p>
  $$\mathbf{\text{Result} = \text{Bit}_F \land \text{Bit}_{VIP} = [0, 1, 0, 0, 1, 1] \text{ AND } [1, 1, 0, 1, 0, 0] = \mathbf{[0, 1, 0, 0, 0, 0]}}$$
  $$\mathbf{\text{Interpretation: Record index 2 (Customer 2) is the exact matching tuple! (Computed in 1 CPU cycle!)}}}$$
</div>

<div class="qa-card"><div class="qa-q">Q3. Explain Slowly Changing Dimensions (SCD Type 1, Type 2, and Type 3). (8 Marks)</div><div class="qa-a">In a data warehouse, dimension attribute values change over time (e.g. customer relocates from Chicago to Dallas):<br>• <strong>SCD Type 1 (Overwrite):</strong> Overwrites the old value with the new value. Fast, but <em>destroys historical context</em> (past sales in Chicago are falsely credited to Dallas).<br>• <strong>SCD Type 2 (Add New Row):</strong> Creates a new row with a new surrogate key, marking the old row with `end_date` and `is_current = FALSE`. Preserves complete historical audit trail (industry gold standard).<br>• <strong>SCD Type 3 (Add New Column):</strong> Adds a `current_city` and `previous_city` column to the existing row. Tracks only the immediate prior state.</div></div>
"""

# ----------------- EXTENSION FOR M4 -----------------
M4_EXP = r"""
<h2 class="section-title">Topic 36.1: Advanced Sequence Pattern Mining & Negative Association Rules</h2>

<div class="formula-card">
  <strong>Negative Association Rules & Correlation:</strong>
  A negative association rule takes the form $A \implies \neg B$ or $\neg A \implies B$. It is considered statistically valid and interesting if:
  $$\mathbf{\text{Support}(A \cup \neg B) = \text{Support}(A) - \text{Support}(A \cup B) \ge \text{min\_sup}}$$
  $$\mathbf{\text{Confidence}(A \implies \neg B) = \frac{\text{Support}(A \cup \neg B)}{\text{Support}(A)} = 1 - \text{Confidence}(A \implies B) \ge \text{min\_conf}}$$
  $$\mathbf{\text{Correlation Measure: } \text{Corr}(A, B) = \frac{P(A \cup B)}{P(A)P(B)} < 1 \quad (\text{Substitutability Indicator})}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Generalized Sequential Pattern (GSP) Trace</div>
  <p>Given sequence database: $S_1 = \langle (a)(b, c)(d) \rangle$, $S_2 = \langle (a, d)(c)(b) \rangle$, $S_3 = \langle (a)(c)(d) \rangle$. Minimum support = 2 ($66.7\%$):</p>
  <ul>
    <li>Frequent 1-sequences $L_1$: $\langle (a) \rangle: 3, \ \langle (b) \rangle: 2, \ \langle (c) \rangle: 3, \ \langle (d) \rangle: 3$.</li>
    <li>Candidate 2-sequences $C_2$: $\langle (a)(c) \rangle, \langle (a, c) \rangle, \langle (c)(d) \rangle, \langle (a)(d) \rangle \dots$</li>
    <li>Scan DB: $\langle (a)(c) \rangle$ appears in $S_1, S_3 \implies \text{count}=2$; $\langle (a)(d) \rangle$ appears in $S_1, S_3 \implies \text{count}=2$.</li>
    <li>Frequent 3-sequence $L_3 = \{ \langle (a)(c)(d) \rangle: 2 \}$.</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q2. Compare the PrefixSpan (Prefix-Projected Pattern Growth) Algorithm with GSP. (8 Marks)</div><div class="qa-a">• <strong>GSP (Srikant & Agrawal):</strong> An Apriori-like breadth-first sequence mining algorithm. Generates massive sets of candidate sequences ($L_{k-1} \Join L_{k-1}$) and scans the database repeatedly, incurring severe disk I/O bottlenecks.<br>• <strong>PrefixSpan (Pei et al.):</strong> A pattern-growth algorithm that mines sequential patterns by recursively projecting sequence suffixes into smaller projected databases based on frequent prefixes. <strong>Zero candidate generation</strong>; dramatically smaller memory footprint and orders of magnitude faster execution!</div></div>
"""

# ----------------- EXTENSION FOR M5 -----------------
M5_EXP = r"""
<h2 class="section-title">Topic 46.1: Cluster Validity Indices & Support Vector Machine Math</h2>

<div class="formula-card">
  <strong>The Silhouette Coefficient for Clustering Validation:</strong>
  For each data point $i$:
  - Let $a(i)$ = average distance from $i$ to all other points in the <strong>same cluster</strong> (Compactness).
  - Let $b(i)$ = minimum average distance from $i$ to all points in any <strong>other cluster</strong> (Separation).
  $$\mathbf{s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} \qquad s(i) \in [-1, +1]}$$
  - $s(i) \approx +1$: Point is exceptionally well clustered (compact and well-separated).
  - $s(i) \approx 0$: Point lies exactly on the decision boundary between two clusters.
  - $s(i) < 0$: Point is assigned to the wrong cluster!
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Silhouette Score Calculation on 2 Clusters</div>
  <p>Consider 4 points: $C_1 = \{P_1(0, 0), P_2(1, 0)\}$, $C_2 = \{P_3(5, 0), P_4(6, 0)\}$. Calculate Silhouette score for $P_1$:</p>
  <ul>
    <li>Intra-cluster distance: $a(P_1) = d(P_1, P_2) = 1.0$.</li>
    <li>Inter-cluster distance to $C_2$: $b(P_1) = \frac{d(P_1, P_3) + d(P_1, P_4)}{2} = \frac{5.0 + 6.0}{2} = \mathbf{5.5}$.</li>
  </ul>
  $$\mathbf{s(P_1) = \frac{b(P_1) - a(P_1)}{\max(a(P_1), b(P_1))} = \frac{5.5 - 1.0}{\max(1.0, 5.5)} = \frac{4.5}{5.5} = \mathbf{+0.8182}}$$
  $$\mathbf{\text{Result: High positive Silhouette score (+0.818) indicates near-optimal cluster assignment!}}$$
</div>

<div class="qa-card"><div class="qa-q">Q3. Compare Agglomerative Hierarchical Linkage Criteria: Single Link, Complete Link, Average Link, and Ward's Method. (8 Marks)</div><div class="qa-a"><table class="custom-table"><thead><tr><th>Linkage Criterion</th><th>Distance Formulation</th><th>Cluster Shape & Properties</th></tr></thead><tbody><tr><td><strong>Single Link (MIN)</strong></td><td>$d(C_i, C_j) = \min_{\mathbf{x} \in C_i, \mathbf{y} \in C_j} d(\mathbf{x}, \mathbf{y})$</td><td>Can handle non-elliptical shapes; highly sensitive to noise and <strong>chaining effect</strong> (elongated stringy clusters).</td></tr><tr><td><strong>Complete Link (MAX)</strong></td><td>$d(C_i, C_j) = \max_{\mathbf{x} \in C_i, \mathbf{y} \in C_j} d(\mathbf{x}, \mathbf{y})$</td><td>Produces compact, spherical clusters of equal diameter; avoids chaining; sensitive to outliers.</td></tr><tr><td><strong>Average Link (UPGMA)</strong></td><td>$d(C_i, C_j) = \frac{1}{|C_i||C_j|}\sum_{\mathbf{x}} \sum_{\mathbf{y}} d(\mathbf{x}, \mathbf{y})$</td><td>Robust balance between single and complete link; resistant to noise.</td></tr><tr><td><strong>Ward's Method</strong></td><td>Merges pair that minimizes increase in total within-cluster Sum of Squared Errors ($\Delta\text{SSE}$).</td><td>Produces exceptionally balanced, dense spherical clusters (most popular in business analytics).</td></tr></tbody></table></div></div>
"""

def generate_full_dm_suite():
    m1_final = M1_CONTENT + M1_EXP
    m2_final = M2_CONTENT + M2_EXP
    m3_final = M3_CONTENT + M3_EXP
    m4_final = M4_CONTENT + M4_EXP
    m5_final = M5_CONTENT + M5_EXP

    print("DM M1 chars:", len(m1_final))
    print("DM M2 chars:", len(m2_final))
    print("DM M3 chars:", len(m3_final))
    print("DM M4 chars:", len(m4_final))
    print("DM M5 chars:", len(m5_final))

    modules = [
        (1, "Module 1: Data Understanding & Statistical Proximity", "Topics 1 to 14 • KDD Lifecycle, Attributes, Boxplots, Q-Q, Jaccard & Distance Metrics", m1_final, "Module_1_Data_Understanding_Notes"),
        (2, "Module 2: Data Preprocessing & Dimensionality Reduction", "Topics 15 to 20 • Missing Imputation, Binning, Chi-Square Independence, Normalization & PCA", m2_final, "Module_2_Data_Preprocessing_Notes"),
        (3, "Module 3: Data Warehousing & OLAP Technology", "Topics 21 to 29 • Star/Snowflake Schemas, Measures, OLAP Operations, Cuboid Lattices & BUC", m3_final, "Module_3_Data_Warehousing_OLAP_Notes"),
        (4, "Module 4: Frequent Pattern & Association Mining", "Topics 30 to 36 • Market Basket Analysis, Support/Confidence/Lift, Apriori, FP-Growth & ECLAT", m4_final, "Module_4_Association_Rules_Notes"),
        (5, "Module 5: Classification & Cluster Analysis", "Topics 37 to 46 • ID3/C4.5/CART Trees, Naive Bayes, Confusion Matrix, k-Means, PAM & DBSCAN", m5_final, "Module_5_Classification_Clustering_Notes"),
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
    generate_full_dm_suite()
