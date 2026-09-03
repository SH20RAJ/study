#!/usr/bin/env python3
"""
Final Crown 10-Page Completion for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from finalize_dm_10_pages_true import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2,
    DM_REVISION_MASTER_10
)

# Boosts
M2_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 13: Principal Component Analysis (PCA) Variance Proof & SVD Relationship</div>
  <p>Prove that the principal component directions are given by the eigenvectors of the sample covariance matrix $\mathbf{\Sigma}$:</p>
  <ul>
    <li>Objective: Maximize projected variance $\mathbf{w}^T \mathbf{\Sigma} \mathbf{w}$ subject to $\|\mathbf{w}\|_2^2 = \mathbf{w}^T \mathbf{w} = 1$.</li>
    <li>Lagrangian: $\mathcal{L}(\mathbf{w}, \lambda) = \mathbf{w}^T \mathbf{\Sigma} \mathbf{w} - \lambda(\mathbf{w}^T \mathbf{w} - 1)$.</li>
    <li>Taking gradient with respect to $\mathbf{w}$ and setting to zero:
      $$\nabla_{\mathbf{w}} \mathcal{L} = 2\mathbf{\Sigma}\mathbf{w} - 2\lambda\mathbf{w} = 0 \implies \mathbf{\mathbf{\Sigma}\mathbf{w} = \lambda\mathbf{w}}$$
    </li>
    <li>This is the standard eigenvector equation! Multiplying by $\mathbf{w}^T$: $\mathbf{w}^T \mathbf{\Sigma} \mathbf{w} = \lambda \mathbf{w}^T \mathbf{w} = \lambda$.</li>
    <li>$$\mathbf{\text{Maximum variance is achieved by choosing the eigenvector corresponding to the largest eigenvalue } \lambda_{\text{max}}!}$$</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q13. Explain the V-Optimal Histogram Construction for Numerosity Reduction. (8 Marks)</div><div class="qa-a">A <strong>V-Optimal Histogram</strong> partitions $N$ data values into $B$ buckets such that the weighted variance of the bucket estimates is minimized across all possible partitionings:
$$\mathbf{\min \sum_{j=1}^B \sum_{i \in \text{Bucket}_j} (x_i - \bar{x}_j)^2}$$
Dynamic programming computes the globally optimal bucket boundaries in $O(B \cdot N^2)$ time. V-Optimal histograms provide the most statistically accurate selectivity estimation for database query optimizers!</div></div>
"""

M3_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 14: Semi-Additive vs Additive vs Non-Additive Measure Design</div>
  <p>In a financial banking data warehouse:</p>
  <ul>
    <li><strong>`Transaction_Amount`:</strong> Additive across Account, Branch, and Time ($\sum \text{Amount}$ is meaningful).</li>
    <li><strong>`Account_Ending_Balance`:</strong> <strong>Semi-Additive</strong> across Account and Branch, but NON-additive across Time (must use `Current_Balance` snapshot or `Avg_Balance` over time).</li>
    <li><strong>`Loan_Interest_Rate_%`:</strong> <strong>Non-Additive</strong> across all dimensions (must compute weighted average: $\frac{\sum \text{Balance} \times \text{Rate}}{\sum \text{Balance}}$).</li>
  </ul>
</div>
"""

M4_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 15: Cross-Support Property & Hyperclique Pattern Mining</div>
  <p>When items with vastly different support levels appear together (e.g. `Caviar` (support 0.1%) and `Milk` (support 80%)), standard confidence generates spurious cross-support rules:</p>
  <ul>
    <li><strong>H-Confidence Metric:</strong>
      $$\mathbf{\text{h-conf}(X) = \frac{\text{Support}(X)}{\max_{i \in X} \text{Support}(\{i\})}}$$
    </li>
    <li>A pattern $X$ is a <strong>Hyperclique Pattern</strong> if $\text{h-conf}(X) \ge h_{\text{min}}$. Guarantees all items in the pattern have strong mutual affinity!</li>
  </ul>
</div>
"""

M5_CROWN2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 16: Complete Naive Bayes Full Likelihood Table Proof</div>
  <p>Given prior probabilities $P(\text{Play}=\text{Yes}) = \frac{9}{14}, P(\text{Play}=\text{No}) = \frac{5}{14}$, and evidence $X = (\text{Outlook}=\text{Sunny}, \text{Temp}=\text{Cool}, \text{Humidity}=\text{High}, \text{Wind}=\text{Strong})$:</p>
  $$P(X \mid \text{Yes}) = \left(\frac{2}{9}\right) \left(\frac{3}{9}\right) \left(\frac{3}{9}\right) \left(\frac{3}{9}\right) = \frac{2 \times 3 \times 3 \times 3}{6561} = \frac{54}{6561} \approx \mathbf{0.00823}$$
  $$P(X \mid \text{No}) = \left(\frac{3}{5}\right) \left(\frac{1}{5}\right) \left(\frac{4}{5}\right) \left(\frac{3}{5}\right) = \frac{3 \times 1 \times 4 \times 3}{625} = \frac{36}{625} = \mathbf{0.05760}$$
  $$\mathbf{P(X, \text{Yes}) = 0.00823 \times \frac{9}{14} = \mathbf{0.00529} \qquad P(X, \text{No}) = 0.05760 \times \frac{5}{14} = \mathbf{0.02057}}$$
  $$\mathbf{\text{Posterior: } P(\text{No} \mid X) = \frac{0.02057}{0.00529 + 0.02057} = \frac{0.02057}{0.02586} = \mathbf{79.54\% \implies \text{Predict: NO PLAY!}}}$$
