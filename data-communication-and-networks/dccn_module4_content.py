# DCCN Module 4 Exhaustive Content (9 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DCCN_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Wide Area Networks (WAN) & Local Area Networks (LAN) — Complete Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 30:</strong> Switching Networks (Circuit vs. Packet Switching Paradigms)</div>
    <div><strong>Topic 31:</strong> Circuit-Switching Networks (3 Phases: Setup, Transfer, Teardown)</div>
    <div><strong>Topic 32:</strong> Circuit-Switching Concepts (Blocking, Dedicated Resources)</div>
    <div><strong>Topic 33:</strong> Packet-Switching Principles (Datagram vs. Virtual-Circuit)</div>
    <div><strong>Topic 34:</strong> Cellular Network Principles (Cell Geometry, Frequency Reuse, Handoff)</div>
    <div><strong>Topic 35:</strong> Cellular Generations Evolution (1G Voice to 5G Ultra-Low Latency)</div>
    <div><strong>Topic 36:</strong> Network Topologies (Bus, Star, Ring, Mesh, Tree Analysis)</div>
    <div><strong>Topic 37:</strong> LAN Protocol Architecture (IEEE 802: LLC vs. MAC Sublayers)</div>
    <div><strong>Topic 38:</strong> Virtual Local Area Networks (VLAN Security & Broadcast Domains)</div>
  </div>
</div>

