#!/usr/bin/env python3
"""
100% PASS Precision Builder for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from push_dm_all_10_pages_final import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST,
    REVISION_PERFECT
)

M2_EXTRA_PASS = r"""
<h2 class="section-title">Topic 20.6: Complete Solved Laboratory Problem Bank on Data Cleaning</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 5: Multi-Attribute Missing Imputation via k-Nearest Neighbors (k-NN)</div>
  <p>Consider 5 customer profiles with attributes $\text{Age}$ and $\text{Income}$ (in \$k). A new record $X = (30, ?)$ has missing Income:</p>
  <ul>
    <li>$P_1 = (25, \$40\text{k}), \ P_2 = (32, \$60\text{k}), \ P_3 = (28, \$55\text{k}), \ P_4 = (45, \$90\text{k}), \ P_5 = (31, \$58\text{k})$.</li>
  </ul>
  <p><strong>1. Calculate Euclidean Distances on Normalized Age ($\min=25, \max=45$):</strong></p>
  <ul>
    <li>$d(X, P_1) = \frac{|30-25|}{20} = \frac{5}{20} = 0.25$</li>
    <li>$d(X, P_2) = \frac{|30-32|}{20} = \frac{2}{20} = 0.10$</li>
    <li>$d(X, P_3) = \frac{|30-28|}{20} = \frac{2}{20} = 0.10$</li>
    <li>$d(X, P_4) = \frac{|30-45|}{20} = \frac{15}{20} = 0.75$</li>
    <li>$d(X, P_5) = \frac{|30-31|}{20} = \frac{1}{20} = \mathbf{0.05 \ (Nearest!)}$</li>
  </ul>
  <p><strong>2. Imputation with $k = 3$ Neighbors ($P_5, P_2, P_3$):</strong></p>
  $$\mathbf{\text{Imputed Income} = \frac{\$58\text{k} + \$60\text{k} + \$55\text{k}}{3} = \frac{\$173\text{k}}{3} = \mathbf{\$57.67\text{k}}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 6: Decimal Scaling & Robust Outlier MAD Normalization</div>
  <p>For dataset $X = \{10, 12, 14, 15, 16, 18, 100\}$ with $\text{Median} = 15$:</p>
  <ul>
    <li>Deviations from median $|x_i - 15|$: $\{5, 3, 1, 0, 1, 3, 85\}$.</li>
    <li>Sorted deviations: $\{0, 1, 1, 3, 3, 5, 85\} \implies \text{MAD} = \mathbf{3.0}$.</li>
    <li>Robust Z-score for outlier $100$: $M_i = \frac{0.6745(100 - 15)}{3.0} = \frac{0.6745(85)}{3.0} = \frac{57.33}{3.0} = \mathbf{19.11 \gg 3.5 \implies \text{Extreme Outlier!}}$</li>
  </ul>
</div>
"""

M3_EXTRA_PASS = r"""
<h2 class="section-title">Topic 29.6: Complete Solved Laboratory Problem Bank on OLAP Aggregations</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 6: Bitmap Index Vector Compression via Run-Length Encoding (WAH)</div>
  <p>A high-cardinality bitmap index bit vector has 128 bits containing sparse ones: `00000000 00000000 ... 00000001`:</p>
  <ul>
    <li><strong>Word-Aligned Hybrid (WAH) Compression:</strong> Replaces consecutive sequences of 31-bit zero words with a single 32-bit run word encoding the count.</li>
    <li>Compresses a 100-million-bit sparse bitmap into less than $200\text{ KB}$ of RAM!</li>
    <li>Allows bitwise AND/OR queries to execute directly on the compressed format without decompression!</li>
  </ul>
</div>
"""

M4_EXTRA_PASS = r"""
<h2 class="section-title">Topic 36.6: Complete Solved Laboratory Problem Bank on Association Rules</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 7: Association Rule Conviction & Leverage Calculations</div>
  <p>In a database of 1000 transactions, $\text{Support}(A) = 0.20$, $\text{Support}(B) = 0.60$, $\text{Support}(A \cup B) = 0.18$:</p>
  <ul>
    <li>$\text{Confidence}(A \implies B) = \frac{0.18}{0.20} = \mathbf{0.90 = 90\%}$</li>
    <li>$\text{Lift}(A \implies B) = \frac{0.90}{0.60} = \mathbf{1.50 > 1 \implies \text{Positive correlation}}$</li>
    <li><strong>Leverage:</strong> $\text{Leverage} = P(A \cup B) - P(A)P(B) = 0.18 - (0.20)(0.60) = 0.18 - 0.12 = \mathbf{+0.06}$</li>
    <li><strong>Conviction:</strong> $\text{Conviction} = \frac{1 - P(B)}{1 - \text{Conf}(A \implies B)} = \frac{1 - 0.60}{1 - 0.90} = \frac{0.40}{0.10} = \mathbf{4.00}$</li>
    <li>$\text{Conviction} = 4.00$ implies that the rule would be incorrect 4 times more often if the association were purely accidental!</li>
  </ul>
</div>
"""

M5_EXTRA_PASS = r"""
<h2 class="section-title">Topic 46.6: Complete Solved Laboratory Problem Bank on Clustering & Classification</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 8: k-Medoids Partitioning Around Medoids (PAM) Execution Step</div>
  <p>Given 5 objects with pairwise $L_1$ distances: $P_1(1, 1), P_2(2, 2), P_3(3, 3), P_4(8, 8), P_5(9, 9)$. Initial medoids $M_1 = P_2(2, 2), M_2 = P_4(8, 8)$:</p>
  <ul>
    <li>Initial Total Cost = $d(P_1, P_2) + d(P_3, P_2) + d(P_5, P_4) = (|1-2|+|1-2|) + (|3-2|+|3-2|) + (|9-8|+|9-8|) = 2 + 2 + 2 = \mathbf{6.0}$.</li>
    <li>Swap $P_2$ with non-medoid candidate $P_3(3, 3)$:</li>
    <li>New Cost = $d(P_1, P_3) + d(P_2, P_3) + d(P_5, P_4) = 4 + 2 + 2 = \mathbf{8.0}$.</li>
    <li>$\Delta\text{Cost} = 8.0 - 6.0 = +2.0 > 0 \implies \mathbf{\text{Reject swap! Keep } P_2 \text{ as medoid!}}$</li>
  </ul>
</div>
"""

REVISION_ULTIMATE_PASS = REVISION_PERFECT + r"""
<h2 class="section-title">High-Yield Exam Strategy & Complete Topic Review Checklist</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 11: Five-Number Summary & Outlier Fences</div>
  $$\text{IQR} = Q_3 - Q_1 \qquad \text{Lower} = Q_1 - 1.5(\text{IQR}) \qquad \text{Upper} = Q_3 + 1.5(\text{IQR})$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 12: Chi-Square Test & Degrees of Freedom</div>
  $$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \qquad df = (\text{rows} - 1)(\text{cols} - 1)$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 13: Data Cube Lattice Formula</div>
  $$\text{Total Cuboids with Hierarchies} = \prod_{i=1}^n (L_i + 1)$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 14: FP-Tree Mining Mechanism</div>
  $$\text{Frequent Suffix } X \rightarrow \text{Conditional Pattern Base} \rightarrow \text{Conditional FP-Tree} \rightarrow \text{Frequent Patterns}$$
</div>
"""

def run_pass():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST + M3_EXTRA_PASS
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST + M4_EXTRA_PASS
    m5 = M5_CONTENT + M5_EXP + M5_DEEP + M5_MEGA + M5_ULTRA + M5_FINAL_BOOST + M5_EXTRA_PASS

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
        REVISION_ULTIMATE_PASS
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
    {REVISION_ULTIMATE_PASS}
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
    run_pass()
