# Module 4 Exhaustive Content (7 Topics | 14-16 Pages Target)

DM_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Frequent Pattern Mining & Association Analysis — 7 Topics Syllabus</div>
  <div class="toc-grid">
    <div>1. Basic Concepts of Frequent Pattern Mining</div>
    <div>2. Association Rules (Support & Confidence)</div>
    <div>3. Correlation Analysis (Lift, Chi-Square, Kulczynski)</div>
    <div>4. Frequent Itemset Mining Methods Landscape (Apriori, FP-Growth, ECLAT)</div>
    <div>5. The Apriori Algorithm (Formal Proof, Join & Prune Steps)</div>
    <div>6. Pattern-Growth Approach (FP-Growth, FP-Tree, Conditional Bases)</div>
    <div>7. Interesting Pattern Evaluation Methods (Null-Invariance)</div>
  </div>
</div>

<h2 class="section-title">Topics 1 – 2: Market Basket Analysis & Association Rules</h2>
<p>
  <strong>Frequent Patterns</strong> are itemsets, subsequences, or substructures that appear frequently in a transactional dataset (with frequency not less than a user-specified threshold).
</p>
<p>
  <strong>Market Basket Analysis</strong> investigates customer buying habits by finding associations between the different items that customers place in their shopping baskets:
</p>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="180" height="50" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="110" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Shopping Basket A</text>
    <text x="110" y="52" font-family="Fira Code" font-size="9.5" fill="#2563eb" text-anchor="middle">{Bread, Milk, Butter}</text>

    <path d="M 210 40 L 250 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="260" y="10" width="220" height="60" rx="6" fill="#ccfbf1" stroke="#0f766e" stroke-width="2"/>
    <text x="370" y="34" font-family="Plus Jakarta Sans" font-size="11" font-weight="800" fill="#0f766e" text-anchor="middle">Association Engine</text>
    <text x="370" y="52" font-family="Plus Jakarta Sans" font-size="9.5" fill="#115e59" text-anchor="middle">Support \ge 30%, Conf \ge 70%</text>

    <path d="M 490 40 L 530 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="540" y="15" width="180" height="50" rx="6" fill="#faf5ff" stroke="#a855f7"/>
    <text x="630" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#581c87" text-anchor="middle">Discovered Rule</text>
    <text x="630" y="52" font-family="Fira Code" font-size="9.5" fill="#7e22ce" text-anchor="middle">Bread \implies Milk [40%, 80%]</text>
  </svg>
  <div class="diagram-caption">Figure 4.1: Market Basket Association Rule Extraction</div>
</div>

<h3 class="subsection-title">Mathematical Formulations:</h3>
<ul>
  <li><strong>Itemset:</strong> A set of items $X = \{i_1, i_2, \dots, i_k\}$. A $k$-itemset contains exactly $k$ items.</li>
  <li><strong>Support Count ($\sigma(X)$):</strong> The absolute number of transactions in database $D$ containing itemset $X$:
    $$\sigma(X) = |\{ T \in D \mid X \subseteq T \}|$$
  </li>
  <li><strong>Relative Support ($s$):</strong> Fraction of transactions containing $X$:
    $$\text{Support}(X) = \frac{\sigma(X)}{|D|}$$
  </li>
  <li><strong>Association Rule:</strong> An expression $A \implies B$ where $A \subset I, B \subset I$, and $A \cap B = \emptyset$.
    $$\text{Support}(A \implies B) = P(A \cup B) = \frac{\sigma(A \cup B)}{|D|}$$
    $$\text{Confidence}(A \implies B) = P(B \mid A) = \frac{\sigma(A \cup B)}{\sigma(A)} = \frac{\text{Support}(A \cup B)}{\text{Support}(A)}$$
  </li>
</ul>



<h2 class="section-title">Topic 5: The Apriori Algorithm (Level-Wise Search)</h2>

