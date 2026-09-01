# Artificial Intelligence Module 5 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

AI_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Machine Learning Foundations & Neural Networks</div>
  <div class="toc-grid">
    <div>1. Machine Learning Paradigms (Supervised, Unsupervised & Reinforcement Learning)</div>
    <div>2. Inductive Learning Hypothesis, Inductive Bias & Occam's Razor Principle</div>
    <div>3. Decision Tree Representation & The ID3 Induction Algorithm</div>
    <div>4. Entropy ($H(S)$) & Information Gain Mathematical Formulations</div>
    <div>5. Step-by-Step ID3 Calculation Trace on the Benchmark PlayTennis Dataset</div>
    <div>6. C4.5 Algorithm Extensions (Gain Ratio & Continuous Numeric Attributes)</div>
    <div>7. Overfitting Mitigation: Pre-Pruning vs. Post-Pruning Strategies</div>
    <div>8. Computational Learning Theory: The PAC (Probably Approximately Correct) Model</div>
    <div>9. The Artificial Perceptron Model & The Perceptron Convergence Theorem</div>
    <div>10. Non-Linear Activation Functions (Sigmoid, Hyperbolic Tangent, ReLU, Softmax)</div>
    <div>11. Multi-Layer Perceptrons (MLP) & Backpropagation Error Gradient Derivations</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Machine Learning Paradigms & Inductive Bias</h2>
<p>
  A computer program is said to <strong>learn</strong> from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$ (Tom Mitchell, 1997).
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Paradigm</th>
      <th style="width: 35%;">Training Experience ($E$)</th>
      <th style="width: 25%;">Target Objective ($T$)</th>
      <th>Representative Algorithms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Supervised Learning</strong></td>
      <td>Labeled training tuples $\langle \mathbf{x}_i, y_i \rangle$ where ground-truth target label $y_i$ is explicitly provided.</td>
      <td>Classification (discrete labels) or Regression (continuous real values).</td>
      <td>Decision Trees (ID3/C4.5), Support Vector Machines, Neural Networks, Linear Regression.</td>
    </tr>
    <tr>
      <td><strong>2. Unsupervised Learning</strong></td>
      <td>Unlabeled data points $\mathbf{x}_i$ without ground-truth targets.</td>
      <td>Discovering intrinsic clusters, manifold embeddings, and density distributions.</td>
      <td>$k$-Means, Hierarchical Clustering, PCA, Autoencoders, Gaussian Mixture Models.</td>
    </tr>
    <tr>
      <td><strong>3. Reinforcement Learning</strong></td>
      <td>Sequential interaction with environment receiving scalar reward/penalty feedback $r_t$.</td>
      <td>Learning an optimal action policy $\pi^*(s)$ that maximizes expected discounted cumulative reward.</td>
      <td>Q-Learning, SARSA, Deep Q-Networks (DQN), Policy Gradients (PPO).</td>
    </tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">Inductive Learning Hypothesis & Occam's Razor</div>
  <ul>
    <li><strong>Inductive Learning Hypothesis:</strong> Any hypothesis found to approximate the target function well over a sufficiently large set of training examples will also approximate the target function well over unobserved test examples.</li>
    <li><strong>Occam's Razor:</strong> Prefer the simplest hypothesis that fits the training data (e.g., smaller decision trees are statistically less prone to overfitting than complex deep trees).</li>
  </ul>
</div>

<h2 class="section-title">Topic 3 – 5: Decision Tree Induction (ID3 Algorithm & Entropy)</h2>

<div class="formula-card">
  <strong>1. Information Entropy Formula (Shannon, 1948):</strong>
  $$H(S) = - \sum_{i=1}^c p_i \log_2 (p_i)$$
  Where $p_i$ is the proportion of examples in set $S$ belonging to target class $i$. For binary classification ($p_+$ and $p_-$):
  $$H(S) = - p_+ \log_2 (p_+) - p_- \log_2 (p_-)$$
</div>

<div class="formula-card">
  <strong>2. Information Gain Formula:</strong>
  $$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
  Where $S_v$ is the subset of $S$ for which attribute $A$ has value $v$. The ID3 algorithm selects the attribute that maximizes $\text{Gain}(S, A)$ at each node.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: ID3 Split Calculation on PlayTennis Dataset</div>
  <p><strong>Given Dataset:</strong> 14 total examples ($|S| = 14$), with 9 Positive (`Yes`) and 5 Negative (`No`).</p>
  <p><strong>Step 1: Compute Overall Dataset Entropy $H(S)$</strong></p>
  $$H(S) = - \frac{9}{14} \log_2\left(\frac{9}{14}\right) - \frac{5}{14} \log_2\left(\frac{5}{14}\right) = - (0.643 \times -0.637) - (0.357 \times -1.485) = \mathbf{0.940} \text{ bits}$$

  <p><strong>Step 2: Evaluate Attribute `Outlook` (Values: `Sunny` [2+, 3-], `Overcast` [4+, 0-], `Rain` [3+, 2-]):</strong></p>
  <ul>
    <li>$H(S_{\text{Sunny}}) = - \frac{2}{5} \log_2\left(\frac{2}{5}\right) - \frac{3}{5} \log_2\left(\frac{3}{5}\right) = 0.971$</li>
    <li>$H(S_{\text{Overcast}}) = - \frac{4}{4} \log_2(1) - 0 = \mathbf{0.000}$ (Pure leaf!)</li>
    <li>$H(S_{\text{Rain}}) = - \frac{3}{5} \log_2\left(\frac{3}{5}\right) - \frac{2}{5} \log_2\left(\frac{2}{5}\right) = 0.971$</li>
  </ul>
  <p><strong>Step 3: Compute Expected Entropy & Information Gain for `Outlook`:</strong></p>
  $$H(S \mid \text{Outlook}) = \frac{5}{14}(0.971) + \frac{4}{14}(0.000) + \frac{5}{14}(0.971) = 0.347 + 0 + 0.347 = 0.694$$
  $$\text{Gain}(S, \text{Outlook}) = 0.940 - 0.694 = \mathbf{0.246} \text{ bits}$$
  <p><em>Conclusion:</em> Since `Outlook` achieves the highest Information Gain among all candidate attributes (`Gain(Wind)=0.048, Gain(Humidity)=0.151, Gain(Temperature)=0.029`), `Outlook` is selected as the root node!</p>
