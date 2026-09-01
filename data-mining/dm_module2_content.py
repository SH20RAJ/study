# Module 2 Exhaustive Content (6 Topics | 11-13 Pages Target)

DM_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Data Preprocessing & Processing — 6 Topics Syllabus</div>
  <div class="toc-grid">
    <div>1. Data Cleaning (Missing Values, Noise Binning, Regression, Outliers)</div>
    <div>2. Data Integration (Entity Identification, Chi-Square, Pearson, Spearman, Covariance)</div>
    <div>3. Data Transformation (Min-Max, Z-Score, Decimal Scaling, Box-Cox, Log)</div>
    <div>4. Data Reduction (PCA Derivation, SVD, Wavelets, Numerosity, Sampling, Compression)</div>
    <div>5. Data Discretization (Binning, Histograms, Cluster, ChiMerge Step-by-Step)</div>
    <div>6. Concept Hierarchy Generation (Categorical & Numeric 3-4-5 Rule)</div>
  </div>
</div>

<h2 class="section-title">Topic 1: Data Cleaning (Noise, Missing Values & Outliers)</h2>
<p>
  Real-world industrial datasets are inherently "dirty" — incomplete (lacking attribute values or containing only aggregate data), noisy (containing errors, outliers, or transmission corruptions), and inconsistent (containing discrepancies in codes, names, or measurement units).
</p>
<p>
  Data cleaning routines attempt to fill in missing values, smooth out noise while identifying outliers, and correct inconsistencies.
</p>

<h3 class="subsection-title">1. Advanced Strategies for Handling Missing Attribute Values:</h3>
<ol>
  <li><strong>Ignore the Tuple:</strong> Typically done when the target class label is missing in supervised classification tasks. This method is inefficient when the percentage of missing values per attribute varies considerably across records.</li>
  <li><strong>Fill in the Missing Value Manually:</strong> High accuracy but extraordinarily time-consuming, expensive, and infeasible for large multi-gigabyte databases.</li>
  <li><strong>Use a Global Constant:</strong> Replace all missing attribute values with a fixed label such as `"Unknown"` or a sentinel value ($-\infty$). Simple, but may lead the mining algorithm to infer false correlations among tuples sharing the global constant.</li>
  <li><strong>Use Attribute Mean or Median:</strong>
    <ul>
      <li>Use the <strong>Arithmetic Mean</strong> for symmetric (Gaussian) continuous distributions.</li>
      <li>Use the <strong>Median</strong> for highly skewed distributions (e.g., household income or real estate prices).</li>
    </ul>
  </li>
  <li><strong>Use the Attribute Mean/Median for All Samples of the Same Class:</strong> If classifying credit risk, fill missing salary with the mean salary of customers sharing the same credit classification label.</li>
  <li><strong>Use the Most Probable Value (Statistical Imputation):</strong> Determine the missing value using linear regression, Bayesian networks, inference-based tools, or decision tree induction. Considered the most statistically rigorous approach.</li>
  <li><strong>K-Nearest Neighbor (KNN) Imputation:</strong> Identifies the $k$ most similar complete records based on distance metrics (e.g., Euclidean distance) and imputes the weighted average of the neighbors' values:
    $$\hat{x}_i = \frac{\sum_{j \in N_k(i)} \frac{1}{d(x_i, x_j)} x_j}{\sum_{j \in N_k(i)} \frac{1}{d(x_i, x_j)}}$$
  </li>
  <li><strong>Multiple Imputation by Chained Equations (MICE):</strong> A series of iterative regression models where each missing variable is modeled conditionally on other variables in the dataset over multiple imputation cycles.</li>
</ol>

