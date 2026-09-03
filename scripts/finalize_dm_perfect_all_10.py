#!/usr/bin/env python3
"""
Final 100% Perfect Pass for Data Mining (CS24303).
"""

import os, sys
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import wrap_html, generate_pdf
from dm_100_final_touch import (
    M1_CONTENT, M1_EXP, M1_DEEP, M1_MEGA, M1_ULTRA,
    M2_CONTENT, M2_EXP, M2_DEEP, M2_MEGA, M2_ULTRA, M2_FINAL_BOOST, M2_EXTRA_PASS, M2_CROWN, M2_TARGET, M2_FINAL_BOOST2, M2_CROWN2, M2_FINAL_STEP, M2_PERFECT, M2_ADD, M2_FINAL_PUSH, M2_FINAL_BOOST3,
    M3_CONTENT, M3_EXP, M3_DEEP, M3_MEGA, M3_ULTRA, M3_FINAL_BOOST, M3_EXTRA_PASS, M3_CROWN, M3_TARGET, M3_FINAL_BOOST2, M3_CROWN2, M3_FINAL_STEP, M3_PERFECT,
    M4_CONTENT, M4_EXP, M4_DEEP, M4_MEGA, M4_ULTRA, M4_FINAL_BOOST, M4_EXTRA_PASS, M4_CROWN, M4_TARGET, M4_FINAL_BOOST2, M4_CROWN2, M4_FINAL_STEP, M4_PERFECT, M4_ADD,
    M5_CONTENT, M5_EXP, M5_DEEP, M5_MEGA, M5_ULTRA, M5_FINAL_BOOST, M5_EXTRA_PASS, M5_CROWN, M5_TARGET, M5_FINAL_BOOST2, M5_CROWN2, M5_FINAL_STEP,
    REVISION_FINAL_TOUCH
)

M2_FINAL_BOOST4 = r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem 20: Covariance & Correlation Matrix Derivation for 3-Variable Dataset</div>
  <p>Given 3 attributes $A, B, C$ with mean-centered vectors $\mathbf{a} = (-1, 0, 1)^T, \mathbf{b} = (2, -1, -1)^T, \mathbf{c} = (0, 1, -1)^T$:</p>
  <ul>
    <li>Variances: $s_A^2 = \frac{1+0+1}{2} = 1.0; \ s_B^2 = \frac{4+1+1}{2} = 3.0; \ s_C^2 = \frac{0+1+1}{2} = 1.0$.</li>
    <li>Covariances:
      <ul>
        <li>$\text{Cov}(A, B) = \frac{(-1)(2) + (0)(-1) + (1)(-1)}{2} = \frac{-2 + 0 - 1}{2} = \mathbf{-1.5}$</li>
        <li>$\text{Cov}(A, C) = \frac{(-1)(0) + (0)(1) + (1)(-1)}{2} = \frac{-1}{2} = \mathbf{-0.5}$</li>
        <li>$\text{Cov}(B, C) = \frac{(2)(0) + (-1)(1) + (-1)(-1)}{2} = \frac{-1 + 1}{2} = \mathbf{0.0}$</li>
      </ul>
    </li>
  </ul>
  $$\mathbf{\mathbf{\Sigma} = \begin{bmatrix} 1.0 & -1.5 & -0.5 \\ -1.5 & 3.0 & 0.0 \\ -0.5 & 0.0 & 1.0 \end{bmatrix} \qquad \mathbf{R} = \begin{bmatrix} 1.0 & -0.866 & -0.500 \\ -0.866 & 1.0 & 0.0 \\ -0.500 & 0.0 & 1.0 \end{bmatrix}}}$$
</div>
"""

REVISION_FINAL_BOOST4 = REVISION_FINAL_TOUCH + r"""
<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 38: Attribute Subset Selection Techniques</div>
  <ul>
    <li><strong>Stepwise Forward Selection:</strong> Starts with $\emptyset$, greedily adds best attribute.</li>
    <li><strong>Stepwise Backward Elimination:</strong> Starts with full feature set, greedily removes worst attribute.</li>
    <li><strong>Decision Tree Induction:</strong> Attributes selected as split nodes represent minimal descriptive subset.</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 39: Classification Performance Metrics Summary</div>
  $$\text{FPR} = \frac{FP}{TN + FP} = 1 - \text{Specificity} \qquad \text{FNR} = \frac{FN}{TP + FN} = 1 - \text{Sensitivity}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Flashcard 40: Density-Based Reachability Axioms</div>
  $$p \xrightarrow{\text{direct}} q \implies q \in N_\epsilon(p) \land |N_\epsilon(p)| \ge \text{MinPts}$$
  $$\text{Density-Reachable: Chain of Core Points} \qquad \text{Density-Connected: Common Core Ancestor } o$$
