# DCCN Module 3 Exhaustive Content (8 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DCCN_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Error Handling, Data Link Control & Multiplexing — Complete Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 20:</strong> Types of Errors (Single-Bit Errors vs. Burst Errors)</div>
    <div><strong>Topic 21:</strong> Error Detection Techniques (Simple Parity & Limitations)</div>
    <div><strong>Topic 22:</strong> Checksum (1's Complement Summation & Verification)</div>
    <div><strong>Topic 23:</strong> Cyclic Redundancy Check (CRC-32 Modulo-2 Division)</div>
    <div><strong>Topic 24:</strong> Error Correction (Hamming Code & Syndrome Decoding)</div>
    <div><strong>Topic 25 & 26:</strong> Flow & Error Control ARQ (Stop-and-Wait, GBN, Selective Repeat)</div>
    <div><strong>Topic 27:</strong> High-Level Data Link Control (HDLC Frame: I, S, U-Frames)</div>
    <div><strong>Topic 28 & 29:</strong> Multiplexing (FDM, Synchronous TDM vs. Statistical TDM)</div>
  </div>
</div>

<h2 class="section-title">Topic 20 – 22: Error Types & Basic Detection Techniques</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Error Class</th>
      <th style="width: 45%;">Mathematical Definition</th>
      <th>Detection Feasibility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Single-Bit Error</strong></td>
      <td>Only 1 bit in the data block is inverted from $0 \rightarrow 1$ or $1 \rightarrow 0$.</td>
      <td>Easily detected by a single Parity Bit.</td>
    </tr>
    <tr>
      <td><strong>2. Burst Error</strong></td>
      <td>Two or more bits in a sequence are corrupted. Length of burst is measured from first corrupted bit to last corrupted bit.</td>
      <td>Requires Cyclic Redundancy Check (CRC) or 2D Parity.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 23: Cyclic Redundancy Check (CRC) Polynomial Division [UPLOADED PYQ]</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ [UPLOADED PYQ] Solved Problem: CRC for Data `1010011110` with Generator $G = 1011$</div>
  <p><strong>Step 1: Determine Degree of Generator:</strong> $G = 1011$ has degree $r = 3$.</p>
  <p><strong>Step 2: Append $r=3$ zeros to Data:</strong> Augmented Dividend = `1010011110000`.</p>
  <p><strong>Step 3: Modulo-2 XOR Division:</strong></p>
  <pre><code>        1001001011  (Quotient)
1011 ) 1010011110000
       1011
       ----
        001011
          1011
          ----
           00001110
               1011
               ----
                1010
                1011
                ----
                 001000
                   1011
                   ----
                    0110  <-- Remainder CRC = 011</code></pre>
  <p><strong>Step 4: Transmitted Frame:</strong> $\text{Data} + \text{CRC} = \mathbf{1010011110011}$.</p>
</div>

<h2 class="section-title">Topic 24: Error Correction (Hamming Code $(n, k)$ Derivation)</h2>

<div class="formula-card">
  <strong>Hamming Parity Bit Invariants (Hamming, 1950):</strong>
  For $m$ data bits and $r$ parity check bits:
  $$2^r \ge m + r + 1$$
  - Parity bits are placed strictly at bit positions that are powers of 2 ($1, 2, 4, 8, 16, \dots$).
  - Data bits occupy all remaining positions ($3, 5, 6, 7, 9, 10, \dots$).
  - Parity bit $P_k$ checks all bit positions whose binary representation has a $1$ in the $k$-th position.
  - <strong>Syndrome:</strong> Evaluation of parity checks at the receiver forms a binary integer: $000 \implies$ No error; non-zero value indicates the exact corrupted bit position!
</div>

