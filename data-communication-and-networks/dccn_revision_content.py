# DCCN 10-Page Master Revision Exhaustive Content (CS24305)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

DCCN_REVISION_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title">⚡ 10-Page Master Quick Revision — Data Communication & Computer Networks (CS24305)</div>
  <div class="toc-grid">
    <div>Page 1: OSI 7-Layer Model vs. TCP/IP Architecture & Encapsulation</div>
    <div>Page 2: Physical Layer: Nyquist Rate, Shannon Capacity & Manchester Encodings</div>
    <div>Page 3: Data Link Layer: Bit Stuffing, CRC Modulo-2 Division & Hamming Code</div>
    <div>Page 4: Sliding Window ARQs: Stop-and-Wait, Go-Back-N, Selective Repeat Math</div>
    <div>Page 5: Medium Access Control: Pure/Slotted ALOHA, CSMA/CD Minimum Frame Size</div>
    <div>Page 6: Network Layer: IPv4 Header Anatomy, Subnetting Masks & CIDR Lookup</div>
    <div>Page 7: Routing Protocols: Distance Vector (Bellman-Ford) & Link State (Dijkstra)</div>
    <div>Page 8: Transport Layer: TCP 3-Way Handshake & AIMD Congestion Control Rules</div>
    <div>Page 9: Application Layer: DNS Hierarchy, HTTP Evolution & Email (SMTP/IMAP)</div>
    <div>Page 10: Network Security: RSA Public-Key Cryptography Derivations & Solutions</div>
  </div>
</div>

<h2 class="section-title">⚡ Master Formula, Protocol & Channel Capacity Cheat Sheet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Topic / Concept</th>
      <th style="width: 45%;">Core Mathematical Formulation / Rule</th>
      <th>Key Exam Takeaway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nyquist Bit Rate</strong></td>
      <td>$$\text{BitRate}_{\max} = 2 B \log_2(M)$$</td>
      <td>Applies strictly to noiseless channels with $M$ signal levels.</td>
    </tr>
    <tr>
      <td><strong>Shannon Channel Capacity</strong></td>
      <td>$$C = B \log_2(1 + \text{SNR}), \quad \text{SNR} = 10^{\frac{\text{SNR}_{\text{dB}}}{10}}$$</td>
      <td>Theoretical upper bound for noisy thermal Gaussian channels.</td>
    </tr>
    <tr>
      <td><strong>CSMA/CD Minimum Frame</strong></td>
      <td>$$L_{\min} = 2 \times B \times \frac{d}{v}$$</td>
      <td>Guarantees collision detection before frame transmission ends (64 bytes in Ethernet).</td>
    </tr>
    <tr>
      <td><strong>Stop-and-Wait Efficiency</strong></td>
      <td>$$\eta = \frac{1}{1 + 2a}, \quad a = \frac{T_p}{T_t} = \frac{d / v}{L / B}$$</td>
      <td>Becomes very low over high-latency satellite channels ($a \gg 1$).</td>
    </tr>
    <tr>
      <td><strong>GBN vs SR Window Sizes</strong></td>
      <td>$$\text{GBN: } W_s \le 2^m - 1, \quad \text{SR: } W_s \le 2^{m-1}$$</td>
      <td>Prevents sequence number window overlap on lost ACKs.</td>
    </tr>
    <tr>
      <td><strong>RSA Decryption Key</strong></td>
      <td>$$(d \times e) \equiv 1 \pmod{\phi(n)}, \quad \phi(n) = (p-1)(q-1)$$</td>
      <td>Security relies on computational difficulty of factoring $n = pq$.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🔥 Top 10 High-Yield BIT Mesra Exam Questions & Solutions</h2>

<div class="qa-card">
  <div class="qa-q">Q1. A 100 km long cable has a data rate of 100 Mbps. If propagation speed is $2 \times 10^8 \text{ m/s}$, find the minimum frame size for CSMA/CD. (6 Marks)</div>
  <div class="qa-a">
    1. $T_p = \frac{d}{v} = \frac{100 \times 10^3 \text{ m}}{2 \times 10^8 \text{ m/s}} = 5 \times 10^{-4} \text{ s} = 0.5 \text{ ms}$.<br>
    2. $L_{\min} = 2 \times B \times T_p = 2 \times (100 \times 10^6 \text{ bps}) \times (5 \times 10^{-4} \text{ s}) = \mathbf{100,000} \text{ bits} = \mathbf{12,500} \text{ bytes}$.
  </div>
</div>
"""