<h3 class="subsection-title">2. Smoothing Noisy Data via Binning Techniques:</h3>
<p>
  Binning methods smooth sorted data values by consulting their neighborhood (local values around each point):
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem 1: Binning Smoothing Methods</div>
  <p><strong>Sorted Data for Price Attribute:</strong> $4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34$ ($n=12$).</p>
  <p><strong>Step 1: Partition into 3 Equal-Frequency (Equal-Depth) Bins (Depth = 4 items/bin):</strong></p>
  <ul>
    <li>$\text{Bin 1: } [4, 8, 9, 15]$</li>
    <li>$\text{Bin 2: } [21, 21, 24, 25]$</li>
    <li>$\text{Bin 3: } [26, 28, 29, 34]$</li>
  </ul>

  <p><strong>Step 2: Smoothing by Bin Means:</strong></p>
  <ul>
    <li>$\text{Mean}(\text{Bin 1}) = \frac{4 + 8 + 9 + 15}{4} = \frac{36}{4} = \mathbf{9} \implies \text{Bin 1: } [9, 9, 9, 9]$</li>
    <li>$\text{Mean}(\text{Bin 2}) = \frac{21 + 21 + 24 + 25}{4} = \frac{91}{4} = \mathbf{22.75} \implies \text{Bin 2: } [23, 23, 23, 23]$</li>
    <li>$\text{Mean}(\text{Bin 3}) = \frac{26 + 28 + 29 + 34}{4} = \frac{117}{4} = \mathbf{29.25} \implies \text{Bin 3: } [29, 29, 29, 29]$</li>
  </ul>

  <p><strong>Step 3: Smoothing by Bin Boundaries (Min and Max of Each Bin):</strong></p>
  <ul>
    <li>$\text{Bin 1 (Min = 4, Max = 15): } 8 \rightarrow 4, \ 9 \rightarrow 15 \implies [4, 4, 15, 15]$</li>
    <li>$\text{Bin 2 (Min = 21, Max = 25): } 24 \rightarrow 25 \implies [21, 21, 25, 25]$</li>
    <li>$\text{Bin 3 (Min = 26, Max = 34): } 28 \rightarrow 26, \ 29 \rightarrow 26 \implies [26, 26, 26, 34]$</li>
  </ul>
</div>

<h3 class="subsection-title">3. Regression & Outlier Clustering for Smoothing:</h3>
<ul>
  <li><strong>Linear Regression:</strong> Fits data to a straight line $y = wx + b$. Where slope $w = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$ and intercept $b = \bar{y} - w\bar{x}$. Values are replaced by their predicted regression coordinates.</li>
  <li><strong>Multiple Linear Regression:</strong> Fits multidimensional attributes to a hyper-plane $y = w_0 + w_1 x_1 + w_2 x_2 + \dots + w_n x_n$.</li>
  <li><strong>Cluster Analysis for Outlier Detection:</strong> Similar values are organized into clusters. Values falling outside major cluster boundaries (e.g. distance $> 3\sigma$ from centroid) are flagged as outliers.</li>
  <li><strong>Local Outlier Factor (LOF):</strong> Measures local density deviation of a given object with respect to its surrounding $k$-nearest neighbors. An object with density substantially lower than its neighbors is identified as a local outlier.</li>
</ul>

<div class="page-break"></div>

<h2 class="section-title">Topic 2: Data Integration & Redundancy Correlation Analysis</h2>

<p>
  <strong>Data Integration</strong> combines data from multiple heterogeneous sources into a coherent store. Key challenges include:
</p>
<ul>
  <li><strong>Entity Identification Problem:</strong> Matching real-world entities across databases (e.g., ensuring `customer_id` in DB1 matches `cust_number` in DB2 using schema metadata).</li>
  <li><strong>Redundancy & Correlation:</strong> An attribute may be redundant if it can be derived from another attribute. Redundancy leads to dimensional bloat, increased storage overhead, and algorithm bias.</li>
</ul>