<h2 class="section-title">Topic 25 & 26: Sliding Window Flow & Error Control ARQ Protocols [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">ARQ Protocol</th>
      <th style="width: 25%;">Sender Window ($W_s$)</th>
      <th style="width: 25%;">Receiver Window ($W_r$)</th>
      <th>Key Retransmission Behavior & Efficiency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Stop-and-Wait ARQ</strong></td>
      <td>$W_s = 1$</td>
      <td>$W_r = 1$</td>
      <td>Sender waits for ACK before sending next frame. Low efficiency on long propagation delays ($\eta = \frac{1}{1 + 2a}$).</td>
    </tr>
    <tr>
      <td><strong>2. Go-Back-N (GBN) [UPLOADED PYQ]</strong></td>
      <td>$W_s \le 2^m - 1$</td>
      <td>$W_r = 1$ (Cumulative ACK)</td>
      <td>When frame $k$ is lost or damaged, receiver discards all subsequent out-of-order frames. Sender retransmits all frames from $k$ onwards.</td>
    </tr>
    <tr>
      <td><strong>3. Selective Repeat (SR)</strong></td>
      <td>$W_s \le 2^{m-1}$</td>
      <td>$W_r \le 2^{m-1}$ (Independent ACK)</td>
      <td>Receiver buffers out-of-order frames. Sender retransmits <em>only the specific missing frame</em> $k$, saving bandwidth.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 27: High-Level Data Link Control (HDLC Frame Formats)</h2>

<div class="diagram-container">
  <svg width="100%" height="70" viewBox="0 0 740 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="80" height="40" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="60" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#1e40af" text-anchor="middle">Flag (8b)</text>

    <rect x="105" y="15" width="90" height="40" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="150" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#1e40af" text-anchor="middle">Address (8b)</text>

    <rect x="200" y="15" width="95" height="40" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="247" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#92400e" text-anchor="middle">Control (8/16b)</text>

    <rect x="300" y="15" width="220" height="40" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="410" y="38" font-family="Plus Jakarta Sans" font-size="10.5" font-weight="700" fill="#14532d" text-anchor="middle">Information Payload (Variable)</text>

    <rect x="525" y="15" width="95" height="40" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="572" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#581c87" text-anchor="middle">FCS / CRC (16b)</text>

    <rect x="625" y="15" width="80" height="40" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="665" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#1e40af" text-anchor="middle">Flag (8b)</text>
  </svg>
  <div class="diagram-caption">Figure 3.1: Universal HDLC Frame Architecture with Flag `01111110` Delimiters</div>
</div>

<div class="callout callout-info">
  <div class="callout-title">🧠 The 3 HDLC Frame Formats</div>
  <ul>
    <li><strong>1. Information Frames (I-Frames):</strong> Carries user data payload and piggybacked ACKs ($N(S)$ send sequence and $N(R)$ receive sequence).</li>
    <li><strong>2. Supervisory Frames (S-Frames):</strong> Carries flow/error control without payload (RR - Receive Ready, RNR - Receive Not Ready, REJ - Reject / NAK).</li>
    <li><strong>3. Unnumbered Frames (U-Frames):</strong> Used for link initialization, mode setting (SABM - Set Asynchronous Balanced Mode), and link disconnection (DISC).</li>
  </ul>
</div>

<h2 class="section-title">Topic 28 & 29: Multiplexing (FDM, Synchronous vs. Statistical TDM) [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">Synchronous TDM</th>
      <th>Statistical / Asynchronous TDM [UPLOADED PYQ]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Time Slot Allocation</strong></td>
      <td>Pre-assigned, fixed, dedicated time slots to each input line in a round-robin cycle.</td>
      <td>Time slots allocated dynamically on-demand only to active input lines with data to send.</td>
    </tr>
    <tr>
      <td><strong>Bandwidth Efficiency</strong></td>
      <td>Low: if an input line has no data to transmit, its allocated time slot goes completely empty/wasted.</td>
      <td>High: zero wasted empty slots. Total input data rate can exceed the aggregate multiplexed link capacity.</td>
    </tr>
    <tr>
      <td><strong>Addressing Overhead</strong></td>
      <td>No addressing needed in slot (receiver knows source by slot position).</td>
      <td>Each slot requires header addressing metadata to identify source/destination.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M3 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Differentiate between Stop-and-Wait ARQ and Go-Back-N ARQ. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Sender Window Size:</strong> Stop-and-Wait has $W_s = 1$; Go-Back-N has $W_s = 2^m - 1 > 1$, enabling continuous transmission pipelining.<br>
    2. <strong>Channel Utilization:</strong> Stop-and-Wait has very poor link utilization ($\eta = \frac{1}{1 + 2a}$); GBN achieves near 100% utilization when $W_s \ge 1 + 2a$.<br>
    3. <strong>Retransmission Scope:</strong> In Stop-and-Wait, only 1 frame is retransmitted on timeout; in GBN, the entire window of $N$ unacknowledged frames is retransmitted upon a single lost frame.
  </div>
</div>
"""
