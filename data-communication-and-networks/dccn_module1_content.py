# DCCN Module 1 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

DCCN_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Transmission Fundamentals & Physical Layer Architectures</div>
  <div class="toc-grid">
    <div>1. Data Communication Components & Network Topologies (Mesh, Star, Bus, Ring)</div>
    <div>2. The OSI 7-Layer Reference Model vs. TCP/IP 5-Layer Protocol Architecture</div>
    <div>3. Analog vs. Digital Signals, Composite Signals & Fourier Spectral Analysis</div>
    <div>4. Transmission Impairments (Attenuation, Distortion, Thermal & Cross-Talk Noise)</div>
    <div>5. Nyquist Maximum Bit Rate Formula for Noiseless Channels & Multi-Level Signaling</div>
    <div>6. Shannon Channel Capacity Theorem for Noisy Channels & Decibel ($\text{dB}$) Math</div>
    <div>7. Line Coding Schemes: NRZ-L, NRZ-I, Manchester, Differential Manchester & AMI</div>
    <div>8. Scrambling Techniques for Synchronization: B8ZS (North America) & HDB3 (Europe)</div>
    <div>9. Transmission Media: Guided (Twisted Pair, Coax, Fiber) vs. Unguided (Radio, Micro)</div>
    <div>10. Optical Fiber Physics: Step-Index, Graded-Index, Single-Mode vs. Multi-Mode</div>
    <div>11. Multiplexing Fundamentals: FDM, Synchronous TDM, Statistical TDM & WDM</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Network Topologies & Layered Architectures</h2>
<p>
  A <strong>Computer Network</strong> is an interconnected collection of autonomous computing devices capable of exchanging data frames and packets through transmission channels.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">OSI Layer</th>
      <th style="width: 22%;">Protocol Data Unit (PDU)</th>
      <th style="width: 35%;">Core Responsibilities & Header Additions</th>
      <th>Standard Protocols & Hardware</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>7. Application</strong></td>
      <td>Message / Data</td>
      <td>Network virtual terminal, file transfer, directory services, user interface.</td>
      <td>HTTP, HTTPS, DNS, SMTP, FTP, SSH</td>
    </tr>
    <tr>
      <td><strong>6. Presentation</strong></td>
      <td>Data</td>
      <td>Data encryption/decryption (TLS), data compression (gzip), syntax translation (ASCII, UTF-8).</td>
      <td>TLS 1.3, JPEG, MPEG, ASN.1</td>
    </tr>
    <tr>
      <td><strong>5. Session</strong></td>
      <td>Data</td>
      <td>Dialog control, token management, session synchronization checkpoints.</td>
      <td>RPC, NetBIOS, PPTP, Sockets</td>
    </tr>
    <tr>
      <td><strong>4. Transport</strong></td>
      <td>Segment (TCP) / Datagram (UDP)</td>
      <td>End-to-end process-to-process delivery, port addressing, flow control, segment reassembly.</td>
      <td>TCP, UDP, SCTP, QUIC</td>
    </tr>
    <tr>
      <td><strong>3. Network</strong></td>
      <td>Packet / Datagram</td>
      <td>Host-to-host logical addressing (IPv4/IPv6), packet routing, fragmentation, congestion control.</td>
      <td>IP, ICMP, OSPF, BGP (Routers)</td>
    </tr>
    <tr>
      <td><strong>2. Data Link</strong></td>
      <td>Frame</td>
      <td>Hop-to-hop node delivery, physical MAC addressing, framing, CRC error detection, MAC access.</td>
      <td>Ethernet (802.3), Wi-Fi (802.11), PPP (Switches)</td>
    </tr>
    <tr>
      <td><strong>1. Physical</strong></td>
      <td>Raw Bits (`0`/`1`)</td>
      <td>Transmission of uninterpreted bit streams over physical media, signal encoding, baud rates.</td>
      <td>Manchester, NRZ, RS-232, RJ-45 (Hubs, Cables)</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 4 – 6: Channel Capacity Theorems & Decibel Formulations</h2>

<div class="formula-card">
  <strong>1. Nyquist Bit Rate Formula (For Noiseless Channels):</strong>
  $$\text{BitRate}_{\max} = 2 \times B \times \log_2(M) \quad \text{bps}$$
  Where $B$ is the analog bandwidth in Hertz ($\text{Hz}$), and $M$ is the number of distinct signal voltage levels.
</div>

