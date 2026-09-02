# DCCN Module 1 Exhaustive Content (13 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DCCN_M1_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module I: Data Communication & Networking Overview — Complete 13-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 1:</strong> Communication Model (Sender, Message, Medium, Protocol)</div>
    <div><strong>Topic 2:</strong> Data Communications (Simplex, Half-Duplex, Full-Duplex)</div>
    <div><strong>Topic 3:</strong> Networks (PAN, LAN, MAN, WAN Taxonomies)</div>
    <div><strong>Topic 4:</strong> The Internet (Packet Switching & TCP/IP Suite)</div>
    <div><strong>Topic 5:</strong> OSI 7-Layer Reference Model & Layer Functions</div>
    <div><strong>Topic 6:</strong> TCP/IP 4-Layer Protocol Architecture (OSI vs. TCP/IP)</div>
    <div><strong>Topic 7:</strong> Standards & Protocol Layers (Modularity & Encapsulation)</div>
    <div><strong>Topic 8:</strong> Internet Applications (HTTP, SMTP, DNS, FTP, DHCP)</div>
    <div><strong>Topic 9:</strong> Data Transmission Concepts (Bit vs. Baud, Latency = Tt+Tp+Tq+Tpr)</div>
    <div><strong>Topic 10:</strong> Analog Data Transmission (Amplitude, Frequency, Phase)</div>
    <div><strong>Topic 11:</strong> Digital Data Transmission (Discrete Levels vs. Analog)</div>
    <div><strong>Topic 12:</strong> Transmission Impairments (Attenuation, Distortion, Noise)</div>
    <div><strong>Topic 13:</strong> Channel Capacity (Nyquist Noiseless vs. Shannon Noisy Capacity)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 & 2: Communication Model & Transmission Modes</h2>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="110" height="50" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="75" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Sender (Source)</text>
    <text x="75" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Generates Data</text>

    <path d="M 130 40 L 175 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="180" y="15" width="100" height="50" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="230" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Transmitter</text>
    <text x="230" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Encodes Signal</text>

    <path d="M 280 40 L 325 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="330" y="15" width="140" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="400" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#92400e" text-anchor="middle">Transmission Medium</text>
    <text x="400" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#b45309" text-anchor="middle">Guided / Unguided Path</text>

    <path d="M 470 40 L 515 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="520" y="15" width="95" height="50" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="567" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#14532d" text-anchor="middle">Receiver</text>
    <text x="567" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#16a34a" text-anchor="middle">Recovers Signal</text>

    <path d="M 615 40 L 640 40" stroke="#0284c7" stroke-width="2"/>

    <rect x="645" y="15" width="80" height="50" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="685" y="38" font-family="Plus Jakarta Sans" font-size="11" font-weight="700" fill="#1e40af" text-anchor="middle">Destination</text>
    <text x="685" y="52" font-family="Plus Jakarta Sans" font-size="9" fill="#2563eb" text-anchor="middle">Consumes</text>
  </svg>
  <div class="diagram-caption">Figure 1.1: Simplified Communication Model & Five Essential Components (S-M-M-P)</div>
</div>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Hook: S-M-M-P</div>
  <strong>S</strong>ender $\rightarrow$ <strong>M</strong>essage $\rightarrow$ <strong>M</strong>edium $\rightarrow$ <strong>P</strong>rotocol (Syntax, Semantics, Timing)
</div>

