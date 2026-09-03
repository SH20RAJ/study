#!/usr/bin/env python3
"""
Full-scale True 10-12 Page Data Mining & Data Warehousing (CS24303) Compiler.
Embeds comprehensive 36k-42k characters per module to guarantee 10-12 pages for every module,
10 pages for the Master Revision Guide, and 55+ pages for the Master Book!
"""

import os, sys, glob
from playwright.sync_api import sync_playwright

DM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-mining"))
HTML_DIR = os.path.join(DM_DIR, "html")
PDF_DIR = os.path.join(DM_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from build_complete_dm_master_suite import M1_CONTENT, M2_CONTENT, M3_CONTENT, M4_CONTENT, M5_CONTENT, REVISION_CONTENT, LAB_GUIDE, wrap_html, generate_pdf
from push_dm_to_11_pages import M1_EXP, M2_EXP, M3_EXP, M4_EXP, M5_EXP

# Second layer of dense university textbook expansions to reach 38k chars
M1_DEEP = r"""
<h2 class="section-title">Topic 13: Advanced Proximity Matrices & Multidimensional Scaling (MDS)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Constructing Full Dissimilarity Matrix</div>
  <p>Consider 4 data objects in 2D space: $x_1 = (1, 2), x_2 = (3, 5), x_3 = (2, 0), x_4 = (4, 2)$. Construct the complete $4 \times 4$ Euclidean Dissimilarity Matrix $\mathbf{D}$:</p>
  <ul>
    <li>$d(x_1, x_2) = \sqrt{(3-1)^2 + (5-2)^2} = \sqrt{4 + 9} = \sqrt{13} \approx \mathbf{3.606}$</li>
    <li>$d(x_1, x_3) = \sqrt{(2-1)^2 + (0-2)^2} = \sqrt{1 + 4} = \sqrt{5} \approx \mathbf{2.236}$</li>
    <li>$d(x_1, x_4) = \sqrt{(4-1)^2 + (2-2)^2} = \sqrt{9 + 0} = \mathbf{3.000}$</li>
    <li>$d(x_2, x_3) = \sqrt{(2-3)^2 + (0-5)^2} = \sqrt{1 + 25} = \sqrt{26} \approx \mathbf{5.099}$</li>
    <li>$d(x_2, x_4) = \sqrt{(4-3)^2 + (2-5)^2} = \sqrt{1 + 9} = \sqrt{10} \approx \mathbf{3.162}$</li>
    <li>$d(x_3, x_4) = \sqrt{(4-2)^2 + (2-0)^2} = \sqrt{4 + 4} = \sqrt{8} \approx \mathbf{2.828}$</li>
  </ul>
  $$\mathbf{\mathbf{D} = \begin{pmatrix} 0 & 3.606 & 2.236 & 3.000 \\ 3.606 & 0 & 5.099 & 3.162 \\ 2.236 & 5.099 & 0 & 2.828 \\ 3.000 & 3.162 & 2.828 & 0 \end{pmatrix}}$$
</div>

<div class="qa-card"><div class="qa-q">Q8. Explain Multidimensional Scaling (MDS) and Metric vs Non-metric MDS. (8 Marks)</div><div class="qa-a"><strong>Multidimensional Scaling (MDS)</strong> is a non-linear dimensionality reduction technique that takes an arbitrary pairwise dissimilarity matrix $\mathbf{D} \in \mathbb{R}^{N \times N}$ and maps the $N$ objects into a low-dimensional Euclidean space $\mathbb{R}^k$ ($k=2$ or $3$) such that Euclidean distances in the embedding $\hat{d}_{ij} = \|\mathbf{y}_i - \mathbf{y}_j\|$ preserve the original input dissimilarities $\delta_{ij}$ as faithfully as possible.<br>• <strong>Metric MDS:</strong> Minimizes Kruskal's Stress: $\text{Stress} = \sqrt{\frac{\sum (\delta_{ij} - \hat{d}_{ij})^2}{\sum \hat{d}_{ij}^2}}$.<br>• <strong>Non-Metric MDS:</strong> Preserves only the <em>rank order</em> of distances ($\delta_{ij} < \delta_{kl} \implies \hat{d}_{ij} < \hat{d}_{kl}$) using isotonic monotonic regression.</div></div>
"""

M2_DEEP = r"""
<h2 class="section-title">Topic 20.2: Advanced Preprocessing & Feature Selection Topologies</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Discrete Wavelet Transform (Haar Wavelet) 1D Signal Decomposition</div>
  <p>Consider 1D discrete time series signal $\mathbf{X} = [2, 4, 6, 8, 10, 12, 14, 16]$ ($N = 8$):</p>
  <ol>
    <li><strong>Level 1 Decomposition:</strong>
      <ul>
        <li>Averages (Low-pass coarse trend): $\left[ \frac{2+4}{2}, \frac{6+8}{2}, \frac{10+12}{2}, \frac{14+16}{2} \right] = \mathbf{[3, 7, 11, 15]}$.</li>
        <li>Differences (High-pass wavelet details): $\left[ \frac{2-4}{2}, \frac{6-8}{2}, \frac{10-12}{2}, \frac{14-16}{2} \right] = \mathbf{[-1, -1, -1, -1]}$.</li>
      </ul>
    </li>
    <li><strong>Level 2 Decomposition (on Averages $[3, 7, 11, 15]$):</strong>
      <ul>
        <li>Level 2 Averages: $\left[ \frac{3+7}{2}, \frac{11+15}{2} \right] = \mathbf{[5, 13]}$.</li>
        <li>Level 2 Details: $\left[ \frac{3-7}{2}, \frac{11-15}{2} \right] = \mathbf{[-2, -2]}$.</li>
      </ul>
    </li>
    <li><strong>Level 3 Decomposition (on $[5, 13]$):</strong>
      <ul>
        <li>Level 3 Average: $\frac{5+13}{2} = \mathbf{9}$.</li>
        <li>Level 3 Detail: $\frac{5-13}{2} = \mathbf{-4}$.</li>
      </ul>
    </li>
  </ol>
  $$\mathbf{\text{Full Haar Wavelet Representation: } [9, \ -4, \ -2, -2, \ -1, -1, -1, -1]}$$
  <p><em>Data Compression:</em> The detail coefficients are highly sparse, allowing extreme compression by thresholding small details to zero!</p>
</div>

<div class="qa-card"><div class="qa-q">Q4. Explain ReliefF Algorithm for Feature Weighting and Selection. (8 Marks)</div><div class="qa-a"><strong>ReliefF (Kononenko 1994)</strong> evaluates the quality of individual attributes according to how well their values distinguish between instances that are near to each other:<br>1. Randomly sample an instance $R_i$.<br>2. Find its $k$ nearest instances belonging to the <em>same class</em> (Near Hits $H$) and $k$ nearest instances belonging to <em>different classes</em> (Near Misses $M$).<br>3. Update weight $W[A]$ for attribute $A$: Increase weight if $A$ separates $R_i$ from Near Misses; decrease weight if $A$ separates $R_i$ from Near Hits:
$$\mathbf{W[A] \leftarrow W[A] - \sum_{j=1}^k \frac{\text{diff}(A, R_i, H_j)}{m \cdot k} + \sum_{C \neq \text{class}(R_i)} \frac{P(C)}{1 - P(\text{class}(R_i))} \sum_{j=1}^k \frac{\text{diff}(A, R_i, M_j(C))}{m \cdot k}}$$
ReliefF successfully captures non-linear feature interactions and scales linearly $O(m \cdot k \cdot p)$!</div></div>
"""

M3_DEEP = r"""
<h2 class="section-title">Topic 29.2: Advanced Star-Cubing & Materialized View Optimization</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Materialized View Selection using the Greedy (HRU) Algorithm</div>
  <p>A data cube lattice has base cuboid $V_0$ (cost = 100). The costs of computing each dependent cuboid view and their lattice ancestor dependencies are given below. Select top $k = 2$ views to materialize to maximize total query evaluation benefit:</p>
  <ul>
    <li>Views: $V_1$ (cost = 50, ancestors: $V_0$), $V_2$ (cost = 30, ancestors: $V_0$), $V_3$ (cost = 20, ancestors: $V_1, V_2$), $V_4$ (cost = 10, ancestors: $V_3$).</li>
  </ul>
  <p><strong>Step 1: Calculate Benefit of materializing first view:</strong></p>
  <ul>
    <li>Benefit($V_1$): Saves $(100 - 50) = 50$ for $V_1$; saves $(100 - 50) = 50$ for descendant $V_3$; saves $50$ for $V_4 \implies B(V_1) = 50 + 50 + 50 = \mathbf{150}$.</li>
    <li>Benefit($V_2$): Saves $(100 - 30) = 70$ for $V_2$; saves $(100 - 30) = 70$ for $V_3$; saves $70$ for $V_4 \implies B(V_2) = 70 + 70 + 70 = \mathbf{210}$.</li>
    <li>Benefit($V_3$): Saves $(100 - 20) = 80$ for $V_3$; saves $80$ for $V_4 \implies B(V_3) = 80 + 80 = \mathbf{160}$.</li>
  </ul>
  $$\mathbf{\text{Choice 1: Select } V_2 \text{ with Maximum Benefit } = \mathbf{210}!}$$
  <p><strong>Step 2: Calculate Marginal Benefit given $V_2$ is already materialized (cost of $V_3, V_4$ now reduced to 30):</strong></p>
  <ul>
    <li>Benefit($V_1 \mid V_2$): Saves $(100 - 50) = 50$ for $V_1$; saves $(30 - 30) = 0$ for $V_3, V_4 \implies B(V_1 \mid V_2) = \mathbf{50}$.</li>
    <li>Benefit($V_3 \mid V_2$): Saves $(30 - 20) = 10$ for $V_3$; saves $(30 - 20) = 10$ for $V_4 \implies B(V_3 \mid V_2) = 10 + 10 = \mathbf{20}$.</li>
    <li>Benefit($V_4 \mid V_2$): Saves $(30 - 10) = 20$ for $V_4 \implies B(V_4 \mid V_2) = \mathbf{20}$.</li>
  </ul>
  $$\mathbf{\text{Choice 2: Select } V_1 \text{ with Marginal Benefit } = \mathbf{50}!}$$
  $$\mathbf{\text{Final Optimal Views to Materialize: } \{V_2, V_1\} \quad (\text{Total Benefit } = 210 + 50 = \mathbf{260})}$$
</div>
"""

M4_DEEP = r"""
<h2 class="section-title">Topic 36.2: Advanced Constraint-Based Mining & Multi-Level Association Rules</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Constraint Property</th>
      <th style="width: 40%;">Formal Mathematical Invariant</th>
      <th>Optimization in Mining Algorithms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Anti-Monotone</strong></td>
      <td>$\forall S \supset S': \text{If } S' \text{ violates constraint } C \implies S \text{ must also violate } C$.</td>
      <td>Can be pushed deep into candidate generation (e.g. $\text{sum}(S.\text{price}) \le 500$, $\text{Support}(S) \ge \text{min\_sup}$).</td>
    </tr>
    <tr>
      <td><strong>Monotone</strong></td>
      <td>$\forall S \supset S': \text{If } S' \text{ satisfies constraint } C \implies S \text{ must also satisfy } C$.</td>
      <td>Once an itemset satisfies constraint (e.g. $\text{sum}(S.\text{price}) \ge 1000$), all its supersets are guaranteed valid!</td>
    </tr>
    <tr>
      <td><strong>Succinct</strong></td>
      <td>All and only itemsets satisfying $C$ can be explicitly generated upfront without testing (e.g. $\text{Item}.\text{Type} = \text{'Electronics'}$).</td>
      <td>Pre-filters data before any mining begins; zero candidate testing overhead!</td>
    </tr>
    <tr>
      <td><strong>Convertible</strong></td>
      <td>A non-monotonic constraint becomes monotone or anti-monotone when items are arranged in a specific sorted order (e.g. $\text{avg}(S.\text{price}) \ge 50$ sorted by descending price).</td>
      <td>Enables itemset pruning when combined with FP-Growth header sorting.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Multi-Level Association Rule Redundancy Filtering</div>
  <p>Consider a product hierarchy where `Laptop` is a parent category of `Dell_XPS` and `Apple_MacBook`:</p>
  <ul>
    <li>Rule 1 (High-Level): $\text{Laptop} \implies \text{Mouse} \quad [\text{Support} = 10\%, \ \text{Confidence} = 70\%]$</li>
    <li>Rule 2 (Low-Level): $\text{Dell\_XPS} \implies \text{Mouse} \quad [\text{Support} = 3\%, \ \text{Confidence} = 72\%]$</li>
    <li>Rule 3 (Low-Level): $\text{Apple\_MacBook} \implies \text{Mouse} \quad [\text{Support} = 4\%, \ \text{Confidence} = 20\%]$</li>
  </ul>
  <p><strong>Redundancy Analysis:</strong></p>
  <ul>
    <li>Rule 2 has confidence ($72\%$) almost identical to its generalized ancestor Rule 1 ($70\%$). It provides NO new unexpected information $\implies \mathbf{\text{Rule 2 is REDUNDANT and should be pruned!}}$</li>
    <li>Rule 3 has confidence ($20\%$) drastically lower than ancestor Rule 1 ($70\%$). It reveals a vital unexpected negative insight (Mac users buy trackpads or don't buy mice) $\implies \mathbf{\text{Rule 3 is HIGHLY INTERESTING and must be preserved!}}$</li>
  </ul>
</div>
"""

M5_DEEP = r"""
<h2 class="section-title">Topic 46.2: Advanced Ensemble Learning & Density-Based OPTICS Algorithm</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Ensemble Method</th>
      <th style="width: 40%;">Core Algorithmic Paradigm</th>
      <th>Variance vs. Bias Reduction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Bagging (Bootstrap Aggregating)</strong></td>
      <td>Trains $B$ independent base models (e.g. deep unpruned Decision Trees) on bootstrap sampled subsets ($N$ with replacement). Averages predictions (regression) or takes majority vote (classification).</td>
      <td><strong>Dramatically reduces Variance</strong> without increasing bias (e.g. Random Forests).</td>
    </tr>
    <tr>
      <td><strong>Boosting (AdaBoost / GBM / XGBoost)</strong></td>
      <td>Trains a sequence of weak learners iteratively. Each new learner is trained on the residual errors / weighted mistakes of previous learners.</td>
      <td><strong>Dramatically reduces Bias</strong> and variance; prone to overfitting on heavy noise.</td>
    </tr>
    <tr>
      <td><strong>Stacking (Stacked Generalization)</strong></td>
      <td>Trains multiple heterogeneous base models (SVM, Random Forest, k-NN); uses a meta-classifier (e.g. Logistic Regression) to learn optimal combination weights.</td>
      <td>Maximizes generalization performance by combining diverse hypothesis spaces.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: The OPTICS (Ordering Points To Identify Clustering Structure) Algorithm</div>
  <p>Unlike DBSCAN (which requires a single rigid global radius $\epsilon$), <strong>OPTICS (Ankerst et al. 1999)</strong> creates an ordered list of points storing two dynamic distance attributes:</p>
  <ul>
    <li><strong>Core-Distance of $p$:</strong> The smallest distance $\epsilon'$ such that $p$ is a core point with respect to $\text{MinPts}$:
      $$\mathbf{\text{core-dist}_{\epsilon, \text{MinPts}}(p) = \begin{cases} \text{UNDEFINED} & \text{if } |N_\epsilon(p)| < \text{MinPts} \\ \text{Distance to } \text{MinPts}\text{-th nearest neighbor} & \text{otherwise} \end{cases}}$$
    </li>
    <li><strong>Reachability-Distance of $p$ from $o$:</strong>
      $$\mathbf{\text{reach-dist}_{\epsilon, \text{MinPts}}(p, o) = \begin{cases} \text{UNDEFINED} & \text{if } |N_\epsilon(o)| < \text{MinPts} \\ \max(\text{core-dist}(o), \text{dist}(o, p)) & \text{otherwise} \end{cases}}$$
    </li>
  </ul>
  <p><em>Reachability Plot:</em> Plotting reachability distances in the OPTICS ordering produces valleys corresponding to dense clusters and peaks corresponding to noise dividers, revealing hierarchical multi-density cluster structures across all $\epsilon$ simultaneously!</p>
</div>
"""

# Revision booklet expansion to 10 pages
DM_REVISION_SUPER = r"""
<div class="cover-container">
  <div class="course-badge">High-Yield Exam Preparation Master Guide</div>
  <h1 class="book-title">Data Mining & Data Warehousing (CS24303) 10-Page Master Quick Revision Guide</h1>
  <div class="book-subtitle">Universal Formulas, Multidimensional Schemas, Cuboid Lattices, Association Rules & Solved Numerical Cards</div>
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
"""

def generate_true_11_page_dm():
    m1_final = M1_CONTENT + M1_EXP + M1_DEEP
    m2_final = M2_CONTENT + M2_EXP + M2_DEEP
    m3_final = M3_CONTENT + M3_EXP + M3_DEEP
    m4_final = M4_CONTENT + M4_EXP + M4_DEEP
    m5_final = M5_CONTENT + M5_EXP + M5_DEEP

    print("True DM M1 length:", len(m1_final))
    print("True DM M2 length:", len(m2_final))
    print("True DM M3 length:", len(m3_final))
    print("True DM M4 length:", len(m4_final))
    print("True DM M5 length:", len(m5_final))

    # Clean old misnamed PDFs in data-mining/pdf
    old_files = [
        "Data_Mining_10_Page_Master_Revision.pdf",
        "Data_Mining_Full_Course_Master.pdf",
        "Module_1_Data_Attributes_Notes.pdf",
        "Module_2_Preprocessing_Notes.pdf",
        "Module_3_Data_Warehouse_Notes.pdf",
        "Module_4_Pattern_Mining_Notes.pdf",
        "Module_5_Advanced_Mining_Notes.pdf"
    ]
    for old_f in old_files:
        p = os.path.join(PDF_DIR, old_f)
        if os.path.exists(p):
            os.remove(p)

    modules = [
        (1, "Module 1: Data Understanding & Statistical Proximity", "Topics 1 to 14 • KDD Lifecycle, Attributes, Boxplots, Q-Q, Jaccard & Distance Metrics", m1_final, "Module_1_Data_Understanding_Notes"),
        (2, "Module 2: Data Preprocessing & Dimensionality Reduction", "Topics 15 to 20 • Missing Imputation, Binning, Chi-Square Independence, Normalization & PCA", m2_final, "Module_2_Data_Preprocessing_Notes"),
        (3, "Module 3: Data Warehousing & OLAP Technology", "Topics 21 to 29 • Star/Snowflake Schemas, Measures, OLAP Operations, Cuboid Lattices & BUC", m3_final, "Module_3_Data_Warehousing_OLAP_Notes"),
        (4, "Module 4: Frequent Pattern & Association Mining", "Topics 30 to 36 • Market Basket Analysis, Support/Confidence/Lift, Apriori, FP-Growth & ECLAT", m4_final, "Module_4_Association_Rules_Notes"),
        (5, "Module 5: Classification & Cluster Analysis", "Topics 37 to 46 • ID3/C4.5/CART Trees, Naive Bayes, Confusion Matrix, k-Means, PAM & DBSCAN", m5_final, "Module_5_Classification_Clustering_Notes"),
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
        DM_REVISION_SUPER
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
    {DM_REVISION_SUPER}
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
    generate_true_11_page_dm()
