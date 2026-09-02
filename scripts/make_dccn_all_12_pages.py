#!/usr/bin/env python3
"""
Adds deep, exhaustive university-level textbook sections to all 5 DCCN modules
so that EVERY SINGLE MODULE PDF is solidly between 11 and 13 pages!
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

M1_ADD = r"""
<h2 class="section-title">Topic 13.7: Exhaustive Signal Analysis & Fourier Representation</h2>

<p>
  According to <strong>Fourier Analysis</strong>, any composite analog periodic signal can be decomposed into an infinite sum of simple sine and cosine waves (harmonics):
  $$x(t) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[ a_n \cos(2\pi n f_0 t) + b_n \sin(2\pi n f_0 t) \right]$$
  Where $f_0 = 1/T$ is the fundamental harmonic frequency. When a square wave (representing digital binary pulses) is transmitted over a physical channel with finite bandwidth $B$, the channel filters out high-frequency harmonics, rounding the sharp rectangular edges.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: Harmonic Bandwidth Requirements for Square Waves</div>
  <p>A digital system transmits a square wave clock signal at fundamental frequency $f_0 = 1\text{ MHz}$ ($1\text{ Mbps}$ rate for alternating `0101`).</p>
  <ul>
    <li>To transmit fundamental only: Bandwidth $B = 1\text{ MHz}$ $\implies$ Approximate sine wave shape.</li>
    <li>To transmit up to 3rd harmonic ($3\text{ MHz}$): Bandwidth $B = 3\text{ MHz}$ $\implies$ Noticeable squaring of corners.</li>
    <li>To transmit up to 5th harmonic ($5\text{ MHz}$): Bandwidth $B = 5\text{ MHz}$ $\implies$ Sharp, reliable digital pulse edges!</li>
  </ul>
  <p><em>Standard Telecom Rule:</em> A transmission channel must pass at least up to the <strong>5th harmonic</strong> ($B \ge 5 f_0$) to enable reliable, low-jitter threshold detection at the receiver!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 7: Signal-to-Noise Ratio (SNR) in Cascaded Amplifiers (Friis Formula)</div>
  <p>Two amplifiers are connected in cascade: Amplifier 1 has Gain $G_1 = 10\text{ dB}$ ($G_1 = 10$) and Noise Figure $F_1 = 3\text{ dB}$ ($F_1 = 2$). Amplifier 2 has Gain $G_2 = 20\text{ dB}$ ($G_2 = 100$) and Noise Figure $F_2 = 6\text{ dB}$ ($F_2 = 4$). Calculate the total system Noise Figure ($F_{\text{total}}$) using the <strong>Friis Formula</strong>.</p>
  $$\mathbf{F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} = 2 + \frac{4 - 1}{10} = 2 + 0.3 = \mathbf{2.3}}$$
  $$\mathbf{F_{\text{total(dB)}} = 10 \log_{10}(2.3) \approx \mathbf{3.62 \text{ dB}}}$$
  <p><em>Design Insight:</em> The noise figure of the first amplifier dominates the overall receiver noise performance, proving that low-noise pre-amplifiers (LNAs) must always be placed at the very front of the antenna receiver chain!</p>
</div>
"""

M2_ADD = r"""
<h2 class="section-title">Topic 19.6: Exhaustive Digital Carrier Modulation & Constellation Geometry</h2>