<h3 class="subsection-title">1. Chi-Square ($\chi^2$) Correlation Test for Nominal Attributes:</h3>
$$\chi^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}}, \qquad \text{where } E_{ij} = \frac{\text{row\_total}_i \times \text{col\_total}_j}{N}$$

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem 2: Chi-Square ($\chi^2$) Contingency Table Test</div>
  <p><strong>Contingency Table (Gender vs. Fiction Book Preference):</strong></p>
  <table class="custom-table">
    <tr><th>Gender</th><th>Prefers Fiction</th><th>Prefers Non-Fiction</th><th>Row Total</th></tr>
    <tr><td><strong>Male</strong></td><td>250 (Observed $O_{11}$)</td><td>200 (Observed $O_{12}$)</td><td>450</td></tr>
    <tr><td><strong>Female</strong></td><td>50 (Observed $O_{21}$)</td><td>100 (Observed $O_{22}$)</td><td>150</td></tr>
    <tr><td><strong>Col Total</strong></td><td>300</td><td>300</td><td>$N = 600$</td></tr>
  </table>
  <p><strong>Step 1: Compute Expected Frequencies ($E_{ij}$):</strong></p>
  <ul>
    <li>$E_{11} = \frac{450 \times 300}{600} = \mathbf{225}, \quad E_{12} = \frac{450 \times 300}{600} = \mathbf{225}$</li>
    <li>$E_{21} = \frac{150 \times 300}{600} = \mathbf{75}, \quad E_{22} = \frac{150 \times 300}{600} = \mathbf{75}$</li>
  </ul>
  <p><strong>Step 2: Compute $\chi^2$ Statistic:</strong></p>
  $$\chi^2 = \frac{(250 - 225)^2}{225} + \frac{(200 - 225)^2}{225} + \frac{(50 - 75)^2}{75} + \frac{(100 - 75)^2}{75} = \frac{625}{225} + \frac{625}{225} + \frac{625}{75} + \frac{625}{75} = 2.78 + 2.78 + 8.33 + 8.33 = \mathbf{22.22}$$
  <p><strong>Step 3: Hypothesis Testing:</strong> Degrees of freedom $\nu = (r-1)(c-1) = (2-1)(2-1) = 1$. The critical value of $\chi^2$ at significance $\alpha = 0.001$ is $10.83$. Since $22.22 > 10.83$, the hypothesis of independence is strongly rejected $\implies$ <strong>Gender and Book Preference are statistically correlated!</strong></p>
</div>

<h3 class="subsection-title">2. Correlation Coefficient (Pearson's $r$) for Numeric Data:</h3>
$$r_{A, B} = \frac{\sum_{i=1}^n (a_i - \bar{A})(b_i - \bar{B})}{(n-1) s_A s_B} = \frac{\sum_{i=1}^n (a_i b_i) - n \bar{A}\bar{B}}{(n-1) s_A s_B}$$
<ul>
  <li>$r > 0$: $A$ and $B$ are <strong>positively correlated</strong> (values of $A$ increase as $B$ increases).</li>
  <li>$r = 0$: $A$ and $B$ are <strong>independent / uncorrelated</strong>.</li>
  <li>$r < 0$: $A$ and $B$ are <strong>negatively correlated</strong> (as $A$ increases, $B$ decreases).</li>
</ul>

<h3 class="subsection-title">3. Spearman's Rank Correlation Coefficient ($\rho$):</h3>
<p>Used for ordinal attributes or monotonic non-linear numeric data:</p>
$$\rho = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)}$$
<p>Where $d_i = \text{rank}(a_i) - \text{rank}(b_i)$ is the difference between ranks of tuple $i$.</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Spearman's Rank Correlation</div>
  <p><strong>Given Student Exam Ranks in Data Mining ($X$) and Machine Learning ($Y$):</strong></p>
  <table class="custom-table">
    <tr><th>Student</th><th>Rank X</th><th>Rank Y</th><th>$d_i = X - Y$</th><th>$d_i^2$</th></tr>
    <tr><td>S1</td><td>1</td><td>2</td><td>-1</td><td>1</td></tr>
    <tr><td>S2</td><td>2</td><td>1</td><td>1</td><td>1</td></tr>
    <tr><td>S3</td><td>3</td><td>4</td><td>-1</td><td>1</td></tr>
    <tr><td>S4</td><td>4</td><td>3</td><td>1</td><td>1</td></tr>
    <tr><td>S5</td><td>5</td><td>5</td><td>0</td><td>0</td></tr>
    <tr><td><strong>Total</strong></td><td>-</td><td>-</td><td>-</td><td>$\sum d_i^2 = \mathbf{4}$</td></tr>
  </table>
  <p><strong>Calculation ($n=5$):</strong></p>
  $$\rho = 1 - \frac{6 \times 4}{5(25 - 1)} = 1 - \frac{24}{120} = 1 - 0.20 = \mathbf{0.80}$$
  <p>Strong positive rank correlation ($\rho = 0.80$) between Data Mining and Machine Learning performance!</p>
