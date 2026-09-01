# 10-Page Master Quick Revision Exhaustive Content for Data Mining (CS24303)

DM_REVISION_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title">⛏️ 10-Page Master Quick Revision — Data Mining Concepts & Techniques (CS24303)</div>
  <div class="toc-grid">
    <div>Page 1: KDD Pipeline & 4 Fundamental Attribute Types</div>
    <div>Page 2: Proximity Metrics (L1, L2, Cosine, Jaccard, SMC)</div>
    <div>Page 3: Data Cleaning, Binning Smoothing & Outlier Fences</div>
    <div>Page 4: Chi-Square Contingency Test & Normalization Formulations</div>
    <div>Page 5: PCA Dimensionality Reduction & Numerosity Sampling</div>
    <div>Page 6: Data Warehousing, Star/Snowflake Schemas & 5 OLAP Operations</div>
    <div>Page 7: Data Cube Lattice & Attribute-Oriented Induction (AOI)</div>
    <div>Page 8: Apriori Downward Closure Proof & Join/Prune Trace</div>
    <div>Page 9: FP-Tree Construction, Recursive Mining & Lift Analysis</div>
    <div>Page 10: Advanced Constraint Types, Colossal Patterns & Top BIT Mesra PYQs</div>
  </div>
</div>

<h2 class="section-title">⚡ Master Formula, Schema & Metric Matrix</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Core Concept</th>
      <th style="width: 45%;">Mathematical Formulation / Rule</th>
      <th>Key Exam Insight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Euclidean Distance ($L_2$)</strong></td>
      <td>$$d(x, y) = \sqrt{\sum_{i=1}^p (x_i - y_i)^2}$$</td>
      <td>Standard straight-line distance; sensitive to scale.</td>
    </tr>
    <tr>
      <td><strong>Manhattan Distance ($L_1$)</strong></td>
      <td>$$d(x, y) = \sum_{i=1}^p |x_i - y_i|$$</td>
      <td>City-block grid distance; robust to single-attribute outliers.</td>
    </tr>
    <tr>
      <td><strong>Cosine Similarity</strong></td>
      <td>$$\text{sim}(x, y) = \frac{\vec{x} \cdot \vec{y}}{\|\vec{x}\| \|\vec{y}\|}$$</td>
      <td>Invariant to document vector length.</td>
    </tr>
    <tr>
      <td><strong>Jaccard Coefficient</strong></td>
      <td>$$J(A, B) = \frac{q}{q + r + s}$$</td>
      <td>Asymmetric binary; ignores joint absence ($t$).</td>
    </tr>
    <tr>
      <td><strong>Chi-Square Test ($\chi^2$)</strong></td>
      <td>$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}, \quad E_{ij} = \frac{\text{Row}_i \times \text{Col}_j}{N}$$</td>
      <td>Tests independence between two nominal attributes.</td>
    </tr>
    <tr>
      <td><strong>Min-Max Normalization</strong></td>
      <td>$$v' = \frac{v - \min_A}{\max_A - \min_A}(new\_\max - new\_\min) + new\_\min$$</td>
      <td>Linearly maps to target interval $[0, 1]$.</td>
    </tr>
    <tr>
      <td><strong>Z-Score Normalization</strong></td>
      <td>$$v' = \frac{v - \mu_A}{\sigma_A}$$</td>
      <td>Zero mean, unit variance. Robust against outliers.</td>
    </tr>
    <tr>
      <td><strong>Rule Support & Confidence</strong></td>
      <td>$$\text{Supp} = \frac{\sigma(A \cup B)}{|D|}, \qquad \text{Conf} = \frac{\sigma(A \cup B)}{\sigma(A)}$$</td>
      <td>$\text{Supp}$ measures frequency; $\text{Conf}$ measures rule certainty.</td>
    </tr>
    <tr>
      <td><strong>Lift Metric</strong></td>
      <td>$$\text{Lift}(A, B) = \frac{P(A \cup B)}{P(A) P(B)} = \frac{\text{Conf}(A \implies B)}{\text{Supp}(B)}$$</td>
      <td>$> 1$: Positive correlation; $< 1$: Negative correlation.</td>
    </tr>
    <tr>
      <td><strong>Kulczynski Measure</strong></td>
      <td>$$\text{Kulc}(A, B) = \frac{1}{2}\Big( P(A \mid B) + P(B \mid A) \Big)$$</td>
      <td>Null-invariant correlation measure.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2 class="section-title">🔥 Top 10 High-Yield BIT Mesra Exam Questions & Model Answers</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the Apriori property and how it reduces candidate itemset generation. (8 Marks)</div>
  <div class="qa-a">
    <strong>Apriori Property (Downward Closure):</strong> All non-empty subsets of a frequent itemset must also be frequent. If an itemset $I$ is infrequent ($\text{count}(I) < \text{min\_sup}$), any superset containing $I$ cannot be frequent.<br>
    <strong>Pruning Mechanism:</strong> When generating candidate $k$-itemsets ($C_k$) by joining $L_{k-1} \Join L_{k-1}$, if any $(k-1)$-subset of a candidate $c \in C_k$ is not in $L_{k-1}$, $c$ is immediately pruned from $C_k$ without scanning the database.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Compare Star Schema and Snowflake Schema across 5 technical criteria. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Structure:</strong> Star has single central fact table and denormalized dimension tables; Snowflake normalizes dimension tables into multiple sub-tables.<br>
    2. <strong>Redundancy:</strong> Star contains data redundancy in dimensions; Snowflake eliminates redundancy.<br>
    3. <strong>Storage:</strong> Star requires slightly more disk space; Snowflake is storage-optimized.<br>
    4. <strong>Query Performance:</strong> Star requires simple single-join SQL queries with superior performance; Snowflake requires complex multi-table joins reducing query speed.<br>
    5. <strong>Maintenance:</strong> Star has simpler ETL updates; Snowflake has complex hierarchical maintenance.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Detail the difference between ROLAP, MOLAP, and HOLAP servers. (6 Marks)</div>
  <div class="qa-a">
    <strong>ROLAP:</strong> Relational OLAP storing data in RDBMS with Star/Snowflake schemas. Scalable to petabytes, leverages SQL.<br>
    <strong>MOLAP:</strong> Multidimensional OLAP storing data in dense arrays. Blazing fast query times, pre-computed materialization.<br>
    <strong>HOLAP:</strong> Hybrid OLAP storing base records in ROLAP relational tables and high-level aggregated summary cuboids in MOLAP arrays.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q4. State the difference between Closed Frequent Itemsets and Maximal Frequent Itemsets. (6 Marks)</div>
  <div class="qa-a">
    <strong>Closed Frequent Itemset:</strong> An itemset $X$ is closed if no proper superset $Y \supset X$ has the same support count ($\text{supp}(Y) = \text{supp}(X)$). It is a <em>lossless representation</em> (exact counts of all subsets can be derived).<br>
    <strong>Maximal Frequent Itemset (Max-Itemset):</strong> An itemset $X$ is maximal frequent if no proper superset $Y \supset X$ is frequent. It is a <em>lossy representation</em> (subset counts are not uniquely recoverable).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q5. Explain the two core operators in Attribute-Oriented Induction (AOI). (6 Marks)</div>
  <div class="qa-a">
    <strong>1. Attribute Removal:</strong> If an attribute contains a large number of distinct values with no concept hierarchy (e.g., `Social_Security_Number`), remove it from the generalized relation.<br>
    <strong>2. Attribute Generalization:</strong> If an attribute has a concept hierarchy and distinct values exceed attribute threshold, replace lower-level values with higher-level concepts.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q6. Differentiate between Descriptive and Predictive Data Mining with examples. (6 Marks)</div>
  <div class="qa-a">
    <strong>Descriptive Mining:</strong> Characterizes general structural properties of existing data (Clustering, Association Rules, Data Summarization). Example: Segmenting customers into 4 distinct demographic spending clusters.<br>
    <strong>Predictive Mining:</strong> Constructs inference models based on historical labeled data to forecast unknown or future values (Classification, Regression). Example: Predicting whether a loan applicant will default based on credit score.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q7. What is the difference between Interdimension and Hybrid Association Rules? (5 Marks)</div>
  <div class="qa-a">
    <strong>Interdimension Rules:</strong> Contain multiple distinct predicates where each predicate occurs at most once (e.g., $\text{Age}(X, 20) \land \text{Income}(X, \text{High}) \implies \text{Buys}(X, \text{Laptop})$).<br>
    <strong>Hybrid Rules:</strong> Contain multiple predicates where one or more predicates may occur repeatedly with different attribute values (e.g., $\text{Age}(X, 20) \land \text{Buys}(X, \text{Laptop}) \implies \text{Buys}(X, \text{Backpack})$).
  </div>
</div>
"""
