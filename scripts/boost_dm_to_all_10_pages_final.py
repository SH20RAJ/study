#!/usr/bin/env python3
"""
Final Master 10-12 Page Data Mining Suite Compiler.
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from make_dm_10_pages_exact import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA,
    REVISION_ULTIMATE
)

# ----------------- MODULE 1 ULTRA BOOST -----------------
M1_ULTRA = r"""
<h2 class="section-title">Topic 15: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 3: Complete Five-Number Summary & Skewness Analysis on Examination Scores</div>
  <p>Consider the final examination marks of 16 engineering students:</p>
  $$\mathbf{X = \{35, 42, 48, 52, 56, 58, 60, 62, 65, 68, 72, 75, 78, 82, 88, 98\}}$$
  <p><strong>1. Five-Number Summary ($N = 16$):</strong></p>
  <ul>
    <li><strong>Min:</strong> $\mathbf{35}$</li>
    <li><strong>$Q_1$:</strong> Median of lower 8 values $\{35, 42, 48, 52, 56, 58, 60, 62\} \implies \frac{52 + 56}{2} = \mathbf{54.0}$</li>
    <li><strong>Median ($Q_2$):</strong> $\frac{x_8 + x_9}{2} = \frac{62 + 65}{2} = \mathbf{63.5}$</li>
    <li><strong>$Q_3$:</strong> Median of upper 8 values $\{65, 68, 72, 75, 78, 82, 88, 98\} \implies \frac{75 + 78}{2} = \mathbf{76.5}$</li>
    <li><strong>Max:</strong> $\mathbf{98}$</li>
  </ul>
  <p><strong>2. Interquartile Range & Outlier Boundaries:</strong></p>
  $$\text{IQR} = Q_3 - Q_1 = 76.5 - 54.0 = \mathbf{22.5}$$
  $$\text{Lower Outlier Fence} = 54.0 - 1.5(22.5) = 54.0 - 33.75 = \mathbf{20.25}$$
  $$\text{Upper Outlier Fence} = 76.5 + 1.5(22.5) = 76.5 + 33.75 = \mathbf{110.25}$$
  $$\mathbf{\text{Conclusion: All data points lie within } [20.25, 110.25] \implies \mathbf{\text{Zero Outliers Present!}}}$$
</div>

<div class="qa-card"><div class="qa-q">Q11. Explain Pearson's Mode Skewness and Bowley's Quartile Skewness Coefficient. (8 Marks)</div><div class="qa-a">• <strong>Pearson's Mode Skewness:</strong> $S_k = \frac{\text{Mean} - \text{Mode}}{\sigma} \approx \frac{3(\text{Mean} - \text{Median})}{\sigma}$. Measures asymmetry standardized by standard deviation.<br>• <strong>Bowley's Quartile Skewness (Galton's Coefficient):</strong>
$$\mathbf{B_q = \frac{(Q_3 - Q_2) - (Q_2 - Q_1)}{(Q_3 - Q_2) + (Q_2 - Q_1)} = \frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}}$$
$B_q \in [-1, +1]$. $B_q > 0 \implies \text{Right Skew}$; $B_q = 0 \implies \text{Symmetric}$; $B_q < 0 \implies \text{Left Skew}$. Robust to extreme outliers because it depends solely on quartiles!</div></div>
"""

# ----------------- MODULE 2 ULTRA BOOST -----------------
M2_ULTRA = r"""
<h2 class="section-title">Topic 20.4: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 3: Complete 2D Principal Component Analysis (PCA) Eigenvalue Derivation</div>
  <p>Consider 4 centered 2D data points: $\mathbf{x}_1 = (-1, -1)^T, \mathbf{x}_2 = (-1, 1)^T, \mathbf{x}_3 = (1, -1)^T, \mathbf{x}_4 = (1, 1)^T$ with correlation covariance $\mathbf{\Sigma} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$:</p>
  <p><strong>1. Characteristic Polynomial:</strong></p>
  $$\det(\mathbf{\Sigma} - \lambda\mathbf{I}) = \det\begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$$
  $$\mathbf{(\lambda - 3)(\lambda - 1) = 0 \implies \lambda_1 = 3, \quad \lambda_2 = 1}$$
  <p><strong>2. First Principal Component Eigenvector ($\lambda_1 = 3$):</strong></p>
  $$(\mathbf{\Sigma} - 3\mathbf{I})\mathbf{e}_1 = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} e_{11} \\ e_{12} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies -e_{11} + e_{12} = 0 \implies e_{11} = e_{12}$$
  $$\mathbf{\text{Normalized First Principal Component: } \mathbf{e}_1 = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} \approx \begin{bmatrix} 0.7071 \\ 0.7071 \end{bmatrix}}$$
  <p><strong>3. Explained Variance Ratio:</strong></p>
  $$\mathbf{\text{EVR}_1 = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{3}{3 + 1} = \frac{3}{4} = \mathbf{75\% \text{ of total dataset variance captured in 1D!}}}$$
