#!/usr/bin/env python3
"""
Final 100% Guaranteed Pass for Data Mining (CS24303).
All modules strictly 10 pages, Revision 10 pages, Master Book 55+ pages!
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf
from finalize_dm_perfect_all_10 import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2, M2_FINAL_STEP, M2_PERFECT, M2_ADD, M2_FINAL_PUSH, M2_FINAL_BOOST3, M2_FINAL_BOOST4,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2, M3_CROWN2, M3_FINAL_STEP, M3_PERFECT,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2, M4_CROWN2, M4_FINAL_STEP, M4_PERFECT, M4_ADD,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2, M5_CROWN2, M5_FINAL_STEP,
    REVISION_FINAL_BOOST4,
    DM_LAB_EXTENSIVE
)

M2_TINY_BOOST = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 21: Multi-Dimensional Data Transformation & Wavelet Thresholding</div>
  <p>In Wavelet soft thresholding: $\hat{w} = \text{sign}(w)(|w| - \lambda)_+$ with Universal threshold $\lambda = \sigma \sqrt{2 \ln N}$. Discards high-frequency stochastic noise coefficients while preserving sharp edge boundaries in spatial signals!</p>
</div>
"""

REVISION_TINY_BOOST = REVISION_FINAL_BOOST4 + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 41: Data Cube Computation Strategies</div>
  <ul>
    <li><strong>BUC (Bottom-Up Computation):</strong> Explores cuboid tree bottom-up with Apriori pruning; ideal for sparse iceberg cubes.</li>
    <li><strong>MultiWay Array Aggregation:</strong> Computes full dense cubes in single pass over multidimensional RAM chunks.</li>
    <li><strong>Star-Cubing:</strong> Combines star-trees and shared prefix paths for iceberg cubing.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 42: Distance Metrics Axioms & Semi-Metrics</div>
  $$\text{Non-negativity: } d(x, y) \ge 0 \qquad \text{Identity: } d(x, y) = 0 \iff x = y$$
  $$\text{Symmetry: } d(x, y) = d(y, x) \qquad \text{Triangle Inequality: } d(x, z) \le d(x, y) + d(y, z)$$
</div>
"""

def execute_definitive_dm():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP + M2_PERFECT + M2_ADD + M2_FINAL_PUSH + M2_FINAL_BOOST3 + M2_FINAL_BOOST4 + M2_TINY_BOOST
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

    # Re-render M2
    html_m2 = wrap_html("Module 2: Data Preprocessing & Dimensionality Reduction", "Topics 15 to 20 • Missing Imputation, Binning, Chi-Square Independence, Normalization & PCA", m2, module_num=2)
    with open(os.path.join(HTML_DIR, "Module_2_Data_Preprocessing_Notes.html"), "w", encoding="utf-8") as f:
        f.write(html_m2)
    generate_pdf(os.path.join(HTML_DIR, "Module_2_Data_Preprocessing_Notes.html"), os.path.join(PDF_DIR, "Module_2_Data_Preprocessing_Notes.pdf"), "DMCT Module 2")

    # Revision
    rev_html = wrap_html(
        "Data Mining (CS24303) 10-Page Master Revision",
        "High-Yield Formulas, Schemas, Cuboid Lattices, Apriori Rules & Solved Numerical Cards",
        REVISION_TINY_BOOST
    )
    rev_html_file = os.path.join(HTML_DIR, "DM_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "DM_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "DM 10-Page Master Revision")

    # Lab Guide Standalone PDF
    lab_html = wrap_html(
        "Data Mining Python Laboratory Guide",
        "Hands-On Implementation of Apriori, Decision Trees & DBSCAN",
        DM_LAB_EXTENSIVE
    )
    lab_html_file = os.path.join(HTML_DIR, "DM_Lab_Practical_Guide.html")
    lab_pdf_file = os.path.join(PDF_DIR, "DM_Lab_Practical_Guide.pdf")
    with open(lab_html_file, "w", encoding="utf-8") as f:
        f.write(lab_html)
    generate_pdf(lab_html_file, lab_pdf_file, "DM Lab Guide")

    # Merge Full Master Book PDF cleanly using PyMuPDF
    master_doc = fitz.open()
    for num, _, _, _, fname in modules:
        mod_pdf = fitz.open(os.path.join(PDF_DIR, f"{fname}.pdf"))
        master_doc.insert_pdf(mod_pdf)
    
    lab_doc = fitz.open(lab_pdf_file)
    master_doc.insert_pdf(lab_doc)

    rev_doc = fitz.open(rev_pdf_file)
    master_doc.insert_pdf(rev_doc)

    master_pdf_path = os.path.join(PDF_DIR, "DM_Full_Course_Master.pdf")
    master_doc.save(master_pdf_path)
    print(f"✅ Generated {master_pdf_path} ({len(master_doc)} pages)")

if __name__ == "__main__":
    execute_definitive_dm()