</div>

<h2 class="section-title">Topic 9 & 10: Artificial Neural Networks & The Perceptron</h2>

<p>
  The <strong>Perceptron (Rosenblatt, 1958)</strong> is the foundational linear binary classifier model:
</p>
$$y = f(\mathbf{w}^T \mathbf{x} + b) = f\left( \sum_{i=1}^n w_i x_i + b \right)$$

<div class="callout callout-info">
  <div class="callout-title">Perceptron Learning Rule & Convergence Theorem</div>
  $$\mathbf{w} \leftarrow \mathbf{w} + \eta (y_{\text{true}} - y_{\text{pred}}) \mathbf{x}$$
  Where $\eta \in (0, 1]$ is the learning rate.<br>
  <strong>Convergence Theorem:</strong> If the training dataset is <strong>linearly separable</strong>, the perceptron learning rule is guaranteed to converge to a separating hyperplane in a finite number of weight update steps! If the data is not linearly separable (e.g., the XOR function), single-layer perceptrons fail completely (Minsky & Papert, 1969).
</div>

<h3 class="subsection-title">Standard Non-Linear Activation Functions:</h3>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Activation Function</th>
      <th style="width: 35%;">Mathematical Equation</th>
      <th style="width: 20%;">Output Range</th>
      <th>Derivative $\sigma'(z)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Logistic Sigmoid</strong></td>
      <td>$$\sigma(z) = \frac{1}{1 + e^{-z}}$$</td>
      <td>$(0, 1)$</td>
      <td>$\sigma(z)(1 - \sigma(z))$</td>
    </tr>
    <tr>
      <td><strong>2. Hyperbolic Tangent ($\tanh$)</strong></td>
      <td>$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$</td>
      <td>$(-1, 1)$</td>
      <td>$1 - \tanh^2(z)$</td>
    </tr>
    <tr>
      <td><strong>3. Rectified Linear Unit (ReLU)</strong></td>
      <td>$$f(z) = \max(0, z)$$</td>
      <td>$[0, \infty)$</td>
      <td>$1 \text{ if } z > 0 \text{ else } 0$</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 11: Multi-Layer Perceptrons (MLP) & Backpropagation</h2>

<div class="formula-card">
  <strong>Backpropagation Gradient Descent Weight Update:</strong>
  $$w_{ij} \leftarrow w_{ij} - \eta \frac{\partial E}{\partial w_{ij}}$$
  Where total sum-of-squares error $E = \frac{1}{2} \sum_k (t_k - y_k)^2$.<br>
  Using the Chain Rule of Calculus:
  $$\frac{\partial E}{\partial w_{ij}} = \frac{\partial E}{\partial \text{net}_j} \frac{\partial \text{net}_j}{\partial w_{ij}} = - \delta_j \cdot x_i$$
  - For output neuron $k$: $\delta_k = (t_k - y_k) \cdot g'(\text{net}_k)$
  - For hidden neuron $j$: $\delta_j = g'(\text{net}_j) \cdot \sum_k w_{jk} \delta_k$
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module V)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Why can a single-layer perceptron not learn the XOR function, and how do Multi-Layer Perceptrons solve this? (8 Marks)</div>
  <div class="qa-a">
    - <strong>Linear Separability Limitation:</strong> The XOR truth table has outputs `(0,0)->0, (0,1)->1, (1,0)->1, (1,1)->0`. Plotting these 4 points on a 2D plane reveals that no single straight line (hyperplane $\mathbf{w}^T\mathbf{x} + b = 0$) can separate class 1 from class 0.<br>
    - <strong>Multi-Layer Perceptrons (MLP) Solution:</strong> By adding a hidden layer of non-linear neurons, the network transforms the input space into a higher-dimensional feature space where the points become linearly separable. Two hidden neurons represent intermediate `NAND` and `OR` hyperplanes, which are then combined by an output `AND` neuron.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q2. Derive the Backpropagation weight update rule for a hidden-to-output weight. (10 Marks)</div>
  <div class="qa-a">
    Let $E = \frac{1}{2} (t_k - y_k)^2$, where $y_k = \sigma(\text{net}_k)$ and $\text{net}_k = \sum_j w_{jk} h_j$.<br>
    Applying the Chain Rule:<br>
    $$\frac{\partial E}{\partial w_{jk}} = \frac{\partial E}{\partial y_k} \cdot \frac{\partial y_k}{\partial \text{net}_k} \cdot \frac{\partial \text{net}_k}{\partial w_{jk}}$$
    1. $\frac{\partial E}{\partial y_k} = -(t_k - y_k)$<br>
    2. $\frac{\partial y_k}{\partial \text{net}_k} = y_k (1 - y_k)$ (Sigmoid derivative)<br>
    3. $\frac{\partial \text{net}_k}{\partial w_{jk}} = h_j$<br>
    Defining error signal $\delta_k = (t_k - y_k) y_k (1 - y_k)$, we get:<br>
    $$\frac{\partial E}{\partial w_{jk}} = - \delta_k h_j \implies w_{jk} \leftarrow w_{jk} + \eta \delta_k h_j$$
  </div>
</div>
"""
