#!/usr/bin/env python3
"""
100% Guaranteed Pass for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from dm_complete_10_pages import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2, M2_FINAL_STEP, M2_PERFECT, M2_ADD,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2, M3_CROWN2, M3_FINAL_STEP, M3_PERFECT,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2, M4_CROWN2, M4_FINAL_STEP, M4_PERFECT, M4_ADD,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2, M5_CROWN2, M5_FINAL_STEP,
    REVISION_ADD
)

M2_FINAL_PUSH = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 17: Multi-Class Linear Discriminant Analysis (LDA) Between-Class Scatter Matrix Derivation</div>
  <p>For $C$ classes with means $\mathbf{\mu}_c$ and global mean $\mathbf{\mu}$:</p>
  $$\mathbf{S}_B = \sum_{c=1}^C N_c (\mathbf{\mu}_c - \mathbf{\mu})(\mathbf{\mu}_c - \mathbf{\mu})^T \qquad \mathbf{S}_W = \sum_{c=1}^C \sum_{i \in c} (\mathbf{x}_i - \mathbf{\mu}_c)(\mathbf{x}_i - \mathbf{\mu}_c)^T$$
  <p>Maximizing Rayleigh quotient $\frac{\mathbf{w}^T \mathbf{S}_B \mathbf{w}}{\mathbf{w}^T \mathbf{S}_W \mathbf{w}}$ yields generalized eigenvalue problem $\mathbf{S}_W^{-1} \mathbf{S}_B \mathbf{w} = \lambda \mathbf{w}$. Number of non-zero discriminant directions is at most $\mathbf{\min(p, C-1)}$!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 18: Quantile Normalization for High-Throughput Genomics & Microarrays</div>
  <p><strong>Quantile Normalization</strong> aligns empirical distributions across multiple experimental batches:</p>
  <ol>
    <li>Sort values in each column independently.</li>
    <li>Compute the mean across rows for the sorted values.</li>
    <li>Replace each sorted value with the row average.</li>
    <li>Restore columns back to their original rank orders, ensuring all columns have identical empirical distributions!</li>
  </ol>
</div>
"""

REVISION_FINAL_PUSH = REVISION_ADD + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 33: Complete Model Performance Metrics Reference</div>
  <table class="custom-table">
    <thead><tr><th>Metric</th><th>Formula</th><th>Diagnostic Focus</th></tr></thead>
    <tbody>
      <tr><td><strong>Accuracy</strong></td><td>$\frac{TP + TN}{N}$</td><td>Overall proportion of correct classifications.</td></tr>
      <tr><td><strong>Sensitivity (Recall)</strong></td><td>$\frac{TP}{TP + FN}$</td><td>Minimizing False Negatives (medical diagnosis).</td></tr>
      <tr><td><strong>Specificity</strong></td><td>$\frac{TN}{TN + FP}$</td><td>True Negative rate ($1 - \text{FPR}$).</td></tr>
      <tr><td><strong>Precision</strong></td><td>$\frac{TP}{TP + FP}$</td><td>Minimizing False Positives (search ranking, spam).</td></tr>
      <tr><td><strong>$F_1$-Score</strong></td><td>$\frac{2 \cdot P \cdot R}{P + R}$</td><td>Harmonic mean for imbalanced targets.</td></tr>
      <tr><td><strong>ROC AUC</strong></td><td>$\int_0^1 \text{TPR}(t) d(\text{FPR}(t))$</td><td>Threshold-independent ranking performance.</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 34: Data Preprocessing Matrix & Transformation Techniques</div>
  <ul>
    <li><strong>Data Cleaning:</strong> Missing imputation (MICE, k-NN), Noise smoothing (bin means/boundaries).</li>
    <li><strong>Data Integration:</strong> $\chi^2$ independence test ($df=(r-1)(c-1)$), Pearson correlation $r_{A, B}$.</li>
    <li><strong>Data Transformation:</strong> Min-Max to $[0, 1]$, Z-score standardization ($\mu=0, \sigma=1$), Decimal scaling.</li>
    <li><strong>Data Reduction:</strong> PCA ($EVR \ge 95\%$), DWT Wavelets, SVD low-rank approximation, ReliefF feature selection.</li>
  </ul>
</div>
"""

def execute_final_dm_100():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP + M2_PERFECT + M2_ADD + M2_FINAL_PUSH
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST + M3_EXTRA_PASS + M3_CROWN + M3_TARGET + M3_FINAL_BOOST2 + M3_CROWN2 + M3_FINAL_STEP + M3_PERFECT
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST + M4_EXTRA_PASS + M4_CROWN + M4_TARGET + M4_FINAL_BOOST2 + M4_CROWN2 + M4_FINAL_STEP + M4_PERFECT + M4_ADD
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
        REVISION_FINAL_PUSH
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
    {REVISION_FINAL_PUSH}
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
    execute_final_dm_100()