</div>
"""

# Massive Revision Guide (28k chars)
DM_REVISION_MASSIVE_10 = DM_REVISION_MASTER_10 + r"""
<h2 class="section-title">Comprehensive 10-Page Master Revision Examination Compendium</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 19: Full Data Preprocessing Pipeline Checklist</div>
  <ul>
    <li><strong>1. Data Cleaning:</strong> Missing values (impute mean/mode/k-NN), Noise smoothing (bin means, bin boundaries).</li>
    <li><strong>2. Data Integration:</strong> $\chi^2$ independence test for nominal data, Pearson $r$ / Covariance for numeric data.</li>
    <li><strong>3. Data Reduction:</strong> Dimensionality reduction (PCA, Wavelet, SVD, t-SNE), Numerosity reduction (Histograms, Clustering).</li>
    <li><strong>4. Data Transformation:</strong> Normalization (Min-Max, Z-score, Decimal scaling), Discretization (ChiMerge, Equi-depth binning).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 20: Data Warehouse Architecture Reference</div>
  <ul>
    <li><strong>Bottom Tier:</strong> Warehouse Database Server (relational back-end data store).</li>
    <li><strong>Middle Tier:</strong> OLAP Server (ROLAP relational engines, MOLAP multidimensional servers, or HOLAP hybrid).</li>
    <li><strong>Top Tier:</strong> Front-End Client Tools (Analysis, Query/Reporting, Data Mining engines).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 21: Full Association Mining Formulas</div>
  $$\text{Support}(A \implies B) = \frac{\text{count}(A \cup B)}{N} \qquad \text{Confidence}(A \implies B) = \frac{\text{count}(A \cup B)}{\text{count}(A)}$$
  $$\text{Lift}(A \implies B) = \frac{\text{Conf}(A \implies B)}{\text{Support}(B)} \qquad \text{Leverage} = P(A \cup B) - P(A)P(B)$$
  $$\text{Conviction} = \frac{1 - \text{Support}(B)}{1 - \text{Conf}(A \implies B)} \qquad \text{Jaccard}(A, B) = \frac{P(A \cup B)}{P(A) + P(B) - P(A \cup B)}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 22: Classification Decision Criteria</div>
  <ul>
    <li><strong>Information Gain (ID3):</strong> $\text{Gain}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$</li>
    <li><strong>Gain Ratio (C4.5):</strong> $\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}$</li>
    <li><strong>Gini Impurity (CART):</strong> $\text{Gini}(S) = 1 - \sum p_i^2$</li>
    <li><strong>Misclassification Error:</strong> $\text{Error}(S) = 1 - \max(p_i)$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 23: Complete Clustering Paradigms Summary</div>
  <table class="custom-table">
    <thead><tr><th>Method</th><th>Core Algorithm</th><th>Strengths & Limitations</th></tr></thead>
    <tbody>
      <tr><td><strong>Partitioning</strong></td><td>k-Means, k-Medoids (PAM)</td><td>Fast $O(t k N)$; spherical clusters only; sensitive to initialization.</td></tr>
      <tr><td><strong>Hierarchical</strong></td><td>AGNES (bottom-up), DIANA (top-down)</td><td>Dendrogram hierarchy; $O(N^2)$ distance matrix; irreversible merges.</td></tr>
      <tr><td><strong>Density-Based</strong></td><td>DBSCAN, OPTICS, DENCLUE</td><td>Arbitrary non-convex shapes; filters noise outliers; $O(N \log N)$ with spatial index.</td></tr>
      <tr><td><strong>Grid-Based</strong></td><td>STING, CLIQUE, WaveCluster</td><td>Quantized spatial grid cells; fast $O(K)$ query speed independent of $N$.</td></tr>
    </tbody>
  </table>
</div>
"""

def compile_crown():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST + M3_EXTRA_PASS + M3_CROWN + M3_TARGET + M3_FINAL_BOOST2 + M3_CROWN2
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST + M4_EXTRA_PASS + M4_CROWN + M4_TARGET + M4_FINAL_BOOST2 + M4_CROWN2
    m5 = M5_CONTENT + M5_EXP + M5_DEEP + M5_MEGA + M5_ULTRA + M5_FINAL_BOOST + M5_EXTRA_PASS + M5_CROWN + M5_TARGET + M5_FINAL_BOOST2 + M5_CROWN2

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
        DM_REVISION_MASSIVE_10
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
    {DM_REVISION_MASSIVE_10}
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
    compile_crown()