</div>

<div class="qa-card"><div class="qa-q">Q7. Explain the Difference between L1-Norm (Lasso) and L2-Norm (Ridge) Regularization in Regression. (8 Marks)</div><div class="qa-a">• <strong>Ridge Regression ($L_2$):</strong> Penalizes squared magnitude of coefficients ($\lambda \sum \beta_j^2$). Shrinks weights smoothly toward zero, preventing multicollinearity, but <em>never sets weights strictly to zero</em> (does not perform feature selection).<br>• <strong>Lasso Regression ($L_1$):</strong> Penalizes absolute value of coefficients ($\lambda \sum |\beta_j|$). Due to the diamond geometric contour of the $L_1$ ball, optimal solutions hit coordinate axes, driving irrelevant feature weights <strong>strictly to zero</strong> ($\beta_j = 0$), performing automatic sparse feature selection!</div></div>
"""

# ----------------- MODULE 3 ULTRA BOOST -----------------
M3_ULTRA = r"""
<h2 class="section-title">Topic 29.4: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 4: Star-Cubing Shared-Prefix Tree Construction</div>
  <p><strong>Star-Cubing (Xu et al. 2001)</strong> integrates top-down and bottom-up data cube computation with star-tree structures:</p>
  <ul>
    <li>Compresses identical attribute prefixes into single tree paths.</li>
    <li>If a subtree's aggregate count satisfies `min_support`, compute all descendant cuboid aggregations simultaneously.</li>
    <li>If an aggregate fails `min_support`, prune the entire star-tree branch (star-node reduction).</li>
    <li>Achieves up to $\mathbf{100\times}$ speedup over naive array cubing algorithms!</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q6. Compare Fact Tables vs Dimension Tables in Data Warehouse Design. (8 Marks)</div><div class="qa-a"><table class="custom-table"><thead><tr><th>Dimension</th><th>Fact Table</th><th>Dimension Table</th></tr></thead><tbody><tr><td><strong>Contents</strong></td><td>Numeric additive business measurements (revenue, quantities) and composite FKs.</td><td>Descriptive qualitative textual context (names, categories, addresses).</td></tr><tr><td><strong>Growth & Size</strong></td><td>Massive (millions to billions of rows; grows continuously).</td><td>Small to moderate (hundreds to thousands of rows).</td></tr><tr><td><strong>Granularity</strong></td><td>Defined at atomic leaf transaction level.</td><td>Hierarchical roll-up levels (Store $\rightarrow$ City $\rightarrow$ State $\rightarrow$ Country).</td></tr><tr><td><strong>Structure</strong></td><td>Tall, narrow (few columns, massive rows).</td><td>Short, wide (many descriptive textual columns).</td></tr></tbody></table></div></div>
"""

# ----------------- MODULE 4 ULTRA BOOST -----------------
M4_ULTRA = r"""
<h2 class="section-title">Topic 36.4: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 5: Complete FP-Tree Conditional Pattern Base Mining Trace</div>
  <p>Consider frequent items in descending order: $L_1 = [f: 4, c: 4, a: 3, b: 3, m: 3, p: 3]$. Suppose we are mining patterns ending in suffix <strong>$p$</strong>:</p>
  <ul>
    <li>Paths leading to $p$ in FP-Tree: $\langle f, c, a, m: 2 \rangle$ and $\langle c, b: 1 \rangle$.</li>
    <li><strong>Conditional Pattern Base for $p$:</strong> $\{ (f, c, a, m): 2, \ (c, b): 1 \}$.</li>
    <li>Accumulate item frequencies: $f: 2, c: 3, a: 2, m: 2, b: 1$.</li>
    <li>With $\text{min\_sup} = 3$, items $f, a, m, b$ are pruned ($< 3$). Only item $c$ remains ($\text{count} = 3 \ge 3$).</li>
    <li><strong>Conditional FP-Tree for $p$:</strong> $\langle c: 3 \rangle$.</li>
    <li><strong>Generated Frequent Patterns ending in $p$:</strong> $\{p\}: 3$ and $\{c, p\}: 3$.</li>
  </ul>
  $$\mathbf{\text{Result: Zero candidate generation required! Directly mined frequent itemset } \{c, p\} \text{ in } O(1) \text{ time!}}$$
</div>

