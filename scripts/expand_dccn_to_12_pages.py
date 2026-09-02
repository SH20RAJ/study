#!/usr/bin/env python3
"""
Expands all DCCN module content files to 36,000 - 45,000 characters each,
ensuring that every single module generates 11 to 14 publication-grade pages in Playwright.
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

# --- M1 EXTRA ---
M1_EXTRA = r"""
<h2 class="section-title">Topic 13.2: Comprehensive Worked Numerical Problems in Physical Layer Physics</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 1: Decibel Loss and Multistage Repeater Amplification</div>
  <p>A signal travels through a transmission line consisting of three consecutive cable sections and two intermediate in-line amplifiers:</p>
  <ul>
    <li>Cable Section 1: Loss of $-12\text{ dB}$</li>
    <li>Amplifier 1: Gain of $+35\text{ dB}$</li>
    <li>Cable Section 2: Loss of $-18\text{ dB}$</li>
    <li>Amplifier 2: Gain of $+20\text{ dB}$</li>
    <li>Cable Section 3: Loss of $-15\text{ dB}$</li>
  </ul>
  <p>If the input signal power is $P_{\text{in}} = 2\text{ mW}$, calculate: (1) Total net gain/loss in dB, and (2) Final output power $P_{\text{out}}$.</p>
  <p><strong>Solution:</strong></p>
  $$\text{Total Net dB} = (-12) + (+35) + (-18) + (+20) + (-15) = \mathbf{+10 \text{ dB (Net Amplification)}}$$
  $$\text{Net dB} = 10 \log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right) \implies 10 = 10 \log_{10}\left(\frac{P_{\text{out}}}{2\text{ mW}}\right)$$
  $$\log_{10}\left(\frac{P_{\text{out}}}{2\text{ mW}}\right) = 1 \implies \frac{P_{\text{out}}}{2\text{ mW}} = 10^1 = 10 \implies \mathbf{P_{\text{out}} = 20 \text{ mW}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 2: Satellite Link Bandwidth-Delay Product (BDP)</div>
  <p>A 100 Mbps satellite link has a propagation delay of 250 ms. Calculate the Bandwidth-Delay Product in bits and bytes.</p>
  <p><strong>Solution:</strong></p>
  $$\text{BDP} = \text{Bandwidth} \times \text{Round-Trip Time (RTT)} = 100 \times 10^6 \text{ bps} \times (2 \times 0.250\text{ s})$$
  $$\text{BDP} = 100 \times 10^6 \times 0.500\text{ s} = \mathbf{50,000,000 \text{ bits}} = \mathbf{6,250,000 \text{ bytes (6.25 MB)}}$$
  <p><em>Interpretation:</em> The sender can transmit 6.25 MB of data before receiving the first ACK acknowledgement!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 3: Multi-Level Signaling Nyquist Limit</div>
  <p>A digital transmission system must transmit 64 kbps over a channel with bandwidth 4 kHz. What is the minimum Signal-to-Noise Ratio (SNR) in dB required to support this data rate according to Shannon's Theorem?</p>
  <p><strong>Solution:</strong></p>
  $$C = B \log_2(1 + \text{SNR}) \implies 64,000 = 4000 \times \log_2(1 + \text{SNR})$$
  $$\log_2(1 + \text{SNR}) = \frac{64,000}{4000} = 16 \implies 1 + \text{SNR} = 2^{16} = 65,536 \implies \text{SNR} = 65,535$$
  $$\mathbf{\text{SNR}_{\text{dB}} = 10 \log_{10}(65,535) \approx 10 \times 4.8165 = \mathbf{48.17 \text{ dB}}}$$
</div>
"""

# --- M2 EXTRA ---
M2_EXTRA = r"""
<h2 class="section-title">Topic 19.2: Advanced Modulation, Constellation Geometry & Delta Modulation</h2>

<p>
  In modern high-speed modems (such as V.90, V.92, DSL, DOCSIS cable modems, and 4G/5G LTE), multi-dimensional constellation geometry allows packing multiple bits per symbol over analog carrier channels.
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Delta Modulation (DM) & Slope Overload Distortion</div>
  <p><strong>Delta Modulation (DM)</strong> transmits only 1 bit per sample, indicating whether the current analog sample amplitude is higher (Bit 1: $+\delta$) or lower (Bit 0: $-\delta$) than the previous staircase approximation.</p>
  <ul>
    <li><strong>Slope Overload Distortion:</strong> Occurs when the input analog signal changes faster than the maximum rate of staircase increase ($|\frac{dx(t)}{dt}| > \frac{\delta}{T_s}$). The staircase cannot keep up with rapid signal rises.</li>
    <li><strong>Granular Noise:</strong> Occurs when the input analog signal is flat or slowly varying. The staircase oscillates continuously above and below the flat signal by $\pm \delta$.</li>
    <li><strong>Adaptive Delta Modulation (ADM):</strong> Dynamically scales step size $\delta$ based on successive bit history (doubles $\delta$ on consecutive 1s to prevent slope overload; shrinks $\delta$ on alternating 0101 to eliminate granular noise).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical: T1 and E1 Digital Carrier Frame Anatomy</div>
  <p><strong>1. North American T1 Carrier System (24 Voice Channels):</strong></p>
  $$\text{Each voice channel} = 8\text{ bits/sample} \times 8000\text{ samples/sec} = 64\text{ kbps}$$
  $$\text{T1 Frame} = (24 \text{ channels} \times 8\text{ bits}) + 1\text{ Framing Bit} = 192 + 1 = \mathbf{193 \text{ bits/frame}}$$
  $$\mathbf{\text{T1 Bit Rate} = 193 \text{ bits/frame} \times 8000 \text{ frames/sec} = \mathbf{1,544,000 \text{ bps (1.544 Mbps)}}}$$
  <p><strong>2. European E1 Carrier System (32 Voice Channels):</strong></p>
  $$\text{E1 Frame} = 32 \text{ channels} \times 8\text{ bits} = \mathbf{256 \text{ bits/frame}}$$
  $$\mathbf{\text{E1 Bit Rate} = 256 \text{ bits/frame} \times 8000 \text{ frames/sec} = \mathbf{2,048,000 \text{ bps (2.048 Mbps)}}}$$
  <p><em>Note:</em> Channel 0 is reserved for framing/synchronization; Channel 16 is reserved for out-of-band signaling (SS7).</p>
</div>
"""

# --- M3 EXTRA ---
M3_EXTRA = r"""
<h2 class="section-title">Topic 27.2: Comprehensive Sliding Window Mathematical Derivations & Buffer Protocols</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Mathematical Proof: Maximum Window Size for Go-Back-N ($W_S = 2^k - 1$)</div>
  <p>Suppose $k=2$ bit sequence numbers ($0, 1, 2, 3$). If the sender were allowed a window size of $W_S = 2^k = 4$:</p>
  <ol>
    <li>Sender transmits frames $0, 1, 2, 3$. Receiver receives all 4 frames and emits $\text{ACK } 0$ (expecting frame 0 next).</li>
    <li>If all ACKs are lost in transit: Sender times out and retransmits frame 0.</li>
    <li><strong>Fatal Ambiguity:</strong> Receiver cannot determine whether this incoming frame 0 is a <em>retransmission of the old frame 0</em> or a <em>brand-new frame 0 of the next sequence cycle</em>!</li>
    <li>To guarantee complete non-overlapping receiver expectations: $\mathbf{W_S + W_R \le 2^k \implies W_S + 1 \le 2^k \implies W_S \le 2^k - 1}$.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Mathematical Proof: Maximum Window Size for Selective Repeat ($W_S = W_R = 2^{k-1}$)</div>
  <p>In Selective Repeat, the receiver accepts out-of-order frames within its window $W_R$.</p>
  $$\text{To prevent window overlap between old and new cycles: } W_S + W_R \le 2^k$$
  $$\text{Setting symmetric windows } W_S = W_R = N: \quad 2N \le 2^k \implies \mathbf{N \le 2^{k-1}}$$
  <p>For $k=3$ bits ($0\dots7$): Maximum window size for Selective Repeat is $\mathbf{W_S = 2^{3-1} = 4}$.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical: Stop-and-Wait ARQ Efficiency with Frame Transmission Errors</div>
  <p>A $1\text{ Mbps}$ link with $T_{\text{prop}} = 20\text{ ms}$ transmits $1000\text{ byte}$ frames. If the frame error probability is $P_f = 0.1$ ($10\%$ packet loss), calculate the effective throughput.</p>
  <p><strong>Solution:</strong></p>
  $$T_{\text{trans}} = \frac{8000\text{ bits}}{10^6\text{ bps}} = 8\text{ ms} \implies a = \frac{20\text{ ms}}{8\text{ ms}} = 2.5$$
  $$\text{Ideal Efficiency: } \eta_0 = \frac{1}{1 + 2a} = \frac{1}{1 + 2(2.5)} = \frac{1}{6} \approx 16.67\%$$
  $$\text{Efficiency with Error Rate } P_f: \quad \mathbf{\eta = \eta_0 \times (1 - P_f) = \frac{1 - 0.1}{6} = \frac{0.9}{6} = 0.15 = \mathbf{15\%}}$$
  $$\mathbf{\text{Effective Throughput} = \eta \times \text{Bandwidth} = 0.15 \times 1\text{ Mbps} = \mathbf{150 \text{ kbps}}}$$
</div>
"""

# --- M4 EXTRA ---
M4_EXTRA = r"""
<h2 class="section-title">Topic 36.2: Advanced Ethernet Switching, VLANs & Spanning Tree Calculations</h2>

<p>
  Modern enterprise local area networks replace shared collision domains with <strong>Full-Duplex Layer 2 Switched Ethernet</strong> and <strong>Virtual Local Area Networks (VLANs, IEEE 802.1Q)</strong>.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Switching Technique</th>
      <th style="width: 45%;">Operating Architecture</th>
      <th>Latency & Error Propagation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Store-and-Forward</strong></td>
      <td>Switch buffers entire frame in memory, verifies 32-bit CRC checksum, checks destination MAC in CAM table, and forwards frame.</td>
      <td>Highest latency (proportional to frame size); 100% immune to corrupt frames (discards CRC errors).</td>
    </tr>
    <tr>
      <td><strong>2. Cut-Through</strong></td>
      <td>Switch reads only first 6 bytes (Destination MAC) and immediately begins forwarding frame to target port before receiving remainder.</td>
      <td><strong>Lowest Latency:</strong> Fixed instant forwarding; propagates corrupt frames and collision fragments.</td>
    </tr>
    <tr>
      <td><strong>3. Fragment-Free</strong></td>
      <td>Switch buffers first 64 bytes (collision window) before forwarding.</td>
      <td>Filters out all collision fragments (runt frames $< 64$ bytes) with minimal latency penalty.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Spanning Tree Protocol (STP) Bridge Port Calculation</div>
  <p>Consider 3 switches $S_1, S_2, S_3$ connected in a ring with Gigabit links (Path Cost = 4):</p>
  <ul>
    <li>$S_1$ Bridge ID: `32768:00-11-22-33-44-01`</li>
    <li>$S_2$ Bridge ID: `32768:00-11-22-33-44-02`</li>
    <li>$S_3$ Bridge ID: `32768:00-11-22-33-44-03`</li>
  </ul>
  <p><strong>STP State Derivation:</strong></p>
  <ol>
    <li><strong>Root Bridge Election:</strong> $S_1$ has the lowest MAC address $\implies$ $\mathbf{S_1 \text{ is elected ROOT BRIDGE}}$. All ports on $S_1$ become <strong>Designated Ports (Forwarding)</strong>.</li>
    <li><strong>Root Ports on $S_2$ and $S_3$:</strong> Port facing $S_1$ on $S_2$ has cost 4 $\implies$ <strong>Root Port</strong>. Port facing $S_1$ on $S_3$ has cost 4 $\implies$ <strong>Root Port</strong>.</li>
    <li><strong>Link between $S_2$ and $S_3$:</strong> Both have cost 4 to Root. Tie-breaker: $S_2$ has lower Bridge ID than $S_3$. Therefore, $S_2$'s port becomes <strong>Designated Port</strong>, and $S_3$'s port is placed in <strong>BLOCKING STATE</strong>, breaking the loop!</li>
  </ol>
</div>
"""

# --- M5 EXTRA ---
M5_EXTRA = r"""
<h2 class="section-title">Topic 52.2: Comprehensive Network Layer & Transport Layer Solved Numericals</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 1: Dijkstra's Link State Shortest Path Algorithm Trace</div>
  <p>Find the shortest paths from source router $A$ to all nodes in network graph:</p>
  <ul>
    <li>Edges: $A-B: 2, \ A-C: 5, \ B-C: 2, \ B-D: 4, \ C-D: 1, \ C-E: 5, \ D-E: 1$</li>
  </ul>
  <p><strong>Execution Trace Table:</strong></p>
  <table class="custom-table">
    <thead><tr><th>Step</th><th>Visited Set $N'$</th><th>$D(B), p(B)$</th><th>$D(C), p(C)$</th><th>$D(D), p(D)$</th><th>$D(E), p(E)$</th></tr></thead>
    <tbody>
      <tr><td>0</td><td>$\{A\}$</td><td>$2, A$</td><td>$5, A$</td><td>$\infty$</td><td>$\infty$</td></tr>
      <tr><td>1</td><td>$\{A, B\}$</td><td><strong>2, A</strong></td><td>$4, B$</td><td>$6, B$</td><td>$\infty$</td></tr>
      <tr><td>2</td><td>$\{A, B, C\}$</td><td>2, A</td><td><strong>4, B</strong></td><td>$5, C$</td><td>$9, C$</td></tr>
      <tr><td>3</td><td>$\{A, B, C, D\}$</td><td>2, A</td><td>4, B</td><td><strong>5, C</strong></td><td>$6, D$</td></tr>
      <tr><td>4</td><td>$\{A, B, C, D, E\}$</td><td>2, A</td><td>4, B</td><td>5, C</td><td><strong>6, D</strong></td></tr>
    </tbody>
  </table>
  <p><strong>Shortest Paths from $A$:</strong> to $B = 2$, to $C = 4$ ($A \rightarrow B \rightarrow C$), to $D = 5$ ($A \rightarrow B \rightarrow C \rightarrow D$), to $E = 6$ ($A \rightarrow B \rightarrow C \rightarrow D \rightarrow E$).</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 2: TCP AIMD Congestion Window Evolution</div>
  <p>A TCP Reno connection has $\text{ssthresh} = 16\text{ MSS}$. It starts in Slow Start ($\text{cwnd} = 1$). Trace $\text{cwnd}$ over successive RTTs until a timeout occurs at $\text{cwnd} = 20$, followed by 3 duplicate ACKs at $\text{cwnd} = 12$:</p>
  <ol>
    <li><strong>RTT 1–5 (Slow Start):</strong> $\text{cwnd}$ doubles: $1 \rightarrow 2 \rightarrow 4 \rightarrow 8 \rightarrow 16\text{ MSS}$ (Reaches $\text{ssthresh}$).</li>
    <li><strong>RTT 6–9 (Congestion Avoidance):</strong> Linear growth: $17 \rightarrow 18 \rightarrow 19 \rightarrow 20\text{ MSS}$.</li>
    <li><strong>Timeout at $\text{cwnd} = 20$:</strong> Sets $\text{ssthresh} \leftarrow 20/2 = 10\text{ MSS}$, resets $\text{cwnd} \leftarrow 1\text{ MSS}$, re-enters Slow Start.</li>
    <li><strong>RTT 10–14:</strong> Doubles $1 \rightarrow 2 \rightarrow 4 \rightarrow 8 \rightarrow 10$ ($\text{ssthresh}$ reached), then linear: $11 \rightarrow 12\text{ MSS}$.</li>
    <li><strong>3 Duplicate ACKs at $\text{cwnd} = 12$:</strong> Fast Retransmit! Sets $\text{ssthresh} \leftarrow 12/2 = 6\text{ MSS}$, sets $\text{cwnd} \leftarrow 6 + 3 = 9\text{ MSS}$ in Fast Recovery!</li>
  </ol>
</div>
"""

def expand_all():
    files_to_expand = [
        ("dccn_module1_content.py", "Topic 13.2: Comprehensive Worked Numerical", M1_EXTRA),
        ("dccn_module2_content.py", "Topic 19.2: Advanced Modulation", M2_EXTRA),
        ("dccn_module3_content.py", "Topic 27.2: Comprehensive Sliding Window", M3_EXTRA),
        ("dccn_module4_content.py", "Topic 36.2: Advanced Ethernet Switching", M4_EXTRA),
        ("dccn_module5_content.py", "Topic 52.2: Comprehensive Network Layer", M5_EXTRA),
    ]
    
    for fname, check_str, extra_text in files_to_expand:
        fpath = os.path.join(DCCN_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        if check_str not in content:
            content = content.rstrip().rstrip('"""').rstrip() + extra_text + '\n"""\n'
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Expanded {fname}")

if __name__ == "__main__":
    expand_all()