<div class="callout callout-info">
  <div class="callout-title">The Apriori Downward Closure Property (Apriori Property)</div>
  <strong>Theorem:</strong> All non-empty subsets of a frequent itemset must also be frequent.<br>
  <strong>Formal Proof:</strong> Let $I$ be an itemset and $I' \subseteq I$. Every transaction $T \in D$ that contains $I$ must inherently contain all of its subsets $I'$ (since $I \subseteq T \implies I' \subseteq T$). Therefore:
  $$\sigma(I') = |\{ T \in D \mid I' \subseteq T \}| \ge |\{ T \in D \mid I \subseteq T \}| = \sigma(I)$$
  If $I$ is frequent ($\sigma(I) \ge \text{min\_sup}$), then $\sigma(I') \ge \text{min\_sup}$, proving that $I'$ is also frequent.<br>
  <strong>Pruning Rule (Contrapositive):</strong> If any $(k-1)$-subset of a candidate $k$-itemset $C_k$ is infrequent ($< \text{min\_sup}$), then $C_k$ cannot be frequent and is immediately pruned before database scanning!
</div>

<h3 class="subsection-title">Two-Step Candidate Generation Mechanism:</h3>
<ol>
  <li><strong>Join Step ($L_{k-1} \Join L_{k-1} \rightarrow C_k$):</strong> Join two frequent $(k-1)$-itemsets $l_1, l_2 \in L_{k-1}$ if their first $k-2$ items are identical and the last item of $l_1$ is lexicographically smaller than $l_2$:
    $$(l_1[1] = l_2[1]) \land \dots \land (l_1[k-2] = l_2[k-2]) \land (l_1[k-1] < l_2[k-1])$$
  </li>
  <li><strong>Prune Step:</strong> For each candidate $c \in C_k$, check all $(k-1)$-subsets of $c$. If any subset $\notin L_{k-1}$, delete $c$ from $C_k$.</li>
</ol>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Complete Apriori Trace on 9 Transactions</div>
  <p><strong>Transaction Database ($D$):</strong></p>
  <table class="custom-table">
    <tr><th>TID</th><th>Items Purchased</th></tr>
    <tr><td>T100</td><td>I1, I2, I5</td></tr>
    <tr><td>T200</td><td>I2, I4</td></tr>
    <tr><td>T300</td><td>I2, I3</td></tr>
    <tr><td>T400</td><td>I1, I2, I4</td></tr>
    <tr><td>T500</td><td>I1, I3</td></tr>
    <tr><td>T600</td><td>I2, I3</td></tr>
    <tr><td>T700</td><td>I1, I3</td></tr>
    <tr><td>T800</td><td>I1, I2, I3, I5</td></tr>
    <tr><td>T900</td><td>I1, I2, I3</td></tr>
  </table>
  <p><strong>Parameter:</strong> $\text{min\_sup} = 2$ ($\approx 22.2\%$), $\text{min\_conf} = 70\%$.</p>
  <p><strong>Complete Iterative Trace:</strong></p>
  <ol>
    <li><strong>Pass 1:</strong>
      <ul>
        <li>$C_1 = \{ \{I1\}:6, \{I2\}:7, \{I3\}:6, \{I4\}:2, \{I5\}:2 \}$.</li>
        <li>All items have count $\ge 2 \implies L_1 = C_1$.</li>
      </ul>
    </li>
    <li><strong>Pass 2:</strong>
      <ul>
        <li>Join $L_1 \Join L_1 \rightarrow C_2 = \{ \{I1, I2\}, \{I1, I3\}, \{I1, I4\}, \{I1, I5\}, \{I2, I3\}, \{I2, I4\}, \{I2, I5\}, \{I3, I4\}, \{I3, I5\}, \{I4, I5\} \}$.</li>
        <li>Scan DB $\rightarrow L_2 = \{ \{I1, I2\}:4, \{I1, I3\}:4, \{I1, I5\}:2, \{I2, I3\}:4, \{I2, I4\}:2, \{I2, I5\}:2 \}$.</li>
        <li>Infrequent items dropped: $\{I3, I4\}:0, \{I3, I5\}:1, \{I4, I5\}:0$.</li>
      </ul>
    </li>
    <li><strong>Pass 3:</strong>
      <ul>
        <li>Join $L_2 \Join L_2 \rightarrow$ Candidates:
          <ul>
            <li>$\{I1, I2\} \Join \{I1, I3\} \rightarrow \{I1, I2, I3\}$. Subsets: $\{I1, I2\}, \{I1, I3\}, \{I2, I3\} \in L_2 \implies \mathbf{Keep}$.</li>
            <li>$\{I1, I2\} \Join \{I1, I5\} \rightarrow \{I1, I2, I5\}$. Subsets: $\{I1, I2\}, \{I1, I5\}, \{I2, I5\} \in L_2 \implies \mathbf{Keep}$.</li>
            <li>$\{I2, I3\} \Join \{I2, I4\} \rightarrow \{I2, I3, I4\}$. Subset $\{I3, I4\} \notin L_2 \implies \mathbf{Pruned!}$</li>
          </ul>
        </li>
        <li>$C_3 = \{ \{I1, I2, I3\}, \{I1, I2, I5\} \}$.</li>
        <li>Scan DB $\rightarrow L_3 = \{ \{I1, I2, I3\}:2, \{I1, I2, I5\}:2 \}$.</li>
      </ul>
    </li>
    <li><strong>Pass 4:</strong> Join $L_3 \Join L_3 \rightarrow \{I1, I2, I3, I5\}$. Subset $\{I2, I3, I5\} \notin L_3 \implies \mathbf{Pruned!}$ Algorithm terminates.</li>
  </ol>
  <p><strong>Rule Generation from Frequent Itemset $\{I1, I2, I5\}$ ($\sigma = 2$):</strong></p>
  <ul>
    <li>Rule $\{I1, I5\} \implies \{I2\}$: $\text{Conf} = \frac{\sigma(I1, I2, I5)}{\sigma(I1, I5)} = \frac{2}{2} = \mathbf{100\% \ge 70\% \implies Strong Rule!}$</li>
    <li>Rule $\{I2, I5\} \implies \{I1\}$: $\text{Conf} = \frac{\sigma(I1, I2, I5)}{\sigma(I2, I5)} = \frac{2}{2} = \mathbf{100\% \ge 70\% \implies Strong Rule!}$</li>
    <li>Rule $\{I5\} \implies \{I1, I2\}$: $\text{Conf} = \frac{\sigma(I1, I2, I5)}{\sigma(I5)} = \frac{2}{2} = \mathbf{100\% \ge 70\% \implies Strong Rule!}$</li>
    <li>Rule $\{I1, I2\} \implies \{I5\}$: $\text{Conf} = \frac{\sigma(I1, I2, I5)}{\sigma(I1, I2)} = \frac{2}{4} = \mathbf{50\% < 70\% \implies Rejected!}$</li>
  </ul>
</div>



<h2 class="section-title">Topic 4: Vertical Data Format (ECLAT Algorithm)</h2>
<p>
  <strong>ECLAT (Equivalence Class Transformation)</strong> mines frequent itemsets using a <strong>Vertical Data Format</strong> where each item is associated with its <strong>TID-list</strong> (list of transaction IDs containing the item):
</p>

<table class="custom-table">
  <thead>
    <tr><th>Item</th><th>TID-List</th><th>Support Count</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>I1</strong></td><td>{T100, T400, T500, T700, T800, T900}</td><td>6</td></tr>
    <tr><td><strong>I2</strong></td><td>{T100, T200, T300, T400, T600, T800, T900}</td><td>7</td></tr>
    <tr><td><strong>I3</strong></td><td>{T300, T500, T600, T700, T800, T900}</td><td>6</td></tr>
    <tr><td><strong>I4</strong></td><td>{T200, T400}</td><td>2</td></tr>
    <tr><td><strong>I5</strong></td><td>{T100, T800}</td><td>2</td></tr>
  </tbody>
</table>

<p><strong>TID-List Intersections for 2-Itemsets:</strong></p>
<ul>
  <li>$\text{TID}(I1, I2) = \text{TID}(I1) \cap \text{TID}(I2) = \{T100, T400, T800, T900\} \implies \mathbf{Count = 4 \ge 2}$</li>
  <li>$\text{TID}(I1, I3) = \{T500, T700, T800, T900\} \implies \mathbf{Count = 4 \ge 2}$</li>
  <li>$\text{TID}(I1, I5) = \{T100, T800\} \implies \mathbf{Count = 2 \ge 2}$</li>
  <li>$\text{TID}(I2, I3) = \{T300, T600, T800, T900\} \implies \mathbf{Count = 4 \ge 2}$</li>
  <li>$\text{TID}(I2, I4) = \{T200, T400\} \implies \mathbf{Count = 2 \ge 2}$</li>
  <li>$\text{TID}(I2, I5) = \{T100, T800\} \implies \mathbf{Count = 2 \ge 2}$</li>
</ul>



<h2 class="section-title">Topic 6: The FP-Growth Algorithm (Mining Without Candidate Generation)</h2>

<p>
  <strong>FP-Growth (Frequent Pattern Growth)</strong> overcomes the major performance bottlenecks of the Apriori algorithm (repeated full database scans and huge candidate itemset generation $C_k$).
</p>

<h3 class="subsection-title">The Two-Step FP-Growth Architecture:</h3>
<ol>
  <li><strong>Step 1: Construct the Compact FP-Tree:</strong>
    <ul>
      <li>Scan database once to compute support counts of 1-itemsets; sort frequent items in descending order of support ($I2:7 > I1:6 > I3:6 > I4:2 > I5:2$).</li>
      <li>Scan database a second time. For each transaction, insert items into a shared prefix tree (FP-Tree). Shared transaction prefixes share branch nodes, incrementing branch counts.</li>
      <li>Construct the <strong>Header Table</strong> containing item heads and horizontal linked-list node pointers traversing all identical items in the tree.</li>
    </ul>
  </li>
  <li><strong>Step 2: Mine the FP-Tree Recursively (Bottom-Up):</strong>
    <p>We extract Conditional Pattern Bases and construct Conditional FP-Trees starting from the bottom of the Header Table:</p>
    <table class="custom-table">
      <thead>
        <tr>
          <th>Item</th>
          <th>Conditional Pattern Base</th>
          <th>Conditional FP-Tree</th>
          <th>Frequent Patterns Generated</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>I5</strong></td>
          <td>$\{I2, I1: 1\}, \ \{I2, I1, I3: 1\}$</td>
          <td>$\langle I2: 2, I1: 2 \rangle$</td>
          <td>$\{I2, I5: 2\}, \ \{I1, I5: 2\}, \ \{I2, I1, I5: 2\}$</td>
        </tr>
        <tr>
          <td><strong>I4</strong></td>
          <td>$\{I2: 1\}, \ \{I2, I1: 1\}$</td>
          <td>$\langle I2: 2 \rangle$</td>
          <td>$\{I2, I4: 2\}$</td>
        </tr>
        <tr>
          <td><strong>I3</strong></td>
          <td>$\{I2, I1: 2\}, \ \{I2: 2\}, \ \{I1: 2\}$</td>
          <td>$\langle I2: 4, I1: 4 \rangle$</td>
          <td>$\{I2, I3: 4\}, \ \{I1, I3: 4\}, \ \{I2, I1, I3: 2\}$</td>
        </tr>
        <tr>
          <td><strong>I1</strong></td>
          <td>$\{I2: 4\}$</td>
          <td>$\langle I2: 4 \rangle$</td>
          <td>$\{I2, I1: 4\}$</td>
        </tr>
      </tbody>
    </table>
  </li>
</ol>



<h2 class="section-title">Topic 3 & 7: Interesting Pattern Evaluation Metrics</h2>

<div class="formula-card">
  <strong>Lift Correlation Formulation:</strong>
  $$\text{Lift}(A, B) = \frac{P(A \cup B)}{P(A) P(B)} = \frac{\text{Confidence}(A \implies B)}{\text{Support}(B)}$$
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Metric Name</th>
      <th style="width: 45%;">Mathematical Formula</th>
      <th>Interpretation & Properties</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Lift</strong></td>
      <td>$$\text{Lift}(A, B) = \frac{P(A \cup B)}{P(A) P(B)}$$</td>
      <td>$> 1$: Positively correlated.<br>$= 1$: Independent.<br>$< 1$: Negatively correlated.</td>
    </tr>
    <tr>
      <td><strong>Max-Confidence</strong></td>
      <td>$$\text{Max\_Conf}(A, B) = \max(P(A \mid B), P(B \mid A))$$</td>
      <td>Null-invariant metric.</td>
    </tr>
    <tr>
      <td><strong>Kulczynski (Kulc)</strong></td>
      <td>$$\text{Kulc}(A, B) = \frac{1}{2} \Big( P(A \mid B) + P(B \mid A) \Big)$$</td>
      <td>Arithmetic mean of conditional probabilities; <strong>Null-invariant</strong> (unaffected by total transaction size $|D|$).</td>
    </tr>
    <tr>
      <td><strong>Imbalance Ratio (IR)</strong></td>
      <td>$$\text{IR}(A, B) = \frac{|\text{supp}(A) - \text{supp}(B)|}{\text{supp}(A) + \text{supp}(B) - \text{supp}(A \cup B)}$$</td>
      <td>Measures asymmetry in itemset support; used in tandem with Kulc.</td>
    </tr>
    <tr>
      <td><strong>Cosine (Itemsets)</strong></td>
      <td>$$\text{Cosine}(A, B) = \frac{P(A \cup B)}{\sqrt{P(A) P(B)}} = \sqrt{P(A \mid B) P(B \mid A)}$$</td>
      <td>Geometric mean of conditional probabilities; Null-invariant.</td>
    </tr>
  </tbody>
</table>



<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module IV)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare Apriori and FP-Growth algorithms across 5 critical engineering metrics. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Candidate Generation:</strong> Apriori generates millions of candidate $k$-itemsets ($C_k$); FP-Growth generates zero candidates.<br>
    2. <strong>Database Scans:</strong> Apriori requires $k_{\max} + 1$ full scans of $D$; FP-Growth requires exactly 2 database scans.<br>
    3. <strong>Data Structure:</strong> Apriori uses flat transactional arrays and hash trees; FP-Growth builds a highly compressed prefix tree with linked header tables.<br>
    4. <strong>Memory Usage:</strong> Apriori requires huge RAM for candidate sets $C_k$; FP-Growth is memory compact via shared transaction prefixes.<br>
    5. <strong>Mining Strategy:</strong> Apriori is breadth-first (level-wise); FP-Growth is depth-first (divide-and-conquer).
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Why is Support-Confidence framework insufficient for evaluating pattern interestingness? (6 Marks)</div>
  <div class="qa-a">
    <strong>Answer:</strong> A rule can have high support and high confidence yet be completely uninteresting or deceptive. For example, in a grocery store where $75\%$ of all customers purchase coffee, the rule $\text{Tea} \implies \text{Coffee}$ might have $75\%$ confidence simply because coffee is popular overall, even though drinking tea might actually decrease the likelihood of buying coffee (negative correlation). Metrics like <strong>Lift</strong> and <strong>Kulczynski</strong> normalize for base individual item probabilities, exposing true causal affinity.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q3. What is Null-Invariance in pattern evaluation and why is it crucial for massive transaction databases? (6 Marks)</div>
  <div class="qa-a">
    <strong>Answer:</strong> A pattern interestingness measure $M$ is <strong>Null-Invariant</strong> if its value is completely unaffected by the number of transactions that contain neither item $A$ nor item $B$ ($0-0$ negative transactions). In web transaction logs and massive e-commerce databases with millions of total transactions, the number of null transactions is astronomical. Non-null-invariant measures (like $\chi^2$ and Lift) become severely distorted by total transaction count $|D|$, whereas null-invariant measures (like Kulczynski and Cosine) accurately measure true item affinity regardless of database size.
  </div>
</div>
"""