</div>

<h3 class="subsection-title">4. Covariance Between Numeric Attributes:</h3>
$$\text{Cov}(A, B) = E[(A - \bar{A})(B - \bar{B})] = \frac{\sum_{i=1}^n (a_i - \bar{A})(b_i - \bar{B})}{n-1}$$
<p>Note: $r_{A, B} = \frac{\text{Cov}(A, B)}{s_A s_B}$. If $\text{Cov}(A, B) > 0$, both attributes vary in the same direction.</p>

<div class="page-break"></div>

<h2 class="section-title">Topic 3: Data Transformation (Normalization Formulations)</h2>

<p>Data transformation converts the data into forms appropriate for mining, preventing attributes with initially large ranges (e.g., `Salary` in thousands) from dominating attributes with smaller ranges (e.g., `Age` in tens).</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Method</th>
      <th style="width: 45%;">Mathematical Formulation</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Min-Max Normalization</strong></td>
      <td>$$v' = \frac{v - \min_A}{\max_A - \min_A} (new\_\max_A - new\_\min_A) + new\_\min_A$$</td>
      <td>Preserves exact linear relationships among data values; maps values to $[0, 1]$; encounters "out-of-bounds" error on future data exceeding range.</td>
    </tr>
    <tr>
      <td><strong>2. Z-Score Normalization (Zero-Mean)</strong></td>
      <td>$$v' = \frac{v - \mu_A}{\sigma_A}$$</td>
      <td>Transforms data to have mean $\mu = 0$ and standard deviation $\sigma = 1$; extraordinarily robust when min and max are unknown or extreme outliers exist.</td>
    </tr>
    <tr>
      <td><strong>3. Decimal Scaling</strong></td>
      <td>$$v' = \frac{v}{10^j} \quad \text{where } j \text{ is smallest integer such that } \max(|v'|) < 1$$</td>
      <td>Fast bit-shift operation; normalizes by moving decimal point.</td>
    </tr>
    <tr>
      <td><strong>4. Box-Cox Power Transform</strong></td>
      <td>$$y^{(\lambda)} = \begin{cases} \frac{x^\lambda - 1}{\lambda} & \text{if } \lambda \ne 0 \\ \ln(x) & \text{if } \lambda = 0 \end{cases}$$</td>
      <td>Parametric power transformation used to stabilize variance and normalize non-Gaussian positive distributions.</td>
    </tr>
    <tr>
      <td><strong>5. Log Transformation</strong></td>
      <td>$$v' = \log_{10}(v) \quad \text{or} \quad \ln(v + 1)$$</td>
      <td>Compresses large values and stretches small values; ideal for right-skewed revenue/income curves.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem 3: Normalization Calculations</div>
  <p><strong>Given:</strong> Attribute `Income` with $\min = \$12,000, \max = \$98,000, \mu = \$54,000, \sigma = \$16,000$. Transform value $v = \$73,600$.</p>
  <ol>
    <li><strong>Min-Max Normalization to Range $[0.0, 1.0]$:</strong>
      $$v' = \frac{73,600 - 12,000}{98,000 - 12,000} (1.0 - 0.0) + 0.0 = \frac{61,600}{86,000} = \mathbf{0.716}$$
    </li>
    <li><strong>Z-Score Normalization:</strong>
      $$v' = \frac{73,600 - 54,000}{16,000} = \frac{19,600}{16,000} = \mathbf{1.225}$$
    </li>
    <li><strong>Normalization by Decimal Scaling ($\max = 98,000 \implies j = 5$ since $98,000 / 10^5 = 0.98 < 1$):</strong>
      $$v' = \frac{73,600}{10^5} = \mathbf{0.736}$$
    </li>
  </ol>