<p>
  Digital passband transmission utilizes Orthogonal In-Phase ($I$) and Quadrature ($Q$) carrier bases to synthesize high-density signal constellations:
  $$s(t) = I(t) \sqrt{\frac{2}{T_s}} \cos(2\pi f_c t) - Q(t) \sqrt{\frac{2}{T_s}} \sin(2\pi f_c t)$$
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Modulation Scheme</th>
      <th style="width: 18%;">Bits per Symbol ($k$)</th>
      <th style="width: 25%;">Spectral Efficiency ($\text{bps/Hz}$)</th>
      <th style="width: 20%;">Minimum SNR Required</th>
      <th>Representative Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>BPSK</strong></td><td>$1\text{ bit}$</td><td>$1.0\text{ bps/Hz}$</td><td>Low ($7\text{ dB}$)</td><td>Deep Space, Bluetooth LE</td></tr>
    <tr><td><strong>QPSK</strong></td><td>$2\text{ bits}$</td><td>$2.0\text{ bps/Hz}$</td><td>Moderate ($10\text{ dB}$)</td><td>DVB-S Satellite, 3G UMTS</td></tr>
    <tr><td><strong>8-PSK</strong></td><td>$3\text{ bits}$</td><td>$3.0\text{ bps/Hz}$</td><td>Moderate ($14\text{ dB}$)</td><td>EDGE Cellular (2.75G)</td></tr>
    <tr><td><strong>16-QAM</strong></td><td>$4\text{ bits}$</td><td>$4.0\text{ bps/Hz}$</td><td>High ($17\text{ dB}$)</td><td>Wi-Fi 4 (802.11n), 4G LTE</td></tr>
    <tr><td><strong>64-QAM</strong></td><td>$6\text{ bits}$</td><td>$6.0\text{ bps/Hz}$</td><td>Very High ($23\text{ dB}$)</td><td>Wi-Fi 5 (802.11ac), DVB-C</td></tr>
    <tr><td><strong>256-QAM</strong></td><td>$8\text{ bits}$</td><td>$8.0\text{ bps/Hz}$</td><td>Extremely High ($29\text{ dB}$)</td><td>Wi-Fi 6 (802.11ax), DOCSIS 3.1</td></tr>
    <tr><td><strong>1024-QAM</strong></td><td>$10\text{ bits}$</td><td>$10.0\text{ bps/Hz}$</td><td>Ultra High ($35\text{ dB}$)</td><td>Wi-Fi 6E / Wi-Fi 7 (802.11be)</td></tr>
    <tr><td><strong>4096-QAM</strong></td><td>$12\text{ bits}$</td><td>$12.0\text{ bps/Hz}$</td><td>Peak Clean SNR ($41\text{ dB}$)</td><td>Wi-Fi 7 Enterprise Channels</td></tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: Detailed Pulse Code Modulation (PCM) Dynamic Range & SNR Analysis</div>
  <p>An analog instrumentation sensor signal has bandwidth $f_{\text{max}} = 10\text{ kHz}$ and a required dynamic range of $72\text{ dB}$.</p>
  <ol>
    <li>What is the minimum number of PCM quantization bits ($n$) required to achieve $\text{SQNR} \ge 72\text{ dB}$?</li>
    <li>What is the resulting output digital bit rate when sampled at $25\%$ above the Nyquist rate?</li>
  </ol>
  <p><strong>Solution:</strong></p>
  $$\text{SQNR}_{\text{dB}} \approx 6.02 n + 1.76 \ge 72\text{ dB} \implies 6.02 n \ge 72 - 1.76 = 70.24$$
  $$n \ge \frac{70.24}{6.02} \approx 11.67 \implies \mathbf{n = 12 \text{ bits/sample} \quad (L = 2^{12} = 4096 \text{ levels})}$$
  $$\text{Sampling Rate: } f_s = 1.25 \times (2 \times 10\text{ kHz}) = 1.25 \times 20\text{ kHz} = \mathbf{25 \text{ kHz (25,000 samples/sec)}}$$
  $$\mathbf{\text{Output Bit Rate: } R = f_s \times n = 25,000 \times 12 = \mathbf{300,000 \text{ bps (300 kbps)}}}$$
</div>
"""

M3_ADD = r"""
<h2 class="section-title">Topic 27.6: Linear Block Codes & Parity-Check Matrix Mathematical Foundations</h2>

<p>
  In formal algebraic coding theory, a <strong>Linear $(n, k)$ Block Code</strong> maps $k$-bit data vectors $\mathbf{d} = (d_1, \dots, d_k)$ into $n$-bit codewords $\mathbf{c} = (c_1, \dots, c_n)$ via a **Generator Matrix** $G$:
  $$\mathbf{c = d \cdot G} \quad (\text{Modulo-2 Matrix Multiplication})$$
  Where $G = [I_k \mid P]$ is a $k \times n$ systematic generator matrix ($I_k$ is $k \times k$ identity matrix, $P$ is $k \times (n-k)$ parity submatrix).
</p>