<div class="qa-card"><div class="qa-q">Q5. Explain the Apriori-Tid and Apriori-Hybrid Algorithms. (8 Marks)</div><div class="qa-a">• <strong>Apriori-Tid:</strong> Does NOT scan the raw transactional database after Pass 1. Instead, it generates a synthetic transactional table $\bar{C}_k$ storing tuple IDs alongside candidate itemset IDs. In late passes ($k \ge 3$), $\bar{C}_k$ becomes dramatically smaller than the original database, accelerating support counting.<br>• <strong>Apriori-Hybrid:</strong> Uses standard Apriori in early passes ($k=1, 2$) when $\bar{C}_k$ is larger than the raw database, and automatically switches to Apriori-Tid in later passes ($k \ge 3$) when candidate itemset lists shrink, achieving optimal execution speed!</div></div>
"""

# ----------------- MODULE 5 ULTRA BOOST -----------------
M5_ULTRA = r"""
<h2 class="section-title">Topic 46.4: Master University Exam Problem Bank (Part III)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 6: Complete Confusion Matrix & ROC Curve Coordinates Calculation</div>
  <p>A binary classifier produces probabilities for 5 test samples: $(S_1: 0.9, +), (S_2: 0.8, +), (S_3: 0.6, -), (S_4: 0.4, +), (S_5: 0.1, -)$ ($P=3, N=2$):</p>
  <table class="custom-table">
    <thead><tr><th>Threshold $T$</th><th>Predictions $(\hat{Y})$</th><th>$TP$</th><th>$FP$</th><th>$\text{TPR} = \frac{TP}{3}$</th><th>$\text{FPR} = \frac{FP}{2}$</th><th>ROC Point $(x, y)$</th></tr></thead>
    <tbody>
      <tr><td>$> 0.9$</td><td>$[- - - - -]$</td><td>0</td><td>0</td><td>$0.00$</td><td>$0.00$</td><td>$(0, 0)$</td></tr>
      <tr><td>$0.85$</td><td>$[+ - - - -]$</td><td>1</td><td>0</td><td>$0.33$</td><td>$0.00$</td><td>$(0, 0.33)$</td></tr>
      <tr><td>$0.70$</td><td>$[+ + - - -]$</td><td>2</td><td>0</td><td>$0.67$</td><td>$0.00$</td><td>$(0, 0.67)$</td></tr>
      <tr><td>$0.50$</td><td>$[+ + + - -]$</td><td>2</td><td>1</td><td>$0.67$</td><td>$0.50$</td><td>$(0.50, 0.67)$</td></tr>
      <tr><td>$0.30$</td><td>$[+ + + + -]$</td><td>3</td><td>1</td><td>$1.00$</td><td>$0.50$</td><td>$(0.50, 1.00)$</td></tr>
      <tr><td>$< 0.1$</td><td>$[+ + + + +]$</td><td>3</td><td>2</td><td>$1.00$</td><td>$1.00$</td><td>$(1.00, 1.00)$</td></tr>
    </tbody>
  </table>
  <p><strong>Area Under the Curve (AUC) by Trapezoidal Rule:</strong></p>
  $$\text{AUC} = (0.50 - 0)(0.67) + (1.00 - 0.50)\left(\frac{1.00 + 0.67}{2}\right) = 0.335 + 0.50(0.835) = 0.335 + 0.4175 = \mathbf{0.7525}$$
</div>

