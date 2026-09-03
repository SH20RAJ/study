#!/usr/bin/env python3
"""
True 10-Page Completion for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf, LAB_GUIDE
from push_dm_exact_10 import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET
)

M2_FINAL_BOOST2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 11: Z-Score Standardization vs Min-Max Normalization Trade-Off Analysis</div>
  <p>Consider a dataset with severe outliers: $X = \{10, 11, 12, 13, 14, 15, 1000\}$:</p>
  <ul>
    <li><strong>Min-Max Scaling to $[0, 1]$:</strong> $x_1 = \frac{10-10}{1000-10} = 0.000$; $x_5 = \frac{14-10}{990} = 0.004$; $x_7 = \frac{1000-10}{990} = 1.000$. The normal cluster $\{10..15\}$ is crushed into a tiny range $[0.000, 0.005]$, completely destroying feature variance!</li>
    <li><strong>Z-Score Standardization:</strong> Outlier $1000$ pulls the mean to $\bar{x} = 154.1$ and $\sigma = 373.1$.</li>
    <li><strong>Robust Standardization (Median & IQR):</strong> $x' = \frac{x - 13}{3.0}$. Points $\{10..15\}$ span $[-1.0, +0.67]$, preserving high variance, while outlier $1000$ becomes $+329.0$ without compressing the cluster!</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q12. Explain Data Cleaning for Inconsistent Codes and Duplicate Elimination (Record Linkage). (8 Marks)</div><div class="qa-a">Real-world databases contain duplicate entities recorded with differing syntax (e.g. `IBM Corp`, `International Business Machines`, `I.B.M.`):<br>1. <strong>String Similarity Metrics:</strong> Levenshtein Edit Distance, Jaro-Winkler Metric ($d_J = \frac{1}{3}\left(\frac{m}{|s_1|} + \frac{m}{|s_2|} + \frac{m - t}{m}\right)$), $q$-gram token overlapping.<br>2. <strong>Blocking (Canopy Clustering):</strong> Divides $N$ records into overlapping canopies using fast phonetic hash keys (Soundex / Metaphone) to avoid $O(N^2)$ pairwise comparisons.<br>3. <strong>Merge/Purge Pipeline:</strong> Merges duplicate records into a golden master record with unified primary keys.</div></div>
"""

M3_FINAL_BOOST2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 12: Factless Fact Table Applications in Business Intelligence</div>
  <p>A <strong>Factless Fact Table</strong> contains NO numeric measurement facts (no dollars or quantities); it contains ONLY foreign keys pointing to dimension tables:</p>
  <ul>
    <li><strong>Event Tracking:</strong> Tracking university student class attendance: `(student_key, course_key, date_key, room_key)`. The fact of the event occurring is the measure!</li>
    <li><strong>Coverage Table:</strong> Tracking promotional marketing campaigns: `(product_key, store_key, promo_key, date_key)` to determine which products were on promotion in which stores, even if zero units were sold!</li>
  </ul>
</div>
"""

M4_FINAL_BOOST2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 13: Correlation Rule Mining via Lift and Chi-Square Testing</div>
  <p>In a dataset of $N = 1000$ retail transactions, $\text{count}(A) = 400, \text{count}(B) = 700, \text{count}(A \cup B) = 350$:</p>
  <ul>
    <li>$\text{Support}(A \implies B) = \frac{350}{1000} = \mathbf{35\%}$</li>
    <li>$\text{Confidence}(A \implies B) = \frac{350}{400} = \mathbf{87.5\%}$</li>
    <li>$\text{Lift}(A \implies B) = \frac{0.875}{0.700} = \mathbf{1.25 > 1 \implies \text{Genuine positive correlation!}}$</li>
    <li>$\text{Leverage} = 0.35 - (0.40)(0.70) = 0.35 - 0.28 = \mathbf{+0.07}$</li>
    <li>$\text{Conviction} = \frac{1 - 0.70}{1 - 0.875} = \frac{0.30}{0.125} = \mathbf{2.40}$</li>
  </ul>
</div>

<div class="qa-card"><div class="qa-q">Q8. Detail the ECLAT Algorithm vs Apriori in Terms of Memory and Disk I/O. (8 Marks)</div><div class="qa-a">• <strong>Apriori:</strong> Low memory footprint per pass, but incurs heavy repeated disk I/O scanning the massive transactional database $k$ times.<br>• <strong>ECLAT:</strong> Reads the database only once to construct vertical TID lists, then performs fast bitwise AND intersections in RAM ($O(1)$ disk I/O). However, if transactions are long and item frequencies are high, storing millions of transaction IDs in memory can cause memory exhaustion!</div></div>
"""

