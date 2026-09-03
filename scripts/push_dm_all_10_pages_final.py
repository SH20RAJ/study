#!/usr/bin/env python3
"""
Final push for Data Mining Modules 2, 3, 4, 5 and Revision Guide to guarantee 10-12 pages each and 55+ pages for Master Book!
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from boost_dm_to_all_10_pages_final import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA,
    REVISION_EXPANDED
)

# ----------------- MODULE 2 BOOST -----------------
M2_FINAL_BOOST = r"""
<h2 class="section-title">Topic 20.5: Master University Exam Problem Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 4: Complete Chi-Square Contingency Test with 3x3 Degrees of Freedom</div>
  <p>Test the relationship between Customer Age Group ($\text{Youth, Middle, Senior}$) and Purchase Frequency ($\text{Low, Med, High}$):</p>
  <table class="custom-table">
    <thead><tr><th>Age \ Frequency</th><th>Low</th><th>Medium</th><th>High</th><th>Total</th></tr></thead>
    <tbody>
      <tr><td><strong>Youth</strong></td><td>$O_{11} = 50$</td><td>$O_{12} = 30$</td><td>$O_{13} = 20$</td><td>$100$</td></tr>
      <tr><td><strong>Middle</strong></td><td>$O_{21} = 30$</td><td>$O_{22} = 50$</td><td>$O_{23} = 20$</td><td>$100$</td></tr>
      <tr><td><strong>Senior</strong></td><td>$O_{31} = 20$</td><td>$O_{32} = 20$</td><td>$O_{33} = 60$</td><td>$100$</td></tr>
      <tr><td><strong>Total</strong></td><td>$100$</td><td>$100$</td><td>$100$</td><td>$\mathbf{N = 300}$</td></tr>
    </tbody>
  </table>
  <p><strong>1. Expected Frequencies:</strong> $E_{ij} = \frac{100 \times 100}{300} = \mathbf{33.33}$ for all cells.</p>
  <p><strong>2. Compute $\chi^2$ Statistic:</strong></p>
  $$\chi^2 = \frac{(50-33.33)^2 + (30-33.33)^2 + (20-33.33)^2 + (30-33.33)^2 + (50-33.33)^2 + (20-33.33)^2 + (20-33.33)^2 + (20-33.33)^2 + (60-33.33)^2}{33.33}$$
  $$\chi^2 = \frac{277.89 + 11.09 + 177.69 + 11.09 + 277.89 + 177.69 + 177.69 + 177.69 + 711.29}{33.33} = \frac{1999.98}{33.33} \approx \mathbf{60.00}$$
  <p><strong>3. Decision:</strong> $df = (3-1)(3-1) = 4$. Critical $\chi_{0.05, 4}^2 = 9.488$. $\mathbf{60.00 \gg 9.488 \implies \text{Reject Independence!}}$</p>
</div>

<div class="qa-card"><div class="qa-q">Q8. Explain Principal Component Regression (PCR) and Partial Least Squares (PLS). (8 Marks)</div><div class="qa-a">• <strong>PCR:</strong> A two-step pipeline that first performs unsupervised PCA on the predictors $\mathbf{X}$ to extract the top $k$ principal components $\mathbf{Z}$, and then fits an ordinary least squares regression model predicting $\mathbf{y}$ from $\mathbf{Z}$. Prevents multicollinearity, but because PCA is unsupervised, the chosen components may not necessarily be the most predictive of $\mathbf{y}$!<br>• <strong>PLS (Partial Least Squares):</strong> <strong>Supervised Dimensionality Reduction</strong> that finds latent orthogonal components that maximize the covariance between $\mathbf{X}$ and target $\mathbf{y}$, ensuring retained components have maximal predictive power!</div></div>