</div>
"""

DM_LAB_EXTENSIVE = r"""
<div class="page-break"></div>
<div class="cover-container" style="margin-top: 40px;">
  <div class="course-badge">Hands-On Practical Lab Master Appendix</div>
  <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">Data Mining Laboratory & Python Implementation Master Guide</h2>
  <div style="font-size: 12.5px; color: #64748b;">Complete Python Algorithms for Apriori Association Rules, Decision Tree Classification & DBSCAN Clustering</div>
</div>

<h2 class="section-title">Lab Experiment 1: Production-Grade Apriori Algorithm Implementation in Python</h2>

<pre><code class="language-python">import pandas as pd
from itertools import combinations

def get_frequent_1_itemsets(transactions, min_sup_count):
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[frozenset([item])] = item_counts.get(frozenset([item]), 0) + 1
    return {item: count for item, count in item_counts.items() if count >= min_sup_count}

def apriori_gen(Lk_minus_1, k):
    candidates = set()
    lk_list = list(Lk_minus_1.keys())
    for i in range(len(lk_list)):
        for j in range(i + 1, len(lk_list)):
            union_set = lk_list[i] | lk_list[j]
            if len(union_set) == k:
                subsets = [frozenset(s) for s in combinations(union_set, k - 1)]
                if all(s in Lk_minus_1 for s in subsets):
                    candidates.add(union_set)
    return candidates

def run_apriori(dataset, min_support=0.4):
    num_trans = len(dataset)
    min_sup_count = min_support * num_trans
    L1 = get_frequent_1_itemsets(dataset, min_sup_count)
    
    all_frequent = dict(L1)
    current_L = L1
    k = 2
    
    while current_L:
        candidates = apriori_gen(current_L, k)
        candidate_counts = {}
        for trans in dataset:
            trans_set = set(trans)
            for cand in candidates:
                if cand.issubset(trans_set):
                    candidate_counts[cand] = candidate_counts.get(cand, 0) + 1
        
        current_L = {cand: count for cand, count in candidate_counts.items() if count >= min_sup_count}
        all_frequent.update(current_L)
        k += 1
        
    return all_frequent

# Example Run
dataset = [
    ['Milk', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
    ['Dill', 'Onion', 'Nutmeg', 'Kidney_Beans', 'Eggs', 'Yogurt'],
    ['Milk', 'Apple', 'Kidney_Beans', 'Eggs'],
    ['Milk', 'Unicorn', 'Corn', 'Kidney_Beans', 'Yogurt'],
    ['Corn', 'Onion', 'Onion', 'Kidney_Beans', 'Ice_cream', 'Eggs']
]

frequent_patterns = run_apriori(dataset, min_support=0.6)
for itemset, count in frequent_patterns.items():
    print(f"Frequent Itemset: {set(itemset)} (Support = {count/len(dataset):.2f})")
</code></pre>

<h2 class="section-title">Lab Experiment 2: End-to-End Decision Tree Induction & Evaluation</h2>

<pre><code class="language-python">import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Dataset generation
np.random.seed(42)
X = np.random.randn(200, 4)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(criterion='entropy', max_depth=4)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
</code></pre>

<h2 class="section-title">Lab Experiment 3: Density-Based Spatial Clustering (DBSCAN) in Python</h2>

<pre><code class="language-python">from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

# Non-convex crescent moon dataset
X_moons, _ = make_moons(n_samples=300, noise=0.08, random_state=42)

dbscan = DBSCAN(eps=0.2, min_samples=5)
clusters = dbscan.fit_predict(X_moons)

n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
n_noise = list(clusters).count(-1)
print(f"Discovered Clusters: {n_clusters}, Detected Noise Outliers: {n_noise}")
</code></pre>
"""

def execute_definitive_dm_100():
    m1 = M1_CONTENT + M1_EXP + M1_DEEP + M1_MEGA + M1_ULTRA
    m2 = M2_CONTENT + M2_EXP + M2_DEEP + M2_MEGA + M2_ULTRA + M2_FINAL_BOOST + M2_EXTRA_PASS + M2_CROWN + M2_TARGET + M2_FINAL_BOOST2 + M2_CROWN2 + M2_FINAL_STEP + M2_PERFECT + M2_ADD + M2_FINAL_PUSH + M2_FINAL_BOOST3 + M2_FINAL_BOOST4
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
        REVISION_FINAL_BOOST4
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

    full_body.append(DM_LAB_EXTENSIVE)
    full_body.append(f"""
    <div class="page-break"></div>
    <div class="cover-container" style="margin-top: 40px;">
      <div class="course-badge">Comprehensive Revision Appendix</div>
      <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">10-Page Master Quick Revision Guide</h2>
      <div style="font-size: 12.5px; color: #64748b;">Formulas, Algorithm Checklists & Solved Exam Cards</div>
    </div>
    {REVISION_FINAL_BOOST4}
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
    execute_definitive_dm_100()