<h2 class="section-title">Topic 30 – 33: Switching Paradigms (Circuit vs. Packet Switching) [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Parameter</th>
      <th style="width: 37%;">Circuit Switching</th>
      <th>Packet Switching [UPLOADED PYQ]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Path Establishment</strong></td>
      <td>Dedicated physical path established before data transfer (Setup $\rightarrow$ Transfer $\rightarrow$ Teardown).</td>
      <td>No dedicated end-to-end path; data divided into independent packets routed dynamically.</td>
    </tr>
    <tr>
      <td><strong>Resource Reservation</strong></td>
      <td>Dedicated channel bandwidth reserved 100% (resources wasted if line is idle).</td>
      <td>Statistical multiplexing: bandwidth shared on-demand among all active users.</td>
    </tr>
    <tr>
      <td><strong>Traffic Suitability</strong></td>
      <td>Ideal for continuous, real-time audio/voice communication.</td>
      <td>Ideal for bursty, asynchronous computer data traffic (Internet).</td>
    </tr>
    <tr>
      <td><strong>Delay Characteristics</strong></td>
      <td>Initial connection setup delay; zero queuing delay during active transfer.</td>
      <td>Zero setup delay (in datagram); packets experience variable queuing delay at routers.</td>
    </tr>
  </tbody>
</table>

<h3 class="subsection-title">Datagram vs. Virtual-Circuit Packet Switching [UPLOADED PYQ]:</h3>
<ul>
  <li><strong>Datagram Network (Connectionless — IP):</strong> Each packet contains full source and destination IP addresses and is treated as an independent entity. Intermediate routers make routing decisions per packet; packets may arrive out of order.</li>
  <li><strong>Virtual-Circuit Network (Connection-Oriented — ATM / X.25):</strong> A logical circuit is established upfront. Packets carry a short Virtual Circuit Identifier (VCI) rather than full global addresses. All packets follow the exact same route in sequence.</li>
</ul>

<h2 class="section-title">Topic 34 & 35: Cellular Network Principles & Generations (1G – 5G)</h2>

<div class="callout callout-info">
  <div class="callout-title">Core Cellular Principles: Frequency Reuse & Handoff</div>
  <ul>
    <li><strong>Frequency Reuse:</strong> Geographical service area is divided into regular hexagonal <strong>cells</strong>. Adjacent cells use different frequency sets, but non-adjacent cells separated by minimum reuse distance $D = R \sqrt{3N}$ reuse the same frequencies, dramatically multiplying network capacity!</li>
    <li><strong>Handoff / Handover:</strong> The automatic transition of an active ongoing call/data session from one base station channel to another as the mobile user moves across cell boundaries (Hard Handoff: "Break before make"; Soft Handoff: "Make before break").</li>
  </ul>
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 15%;">Generation</th>
      <th style="width: 35%;">Key Technological Milestone</th>
      <th style="width: 25%;">Core Services & Data Rate</th>
      <th>Multiple Access Tech</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1G (1980s)</strong></td><td>Analog cellular technology.</td><td>Voice only ($\approx 2.4 \text{ kbps}$).</td><td>FDMA</td></tr>
    <tr><td><strong>2G (1990s)</strong></td><td>Digital cellular, encryption, roaming.</td><td>Voice, SMS text ($\approx 64 \text{ kbps}$).</td><td>TDMA / CDMA (GSM)</td></tr>
    <tr><td><strong>3G (2000s)</strong></td><td>Mobile broadband Internet (UMTS).</td><td>Video calling, mobile web ($\approx 2 \text{ Mbps}$).</td><td>WCDMA</td></tr>
    <tr><td><strong>4G (2010s)</strong></td><td>All-IP network, LTE standard.</td><td>HD video streaming, gaming ($\approx 100 \text{ Mbps}$).</td><td>OFDMA</td></tr>
    <tr><td><strong>5G (2020s)</strong></td><td>Millimeter wave, network slicing, massive IoT.</td><td>eMBB, URLLC, mMTC ($1\text{–}10 \text{ Gbps}, < 1 \text{ ms}$).</td><td>Scalable OFDMA</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 36: Physical Network Topologies</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Topology</th>
      <th style="width: 45%;">Structural Layout & Communication</th>
      <th>Key Advantages & Vulnerabilities</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1. Mesh</strong></td><td>Every node has dedicated point-to-point links to all other $N-1$ nodes (Total links $= \frac{N(N-1)}{2}$).</td><td>Ultimate fault tolerance and privacy. High cable cost and complex installation.</td></tr>
    <tr><td><strong>2. Star</strong></td><td>Each node connected to a central controller / switch via dedicated point-to-point link.</td><td>Easy to install, isolate faults. Central switch failure halts entire network.</td></tr>
    <tr><td><strong>3. Bus</strong></td><td>All devices share a single long central backbone cable terminated at both ends.</td><td>Low cabling cost. Backbone cable break disables entire network.</td></tr>
    <tr><td><strong>4. Ring</strong></td><td>Each device has dedicated point-to-point connection to exactly two neighboring nodes in a loop.</td><td>Predictable token traffic. Break in ring disables network (unless dual-ring).</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 37 & 38: LAN Architecture & Virtual LANs (VLAN)</h2>

<p>
  IEEE 802 LAN Architecture divides the OSI Data Link Layer into two distinct sublayers:
</p>
<ol>
  <li><strong>Logical Link Control (LLC — IEEE 802.2):</strong> Independent of physical medium; handles flow control, error control, and upper-layer protocol multiplexing.</li>
  <li><strong>Medium Access Control (MAC):</strong> Dependent on physical topology; governs shared-channel access rules (CSMA/CD in 802.3, CSMA/CA in 802.11) and framing.</li>
</ol>

<div class="callout callout-warning">
  <div class="callout-title">VLAN (Virtual Local Area Network — IEEE 802.1Q)</div>
  A <strong>VLAN</strong> is a logical broadcast domain created by software configuration on switches regardless of physical cable connections. It isolates network broadcast storms, enhances department security, and reduces routing costs!
</div>

<h2 class="section-title">🧠 M4 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Compare Circuit Switching and Packet Switching across 4 architectural parameters. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Connection Setup:</strong> Circuit switching requires explicit 3-phase connection setup; Packet switching (datagram) sends packets immediately with zero setup.<br>
    2. <strong>Resource Utilization:</strong> Circuit switching reserves 100% dedicated channel capacity; Packet switching uses statistical multiplexing to maximize bandwidth utilization.<br>
    3. <strong>Congestion & Delays:</strong> Circuit switching has fixed transmission delay once connected; Packet switching suffers from variable queuing and router processing delays.<br>
    4. <strong>Failure Resilience:</strong> Circuit switching loses the call if any link on the dedicated path breaks; Packet switching automatically reroutes individual packets around failed links.
  </div>
</div>
"""