<div class="qa-card"><div class="qa-q">Q9. Detail the Discretization of Numeric Attributes via Maximum Entropy Splitting. (8 Marks)</div><div class="qa-a"><strong>Maximum Entropy Discretization</strong> partitions a continuous attribute into $k$ intervals such that the Shannon entropy over all bins is maximized. This creates bins that contain approximately equal numbers of data points (equi-frequency), preventing low-density outlier intervals from distorting decision tree splits and probability estimates in Naive Bayes.</div></div>
"""

# ----------------- MODULE 3 BOOST -----------------
M3_FINAL_BOOST = r"""
<h2 class="section-title">Topic 29.5: Master University Exam Problem Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 5: Fact Table Sizing & Storage Capacity Estimation</div>
  <p>A national retail chain with 500 physical stores sells 10,000 distinct products. On average, each store processes 2,000 sales transactions per day with an average of 4 items per transaction:</p>
  <ul>
    <li>Daily sales fact records = $500 \text{ stores} \times 2,000 \text{ transactions} \times 4 \text{ items} = \mathbf{4,000,000 \text{ rows/day}}$.</li>
    <li>Annual fact table growth = $4,000,000 \times 365 = \mathbf{1,460,000,000 \text{ rows/year (1.46 Billion rows/year)}}$.</li>
    <li>Each row consists of 5 integer FKs ($4\text{ bytes} \times 5 = 20\text{ bytes}$) and 3 float measures ($8\text{ bytes} \times 3 = 24\text{ bytes}$) + row overhead ($16\text{ bytes}$) = $\mathbf{60\text{ bytes/row}}$.</li>
    <li>Annual raw storage = $1.46 \times 10^9 \times 60 \approx \mathbf{87.6\text{ GB/year}}$. With B-tree & Bitmap indexing ($2.5\times$ multiplier) $\implies \mathbf{219\text{ GB/year}}$!</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q7. Compare Kimball's Dimensional Bus Architecture with Inmon's Corporate Information Factory (CIF). (10 Marks)</div><div class="qa-a"><table class="custom-table"><thead><tr><th>Dimension</th><th>Bill Inmon (Top-Down CIF)</th><th>Ralph Kimball (Bottom-Up Bus)</th></tr></thead><tbody><tr><td><strong>Central Architecture</strong></td><td>Single enterprise normalized relational DW (3NF). Data marts are departmental downstream extracts.</td><td>No centralized 3NF EDW. The warehouse is the <em>union of all dimensional star-schema data marts</em>.</td></tr><tr><td><strong>Integration Mechanism</strong></td><td>Enterprise Data Model (EDM).</td><td><strong>Conformed Dimensions</strong> and Conformed Facts.</td></tr><tr><td><strong>Implementation Speed</strong></td><td>Slow initial ramp-up (high upfront engineering cost).</td><td>Fast iterative delivery; agile business value per mart.</td></tr><tr><td><strong>End-User Access</strong></td><td>Users query data marts, not the core 3NF EDW.</td><td>Users query dimensional star schemas directly.</td></tr></tbody></table></div></div>

<div class="qa-card"><div class="qa-q">Q8. Detail the Mechanics of Materialized Query Tables (MQT) and Automatic Query Rewrite. (8 Marks)</div><div class="qa-a">A <strong>Materialized Query Table (MQT / Indexed View)</strong> physically stores pre-aggregated query results on disk. When an end-user submits a complex SQL aggregation query (e.g. `SELECT Year, Region, SUM(Sales)...`), the RDBMS <strong>Cost-Based Query Optimizer</strong> automatically rewrites the execution plan to read directly from the compact MQT rather than scanning the massive 1.5-billion-row base fact table, reducing query execution latency from minutes to milliseconds!</div></div>
"""

# ----------------- MODULE 4 BOOST -----------------
M4_FINAL_BOOST = r"""
<h2 class="section-title">Topic 36.5: Master University Exam Problem Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 6: Vertical Data Format Mining with ECLAT Algorithm Trace</div>
  <p>Given transactional database ($N = 4$): $T_1 = \{A, B, C\}, T_2 = \{B, C, D\}, T_3 = \{A, C, D\}, T_4 = \{A, B, C, D\}$ with $\text{min\_sup} = 2$ ($50\%$):</p>
  <ul>
    <li><strong>Vertical TID-Lists ($k=1$):</strong>
      <ul>
        <li>$t(A) = \{1, 3, 4\} \ (\text{count}=3)$</li>
        <li>$t(B) = \{1, 2, 4\} \ (\text{count}=3)$</li>
        <li>$t(C) = \{1, 2, 3, 4\} \ (\text{count}=4)$</li>
        <li>$t(D) = \{2, 3, 4\} \ (\text{count}=3)$</li>
      </ul>
    </li>
    <li><strong>2-Itemset TID-List Intersections ($k=2$):</strong>
      <ul>
        <li>$t(AB) = t(A) \cap t(B) = \{1, 3, 4\} \cap \{1, 2, 4\} = \{1, 4\} \implies \text{count}=2 \ge 2$ (Frequent!)</li>
        <li>$t(AC) = t(A) \cap t(C) = \{1, 3, 4\} \cap \{1, 2, 3, 4\} = \{1, 3, 4\} \implies \text{count}=3 \ge 2$ (Frequent!)</li>
        <li>$t(AD) = t(A) \cap t(D) = \{1, 3, 4\} \cap \{2, 3, 4\} = \{3, 4\} \implies \text{count}=2 \ge 2$ (Frequent!)</li>
        <li>$t(BC) = t(B) \cap t(C) = \{1, 2, 4\} \cap \{1, 2, 3, 4\} = \{1, 2, 4\} \implies \text{count}=3 \ge 2$ (Frequent!)</li>
        <li>$t(BD) = t(B) \cap t(D) = \{1, 2, 4\} \cap \{2, 3, 4\} = \{2, 4\} \implies \text{count}=2 \ge 2$ (Frequent!)</li>
        <li>$t(CD) = t(C) \cap t(D) = \{1, 2, 3, 4\} \cap \{2, 3, 4\} = \{2, 3, 4\} \implies \text{count}=3 \ge 2$ (Frequent!)</li>
      </ul>
    </li>
    <li><strong>3-Itemset Intersections ($k=3$):</strong>
      <ul>
        <li>$t(ABC) = t(AB) \cap t(AC) = \{1, 4\} \cap \{1, 3, 4\} = \{1, 4\} \implies \text{count}=2 \ge 2$</li>
        <li>$t(ABD) = t(AB) \cap t(AD) = \{1, 4\} \cap \{3, 4\} = \{4\} \implies \text{count}=1 < 2$ (Pruned!)</li>
        <li>$t(ACD) = t(AC) \cap t(AD) = \{1, 3, 4\} \cap \{3, 4\} = \{3, 4\} \implies \text{count}=2 \ge 2$</li>
        <li>$t(BCD) = t(BC) \cap t(BD) = \{1, 2, 4\} \cap \{2, 4\} = \{2, 4\} \implies \text{count}=2 \ge 2$</li>
      </ul>
    </li>
  </ul>
  $$\mathbf{\text{Frequent 3-Itemsets: } \{A, B, C\}, \ \{A, C, D\}, \ \{B, C, D\} \quad (\text{Computed in zero database scans!})}$$
