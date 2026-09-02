# Artificial Intelligence Module 5 Exhaustive Content (9 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam Questions

AI_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Machine Learning & Neural Networks — Complete 9-Topic Syllabus Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 31:</strong> What is Learning? (Experience to Performance Improvement)</div>
    <div><strong>Topic 32:</strong> Rote Learning (Direct Memorization & Caching)</div>
    <div><strong>Topic 33:</strong> Learning by Taking Advice (Expert Instruction Parsing)</div>
    <div><strong>Topic 34:</strong> Learning from Examples (Inductive Supervised Classification)</div>
    <div><strong>Topic 35:</strong> Induction vs. Deduction in Machine Learning</div>
    <div><strong>Topic 36:</strong> Formal Learning Theory (Hypothesis Space, Bias & Variance)</div>
    <div><strong>Topic 37:</strong> Neural Net Learning (Perceptrons, Activations & Backpropagation)</div>
    <div><strong>Topic 38:</strong> Underfitting (High Bias, Low Capacity Models)</div>
    <div><strong>Topic 39:</strong> Overfitting (High Variance, Noise Memorization & Regularization)</div>
  </div>
</div>

<h2 class="section-title">Topic 31 – 35: Forms of Machine Learning & Inductive Inference</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Learning Paradigm</th>
      <th style="width: 45%;">Operational Mechanism</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Rote Learning</strong></td>
      <td>Stores computed results and solutions directly in a lookup table / cache. Re-executing retrieves pre-computed solutions.</td>
      <td>Instant $O(1)$ retrieval; zero generalization capability to unseen problem instances.</td>
    </tr>
    <tr>
      <td><strong>2. Learning by Advice</strong></td>
      <td>An external teacher/expert provides high-level instructions, which the system translates into internal operational rules.</td>
      <td>Rapid knowledge bootstrapping; requires complex natural language understanding.</td>
    </tr>
    <tr>
      <td><strong>3. Learning from Examples</strong></td>
      <td>Induces general classification/prediction functions $y = f(x)$ from a set of labeled input-output pairs $\langle x_i, y_i \rangle$.</td>
      <td>The foundation of modern machine learning; requires large representative datasets.</td>
    </tr>
    <tr>
      <td><strong>4. Induction vs. Deduction</strong></td>
      <td>• <strong>Induction:</strong> Derives general hypotheses from specific observations (probabilistic).<br>• <strong>Deduction:</strong> Derives specific consequences from general axioms (guaranteed true).</td>
      <td>Induction discovers new knowledge from data; Deduction proves theorems from axioms.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 36: Formal Learning Theory (Hypothesis Space & Bias-Variance)</h2>

<p>
  A learning algorithm searches through a <strong>Hypothesis Space</strong> $\mathcal{H}$ to select a candidate hypothesis $h \in \mathcal{H}$ that approximates the true underlying target function $f(x)$ with minimal generalization error on unseen data.
</p>

<table class="custom-table">
  <thead><tr><th>Concept</th><th>Mathematical / Theoretical Definition</th></tr></thead>
  <tbody>
    <tr><td><strong>Bias</strong></td><td>Error from erroneous assumptions in the learning algorithm (e.g., assuming linear boundary for nonlinear data).</td></tr>
    <tr><td><strong>Variance</strong></td><td>Error from sensitivity to small fluctuations in the training set (model memorizes random training noise).</td></tr>
    <tr><td><strong>Generalization</strong></td><td>The ability of a trained model to accurately predict labels on novel, previously unseen test samples.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 37: Neural Network Learning & Gradient Descent</h2>

<div class="formula-card">
  <strong>1. Artificial Neuron (Perceptron) Formulation:</strong>
  $$z = \sum_{i=1}^n w_i x_i + b = \mathbf{w}^T \mathbf{x} + b$$
  $$y = f(z) \quad (\text{Activation Function})$$
  - <strong>Sigmoid:</strong> $\sigma(z) = \frac{1}{1 + e^{-z}} \in (0, 1)$
  - <strong>ReLU (Rectified Linear Unit):</strong> $\text{ReLU}(z) = \max(0, z)$
  - <strong>Tanh:</strong> $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} \in (-1, 1)$
</div>

<div class="formula-card">
  <strong>2. Gradient Descent & Backpropagation Weight Update:</strong>
  $$w_{ij} \leftarrow w_{ij} - \eta \frac{\partial \mathcal{L}}{\partial w_{ij}}$$
  Where $\eta > 0$ is the learning rate and $\mathcal{L}$ is the Mean Squared Error loss function $\mathcal{L} = \frac{1}{2}\sum (t_k - y_k)^2$.
</div>

<h2 class="section-title">Topic 38 & 39: Underfitting vs. Overfitting</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Characteristic</th>
      <th style="width: 37%;">Underfitting (High Bias)</th>
      <th>Overfitting (High Variance)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Root Cause</strong></td><td>Model is too simplistic with insufficient expressive capacity.</td><td>Model is excessively complex with too many parameters.</td></tr>
    <tr><td><strong>Training Error</strong></td><td><strong>High</strong> (cannot fit training data).</td><td><strong>Ultra-Low / Zero</strong> (memorizes training noise).</td></tr>
    <tr><td><strong>Testing / Validation Error</strong></td><td><strong>High</strong> (poor performance everywhere).</td><td><strong>High</strong> (fails to generalize to unseen test data).</td></tr>
    <tr><td><strong>Engineering Fixes</strong></td><td>• Increase network depth / model capacity.<br>• Add more expressive polynomial features.<br>• Reduce excessive regularization ($\lambda$).</td><td>• Gather more diverse training data.<br>• Apply $L_2$ Weight Decay / $L_1$ Regularization.<br>• Add Dropout layers & Early Stopping.<br>• Prune decision trees / reduce parameters.</td></tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M5 Active Recall & Exam Questions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Differentiate between Underfitting and Overfitting. What techniques resolve overfitting in neural networks? (8 Marks)</div>
  <div class="qa-a">
    - <strong>Underfitting (High Bias):</strong> Occurs when the model is too simple to capture underlying data trends, yielding high errors on both training and testing datasets.<br>
    - <strong>Overfitting (High Variance):</strong> Occurs when the model is overly complex, memorizing random noise and sample idiosyncrasies, leading to near-zero training error but high test error.<br>
    - <strong>Techniques to Mitigate Overfitting:</strong><br>
      1. <em>Regularization ($L_1/L_2$):</em> Penalizes large weight magnitudes in the loss function ($\mathcal{L}_{\text{total}} = \mathcal{L} + \lambda \|\mathbf{w}\|^2$).<br>
      2. <em>Dropout:</em> Randomly deactivates a fraction $p$ of hidden neurons during each training step.<br>
      3. <em>Early Stopping:</em> Halts training when validation loss stops improving.<br>
      4. <em>Data Augmentation:</em> Synthetically expands training set size through geometric transformations.
  </div>
</div>
"""