<div class="formula-card">
  <strong>Parity Check Matrix $H$ & Syndrome Decoding Vector $\mathbf{S}$:</strong>
  $$\mathbf{H = [P^T \mid I_{n-k}]} \quad ((n-k) \times n \text{ Matrix})$$
  $$\mathbf{S = r \cdot H^T} \quad (\text{Where } \mathbf{r} = \mathbf{c} \oplus \mathbf{e} \text{ is the received vector})$$
  - If $\mathbf{S} = \mathbf{0}$: Zero errors detected $\implies$ Accept $\mathbf{r}$.
  - If $\mathbf{S} \neq \mathbf{0}$: The syndrome $\mathbf{S}$ matches the $i$-th column of $H$, identifying that bit position $i$ contains the bit error!
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Complete Systematic $(7, 4)$ Hamming Code Matrix Trace</div>
  <p>Let $G = \begin{bmatrix} 1 & 0 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 & 1 & 1 \end{bmatrix}$. Encode dataword $\mathbf{d} = [1, 0, 1, 1]$:</p>
  $$\mathbf{c} = [1, 0, 1, 1] \cdot G = \mathbf{[1, 0, 1, 1, 0, 1, 0]}$$
  <p>Suppose received vector is $\mathbf{r} = [1, 0, \mathbf{0}, 1, 0, 1, 0]$ (Bit 3 corrupted). Then:</p>
  $$\mathbf{S = r \cdot H^T = [0, 1, 1]}^T \implies \text{Matches Column 3 of } H \implies \mathbf{\text{Error is in Bit 3! Flip Bit 3 to 1 to correct!}}$$
</div>
"""

M4_ADD = r"""
<h2 class="section-title">Topic 36.6: Advanced Multi-Access Markov Chains & High-Speed Ethernet Fabrics</h2>

<p>
  The theoretical throughput of Random Access MAC protocols under saturation load is modeled via Poisson arrival processes and Markov birth-death state chains:
</p>

<div class="formula-card">
  <strong>Slotted ALOHA vs. 1-Persistent CSMA Throughput Derivations:</strong>
  - <strong>Slotted ALOHA:</strong> $S = G e^{-G} \implies S_{\text{max}} = \frac{1}{e} = \mathbf{36.8\%}$ (at offer load $G = 1$).
  - <strong>Non-Persistent CSMA:</strong> $\mathbf{S = \frac{G e^{-a G}}{G(1 + 2a) + e^{-a G}}} \implies S_{\text{max}} \approx \mathbf{82\%}$ (for small $a = 0.01$).
  - <strong>1-Persistent CSMA:</strong> $\mathbf{S = \frac{G [1 + G + a G (1 + G + a G/2)] e^{-G(1+2a)}}{G(1 + 2a) - (1 - e^{-a G}) + (1 + a G) e^{-G(1+a)}}} \approx \mathbf{53\%}$.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Complete 5-Switch Spanning Tree Protocol (STP) Convergence Trace</div>
  <p>Consider 5 enterprise switches $S_1, S_2, S_3, S_4, S_5$ interconnected with 100 Mbps Fast Ethernet links (Link Cost = 19):</p>
  <ul>
    <li>$S_1$: MAC `00:00:0A:11:00:01`, Priority 32768 $\implies$ <strong>ELECTED ROOT BRIDGE (Lowest MAC)</strong>.</li>
    <li>All ports on $S_1$ are designated as <strong>Designated Ports (Forwarding)</strong>.</li>
    <li>$S_2, S_3$ connected directly to $S_1$: Cost = 19 $\implies$ Ports facing $S_1$ are <strong>Root Ports</strong>.</li>
    <li>$S_4, S_5$ connected to $S_2$ and $S_3$: Cost to Root $= 19 + 19 = 38$.</li>
    <li>Redundant links between $S_4$ and $S_5$ are evaluated: $S_4$ has lower MAC than $S_5$. Therefore, $S_4$'s port is Designated, and $S_5$'s port transitions to <strong>BLOCKING STATE</strong>, terminating all broadcast loops!</li>
  </ul>
