# DCCN Module 2 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

DCCN_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Data Link Layer, Error Control & Flow Control ARQs</div>
  <div class="toc-grid">
    <div>1. Data Link Layer Design Issues & Service Models to Network Layer</div>
    <div>2. Framing Mechanisms: Byte Count, Byte Stuffing & Bit Stuffing with Flag `01111110`</div>
    <div>3. Error Detection: Simple Parity, 2D Parity & Internet Checksum Algorithm</div>
    <div>4. Cyclic Redundancy Check (CRC-32): Polynomial Division & Full Worked Traces</div>
    <div>5. Error Correction: Hamming Code $(n, k)$ Derivations & Parity Check Matrices</div>
    <div>6. Flow Control Mechanics: Stop-and-Wait Protocol & Channel Efficiency ($\eta$)</div>
    <div>7. Sliding Window Concepts: Bandwidth-Delay Product & Piggybacking</div>
    <div>8. Go-Back-N (GBN) ARQ Protocol: Sender/Receiver Windows ($W_s \le 2^m - 1$)</div>
    <div>9. Selective Repeat (SR) ARQ Protocol: Independent ACKs & Windows ($W_s \le 2^{m-1}$)</div>
    <div>10. Channel Utilization & Efficiency Proofs: $\eta = \frac{W}{1 + 2a}$ where $a = \frac{T_p}{T_t}$</div>
    <div>11. High-Level Data Link Control (HDLC) Frame Formats & PPP Architecture</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Data Link Framing Mechanisms</h2>
<p>
  The Data Link Layer converts the raw bit stream delivered by the Physical Layer into discrete, manageable packets called <strong>Frames</strong>:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Framing Method</th>
      <th style="width: 45%;">Delimiting Mechanism & Bit/Byte Manipulation</th>
      <th>Key Failure Modes & Mitigations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Character / Byte Count</strong></td>
      <td>Header field contains an integer specifying total number of bytes in frame.</td>
      <td>Fatal synchronization loss: if a transmission error alters the count byte, all subsequent frames are misframed.</td>
    </tr>
    <tr>
      <td><strong>2. Byte Stuffing (Character-Oriented)</strong></td>
      <td>Frames bounded by `FLAG` bytes (`0x7E`). Any occurrence of `FLAG` or escape byte `ESC` (`0x7D`) in payload is prefixed with an `ESC` byte.</td>
      <td>Tied to specific 8-bit character encodings (ASCII).</td>
    </tr>
    <tr>
      <td><strong>3. Bit Stuffing (Bit-Oriented — HDLC)</strong></td>
      <td>Frames delimited by flag pattern `01111110` ($6$ consecutive `1`s). Whenever sender observes $5$ consecutive `1`s in data payload, it unconditionally stuffs a `0` bit.</td>
      <td>Completely code-transparent; handles arbitrary arbitrary binary streams.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 4: Cyclic Redundancy Check (CRC) Polynomial Division</h2>

<div class="formula-card">
  <strong>CRC Transmission Invariants:</strong>
  Let data bit sequence be represented by polynomial $D(x)$ of length $k$, and Generator Polynomial be $G(x)$ of degree $r$.
  1. Append $r$ zero bits to $D(x) \implies D(x) \cdot x^r$.
  2. Divide $D(x) \cdot x^r$ by $G(x)$ using modulo-2 arithmetic (XOR binary division).
  3. The remainder $R(x)$ of length $r$ is the CRC Checksum. Transmitted codeword $T(x) = D(x) \cdot x^r \oplus R(x)$.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: CRC-4 Calculation on Data `1101011011` with Generator $G(x) = x^4 + x + 1$</div>
  <p><strong>Step 1: Convert Generator to Binary String:</strong> $G(x) = 1 \cdot x^4 + 0 \cdot x^3 + 0 \cdot x^2 + 1 \cdot x^1 + 1 \cdot x^0 \implies \mathbf{10011}$ (Degree $r=4$).</p>
  <p><strong>Step 2: Append $r=4$ zeros to Data ($D = 1101011011$):</strong> Augmented Dividend: $\mathbf{11010110110000}$.</p>
  <p><strong>Step 3: Modulo-2 Polynomial XOR Division:</strong></p>
  <pre><code>            1100001010  (Quotient)
10011 ) 11010110110000
        10011
        -----
         10011
         10011
         -----
          000010110
              10011
              -----
               010100
                10011
                -----
                 01110  <-- Remainder R = 1110</code></pre>
  <p><strong>Step 4: Transmitted Codeword:</strong> $11010110110000 \oplus 1110 = \mathbf{11010110111110}$.</p>
</div>

<h2 class="section-title">Topic 6 – 10: Sliding Window Flow Control ARQ Protocols</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Protocol</th>
      <th style="width: 25%;">Sender Window ($W_s$)</th>
      <th style="width: 25%;">Receiver Window ($W_r$)</th>
      <th>Channel Efficiency ($\eta$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Stop-and-Wait</strong></td>
      <td>$W_s = 1$</td>
      <td>$W_r = 1$</td>
      <td>$$\eta = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2a}$$</td>
    </tr>
    <tr>
      <td><strong>2. Go-Back-N (GBN)</strong></td>
      <td>$W_s = 2^m - 1$</td>
      <td>$W_r = 1$ (Cumulative ACK)</td>
      <td>$$\eta = \frac{W_s}{1 + 2a} \quad (\text{if } W_s < 1 + 2a, \text{ else } 100\%)$$</td>
    </tr>
    <tr>
      <td><strong>3. Selective Repeat (SR)</strong></td>
      <td>$W_s = 2^{m-1}$</td>
      <td>$W_r = 2^{m-1}$ (Independent ACK)</td>
      <td>$$\eta = \frac{W_s}{1 + 2a}$$</td>
    </tr>
  </tbody>
</table>
<p><em>Where $m$ = number of sequence number bits, $T_t = \frac{L}{B}$ = transmission time, $T_p = \frac{d}{v}$ = propagation delay, $a = \frac{T_p}{T_t}$.</em></p>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module II)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Why must the maximum sender window size in Selective Repeat ARQ satisfy $W_s \le 2^{m-1}$? (8 Marks)</div>
  <div class="qa-a">
    If $W_s + W_r > 2^m$, an ambiguous overlap occurs between the old sequence number window and the new sequence number window.<br>
    <em>Proof:</em> Suppose $m=2$ (sequence numbers $0, 1, 2, 3$) and $W_s = W_r = 3$. Sender transmits frames $0, 1, 2$. Receiver receives all 3 and shifts window to $[3, 0, 1]$, sending ACKs $0, 1, 2$. If all ACKs are lost in transit, sender times out and retransmits frame $0$. The receiver, expecting new frame $0$ in its current window $[3, 0, 1]$, will accept the duplicate old frame $0$ as new data, causing undetected duplicate data corruption! To prevent window overlap, $W_s + W_r \le 2^m \implies W_s \le 2^{m-1}$.
  </div>
</div>
"""