</div>

<div class="page-break"></div>

<h2 class="section-title">Topic 4: Data Reduction (PCA Mathematical Derivation & Numerosity)</h2>

<p>Complex data analysis and mining on massive datasets may take an impractical amount of time. <strong>Data Reduction</strong> techniques obtain a reduced representation of the dataset that is much smaller in volume yet closely maintains the integrity of the original data.</p>

<h3 class="subsection-title">1. Complete Step-by-Step Mathematical Derivation of PCA:</h3>

<div class="worked-box">
  <div class="worked-title">🏛️ Worked Problem 4: Complete PCA Step-by-Step Matrix Derivation</div>
  <p><strong>Given 4 2D Data Points:</strong> $x_1 = (2, 4), x_2 = (4, 6), x_3 = (6, 8), x_4 = (8, 10)$ ($n=4, d=2$).</p>
  <ol>
    <li><strong>Step 1: Compute Attribute Means:</strong>
      $$\mu_1 = \frac{2 + 4 + 6 + 8}{4} = \mathbf{5.0}, \qquad \mu_2 = \frac{4 + 6 + 8 + 10}{4} = \mathbf{7.0}$$
    </li>
    <li><strong>Step 2: Construct Zero-Mean Centered Matrix ($X$):</strong>
      $$X = \begin{bmatrix} 2 - 5 & 4 - 7 \\ 4 - 5 & 6 - 7 \\ 6 - 5 & 8 - 7 \\ 8 - 5 & 10 - 7 \end{bmatrix} = \begin{bmatrix} -3 & -3 \\ -1 & -1 \\ 1 & 1 \\ 3 & 3 \end{bmatrix}$$
    </li>
    <li><strong>Step 3: Calculate Covariance Matrix ($C = \frac{1}{n-1} X^T X$):</strong>
      $$C = \frac{1}{3} \begin{bmatrix} -3 & -1 & 1 & 3 \\ -3 & -1 & 1 & 3 \end{bmatrix} \begin{bmatrix} -3 & -3 \\ -1 & -1 \\ 1 & 1 \\ 3 & 3 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 20 & 20 \\ 20 & 20 \end{bmatrix} = \begin{bmatrix} 6.67 & 6.67 \\ 6.67 & 6.67 \end{bmatrix}$$
    </li>
    <li><strong>Step 4: Solve for Eigenvalues ($\det(C - \lambda I) = 0$):</strong>
      $$\det \begin{bmatrix} 6.67 - \lambda & 6.67 \\ 6.67 & 6.67 - \lambda \end{bmatrix} = (6.67 - \lambda)^2 - (6.67)^2 = \lambda^2 - 13.33\lambda = 0$$
      $$\lambda(\lambda - 13.33) = 0 \implies \mathbf{\lambda_1 = 13.33}, \quad \mathbf{\lambda_2 = 0.0}$$
    </li>
    <li><strong>Step 5: Compute Eigenvector for Principal Component $\lambda_1 = 13.33$:</strong>
      $$\begin{bmatrix} 6.67 - 13.33 & 6.67 \\ 6.67 & 6.67 - 13.33 \end{bmatrix} \begin{bmatrix} e_{11} \\ e_{12} \end{bmatrix} = \begin{bmatrix} -6.67 & 6.67 \\ 6.67 & -6.67 \end{bmatrix} \begin{bmatrix} e_{11} \\ e_{12} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies e_{11} = e_{12}$$
      Normalized unit eigenvector: $e_1 = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} \approx \begin{bmatrix} 0.707 \\ 0.707 \end{bmatrix}$.
    </li>
    <li><strong>Step 6: Proportion of Total Variance Explained:</strong>
      $$\frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{13.33}{13.33 + 0.0} = \mathbf{100\%}$$
      The dataset can be compressed from 2 dimensions down to 1 dimension with <strong>zero information loss!</strong>
    </li>
  </ol>