</div>
"""

M5_ADD = r"""
<h2 class="section-title">Topic 52.6: Advanced TCP State Transition Machine & Congestion Control Math</h2>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="20" width="90" height="40" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.2"/>
    <text x="65" y="44" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#991b1b" text-anchor="middle">CLOSED</text>

    <path d="M 110 40 L 160 40" stroke="#0284c7" stroke-width="1.8"/>

    <rect x="165" y="20" width="100" height="40" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="215" y="44" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#1e40af" text-anchor="middle">SYN_SENT</text>

    <path d="M 265 40 L 315 40" stroke="#0284c7" stroke-width="1.8"/>

    <rect x="320" y="20" width="120" height="40" rx="4" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.2"/>
    <text x="380" y="44" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#14532d" text-anchor="middle">ESTABLISHED</text>

    <path d="M 440 40 L 490 40" stroke="#0284c7" stroke-width="1.8"/>

    <rect x="495" y="20" width="110" height="40" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
    <text x="550" y="44" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#92400e" text-anchor="middle">FIN_WAIT_1/2</text>

    <path d="M 605 40 L 640 40" stroke="#0284c7" stroke-width="1.8"/>

    <rect x="645" y="20" width="85" height="40" rx="4" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2"/>
    <text x="687" y="44" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#581c87" text-anchor="middle">TIME_WAIT</text>
  </svg>
  <div class="diagram-caption">Figure 5.2: The Classical TCP Client Connection Lifetime State Machine</div>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Variable Length Subnet Masking (VLSM) Enterprise Plan</div>
  <p>An enterprise is allocated IP address block `10.0.0.0/16`. Subnet the block for: (1) Head Office: 10,000 hosts, (2) Branch 1: 5,000 hosts, (3) Branch 2: 2,000 hosts, (4) Branch 3: 1,000 hosts, (5) Five WAN point-to-point links (2 hosts each).</p>
  <ul>
    <li><strong>Head Office (10,000 hosts):</strong> $2^{14} - 2 = 16,382 \ge 10,000 \implies$ Mask: $/18 \ (255.255.192.0) \implies \mathbf{10.0.0.0/18}$ (`.0.1` to `.63.254`).</li>
    <li><strong>Branch 1 (5,000 hosts):</strong> $2^{13} - 2 = 8,190 \ge 5,000 \implies$ Mask: $/19 \ (255.255.224.0) \implies \mathbf{10.0.64.0/19}$ (`.64.1` to `.95.254`).</li>
    <li><strong>Branch 2 (2,000 hosts):</strong> $2^{11} - 2 = 2,046 \ge 2,000 \implies$ Mask: $/21 \ (255.255.248.0) \implies \mathbf{10.0.96.0/21}$ (`.96.1` to `.103.254`).</li>
    <li><strong>Branch 3 (1,000 hosts):</strong> $2^{10} - 2 = 1,022 \ge 1,000 \implies$ Mask: $/22 \ (255.255.252.0) \implies \mathbf{10.0.104.0/22}$ (`.104.1` to `.107.254`).</li>
    <li><strong>5 WAN Links (2 hosts each):</strong> Mask $/30 \ (255.255.255.252) \implies$ `10.0.108.0/30`, `10.0.108.4/30`, `10.0.108.8/30`, `10.0.108.12/30`, `10.0.108.16/30`.</li>
  </ul>
  <p><em>Efficiency:</em> 100% zero address collisions with over $40,000$ IP addresses preserved for future organizational growth!</p>
</div>
"""

def apply_all_adds():
    files = [
        ("dccn_module1_content.py", "Topic 13.7: Exhaustive Signal", M1_ADD),
        ("dccn_module2_content.py", "Topic 19.6: Exhaustive Digital", M2_ADD),
        ("dccn_module3_content.py", "Topic 27.6: Linear Block Codes", M3_ADD),
        ("dccn_module4_content.py", "Topic 36.6: Advanced Multi-Access", M4_ADD),
        ("dccn_module5_content.py", "Topic 52.6: Advanced TCP State", M5_ADD),
    ]
    
    for fname, check_str, add_text in files:
        fpath = os.path.join(DCCN_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if check_str not in c:
            c = c.rstrip().rstrip('"""').rstrip() + add_text + '\n"""\n'
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Applied 12-page boost to {fname}")

if __name__ == "__main__":
    apply_all_adds()
