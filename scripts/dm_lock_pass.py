#!/usr/bin/env python3
"""
Final 10-page locked for DM M2 & Revision.
"""

import os, sys, fitz
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf
from dm_final_pass_10 import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2, M2_FINAL_STEP, M2_PERFECT, M2_ADD, M2_FINAL_PUSH, M2_FINAL_BOOST3, M2_FINAL_BOOST4, M2_TINY_BOOST, M2_FINAL_ONE_PAGE,
    REVISION_FINAL_ONE_PAGE
)

M2_LOCKED = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 23: Fast Fourier Transform (FFT) vs Wavelet Energy Compaction Proof</div>
  <p>For discrete signal $x = [1, 3, 5, 7]$:</p>
  <ul>
    <li>Haar Wavelet level 1 averages: $a_1 = [\frac{1+3}{\sqrt{2}}, \frac{5+7}{\sqrt{2}}] = [2\sqrt{2}, 6\sqrt{2}] \approx [2.828, 8.485]$.</li>
    <li>Haar Wavelet level 1 details: $d_1 = [\frac{1-3}{\sqrt{2}}, \frac{5-7}{\sqrt{2}}] = [-\sqrt{2}, -\sqrt{2}] \approx [-1.414, -1.414]$.</li>
    <li>Haar level 2 average: $a_2 = \frac{2\sqrt{2} + 6\sqrt{2}}{\sqrt{2}} = \mathbf{8.0}$.</li>
    <li>Haar level 2 detail: $d_2 = \frac{2\sqrt{2} - 6\sqrt{2}}{\sqrt{2}} = \mathbf{-4.0}$.</li>
    <li>Transformed Wavelet vector: $\mathbf{W = [8.0, -4.0, -1.414, -1.414]}$. Energy is perfectly conserved: $\|W\|^2 = 64 + 16 + 2 + 2 = 84 = \|x\|^2 = 1 + 9 + 25 + 49 = 84$!</li>
  </ul>
</div>
"""

REVISION_LOCKED = REVISION_FINAL_ONE_PAGE + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 44: Complete Hierarchical Linkage Metrics</div>
  <ul>
    <li><strong>Single Link (Nearest Neighbor):</strong> $d(A, B) = \min_{x \in A, y \in B} d(x, y)$</li>
    <li><strong>Complete Link (Farthest Neighbor):</strong> $d(A, B) = \max_{x \in A, y \in B} d(x, y)$</li>
    <li><strong>Average Link (Group Average):</strong> $d(A, B) = \frac{1}{|A||B|} \sum_{x \in A} \sum_{y \in B} d(x, y)$</li>
    <li><strong>Centroid Link:</strong> $d(A, B) = \|\mathbf{\mu}_A - \mathbf{\mu}_B\|_2$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 45: Complete Master Review Strategy</div>
  <p>Master the 4 Core Pillars: 1. Proximity & Five-number summary, 2. Star/Snowflake & OLAP lattices, 3. Apriori/FP-Tree association rules, 4. Decision trees & DBSCAN density clustering!</p>
</div>
"""

def lock_pass():
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP + M2_PERFECT + M2_ADD + M2_FINAL_PUSH + M2_FINAL_BOOST3 + M2_FINAL_BOOST4 + M2_TINY_BOOST + M2_FINAL_ONE_PAGE + M2_LOCKED

    html_m2 = wrap_html("Module 2: Data Preprocessing & Dimensionality Reduction", "Topics 15 to 20 • Missing Imputation, Binning, Chi-Square Independence, Normalization & PCA", m2, module_num=2)
    with open(os.path.join(HTML_DIR, "Module_2_Data_Preprocessing_Notes.html"), "w", encoding="utf-8") as f:
        f.write(html_m2)
    generate_pdf(os.path.join(HTML_DIR, "Module_2_Data_Preprocessing_Notes.html"), os.path.join(PDF_DIR, "Module_2_Data_Preprocessing_Notes.pdf"), "DMCT Module 2")

    # Revision
    rev_html = wrap_html(
        "Data Mining (CS24303) 10-Page Master Revision",
        "High-Yield Formulas, Schemas, Cuboid Lattices, Apriori Rules & Solved Numerical Cards",
        REVISION_LOCKED
    )
    rev_html_file = os.path.join(HTML_DIR, "DM_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "DM_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "DM 10-Page Master Revision")

    modules = [
        "Module_1_Data_Understanding_Notes",
        "Module_2_Data_Preprocessing_Notes",
        "Module_3_Data_Warehousing_OLAP_Notes",
        "Module_4_Association_Rules_Notes",
        "Module_5_Classification_Clustering_Notes",
    ]

    master_doc = fitz.open()
    for fname in modules:
        mod_pdf = fitz.open(os.path.join(PDF_DIR, f"{fname}.pdf"))
        master_doc.insert_pdf(mod_pdf)
    
    lab_doc = fitz.open(os.path.join(PDF_DIR, "DM_Lab_Practical_Guide.pdf"))
    master_doc.insert_pdf(lab_doc)

    rev_doc = fitz.open(rev_pdf_file)
    master_doc.insert_pdf(rev_doc)

    master_pdf_path = os.path.join(PDF_DIR, "DM_Full_Course_Master.pdf")
    master_doc.save(master_pdf_path)
    print(f"✅ Generated {master_pdf_path} ({len(master_doc)} pages)")

if __name__ == "__main__":
    lock_pass()
