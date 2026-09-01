# DCCN Module 3 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

DCCN_M3_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module III: Medium Access Control (MAC), Local Area Networks & Wireless LANs</div>
  <div class="toc-grid">
    <div>1. Channel Allocation Problem: Static FDM/TDM vs. Dynamic Random Access</div>
    <div>2. Pure ALOHA Protocol Mathematical Throughput Derivation ($S = G e^{-2G} \implies 18.4\%$)</div>
    <div>3. Slotted ALOHA Protocol Mathematical Throughput Derivation ($S = G e^{-G} \implies 36.8\%$)</div>
    <div>4. Carrier Sense Multiple Access (CSMA): 1-Persistent, Non-Persistent, $p$-Persistent</div>
    <div>5. CSMA with Collision Detection (CSMA/CD — IEEE 802.3 Ethernet Standard)</div>
    <div>6. Minimum Frame Size Derivation: $L_{\min} = 2 \times R \times \frac{d}{v}$ in Ethernet</div>
    <div>7. Truncated Binary Exponential Backoff Algorithm ($0 \le k < 2^i$)</div>
    <div>8. Standard Ethernet IEEE 802.3 Frame Structure & Physical MAC 48-Bit Addresses</div>
    <div>9. Fast Ethernet (100 Mbps), Gigabit Ethernet (1 Gbps) & 10-Gigabit Standards</div>
    <div>10. Wireless LANs (IEEE 802.11 Wi-Fi Architecture & CSMA/CA with RTS/CTS)</div>
    <div>11. The Hidden Station & Exposed Station Problems with Virtual Carrier Sensing (NAV)</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 2 & 3: ALOHA Protocols & Poisson Throughput Proofs</h2>

<div class="formula-card">
  <strong>1. Pure ALOHA Throughput Derivation:</strong>
  Let $G$ be the total offered traffic load (frames per frame transmission time $T$).
  - Vulnerable Period in Pure ALOHA $= 2 \times T$ (any frame generated in $(t - T, t + T)$ collides).
  - Under Poisson distribution, probability of zero other frame arrivals is $P(0) = e^{-2G}$.
  - Throughput:
    $$S = G \cdot e^{-2G}$$
  - Maximum Throughput occurs at $\frac{dS}{dG} = e^{-2G}(1 - 2G) = 0 \implies G = 0.5$:
    $$S_{\max} = 0.5 \cdot e^{-1} = \frac{1}{2e} \approx \mathbf{0.184} \quad (18.4\%)$$
</div>

<div class="formula-card">
  <strong>2. Slotted ALOHA Throughput Derivation:</strong>
  - Frames can only be transmitted at discrete slot boundaries.
  - Vulnerable Period $= 1 \times T$.
  - Throughput:
    $$S = G \cdot e^{-G}$$
  - Maximum Throughput occurs at $G = 1.0$:
    $$S_{\max} = 1.0 \cdot e^{-1} = \frac{1}{e} \approx \mathbf{0.368} \quad (36.8\%)$$
</div>

<h2 class="section-title">Topic 5 & 6: CSMA/CD & Minimum Frame Size Equation</h2>

<p>
  In <strong>CSMA/CD (Carrier Sense Multiple Access with Collision Detection)</strong>, a transmitting station continuously listens to the physical cable while transmitting.
</p>

<div class="callout callout-warning">
  <div class="callout-title">The Fundamental CSMA/CD Minimum Frame Size Rule</div>
  To guarantee that a station detects a collision before it finishes transmitting its frame, the transmission time $T_t$ must be at least twice the maximum round-trip propagation delay $2 \times T_p$:
  $$T_t \ge 2 \times T_p \implies \frac{L_{\min}}{B} \ge 2 \times \frac{d}{v} \implies L_{\min} = 2 \times B \times \frac{d}{v}$$
  Where $L_{\min}$ is the minimum frame size in bits, $B$ is the bandwidth in bps, $d$ is the maximum network length in meters, and $v$ is the signal propagation velocity in the cable ($\approx 2 \times 10^8 \text{ m/s}$).
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Classical 10 Mbps Ethernet 64-Byte Minimum Frame Size</div>
  <p>For standard $10\text{ Mbps}$ Ethernet with maximum collision domain distance $2500\text{ meters}$ and 4 repeaters:</p>
  $$2 T_p \approx 51.2 \ \mu\text{s}$$
  $$L_{\min} = 10 \times 10^6 \text{ bps} \times 51.2 \times 10^{-6} \text{ s} = 512 \text{ bits} = \mathbf{64} \text{ bytes}$$
  <p>Frames smaller than 64 bytes are padded with zeroes up to 64 bytes (Runt Frames $< 64$ bytes are discarded as collisions).</p>
</div>

<h2 class="section-title">Topic 10 & 11: Wireless LANs (IEEE 802.11) & The Hidden Station Problem</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Wireless Phenomenon</th>
      <th style="width: 45%;">Geometric Problem Topology</th>
      <th>CSMA/CA RTS/CTS Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Hidden Station Problem</strong></td>
      <td>Station $A$ and Station $C$ can both transmit to Base Station $B$, but $A$ and $C$ are out of range of each other. If both sense carrier simultaneously, they detect an idle channel and transmit, causing severe collisions at $B$.</td>
      <td><strong>RTS/CTS Handshake:</strong> $A$ sends `RTS` (Request to Send). $B$ broadcasts `CTS` (Clear to Send). $C$ overhears $B$'s `CTS` and sets its <strong>Network Allocation Vector (NAV)</strong> to defer transmission.</td>
    </tr>
    <tr>
      <td><strong>2. Exposed Station Problem</strong></td>
      <td>Station $B$ is transmitting to $A$. Station $C$ wants to transmit to $D$. $C$ senses the medium, detects $B$'s transmission, and wrongly defers, even though $C \rightarrow D$ would not interfere with $B \rightarrow A$.</td>
      <td>Resolved by spatial channel reuse and directional antennas.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module III)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the Truncated Binary Exponential Backoff Algorithm used in Ethernet. (8 Marks)</div>
  <div class="qa-a">
    After $i$ collisions for a frame:<br>
    1. The station chooses a random integer $k$ from the uniform range $0 \le k < 2^c$, where $c = \min(i, 10)$.<br>
    2. The station waits $k \times \text{SlotTime}$ ($k \times 51.2 \ \mu\text{s}$ in 10 Mbps Ethernet) before attempting retransmission.<br>
    3. After 10 collisions, the backoff interval freezes at $2^{10} - 1 = 1023$ slots.<br>
    4. If the frame experiences 16 consecutive collisions ($i=16$), the transmission is aborted and an error is reported to the upper layer.
  </div>
</div>
"""