</div>

<h3 class="subsection-title">2. Discrete Wavelet Transforms (DWT) & Haar Decomposition:</h3>
<p>
  DWT transforms a numeric vector $X$ of length $N=2^m$ into wavelet coefficients via hierarchical subband decomposition.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Haar Wavelet Decomposition</div>
  <p><strong>Given 8-Element Signal:</strong> $S = [2, 2, 4, 4, 6, 6, 8, 8]$.</p>
  <ol>
    <li><strong>Level 1 Averages (Approximation):</strong> $\left[\frac{2+2}{2}, \frac{4+4}{2}, \frac{6+6}{2}, \frac{8+8}{2}\right] = [2, 4, 6, 8]$.<br>
        <strong>Level 1 Differences (Detail):</strong> $\left[\frac{2-2}{2}, \frac{4-4}{2}, \frac{6-6}{2}, \frac{8-8}{2}\right] = [0, 0, 0, 0]$.</li>
    <li><strong>Level 2 Averages:</strong> $\left[\frac{2+4}{2}, \frac{6+8}{2}\right] = [3, 7]$.<br>
        <strong>Level 2 Differences:</strong> $\left[\frac{2-4}{2}, \frac{6-8}{2}\right] = [-1, -1]$.</li>
    <li><strong>Level 3 Average (Overall Mean):</strong> $\frac{3+7}{2} = \mathbf{5}$.<br>
        <strong>Level 3 Difference:</strong> $\frac{3-7}{2} = \mathbf{-2}$.</li>
    <li><strong>Full Haar Wavelet Transformed Vector:</strong> $[\mathbf{5}, \mathbf{-2}, \mathbf{-1}, \mathbf{-1}, \mathbf{0}, \mathbf{0}, \mathbf{0}, \mathbf{0}]$.
        Zero detail coefficients can be truncated with zero reconstruction loss!</li>
  </ol>
</div>

<div class="page-break"></div>

<h2 class="section-title">Topics 5 – 6: Data Discretization & Concept Hierarchy Generation</h2>

<p>
  <strong>Data Discretization</strong> reduces the number of values for a given continuous attribute by dividing the range of the attribute into distinct intervals.
</p>

<h3 class="subsection-title">The ChiMerge ($\chi\text{Merge}$) Algorithm:</h3>
<p>
  ChiMerge is a supervised, bottom-up discretization method based on the $\chi^2$ test.
</p>
<ol>
  <li>Sort continuous attribute values in ascending order. Each distinct value forms an initial interval.</li>
  <li>For each pair of adjacent intervals, compute the $\chi^2$ statistic based on class distribution.</li>
  <li>Find the pair of adjacent intervals with the smallest $\chi^2$ value (lowest difference in class labels).</li>
  <li>If the minimum $\chi^2 < \text{threshold}$, merge the two intervals.</li>
  <li>Repeat steps 2–4 until all adjacent intervals have $\chi^2 \ge \text{threshold}$ or number of intervals reaches maximum limit.</li>
</ol>

<h3 class="subsection-title">Concept Hierarchy Generation by the 3-4-5 Rule:</h3>
<p>
  The <strong>3-4-5 Rule</strong> segments numeric intervals naturally into human-friendly chunks:
