#!/usr/bin/env python3
"""
Final 100% Pass Touch for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from dm_100_percent_final_pass import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2, M2_FINAL_STEP, M2_PERFECT, M2_ADD, M2_FINAL_PUSH,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2, M3_CROWN2, M3_FINAL_STEP, M3_PERFECT,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2, M4_CROWN2, M4_FINAL_STEP, M4_PERFECT, M4_ADD,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2, M5_CROWN2, M5_FINAL_STEP,
    REVISION_FINAL_PUSH
)

M2_FINAL_BOOST3 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 19: Discrete Cosine Transform (DCT) vs PCA Data Compression</div>
  <p>The <strong>Discrete Cosine Transform (DCT)</strong> expresses a finite sequence of data points in terms of a sum of cosine functions oscillating at different frequencies:
  $$\mathbf{X_k = \sum_{n=0}^{N-1} x_n \cos\left[ \frac{\pi}{N} \left( n + \frac{1}{2} \right) k \right]}$$
  • <strong>Energy Compaction Property:</strong> DCT concentrates most of the signal energy into the first few low-frequency transform coefficients.<br>• <strong>PCA vs DCT:</strong> PCA requires computing data covariance matrices $O(N p^2)$ and solving eigenvalue polynomials. DCT uses fixed data-independent cosine basis functions, allowing $O(N \log N)$ fast FFT computation (used in JPEG image compression and MP3 audio encoding)!</p>
</div>
"""

REVISION_FINAL_TOUCH = REVISION_FINAL_PUSH + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 35: Apriori Join & Prune Step Rule</div>
  <p>Two frequent $(k-1)$-itemsets $p, q \in L_{k-1}$ are joined if they share the first $k-2$ items ($p[1]=q[1], \dots, p[k-2]=q[k-2]$ and $p[k-1] < q[k-1]$). Candidate $c = p \cup \{q[k-1]\}$ is pruned if ANY of its $(k-1)$ subsets is missing from $L_{k-1}$!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 36: DBSCAN Point Categorization Rule</div>
  <ul>
    <li><strong>Core Point:</strong> $|N_\epsilon(p)| \ge \text{MinPts}$ (Density center)</li>
    <li><strong>Border Point:</strong> $|N_\epsilon(p)| < \text{MinPts}$, but $p \in N_\epsilon(q)$ where $q$ is a core point</li>
    <li><strong>Noise Point:</strong> Neither core nor border (Isolated anomaly)</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 37: Multi-Dimensional Schema Architecture Rule</div>
  <ul>
    <li><strong>Star Schema:</strong> Fact table surrounded by flat de-normalized dimension tables.</li>
    <li><strong>Snowflake Schema:</strong> Fact table surrounded by normalized dimension hierarchy tables.</li>
    <li><strong>Fact Constellation:</strong> Multiple fact tables sharing conformed dimensions.</li>
  </ul>
</div>
"""

def execute_final_touch():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP + M2_PERFECT + M2_ADD + M2_FINAL_PUSH + M2_FINAL_BOOST3
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

    html_m2 = wrap_html("Module 2: Data Preprocessing & Dimensionality Reduction", "Topics 15 to 20 • Missing Imputation, Binning, Chi-Square Independence, Normalization & PCA", m2, module_num=2)
    with open(os.path.join(HTML_DIR, "Module_2_Data_Preprocessing_Notes.html"), "w", encoding="utf-8") as f:
        f.write(html_m2)
    generate_pdf(os.path.join(HTML_DIR, "Module_2_Data_Preprocessing_Notes.html"), os.path.join(PDF_DIR, "Module_2_Data_Preprocessing_Notes.pdf"), "DMCT Module 2")

    # Revision
    rev_html = wrap_html(
        "Data Mining (CS24303) 10-Page Master Revision",
        "High-Yield Formulas, Schemas, Cuboid Lattices, Apriori Rules & Solved Numerical Cards",
        REVISION_FINAL_TOUCH
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
    {REVISION_FINAL_TOUCH}
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
    execute_final_touch()