<h3 class="subsection-title">Data Transmission Modes [UPLOADED PYQ]:</h3>
<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Mode</th>
      <th style="width: 45%;">Directional Flow & Channel Mechanics</th>
      <th>Real-World Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Simplex</strong></td>
      <td>Unidirectional communication ($A \rightarrow B$). Only one device transmits; the other only receives. Channel capacity is 100% dedicated to one direction.</td>
      <td>Keyboard to CPU, Television/Radio broadcast.</td>
    </tr>
    <tr>
      <td><strong>2. Half-Duplex</strong></td>
      <td>Bidirectional communication ($A \rightarrow B$ or $A \leftarrow B$), but <strong>not simultaneously</strong>. Both can transmit, but must alternate turns.</td>
      <td>Walkie-Talkie systems.</td>
    </tr>
    <tr>
      <td><strong>3. Full-Duplex</strong></td>
      <td>Simultaneous bidirectional transmission ($A \rightleftarrows B$). Both stations can transmit and receive concurrently by dividing bandwidth.</td>
      <td>Telephone networks, modern switched Ethernet.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 3 & 4: Network Types & The Global Internet</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 15%;">Network</th>
      <th style="width: 25%;">Geographic Coverage</th>
      <th style="width: 30%;">Ownership & Speed</th>
      <th>Representative Example</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>PAN</strong></td><td>$\approx 10 \text{ meters}$</td><td>Private; moderate speed (Bluetooth / Zigbee).</td><td>Phone $\leftrightarrow$ Smartwatch $\leftrightarrow$ Earbuds</td></tr>
    <tr><td><strong>LAN</strong></td><td>Single room, office, or campus ($\le 1 \text{ km}$).</td><td>Privately owned; high data rate (1 Gbps–10 Gbps).</td><td>University campus / Lab LAN</td></tr>
    <tr><td><strong>MAN</strong></td><td>City or metropolitan area ($5\text{–}50 \text{ km}$).</td><td>Public/Private consortium; high speed.</td><td>Cable TV network across a city</td></tr>
    <tr><td><strong>WAN</strong></td><td>Country, continent, or global ($> 100 \text{ km}$).</td><td>Multiple telecom operators; variable speed.</td><td>The Global Internet</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 5 & 6: OSI 7-Layer Model vs. TCP/IP Architecture [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 15%;">OSI Layer</th>
      <th style="width: 18%;">TCP/IP Layer</th>
      <th style="width: 20%;">PDU Name</th>
      <th>Core Functional Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>7. Application</td><td rowspan="3"><strong>1. Application Layer</strong></td><td rowspan="3">Data / Message</td><td>Provides network services to user apps (HTTP, SMTP, DNS, FTP).</td></tr>
    <tr><td>6. Presentation</td><td>Syntax translation, data encryption/decryption (TLS), data compression.</td></tr>
    <tr><td>5. Session</td><td>Dialog control, session checkpointing, synchronization tokens.</td></tr>
    <tr><td>4. Transport</td><td><strong>2. Transport Layer</strong></td><td>Segment (TCP) / Datagram (UDP)</td><td>Process-to-process delivery, port addressing, flow control, reliability.</td></tr>
    <tr><td>3. Network</td><td><strong>3. Internet Layer</strong></td><td>Packet / Datagram</td><td>Host-to-host routing, logical IP addressing, packet forwarding (IP, ICMP).</td></tr>
    <tr><td>2. Data Link</td><td rowspan="2"><strong>4. Network Access Layer</strong></td><td>Frame</td><td>Hop-to-hop framing, physical MAC addressing, CRC error detection, MAC access.</td></tr>
    <tr><td>1. Physical</td><td>Raw Bits (`0`/`1`)</td><td>Raw bit transmission over physical media, voltage levels, connectors.</td></tr>
  </tbody>
</table>

<div class="callout callout-info">
  <div class="callout-title">🧠 Memory Trick for OSI 7 Layers</div>
  <strong>A</strong>ll <strong>P</strong>eople <strong>S</strong>eem <strong>T</strong>o <strong>N</strong>eed <strong>D</strong>ata <strong>P</strong>rocessing<br>
  (Application $\rightarrow$ Presentation $\rightarrow$ Session $\rightarrow$ Transport $\rightarrow$ Network $\rightarrow$ Data Link $\rightarrow$ Physical)
</div>

<h2 class="section-title">Topic 7 & 8: Standards, Encapsulation & Internet Applications</h2>
<p>
  <strong>Encapsulation</strong> occurs when data travels down the protocol stack at the sender: each layer prepends a protocol header containing control metadata:
</p>
$$\text{Data} \xrightarrow{\text{Transport}} \text{TCP Header} + \text{Data (Segment)} \xrightarrow{\text{Network}} \text{IP Header} + \text{Segment (Packet)} \xrightarrow{\text{Data Link}} \text{Frame Header} + \text{Packet} + \text{CRC Trailer (Frame)}$$

<h2 class="section-title">Topic 9 – 11: Data Transmission Concepts, Latency & Digital Signals</h2>

<div class="formula-card">
  <strong>1. Total End-to-End Latency Formula:</strong>
  $$\text{Latency} = T_{\text{trans}} + T_{\text{prop}} + T_{\text{proc}} + T_{\text{queue}}$$
  - <strong>Transmission Delay ($T_{\text{trans}}$):</strong> Time to push packet bits onto physical link: $T_{\text{trans}} = \frac{L \text{ (bits)}}{B \text{ (bps)}}$.
  - <strong>Propagation Delay ($T_{\text{prop}}$):</strong> Time for a bit to physically travel across distance: $T_{\text{prop}} = \frac{d \text{ (meters)}}{v \text{ (speed of light in medium)}}$.
  - <strong>Bit Rate vs. Baud Rate:</strong> $\text{Bit Rate} = \text{Baud Rate} \times \log_2(M) \text{ bps}$, where $M$ is number of distinct signal voltage levels.
</div>

<h2 class="section-title">Topic 12: Transmission Impairments [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Impairment</th>
      <th style="width: 45%;">Physical Mechanism & Impact</th>
      <th>Engineering Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Attenuation</strong></td>
      <td>Signal energy loss over distance due to medium resistance. Signal power drops logarithmically ($\text{dB}$).</td>
      <td>Periodic Amplifiers (analog) or Regenerative Repeaters (digital).</td>
    </tr>
    <tr>
      <td><strong>2. Distortion</strong></td>
      <td>Signal changes shape because different frequency harmonic components travel at different phase velocities.</td>
      <td>Equalizers and phase delay compensators.</td>
    </tr>
    <tr>
      <td><strong>3. Noise</strong></td>
      <td>Unwanted extraneous electrical signals injected into the channel:
          • <em>Thermal Noise:</em> Agitation of electrons ($N = kTB$).
          • <em>Crosstalk:</em> Electromagnetic coupling between adjacent wire pairs.
          • <em>Impulse Noise:</em> Spikes from lightning, power lines.</td>
      <td>Shielding (STP/Coax), differential twisted pairs, optical fiber.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 13: Channel Capacity Theorems [UPLOADED PYQ]</h2>

<div class="formula-card">
  <strong>1. Nyquist Bit Rate (For Noiseless Channels):</strong>
  $$C = 2 \times B \times \log_2(L) \quad \text{bps}$$
  Where $B$ is channel bandwidth in Hertz ($\text{Hz}$) and $L$ is number of discrete signal voltage levels.
</div>

<div class="formula-card">
  <strong>2. Shannon Channel Capacity (For Noisy Channels with Thermal Noise):</strong>
  $$C = B \times \log_2(1 + \text{SNR}) \quad \text{bps}$$
  Where $\text{SNR} = 10^{\frac{\text{SNR}_{\text{dB}}}{10}}$ is the linear Signal-to-Noise Ratio.
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ [UPLOADED PYQ] Numerical: Shannon Capacity for Bandwidth $4\text{ kHz}$ and $\text{SNR}_{\text{dB}} = 24\text{ dB}$</div>
  <ol>
    <li>Linear $\text{SNR} = 10^{\frac{24}{10}} = 10^{2.4} \approx \mathbf{251.19}$.</li>
    <li>$C = 4000 \times \log_2(1 + 251.19) = 4000 \times \log_2(252.19) \approx 4000 \times 7.978 = \mathbf{31,913} \text{ bps} \ (\approx 32 \text{ kbps})$.</li>
  </ol>
</div>

<h2 class="section-title">🧠 M1 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Compare OSI and TCP/IP models across 5 engineering parameters. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Layer Count:</strong> OSI has 7 layers; TCP/IP has 4 (or 5) layers.<br>
    2. <strong>Origins:</strong> OSI was designed by ISO as a formal conceptual reference model before protocols were written; TCP/IP was designed pragmatically around actual working protocols (ARPANET).<br>
    3. <strong>Services vs Protocols:</strong> OSI strictly separates Services, Interfaces, and Protocols; TCP/IP combines services into protocols directly.<br>
    4. <strong>Network Layer Communication:</strong> OSI supports both Connectionless and Connection-Oriented at Network layer; TCP/IP supports only Connectionless (IP).<br>
    5. <strong>Transport Layer Communication:</strong> OSI supports only Connection-Oriented; TCP/IP supports both Connection-Oriented (TCP) and Connectionless (UDP).
  </div>
</div>
"""
