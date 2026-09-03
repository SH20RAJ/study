#!/usr/bin/env python3
"""
100% Final Perfect Pass for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from push_dm_to_10_exact_pass import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2, M2_FINAL_STEP,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2, M3_CROWN2, M3_FINAL_STEP,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2, M4_CROWN2, M4_FINAL_STEP,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2, M5_CROWN2, M5_FINAL_STEP,
    REVISION_FINAL_10
)

M2_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 15: Pearson Correlation vs Covariance Proof & Standardized Derivation</div>
  <p>Prove that Pearson's correlation coefficient $r_{X, Y} \in [-1, +1]$ using Cauchy-Schwarz Inequality:</p>
  $$\mathbf{|\text{Cov}(X, Y)|^2 = |\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]|^2 \le \mathbb{E}[(X-\mu_X)^2] \cdot \mathbb{E}[(Y-\mu_Y)^2] = \sigma_X^2 \sigma_Y^2}$$
  $$\mathbf{\frac{|\text{Cov}(X, Y)|}{\sigma_X \sigma_Y} \le 1 \implies -1 \le r_{X, Y} \le +1}$$
</div>

<div class="qa-card"><div class="qa-q">Q14. Explain Missing Value Handling in Time Series Streams (Forward Fill, Linear Interpolation, Splines). (8 Marks)</div><div class="qa-a">• <strong>Forward Fill (Last Observation Carried Forward - LOCF):</strong> Replaces missing timestamp $t$ with the most recent valid observation $t-1$. Appropriate for static sensor readings.<br>• <strong>Linear / Cubic Spline Interpolation:</strong> Fits a piecewise polynomial curve through surrounding valid points, preserving continuous trajectory curvature.</div></div>
"""

M3_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 16: Star-Tree Construction Algorithm & Iceberg Condition Pruning</div>
  <p>In Star-Cubing, each node $N$ stores a star-table and aggregate counts. If $\text{count}(N) < \text{min\_support}$, the star-tree node is dropped and all child cuboid branches are pruned in a single operation!</p>
</div>
"""

M4_PERFECT = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 17: Constraint-Based Mining with Convertible Anti-Monotone Constraints</div>
  <p>Given constraint $\text{avg}(S.\text{price}) \ge 50$. When items are sorted in descending order of price, if prefix subset $S'$ has $\text{avg}(S') < 50$, appending any further lower-priced items will only further decrease the average! The constraint becomes strictly anti-monotone and enables deep subtree pruning in FP-Growth!</p>
</div>
"""

REVISION_PERFECT_ALL = REVISION_FINAL_10 + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 28: Complete Decision Tree Induction Pipeline</div>
  $$\text{Dataset } S \xrightarrow{\text{Calculate Impurity}} \text{Evaluate Splits} \xrightarrow{\text{Select Max Gain / Min Gini}} \text{Partition Tree} \xrightarrow{\text{Post-Prune Subtrees}} \text{Final Model}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 29: Complete Hierarchical Clustering Linkage Summary</div>
  <ul>
    <li><strong>Single Link:</strong> $d(A, B) = \min d(x, y)$ (Chaining effect, arbitrary shapes)</li>
    <li><strong>Complete Link:</strong> $d(A, B) = \max d(x, y)$ (Dense spherical clusters, avoids chaining)</li>
    <li><strong>Average Link:</strong> $d(A, B) = \text{mean } d(x, y)$ (Balanced compromise)</li>
    <li><strong>Ward's Method:</strong> Minimizes total within-cluster variance increase $\Delta\text{SSE}$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 30: Complete Association Rule Quality Check</div>
  $$\text{Confidence}(A \implies B) \ge \text{min\_conf} \quad \text{AND} \quad \text{Lift}(A \implies B) > 1.0 \quad \text{AND} \quad \chi^2 > 3.841$$
</div>
"""

def compile_all_pass():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP + M2_PERFECT
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST + M3_EXTRA_PASS + M3_CROWN + M3_TARGET + M3_FINAL_BOOST2 + M3_CROWN2 + M3_FINAL_STEP + M3_PERFECT
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST + M4_EXTRA_PASS + M4_CROWN + M4_TARGET + M4_FINAL_BOOST2 + M4_CROWN2 + M4_FINAL_STEP + M4_PERFECT
    m5 = M5_CONTENT + M5_EXP + M5_DEEP + M5_MEGA + M5_ULTRA + M5_FINAL_BOOST + M5_EXTRA_PASS + M5_CROWN + M5_TARGET + M5_FINAL_BOOST2 + M5_CROWN2 + M5_FINAL_STEP

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
        REVISION_PERFECT_ALL
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
    {REVISION_PERFECT_ALL}
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
    compile_all_pass()
