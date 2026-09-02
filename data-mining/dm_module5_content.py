# Data Mining Module 5 Exhaustive Content (10 Topics Complete + PYQ-Critical Classification & Clustering)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DM_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Advanced Pattern Mining, Classification & Clustering — Complete Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 37:</strong> Pattern Mining Road Map (Itemsets to Multidimensional)</div>
    <div><strong>Topic 38:</strong> Multilevel Pattern Mining (Concept Hierarchy Abstractions)</div>
    <div><strong>Topic 39:</strong> Multidimensional Pattern Mining (Multiple Predicates)</div>
    <div><strong>Topic 40:</strong> Constraint-Based Pattern Mining (Pushing Constraints)</div>
    <div><strong>Topic 41:</strong> Mining High-Dimensional Data & Colossal Patterns</div>
    <div><strong>Topic 42:</strong> Mining Compressed Patterns (Closed vs. Maximal Itemsets)</div>
    <div><strong>Topic 43:</strong> Mining Approximate Patterns & Error Tolerances</div>
    <div><strong>Topic 44 & 45:</strong> Pattern Exploration & Real-World Domain Applications</div>
    <div><strong>PYQ Block A:</strong> Classification (Decision Trees, Naïve Bayes, Backprop & Metrics)</div>
    <div><strong>PYQ Block B:</strong> Clustering (K-Means, PAM Medoids, DBSCAN & BIRCH CF-Trees)</div>
  </div>
</div>

<h2 class="section-title">Topic 37 – 40: Advanced Pattern Mining Methodologies</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Advanced Mining Paradigm</th>
      <th style="width: 45%;">Algorithmic Mechanism & Description</th>
      <th>Key Benefit / Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Multilevel Association</strong></td>
      <td>Mines rules across different concept hierarchy levels (e.g., `Milk => Bread` vs. `Dairy => Baked Goods`).</td>
      <td>Uncovers granular patterns at lower levels and generalized trends at higher levels.</td>
    </tr>
    <tr>
      <td><strong>2. Multidimensional Association</strong></td>
      <td>Involves multiple predicates or dimensions (e.g., `age(X, "20..29") ^ income(X, "50K..60K") => buys(X, "Laptop")`).</td>
      <td>Discovers rich customer demographic profiles beyond simple single-item co-occurrences.</td>
    </tr>
    <tr>
      <td><strong>3. Constraint-Based Mining</strong></td>
      <td>Pushes user-defined constraints (Antimonotonic, Monotonic, Succinct) directly into the mining algorithm.</td>
      <td>Massively prunes the candidate search space; produces only actionable, relevant rules.</td>
    </tr>
    <tr>
      <td><strong>4. Closed vs. Maximal Patterns</strong></td>
      <td>• <strong>Closed Itemset:</strong> An itemset $X$ is closed if no proper superset has the same support.<br>• <strong>Maximal Itemset:</strong> An itemset $X$ is maximal if no proper superset is frequent.</td>
      <td>Compresses millions of frequent itemsets into compact loss-less or lossy representations.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">⭐ PYQ-CRITICAL BLOCK A: Classification Algorithms [UPLOADED PYQ]</h2>

<h3 class="subsection-title">1. Naïve Bayesian Classification [UPLOADED PYQ — IT426 End]:</h3>
<div class="formula-card">
  $$P(C_i \mid \mathbf{X}) = \frac{P(\mathbf{X} \mid C_i) P(C_i)}{P(\mathbf{X})} = \frac{P(C_i) \prod_{k=1}^n P(x_k \mid C_i)}{P(\mathbf{X})}$$
  <strong>Class-Conditional Independence Assumption:</strong> Assumes that the effect of an attribute value on a given class is completely independent of the values of other attributes.
</div>

<h3 class="subsection-title">2. Backpropagation Neural Network Learning [UPLOADED PYQ — IT335 End]:</h3>
<div class="formula-card">
  $$w_{ij} \leftarrow w_{ij} + \Delta w_{ij} = w_{ij} + (l) \text{Err}_j O_i$$
  - For output layer neuron $k$: $\text{Err}_k = O_k (1 - O_k)(T_k - O_k)$
  - For hidden layer neuron $j$: $\text{Err}_j = O_j (1 - O_j) \sum_k \text{Err}_k w_{jk}$