</p>
<ul>
  <li>If an interval covers $3, 6, 7,$ or $9$ distinct units at the most significant digit, partition the range into <strong>3 equal-width intervals</strong> ($3$ for $3, 6, 9$; $3$ for $7$ as $2-3-2$).</li>
  <li>If an interval covers $2, 4,$ or $8$ distinct units, partition the range into <strong>4 equal-width intervals</strong>.</li>
  <li>If an interval covers $1, 5,$ or $10$ distinct units, partition the range into <strong>5 equal-width intervals</strong>.</li>
</ul>

<div class="page-break"></div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module II)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the step-by-step mathematical procedure of Principal Component Analysis (PCA) for data reduction. (10 Marks)</div>
  <div class="qa-a">
    <strong>Answer:</strong>
    1. <strong>Standardize Input Data:</strong> Given $n$ data vectors of dimension $d$, normalize each attribute to zero mean: $x_{ij} \leftarrow x_{ij} - \bar{x}_j$.<br>
    2. <strong>Calculate Covariance Matrix:</strong> Compute $d \times d$ covariance matrix $C = \frac{1}{n-1} X^T X$, where $C_{jk} = \text{cov}(X_j, X_k)$.<br>
    3. <strong>Compute Eigenvalues & Eigenvectors:</strong> Solve characteristic equation $\det(C - \lambda I) = 0$ to find $d$ eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d \ge 0$ and orthonormal eigenvectors $e_1, e_2, \dots, e_d$.<br>
    4. <strong>Select Top $k$ Components:</strong> Choose $k$ eigenvectors corresponding to largest eigenvalues such that cumulative variance explained $\frac{\sum_{i=1}^k \lambda_i}{\sum_{j=1}^d \lambda_j} \ge 0.95$.<br>
    5. <strong>Project Data:</strong> Transform original $n \times d$ matrix $X$ onto $k$-dimensional orthogonal subspace: $Y = X \cdot E_k$, reducing dimensionality from $d$ to $k$ while preserving maximum variance.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Differentiate between Stratified Sampling and Simple Random Sampling with respect to data reduction. (6 Marks)</div>
  <div class="qa-a">
    <strong>Answer:</strong> In Simple Random Sampling (SRS), every tuple in dataset $D$ has an equal probability of selection ($1/N$). If data contains rare skewed classes (e.g., credit card fraud occurring in $0.1\%$ of cases), SRS may completely omit all positive fraud instances in the sample.<br>
    In <strong>Stratified Sampling</strong>, the dataset is partitioned into mutually exclusive non-overlapping strata based on a key attribute (e.g., class label). Random samples are drawn independently from each stratum proportional to its representation, guaranteeing that rare classes are preserved in the reduced dataset.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. Why is data preprocessing considered the most time-consuming phase in the KDD pipeline? (6 Marks)</div>
  <div class="qa-a">
    <strong>Answer:</strong> Real-world operational data is collected from heterogeneous systems without unified validation. Studies show data preprocessing consumes 60–80% of total project time because it must resolve missing values, eliminate noise, reconcile disparate primary/foreign keys across schemas, convert incompatible data formats, remove redundant correlated attributes, and scale continuous numerical ranges without destroying underlying statistical relationships.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q4. Compare Min-Max Normalization and Z-Score Normalization. When should each be chosen? (6 Marks)</div>
  <div class="qa-a">
    <strong>Answer:</strong>
    1. <strong>Min-Max Normalization</strong> bounds data strictly into $[0, 1]$, preserving exact original relative distances. Choose Min-Max when algorithms require inputs in a bounded range (e.g., Neural Network sigmoid activations, Image pixel values).<br>
    2. <strong>Z-Score Normalization</strong> transforms data to $\mu=0, \sigma=1$ without upper/lower bounds. Choose Z-Score when the absolute minimum and maximum are unknown or when severe outliers exist, as Min-Max would compress all normal data into a microscopic interval.
  </div>
</div>
"""
