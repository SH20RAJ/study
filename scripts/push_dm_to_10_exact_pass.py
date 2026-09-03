#!/usr/bin/env python3
"""
Final Exact 10-Page Completion for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from dm_true_10_pages_crown import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2, M3_CROWN2,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2, M4_CROWN2,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2, M5_CROWN2,
    DM_REVISION_MASSIVE_10
)

M2_FINAL_STEP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 14: Kernel Density Estimation (KDE) for Continuous Density Smoothing</div>
  <p>For $N$ observations, <strong>Kernel Density Estimation</strong> computes continuous probability density function $\hat{f}(x)$ with Gaussian kernel $K(u) = \frac{1}{\sqrt{2\pi}}e^{-u^2/2}$ and bandwidth $h$:</p>
  $$\mathbf{\hat{f}(x) = \frac{1}{Nh} \sum_{i=1}^N K\left( \frac{x - x_i}{h} \right) = \frac{1}{Nh\sqrt{2\pi}} \sum_{i=1}^N \exp\left( - \frac{(x - x_i)^2}{2h^2} \right)}$$
  <p><strong>Bandwidth Selection (Silverman's Rule of Thumb):</strong> $h = 0.9 \min\left( \hat{\sigma}, \frac{\text{IQR}}{1.34} \right) N^{-1/5}$. Prevents oversmoothing (high bias) and undersmoothing (spurious variance)!</p>
</div>
"""

M3_FINAL_STEP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 15: Slowly Changing Dimensions Type 4 (History Table) vs Type 6 (Hybrid)</div>
  <p>• <strong>SCD Type 4:</strong> Maintains a primary dimension table with current attributes, and writes historical changes to a separate history fact table.<br>• <strong>SCD Type 6 (1 + 2 + 3):</strong> Hybrid schema containing both historical rows (Type 2) and current overwrite columns (Type 3) alongside surrogate keys!</p>
</div>
"""

M4_FINAL_STEP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 16: Multi-Dimensional Association Rules with Hybrid Quantitative Grid Discretization</div>
  <p>Combines categorical attributes with numeric grid intervals to discover cross-domain rules: $\text{Age}(X, 20..29) \land \text{Occupation}(X, \text{'Engineer'}) \implies \text{Income}(X, \text{'High'}) \ [\text{Conf}=85\%]$.</p>
</div>
"""

M5_FINAL_STEP = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 17: Multi-Class Support Vector Machine (One-vs-Rest vs One-vs-One)</div>
  <p>• <strong>One-vs-Rest (OvR):</strong> Trains $K$ binary classifiers separating class $k$ from all other $K-1$ classes combined. Fast ($K$ models), but sensitive to class imbalance.<br>• <strong>One-vs-One (OvO):</strong> Trains $\frac{K(K-1)}{2}$ binary classifiers separating all pairwise combinations. Slower training, but each classifier is trained on balanced subsets!</p>
</div>
"""

REVISION_FINAL_10 = DM_REVISION_MASSIVE_10 + r"""
<h2 class="section-title">Master Exam Final Checklists & Complete Solved Cards</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 24: KDD vs Data Mining vs Machine Learning</div>
  <ul>
    <li><strong>KDD:</strong> Complete iterative end-to-end knowledge discovery process (Cleaning, Integration, Selection, Transformation, Mining, Evaluation, Presentation).</li>
    <li><strong>Data Mining:</strong> The algorithmic pattern discovery phase of KDD.</li>
    <li><strong>Machine Learning:</strong> Algorithms that learn predictive functions from data.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 25: All Normalization Formulas</div>
  <ul>
    <li><strong>Min-Max:</strong> $v' = \frac{v - \min}{\max - \min}(\text{new\_max} - \text{new\_min}) + \text{new\_min}$</li>
    <li><strong>Z-Score:</strong> $z = \frac{v - \mu}{\sigma}$</li>
    <li><strong>Robust MAD:</strong> $M_i = \frac{0.6745(x_i - \text{Median})}{\text{MAD}}$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 26: Complete Data Warehousing Concepts</div>
  <ul>
    <li><strong>Inmon:</strong> Top-down 3NF centralized enterprise data warehouse.</li>
    <li><strong>Kimball:</strong> Bottom-up dimensional data marts with conformed dimensions.</li>
    <li><strong>Star:</strong> De-normalized, fast OLAP queries.</li>
    <li><strong>Snowflake:</strong> Normalized dimensions, zero redundancy, multi-join queries.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 27: Association Rule Metrics</div>
  $$\text{Support} = \frac{\text{count}(A \cup B)}{N} \qquad \text{Confidence} = \frac{\text{count}(A \cup B)}{\text{count}(A)} \qquad \text{Lift} = \frac{\text{Conf}}{\text{Support}(B)}$$
</div>
"""

def compile_exact_pass():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST + M3_EXTRA_PASS + M3_CROWN + M3_TARGET + M3_FINAL_BOOST2 + M3_CROWN2 + M3_FINAL_STEP
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST + M4_EXTRA_PASS + M4_CROWN + M4_TARGET + M4_FINAL_BOOST2 + M4_CROWN2 + M4_FINAL_STEP
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
        REVISION_FINAL_10
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
    {REVISION_FINAL_10}
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
    compile_exact_pass()