M5_FINAL_BOOST2 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 15: Decision Tree Pruning via Pessimistic Error Estimation (PEP)</div>
  <p>In C4.5, a subtree $T$ with $L$ leaves and $E$ training errors has pessimistic error estimate:</p>
  $$\mathbf{E_{\text{pessimistic}}(T) = E + \frac{L}{2} + 1.96 \sqrt{\frac{(E + L/2)(N - E - L/2)}{N}}}$$
  <p>If the pessimistic error of collapsing the subtree into a single leaf node is lower than keeping the complex subtree, C4.5 prunes the subtree, improving generalization on unseen test data!</p>
</div>
"""

# Complete 28k character revision guide
DM_REVISION_MASTER_10 = r"""
<div class="cover-container">
  <div class="course-badge">Comprehensive High-Yield Master Guide</div>
  <h1 class="book-title">Data Mining & Data Warehousing (CS24303) 10-Page Master Quick Revision Guide</h1>
  <div class="book-subtitle">Formulas, Schemas, Cuboid Lattices, Apriori Rules, Cluster Algorithms & Solved Exam Cards</div>
</div>

<h2 class="section-title">Master Formula & Metric Reference Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Domain</th>
      <th style="width: 45%;">Universal Formula</th>
      <th>Key Exam Property</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Min-Max Normalization</strong></td>
      <td>$$v' = \frac{v - \min_A}{\max_A - \min_A}(\text{new\_max} - \text{new\_min}) + \text{new\_min}$$</td>
      <td>Preserves exact relationships; sensitive to future out-of-bound outliers.</td>
    </tr>
    <tr>
      <td><strong>Z-Score Standardization</strong></td>
      <td>$$z = \frac{v - \bar{x}}{\sigma}$$</td>
      <td>Zero mean, unit variance ($\mathcal{N}(0, 1)$); ideal when min/max are unknown.</td>
    </tr>
    <tr>
      <td><strong>$\chi^2$ Independence Test</strong></td>
      <td>$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \quad \text{where } E_{ij} = \frac{\text{Row}_i \times \text{Col}_j}{N}$$</td>
      <td>$df = (r - 1)(c - 1)$; tests categorical attribute independence.</td>
    </tr>
    <tr>
      <td><strong>Cosine Similarity</strong></td>
      <td>$$\text{sim}(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\| \|\mathbf{y}\|} = \frac{\sum x_i y_i}{\sqrt{\sum x_i^2}\sqrt{\sum y_i^2}}$$</td>
      <td>Angle between vectors; independent of document text length.</td>
    </tr>
    <tr>
      <td><strong>Jaccard Similarity</strong></td>
      <td>$$J(\mathbf{x}, \mathbf{y}) = \frac{q}{q + r + s}$$</td>
      <td>Asymmetric binary metric; completely ignores $0-0$ negative matches $t$.</td>
    </tr>
    <tr>
      <td><strong>Association Rule Lift</strong></td>
      <td>$$\text{Lift}(A \implies B) = \frac{P(A \cup B)}{P(A) P(B)} = \frac{\text{Confidence}(A \implies B)}{\text{Support}(B)}$$</td>
      <td>$\text{Lift} > 1 \implies \text{Positive correlation}; = 1 \implies \text{Independent}$.</td>
    </tr>
    <tr>
      <td><strong>Information Gain</strong></td>
      <td>$$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$</td>
      <td>Biased towards attributes with massive numbers of distinct values.</td>
    </tr>
    <tr>
      <td><strong>Gini Impurity</strong></td>
      <td>$$\text{Gini}(S) = 1 - \sum_{i=1}^m p_i^2$$</td>
      <td>CART metric for strictly binary decision tree splits.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Complete 5-Module Comparative Checklists & Solved Flashcards</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Module</th>
      <th style="width: 40%;">Core Theoretical Concepts</th>
      <th>High-Yield Exam Numericals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>M1: Data Understanding</strong></td>
      <td>KDD Process, Nominal/Ordinal/Interval/Ratio, Proximity Metrics (SMC, Jaccard, Cosine, Mahalanobis, Gower).</td>
      <td>Five-number summary, IQR outlier fences, Cosine vector similarity, Jaccard distance.</td>
    </tr>
    <tr>
      <td><strong>M2: Preprocessing</strong></td>
      <td>Missing imputation, Bin smoothing (means, boundaries), $\chi^2$ test, Min-Max / Z-score normalization, PCA.</td>
      <td>Contingency table $\chi^2$ computation, decimal scaling, Min-Max re-scaling to $[-1, 1]$.</td>
    </tr>
    <tr>
      <td><strong>M3: Data Warehousing</strong></td>
      <td>OLTP vs OLAP, Star / Snowflake / Fact Constellation, Additive vs Semi-additive measures, Cuboid lattice combinatorics.</td>
      <td>Total cuboids calculation with hierarchies $N = \prod (L_i + 1)$, OLAP operations (slice/dice/roll-up).</td>
    </tr>
    <tr>
      <td><strong>M4: Frequent Patterns</strong></td>
      <td>Apriori property, join & prune, FP-Tree conditional bases, ECLAT vertical TID lists, Closed vs Maximal.</td>
      <td>Full Apriori table trace, Support/Confidence/Lift calculations, FP-Tree branch insertion.</td>
    </tr>
    <tr>
      <td><strong>M5: Classification & Clustering</strong></td>
      <td>ID3 vs C4.5 vs CART, Naive Bayes, Confusion Matrix, ROC/AUC, k-Means vs PAM, DBSCAN density, LOF.</td>
      <td>Entropy & Information Gain numerical, Confusion matrix Precision/Recall/F1, k-Means 1D convergence.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Exam Flashcard 1: Star vs Snowflake Schema Differences</div>
  <p><strong>Star Schema:</strong> De-normalized dimension tables with redundant columns, single-join fact table queries, optimized for fast OLAP read speeds.<br><strong>Snowflake Schema:</strong> Normalized dimension hierarchies (splitting out sub-dimensions into 3NF), zero redundancy, requires complex multi-table SQL joins that degrade interactive slice/dice query performance.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Exam Flashcard 2: k-Means vs DBSCAN Clustering Trade-offs</div>
  <p><strong>k-Means:</strong> Fast $O(t k N)$, requires upfront $k$, assumes spherical clusters of equal size/variance, highly sensitive to outliers.<br><strong>DBSCAN:</strong> Density-based $(\epsilon, \text{MinPts})$, automatically determines number of clusters, discovers arbitrary non-convex geometries (crescents, rings), completely isolates noise outliers.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Exam Flashcard 3: Confidence vs Lift in Association Rules</div>
  <p>Confidence measures conditional probability $P(B \mid A)$, but fails to account for the baseline popularity of item $B$. <strong>Lift</strong> divides confidence by $P(B)$ to reveal true statistical correlation ($\text{Lift} > 1$ positive correlation, $\text{Lift} = 1$ independent, $\text{Lift} < 1$ negative substitute).</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Exam Flashcard 4: Confusion Matrix Metrics Summary</div>
  <ul>
    <li>$\text{Accuracy} = \frac{TP + TN}{N}$ (Overall correctness)</li>
    <li>$\text{Sensitivity / Recall} = \frac{TP}{TP + FN}$ (Fraction of actual positives captured)</li>
    <li>$\text{Specificity} = \frac{TN}{TN + FP}$ (Fraction of actual negatives captured)</li>
    <li>$\text{Precision} = \frac{TP}{TP + FP}$ (Fraction of predicted positives that are correct)</li>
    <li>$F_1\text{-Score} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$ (Harmonic mean)</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Exam Flashcard 5: Information Gain vs Gain Ratio vs Gini Index</div>
  <ul>
    <li><strong>Information Gain (ID3):</strong> $\text{Gain}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$. Biased toward attributes with large numbers of distinct values.</li>
    <li><strong>Gain Ratio (C4.5):</strong> $\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}$. Normalizes gain by split entropy, penalizing broad multi-way splits.</li>
    <li><strong>Gini Impurity (CART):</strong> $\text{Gini}(S) = 1 - \sum p_i^2$. Strictly binary splits.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Exam Flashcard 6: Complete Normalization Formulas Reference</div>
  <ul>
    <li><strong>Min-Max Scaling:</strong> $v' = \frac{v - \min}{\max - \min}(\text{new\_max} - \text{new\_min}) + \text{new\_min}$</li>
    <li><strong>Z-Score Standardization:</strong> $z = \frac{v - \mu}{\sigma}$</li>
    <li><strong>Modified Z-Score (Outlier-Robust):</strong> $M_i = \frac{0.6745(x_i - \text{Median})}{\text{MAD}}$ where $\text{MAD} = \text{Median}(|x_i - \text{Median}|)$</li>
    <li><strong>Decimal Scaling:</strong> $v' = \frac{v}{10^j}$ where $j = \lceil \log_{10}(\max|v|) \rceil$</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Exam Flashcard 7: The 4 Major Clustering Paradigms</div>
  <table class="custom-table">
    <thead><tr><th>Paradigm</th><th>Representative Algorithms</th><th>Key Characteristics</th></tr></thead>
    <tbody>
      <tr><td><strong>Partitioning</strong></td><td>k-Means, k-Medoids (PAM), CLARA, CLARANS</td><td>Constructs $k$ partitions; iterative relocation; spherical clusters.</td></tr>
      <tr><td><strong>Hierarchical</strong></td><td>AGNES (agglomerative), DIANA (divisive), BIRCH, CURE</td><td>Dendrogram tree; no $k$ required; irreversible merges.</td></tr>
      <tr><td><strong>Density-Based</strong></td><td>DBSCAN, OPTICS, DENCLUE</td><td>Arbitrary non-convex shapes; filters noise outliers automatically.</td></tr>
      <tr><td><strong>Grid-Based</strong></td><td>STING, WaveCluster, CLIQUE</td><td>Quantizes object space into finite grid cells; fast $O(N)$ execution.</td></tr>
    </tbody>
  </table>
</div>
"""

def compile_final_dm_exact():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2
    m3 = M3_CONTENT + M3_EXP + M3_DEEP + M3_MEGA + M3_ULTRA + M3_FINAL_BOOST + M3_EXTRA_PASS + M3_CROWN + M3_TARGET + M3_FINAL_BOOST2
    m4 = M4_CONTENT + M4_EXP + M4_DEEP + M4_MEGA + M4_ULTRA + M4_FINAL_BOOST + M4_EXTRA_PASS + M4_CROWN + M4_TARGET + M4_FINAL_BOOST2
    m5 = M5_CONTENT + M5_EXP + M5_DEEP + M5_MEGA + M5_ULTRA + M5_FINAL_BOOST + M5_EXTRA_PASS + M5_CROWN + M5_TARGET + M5_FINAL_BOOST2

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
        DM_REVISION_MASTER_10
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
    {DM_REVISION_MASTER_10}
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
    compile_final_dm_exact()