</div>

<h3 class="subsection-title">3. Classification Evaluation Metrics [UPLOADED PYQ]:</h3>
<table class="custom-table">
  <thead>
    <tr><th>Metric</th><th>Formula</th><th>Practical Interpretation</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Accuracy</strong></td><td>$\frac{TP + TN}{TP + TN + FP + FN}$</td><td>Overall proportion of correct predictions.</td></tr>
    <tr><td><strong>Precision</strong></td><td>$\frac{TP}{TP + FP}$</td><td>Out of all predicted positives, how many are truly positive?</td></tr>
    <tr><td><strong>Recall (Sensitivity)</strong></td><td>$\frac{TP}{TP + FN}$</td><td>Out of all actual positive cases, how many were discovered?</td></tr>
    <tr><td><strong>Error Rate</strong></td><td>$\frac{FP + FN}{TP + TN + FP + FN} = 1 - \text{Accuracy}$</td><td>Proportion of misclassified instances.</td></tr>
  </tbody>
</table>

<h2 class="section-title">⭐ PYQ-CRITICAL BLOCK B: Clustering Algorithms [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Algorithm [UPLOADED PYQ]</th>
      <th style="width: 25%;">Clustering Paradigm</th>
      <th style="width: 35%;">Algorithmic Principle</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. K-Means [UPLOADED PYQ]</strong></td>
      <td>Partitioning (Centroid-based)</td>
      <td>Iteratively assigns objects to nearest mean centroid $\mu_j$ and recalculates centroids to minimize $SSE = \sum \sum \|x - \mu_j\|^2$.</td>
      <td>Fast $O(t k n)$; sensitive to noise and outliers; requires $k$ upfront.</td>
    </tr>
    <tr>
      <td><strong>2. PAM (K-Medoids) [UPLOADED PYQ]</strong></td>
      <td>Partitioning (Medoid-based)</td>
      <td>Uses actual representative data points (medoids) instead of mean averages. Iteratively evaluates quality swaps.</td>
      <td>Highly robust to noise and outliers; computationally expensive $O(k(n-k)^2)$.</td>
    </tr>
    <tr>
      <td><strong>3. DBSCAN [UPLOADED PYQ]</strong></td>
      <td>Density-Based</td>
      <td>Grows clusters from high-density core points ($\ge \text{MinPts}$ within $\epsilon$-radius). Marks sparse points as noise.</td>
      <td>Discovers arbitrary-shaped clusters; immune to noise; doesn't require $k$ upfront.</td>
    </tr>
    <tr>
      <td><strong>4. BIRCH [UPLOADED PYQ]</strong></td>
      <td>Hierarchical (Feature Tree)</td>
      <td>Builds an in-memory <strong>CF-Tree (Clustering Feature Tree)</strong> where each node contains $CF = (N, \mathbf{LS}, SS)$.</td>
      <td>Linearly scalable $O(n)$ for massive datasets with single scan of disk.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M5 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ — IT335 End] Explain DBSCAN clustering algorithm with core points, border points, and noise points. (8 Marks)</div>
  <div class="qa-a">
    DBSCAN relies on two parameters: radius $\epsilon$ and density threshold $\text{MinPts}$:<br>
    1. <strong>Core Point:</strong> A point $p$ is a core point if $|N_\epsilon(p)| \ge \text{MinPts}$ (at least $\text{MinPts}$ points lie within distance $\epsilon$).<br>
    2. <strong>Border Point:</strong> A point $q$ is not a core point, but falls within the $\epsilon$-neighborhood of some core point $p$.<br>
    3. <strong>Noise Point:</strong> Any point that is neither a core point nor a border point.<br>
    <em>Clustering:</em> Connects all density-reachable core points into clusters and assigns border points to their adjacent core clusters.
  </div>
</div>
"""