</div>

<div class="qa-card"><div class="qa-q">Q6. Explain the Concept of Correlation Rules and Chi-Square Association Testing. (8 Marks)</div><div class="qa-a">Because Support-Confidence association rules can produce misleading deceptive correlations (when the consequent item is globally popular), <strong>Correlation Rules</strong> augment association mining by testing statistical independence using the Chi-Square metric:
$$\mathbf{\chi^2 = \sum_{i \in \{A, \neg A\}} \sum_{j \in \{B, \neg B\}} \frac{(O_{ij} - E_{ij})^2}{E_{ij}} = \frac{N(O_{11}O_{22} - O_{12}O_{21})^2}{(O_{11}+O_{12})(O_{21}+O_{22})(O_{11}+O_{21})(O_{12}+O_{22})}}$$
If $\chi^2 > 3.841$ (at $\alpha = 0.05, df=1$), the association rule $A \implies B$ is proven to possess genuine statistical correlation rather than accidental co-occurrence!</div></div>
"""

# ----------------- MODULE 5 BOOST -----------------
M5_FINAL_BOOST = r"""
<h2 class="section-title">Topic 46.5: Master University Exam Problem Bank (Part IV)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 7: Complete Support Vector Machine (SVM) Margin & Hyperplane Equations</div>
  <p>Given 3 support vectors in 2D space: $\mathbf{x}_1 = (1, 1)^T, y_1 = -1$; $\mathbf{x}_2 = (2, 0)^T, y_2 = -1$; $\mathbf{x}_3 = (2, 3)^T, y_3 = +1$:</p>
  <ul>
    <li>Normal weight vector: $\mathbf{w} = (0, 1.5)^T$.</li>
    <li>Bias intercept: $b = -3.5$.</li>
    <li><strong>Optimal Separating Hyperplane:</strong> $\mathbf{w}^T \mathbf{x} + b = 0 \implies 0(x_1) + 1.5(x_2) - 3.5 = 0 \implies \mathbf{x_2 = 2.333}$.</li>
    <li><strong>Margin Width ($M$):</strong>
      $$\mathbf{M = \frac{2}{\|\mathbf{w}\|} = \frac{2}{\sqrt{0^2 + 1.5^2}} = \frac{2}{1.5} = \mathbf{1.3333 \text{ units}}}$$
    </li>
    <li><strong>Classification Decision Rule:</strong>
      $$f(\mathbf{x}) = \text{sign}(1.5 x_2 - 3.5) = \begin{cases} +1 & \text{if } x_2 \ge 2.333 \\ -1 & \text{if } x_2 < 2.333 \end{cases}$$
    </li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q7. Explain the Density-Based Spatial Clustering of Applications with Noise (DBSCAN) Time Complexity and Spatial Indexing. (8 Marks)</div><div class="qa-a">• <strong>Naive Complexity:</strong> Without spatial indexing, finding the $\epsilon$-neighborhood for all $N$ points requires computing $N \times N$ pairwise distance comparisons $\implies O(N^2)$ time complexity.<br>• <strong>Spatial Indexing Acceleration:</strong> Using $R^*$-Trees, $k$-d Trees, or Ball Trees to index spatial coordinates reduces $\epsilon$-range query lookups from $O(N)$ to $O(\log N)$, slashing overall DBSCAN execution complexity to $\mathbf{O(N \log N)}$!</div></div>