<div class="qa-card"><div class="qa-q">Q6. Explain BIRCH (Balanced Iterative Reducing and Clustering using Hierarchies) Algorithm and Clustering Feature (CF) Trees. (8 Marks)</div><div class="qa-a"><strong>BIRCH (Zhang, Ramakrishnan, Livny 1996)</strong> clusters massive datasets in a single database scan using <strong>Clustering Feature (CF) Vectors</strong>:
$$\mathbf{CF = \langle N, \mathbf{LS}, SS \rangle = \langle N, \sum_{i=1}^N \mathbf{x}_i, \sum_{i=1}^N \mathbf{x}_i^2 \rangle}$$
• <strong>Additivity Theorem:</strong> $CF_1 + CF_2 = \langle N_1+N_2, \mathbf{LS}_1+\mathbf{LS}_2, SS_1+SS_2 \rangle$.<br>• <strong>CF-Tree:</strong> A height-balanced B-tree storing CF vectors. Inserts points incrementally into leaf nodes based on radius thresholds without holding raw data points in memory! Runs in linear time $O(N)$!</div></div>
"""

# ----------------- REVISION MEGA EXPANSION -----------------
REVISION_EXPANDED = REVISION_ULTIMATE + r"""
<h2 class="section-title">Master Exam Formula Flashcards & Step-by-Step Derivations</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 5: Information Gain vs Gain Ratio vs Gini Index</div>
  <ul>
    <li><strong>Information Gain (ID3):</strong> $\text{Gain}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$. Biased toward attributes with large numbers of distinct values (e.g. `CreditCard_Number`).</li>
    <li><strong>Gain Ratio (C4.5):</strong> $\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}$. Normalizes gain by split entropy, penalizing broad multi-way splits.</li>
    <li><strong>Gini Impurity (CART):</strong> $\text{Gini}(S) = 1 - \sum p_i^2$. Strictly binary splits ($\Delta\text{Gini} = \text{Gini}(S) - \frac{|S_L|}{|S|}\text{Gini}(S_L) - \frac{|S_R|}{|S|}\text{Gini}(S_R)$).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 6: Complete Normalization Formulas Reference</div>
  <ul>
    <li><strong>Min-Max Scaling:</strong> $v' = \frac{v - \min}{\max - \min}(\text{new\_max} - \text{new\_min}) + \text{new\_min}$</li>
    <li><strong>Z-Score Standardization:</strong> $z = \frac{v - \mu}{\sigma}$</li>
    <li><strong>Modified Z-Score (Outlier-Robust):</strong> $M_i = \frac{0.6745(x_i - \text{Median})}{\text{MAD}}$ where $\text{MAD} = \text{Median}(|x_i - \text{Median}|)$</li>
    <li><strong>Decimal Scaling:</strong> $v' = \frac{v}{10^j}$ where $j = \lceil \log_{10}(\max|v|) \rceil$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 7: The 4 Major Clustering Paradigms</div>
  <table class="custom-table">
    <thead><tr><th>Paradigm</th><th>Representative Algorithms</th><th>Key Characteristics</th></tr></thead>
    <tbody>
      <tr><td><strong>Partitioning</strong></td><td>k-Means, k-Medoids (PAM), CLARA, CLARANS</td><td>Constructs $k$ partitions; iterative relocation; spherical clusters.</td></tr>
      <tr><td><strong>Hierarchical</strong></td><td>AGNES (agglomerative), DIANA (divisive), BIRCH, CURE</td><td>Dendrogram tree; no $k$ required; irreversible merges.</td></tr>
      <tr><td><strong>Density-Based</strong></td><td>DBSCAN, OPTICS, DENCLUE</td><td>Arbitrary non-convex shapes; filters noise outliers automatically.</td></tr>
      <tr><td><strong>Grid-Based</strong></td><td>STING, WaveCluster, CLIQUE</td><td>Quantizes object space into finite grid cells; fast $O(N)$ execution.</td></tr>
    </tbody>
  </table>
</div>
"""

def compile_final_pass():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA
    m5 = M5_CONTENT + M5_EXP + M5_DEEP + M5_MEGA + M5_ULTRA

    print("Final Pass M1 length:", len(m1))
    print("Final Pass M2 length:", len(m2))
    print("Final Pass M3 length:", len(m3))
    print("Final Pass M4 length:", len(m4))
    print("Final Pass M5 length:", len(m5))
    print("Final Pass Rev length:", len(REVISION_EXPANDED))

    modules = [
        (1, "Module 1: Data Understanding & Statistical Proximity", "Topics 1 to 14 • KDD Lifecycle, Attributes, Boxplots, Q-Q, Jaccard & Distance Metrics", m1, "Module_1_Data_Understanding_Notes"),
        (2, "Module 2: Data Preprocessing & Dimensionality Reduction", "Topics 15 to 20 • Missing Imputation, Binning, Chi-Square Independence, Normalization & PCA", m2, "Module_2_Data_Preprocessing_Notes"),
        (3, "Module 3: Data Warehousing & OLAP Technology", "Topics 21 to 29 • Star/Snowflake Schemas, Measures, OLAP Operations, Cuboid Lattices & BUC", m3, "Module_3_Data_Warehousing_OLAP_Notes"),
        (4, "Module 4: Frequent Pattern & Association Mining", "Topics 30 to 36 • Market Basket Analysis, Support/Confidence/Lift, Apriori, FP-Growth & ECLAT", m4, "Module_4_Association_Rules_Notes"),
        (5, "Module 5: Classification & Cluster Analysis", "Topics 37 to 46 • ID3/C4.5/CART Trees, Naive Bayes, Confusion Matrix, k-Means, PAM & DBSCAN", m5, "Module_5_Classification_Clustering_Notes"),
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
        REVISION_EXPANDED
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
    {REVISION_EXPANDED}
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
    compile_final_pass()
