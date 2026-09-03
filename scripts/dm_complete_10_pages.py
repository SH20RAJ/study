#!/usr/bin/env python3
"""
Final definitive 10-Page Completion for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from finish_dm_100_percent_final import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2, M2_FINAL_STEP, M2_PERFECT,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2, M3_CROWN2, M3_FINAL_STEP, M3_PERFECT,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2, M4_CROWN2, M4_FINAL_STEP, M4_PERFECT,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2, M5_CROWN2, M5_FINAL_STEP,
    REVISION_PERFECT_ALL
)

M2_ADD = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 16: Discrete Fourier Transform (DFT) vs Wavelet Transform Signal Compression</div>
  <p>For a 1D sequence of length $N = 2^n$, DFT projects data onto complex sinusoids $X_k = \sum_{n=0}^{N-1} x_n e^{-i 2\pi k n / N}$ ($O(N \log N)$ FFT). In contrast, Wavelet transform uses compact dyadic wavelets $\psi_{j, k}(t) = 2^{j/2}\psi(2^j t - k)$, achieving linear $O(N)$ computational complexity and retaining precise time-frequency localization of transient data spikes!</p>
</div>

<div class="qa-card"><div class="qa-q">Q15. Explain Stratified Sampling vs Simple Random Sampling (SRS) in Imbalanced Data Mining. (8 Marks)</div><div class="qa-a">• <strong>Simple Random Sampling (SRS):</strong> Every record has equal probability $1/N$ of selection. On highly imbalanced datasets (e.g. 99% legitimate, 1% fraud), SRS risks drawing zero fraud instances!<br>• <strong>Stratified Sampling:</strong> Divides the dataset into non-overlapping strata (classes $C_1, \dots, C_k$) and draws samples from each stratum proportionally (or equally via oversampling), guaranteeing that rare minority classes are preserved in training subsets!</div></div>
"""

M4_ADD = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 18: Hash-Tree Support Counting in Apriori Pass 3</div>
  <p>To avoid checking every candidate itemset against all transactions, Apriori stores candidate $k$-itemsets in a <strong>Hash Tree</strong> where each internal node contains a hash function $h(item) = item \pmod B$. When matching a transaction $T$, the hash tree recursively routes subsets through matching hash buckets, checking candidates in $O(1)$ tree traversal time rather than linear scans!</p>
</div>
"""

REVISION_ADD = REVISION_PERFECT_ALL + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 31: OLAP Storage Architecture Summary</div>
  <ul>
    <li><strong>ROLAP:</strong> Relational backend, Star/Snowflake schemas, high scalability, SQL engine.</li>
    <li><strong>MOLAP:</strong> Multidimensional array backend, dense matrix offsets, sub-second query latency.</li>
    <li><strong>HOLAP:</strong> Hybrid engine: relational for detailed leaf records, multidimensional arrays for aggregates.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 32: Outlier Detection Techniques Compared</div>
  <ul>
    <li><strong>Statistical:</strong> $3\sigma$ rule, Grubbs' test, Tukey's IQR fences (assumes parametric distribution).</li>
    <li><strong>Distance-Based:</strong> $k$-NN distance thresholding ($O(N^2)$).</li>
    <li><strong>Density-Based:</strong> Local Outlier Factor (LOF) comparing local reachability densities.</li>
    <li><strong>Ensemble:</strong> Isolation Forest (iTrees) measuring average path lengths to isolate anomalies in $O(N \log N)$.</li>
  </ul>
</div>
"""

def run_definitive_dm():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP + M2_PERFECT + M2_ADD
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
        REVISION_ADD
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
    {REVISION_ADD}
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
    run_definitive_dm()