<div class="qa-card"><div class="qa-q">Q8. Detail the Isolation Forest Algorithm for Fast Outlier Detection. (8 Marks)</div><div class="qa-a"><strong>Isolation Forest (Liu et al. 2008)</strong> detects anomalies by explicitly isolating outliers rather than profiling normal data points:<br>1. Randomly build an ensemble of $t$ Isolation Trees (iTrees) by recursively choosing a random feature and selecting a random split value between $\min$ and $\max$.<br>2. <strong>Core Axiom:</strong> Anomalies require far fewer random splits to isolate than normal cluster points, resulting in drastically shorter tree path lengths $h(x)$!<br>3. <strong>Anomaly Score:</strong> $s(x, n) = 2^{-\frac{\mathbb{E}[h(x)]}{c(n)}}$. If $s \rightarrow 1$, instance is definitively an outlier. Runs in blazing fast linear time $O(t \cdot \psi \log \psi)$!</div></div>
"""

# ----------------- REVISION 10-PAGE COMPLETE -----------------
REVISION_PERFECT = REVISION_EXPANDED + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 8: Complete Distance & Dissimilarity Matrix Checklist</div>
  <ul>
    <li><strong>Minkowski Distance ($L_p$):</strong> $d(\mathbf{x}, \mathbf{y}) = (\sum |x_i - y_i|^p)^{1/p}$ ($p=1$ Manhattan, $p=2$ Euclidean, $p=\infty$ Chebyshev $\max |x_i - y_i|$)</li>
    <li><strong>Cosine Distance:</strong> $d_C = 1 - \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\|\|\mathbf{y}\|}$ (Semi-metric; angle invariant)</li>
    <li><strong>Jaccard Distance:</strong> $d_J = \frac{r + s}{q + r + s}$ (Asymmetric binary)</li>
    <li><strong>Simple Matching Coefficient:</strong> $\text{SMC} = \frac{q + t}{q + r + s + t}$ (Symmetric binary)</li>
    <li><strong>Mahalanobis Distance:</strong> $d_M = \sqrt{(\mathbf{x}-\mathbf{y})^T \mathbf{\Sigma}^{-1} (\mathbf{x}-\mathbf{y})}$ (Scale & covariance invariant)</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 9: Association Rule Quality Metrics & Pruning</div>
  <ul>
    <li><strong>Support:</strong> $P(A \cup B)$ (Statistical significance / frequency)</li>
    <li><strong>Confidence:</strong> $P(B \mid A) = \frac{P(A \cup B)}{P(A)}$ (Rule reliability)</li>
    <li><strong>Lift:</strong> $\frac{P(A \cup B)}{P(A)P(B)}$ (Correlation indicator: $>1$ positive, $=1$ independent, $<1$ negative)</li>
    <li><strong>Conviction:</strong> $\frac{P(A)P(\neg B)}{P(A \cup \neg B)} = \frac{1 - \text{Support}(B)}{1 - \text{Confidence}(A \implies B)}$ (Directional dependency)</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 10: Decision Tree Induction Criteria</div>
  <ul>
    <li><strong>Entropy:</strong> $H(S) = - \sum p_i \log_2 p_i$</li>
    <li><strong>Information Gain (ID3):</strong> $\text{Gain}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$</li>
    <li><strong>Gain Ratio (C4.5):</strong> $\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}$ where $\text{SplitInfo} = - \sum \frac{|S_v|}{|S|}\log_2\frac{|S_v|}{|S|}$</li>
    <li><strong>Gini Impurity (CART):</strong> $\text{Gini}(S) = 1 - \sum p_i^2$</li>
  </ul>
</div>
"""

def execute_super_final_dm():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST
    m5 = M5_CONTENT + M5_EXP + M5_DEEP + M5_MEGA + M5_ULTRA + M5_FINAL_BOOST

    print("Super Final M1 length:", len(m1))
    print("Super Final M2 length:", len(m2))
    print("Super Final M3 length:", len(m3))
    print("Super Final M4 length:", len(m4))
    print("Super Final M5 length:", len(m5))
    print("Super Final Rev length:", len(REVISION_PERFECT))

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
        REVISION_PERFECT
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
    {REVISION_PERFECT}
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
    execute_super_final_dm()
