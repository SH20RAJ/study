#!/usr/bin/env python3
"""
100% Pass Final Multi-Module Injector for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from finish_dm_10_pages_100_pass import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS,
    REVISION_ULTIMATE_PASS
)

M2_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 7: Data Discretization by ChiMerge ($\chi^2$-based Interval Merging)</div>
  <p><strong>ChiMerge (Kerber 1992)</strong> is a bottom-up supervised discretization algorithm:</p>
  <ol>
    <li>Sort continuous attribute values and place each distinct value into its own interval.</li>
    <li>For each pair of adjacent intervals, compute the $\chi^2$ statistic with respect to class labels.</li>
    <li>Identify the pair of adjacent intervals with the <strong>smallest $\chi^2$ value</strong> (indicating that their class distributions are most similar).</li>
    <li>Merge that pair into a single interval.</li>
    <li>Repeat steps 2–4 until all adjacent interval pairs have $\chi^2 \ge \text{threshold}$ (or until target number of intervals is reached).</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 8: Feature Extraction using Linear Discriminant Analysis (LDA) Projection</div>
  <p>For 2 classes with means $\mathbf{\mu}_1 = (1, 2)^T, \mathbf{\mu}_2 = (3, 4)^T$ and shared covariance $\mathbf{\Sigma} = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$:</p>
  $$\mathbf{w} \propto \mathbf{\Sigma}^{-1}(\mathbf{\mu}_1 - \mathbf{\mu}_2) = \frac{1}{2}\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} -2 \\ -2 \end{bmatrix} = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$
  $$\mathbf{\text{Optimal 1D Fisher Projection Line: } y = -x_1 - x_2}$$
</div>
"""

M3_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 9: Incremental View Maintenance in Real-Time Data Warehouses</div>
  <p>When operational databases insert new delta records $\Delta R$:</p>
  <ul>
    <li><strong>Counting Algorithm (Gupta et al.):</strong> For view $V = \pi_A(\sigma_C(R \Join S))$, maintain a count column $count(*)$ in the materialized view.</li>
    <li>When a base tuple is deleted, decrement $count(*)$. Only delete the view row when $count(*) = 0$.</li>
    <li>Allows real-time incremental view refreshment without re-computing the full multi-table join!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 10: Star-Cubing Shared-Prefix Path Algorithm</div>
  <p>Constructs a tree where nodes represent attribute-value pairs and links represent prefix sharing. Performs recursive top-down cuboid lattice traversal with bottom-up aggregation!</p>
</div>
"""

M4_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 11: Multi-Dimensional Association Rule Mining on Hybrid Relational Data</div>
  <p>When mining rules across multiple database relations (e.g. `Customer`, `Account`, `Transaction`):</p>
  <pre><code>Rule: age(X, "20..29") ∧ income(X, "40K..60K") ⇒ buys(X, "HDTV") [Support=2%, Confidence=60%]</code></pre>
  <ul>
    <li><strong>Quantitative Attributes Discretization:</strong> Age and Income are mapped to discrete intervals using equi-depth binning.</li>
    <li><strong>Predicate Itemset Representation:</strong> Each (attribute, interval) pair is treated as an item in a multidimensional transaction table.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 12: Sequence Pattern Mining with PrefixSpan Projected Databases</div>
  <p>PrefixSpan mines sequential patterns by projecting sequence suffixes into smaller projected databases, eliminating candidate generation entirely!</p>
</div>
"""

M5_CROWN = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 13: Cost-Complexity Tree Pruning ($Minimal \alpha$ Subtree Selection)</div>
  <p>In CART decision trees, the cost-complexity measure for subtree $T$ with parameter $\alpha \ge 0$ is:</p>
  $$\mathbf{R_\alpha(T) = R(T) + \alpha |T|}$$
  <p>Where $R(T)$ is the misclassification error rate and $|T|$ is the number of leaf nodes. By calculating $\alpha = \frac{R(t) - R(T_t)}{|T_t| - 1}$ for each internal node $t$, CART prunes nodes that produce the smallest error increase per leaf saved!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 14: Non-Linear Kernel Support Vector Machine (RBF Gaussian Kernel)</div>
  <p>The Radial Basis Function (RBF) kernel is formulated as:</p>
  $$\mathbf{K(\mathbf{x}, \mathbf{y}) = \exp\left( - \gamma \|\mathbf{x} - \mathbf{y}\|^2 \right) = \exp\left( - \frac{\|\mathbf{x} - \mathbf{y}\|^2}{2\sigma^2} \right)}$$
  <p>Maps input points into an <em>infinite-dimensional Hilbert space</em>, allowing linear separation of any arbitrary non-linear dataset!</p>
</div>
"""

REVISION_CROWN = REVISION_ULTIMATE_PASS + r"""
<h2 class="section-title">Comprehensive 5-Module Solved Algorithm Cheat-Sheets</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Cheat-Sheet 1: The Complete KDD Process Pipeline</div>
  $$\text{Raw Data} \xrightarrow{\text{Cleaning}} \text{Clean Data} \xrightarrow{\text{Integration}} \text{Data Warehouse} \xrightarrow{\text{Selection/Transformation}} \text{Transformed Data} \xrightarrow{\text{Data Mining}} \text{Patterns} \xrightarrow{\text{Evaluation}} \text{Actionable Knowledge}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Cheat-Sheet 2: Dimensional Schemas Compared</div>
  <ul>
    <li><strong>Star Schema:</strong> Single central fact table, de-normalized dimension tables, fast read queries.</li>
    <li><strong>Snowflake Schema:</strong> Normalized dimension tables in 3NF hierarchies, zero redundancy, complex multi-table SQL joins.</li>
    <li><strong>Fact Constellation:</strong> Multiple shared fact tables with conformed dimensions (Enterprise Bus).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Cheat-Sheet 3: Apriori vs FP-Growth vs ECLAT</div>
  <ul>
    <li><strong>Apriori:</strong> BFS candidate generation $L_{k-1} \Join L_{k-1}$, $k$ database scans.</li>
    <li><strong>FP-Growth:</strong> Divide-and-conquer, compact FP-Tree, 2 database scans, zero candidate generation.</li>
    <li><strong>ECLAT:</strong> Vertical TID-list intersections, zero candidate generation, fast bitwise AND.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Cheat-Sheet 4: Clustering Paradigms Compared</div>
  <ul>
    <li><strong>k-Means:</strong> Partitioning, minimizes SSE, spherical clusters, $O(t k N)$.</li>
    <li><strong>k-Medoids (PAM):</strong> Uses actual medoid points, robust to outliers, $O(k(N-k)^2)$.</li>
    <li><strong>AGNES / DIANA:</strong> Hierarchical dendrogram, no $k$ required, single/complete/average linkage.</li>
    <li><strong>DBSCAN:</strong> Density-based $(\epsilon, \text{MinPts})$, arbitrary shapes, filters noise outliers.</li>
  </ul>
</div>
"""

def compile_crown_pass():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST + M3_EXTRA_PASS + M3_CROWN
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST + M4_EXTRA_PASS + M4_CROWN
    m5 = M5_CONTENT + M5_EXP + M5_DEEP + M5_MEGA + M5_ULTRA + M5_FINAL_BOOST + M5_EXTRA_PASS + M5_CROWN

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
        REVISION_CROWN
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
    {REVISION_CROWN}
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
    compile_crown_pass()