<div class="formula-card">
  <strong>2. Shannon Channel Capacity Theorem (For Noisy Gaussian Channels):</strong>
  $$C = B \times \log_2 \left(1 + \text{SNR}\right) \quad \text{bps}$$
  Where $B$ is the bandwidth ($\text{Hz}$), and $\text{SNR} = \frac{\text{Signal Power}}{\text{Noise Power}}$ is the linear Signal-to-Noise Ratio.<br>
  $$\text{SNR}_{\text{dB}} = 10 \log_{10}(\text{SNR}) \implies \text{SNR} = 10^{\frac{\text{SNR}_{\text{dB}}}{10}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Shannon & Nyquist Capacity Calculation</div>
  <p><strong>Problem:</strong> A telephone line has a bandwidth of $3000\text{ Hz}$ and an $\text{SNR}_{\text{dB}} = 30\text{ dB}$.</p>
  <ol>
    <li>
      <strong>Step 1: Compute Linear $\text{SNR}$ from $\text{dB}$:</strong>
      $$\text{SNR} = 10^{\frac{30}{10}} = 10^3 = \mathbf{1000}$$
    </li>
    <li>
      <strong>Step 2: Apply Shannon's Capacity Formula:</strong>
      $$C = 3000 \times \log_2(1 + 1000) = 3000 \times \log_2(1001) \approx 3000 \times 9.967 = \mathbf{29,901} \text{ bps} \ (\approx 30 \text{ kbps})$$
    </li>
    <li>
      <strong>Step 3: Find Number of Signal Levels $M$ Required by Nyquist to achieve $C$:</strong>
      $$29901 = 2 \times 3000 \times \log_2(M) \implies \log_2(M) = \frac{29901}{6000} \approx 4.9835 \implies M = 2^{4.9835} \approx \mathbf{32} \text{ levels}$$
    </li>
  </ol>
</div>

<h2 class="section-title">Topic 7 & 8: Digital Signal Line Coding Schemes</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Line Coding Scheme</th>
      <th style="width: 45%;">Voltage Transition Rule</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. NRZ-L (Level)</strong></td>
      <td>Bit `0` $\rightarrow$ Positive Voltage ($+V$), Bit `1` $\rightarrow$ Negative Voltage ($-V$).</td>
      <td>Simple; suffers from DC component and baseline wander on long strings of `0`s or `1`s.</td>
    </tr>
    <tr>
      <td><strong>2. NRZ-I (Invert)</strong></td>
      <td>Bit `1` $\rightarrow$ Transition at start of bit interval; Bit `0` $\rightarrow$ No transition.</td>
      <td>Self-clocking for `1`s; still loses clock synchronization on continuous strings of `0`s.</td>
    </tr>
    <tr>
      <td><strong>3. Manchester (IEEE 802.3)</strong></td>
      <td>Bit `0` $\rightarrow$ High-to-Low transition at bit center; Bit `1` $\rightarrow$ Low-to-High transition at center.</td>
      <td>Zero DC component, 100% self-clocking; requires $2 \times$ bandwidth ($B = 2 \times \text{data rate}$).</td>
    </tr>
    <tr>
      <td><strong>4. Differential Manchester</strong></td>
      <td>Always transitions at center. Bit `0` $\rightarrow$ Transition at start; Bit `1` $\rightarrow$ No transition at start.</td>
      <td>Highly immune to wire polarity reversal; used in Token Ring LANs (IEEE 802.5).</td>
    </tr>
    <tr>
      <td><strong>5. AMI (Alternate Mark Inversion)</strong></td>
      <td>Bit `0` $\rightarrow$ Zero Voltage ($0V$); Bit `1` $\rightarrow$ Alternating $+V$ and $-V$.</td>
      <td>Zero DC component; long runs of `0`s lose synchronization (resolved by B8ZS/HDB3 scrambling).</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module I)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. State the difference between OSI and TCP/IP reference models across 5 engineering parameters. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Layer Count:</strong> OSI has 7 layers (Session & Presentation separate); TCP/IP has 4 or 5 layers (combines Session, Presentation, Application).<br>
    2. <strong>Model Origins:</strong> OSI is a theoretical conceptual standard developed by ISO before protocols were written; TCP/IP was designed pragmatically alongside the ARPANET implementation.<br>
    3. <strong>Service Orientation:</strong> OSI strictly separates Service, Interface, and Protocol; TCP/IP merges services into protocols directly.<br>
    4. <strong>Network Layer Communication:</strong> OSI supports both Connection-Oriented and Connectionless at Network layer; TCP/IP supports only Connectionless (IP) at Network layer.<br>
    5. <strong>Transport Layer Communication:</strong> OSI supports only Connection-Oriented at Transport; TCP/IP supports both Connection-Oriented (TCP) and Connectionless (UDP).
  </div>
</div>
"""
