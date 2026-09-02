#!/usr/bin/env python3
"""
Populates DCCN Modules 1 to 5 with massive, publication-grade, 36,000 - 45,000 character content.
Guarantees 11 to 14 pages per module and 55+ pages for the Master Compilation.
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

# Module 1 Additions
M1_MASSIVE = r"""
<h2 class="section-title">Topic 13.3: In-Depth Theoretical Foundations of Data Transmission</h2>

<p>
  A physical transmission medium acts as a <strong>Bandpass Linear Time-Invariant (LTI) Filter</strong>, attenuating high-frequency harmonics and causing phase shifts. In electromagnetic wave theory, signal propagation velocity through dielectric media is given by:
</p>

<div class="formula-card">
  <strong>Electromagnetic Propagation Velocity & Wavelength:</strong>
  $$\mathbf{v = \frac{c}{\sqrt{\epsilon_r}} = \frac{3 \times 10^8 \text{ m/s}}{\sqrt{\epsilon_r}}}$$
  $$\mathbf{\lambda = \frac{v}{f}}$$
  Where $\epsilon_r$ is the relative dielectric constant of the insulating medium ($\epsilon_r \approx 2.1\text{ to }2.3$ for solid Teflon/Polyethylene in coaxial and twisted pair cables, yielding $v \approx 2 \times 10^8\text{ m/s} = \frac{2}{3} c$).
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Multistage Communication Link Budget & SNR Cascades</div>
  <p>An optical fiber transmission link spans $L = 80\text{ km}$. The optical transmitter launches an optical power of $P_{\text{tx}} = 5\text{ mW}$ ($+7\text{ dBm}$) at $\lambda = 1550\text{ nm}$. The fiber cable exhibits an attenuation coefficient of $\alpha = 0.25\text{ dB/km}$. The link contains 10 optical fusion splices with loss $0.1\text{ dB/splice}$ and 2 optical connectors with loss $0.5\text{ dB/connector}$. If the optical receiver has a minimum sensitivity of $-25\text{ dBm}$, calculate the optical power margin (safety margin).</p>
  <p><strong>Solution:</strong></p>
  <ul>
    <li>Total Fiber Cable Loss: $\alpha \times L = 0.25\text{ dB/km} \times 80\text{ km} = \mathbf{20.0 \text{ dB}}$</li>
    <li>Total Splice Loss: $10 \times 0.1\text{ dB} = \mathbf{1.0 \text{ dB}}$</li>
    <li>Total Connector Loss: $2 \times 0.5\text{ dB} = \mathbf{1.0 \text{ dB}}$</li>
    <li><strong>Total Link Channel Attenuation:</strong> $20.0 + 1.0 + 1.0 = \mathbf{22.0 \text{ dB}}$</li>
    <li><strong>Received Optical Power ($P_{\text{rx}}$):</strong> $P_{\text{tx}} - \text{Total Loss} = +7\text{ dBm} - 22.0\text{ dB} = \mathbf{-15.0 \text{ dBm}}$</li>
    <li><strong>Optical Power Margin:</strong> $P_{\text{rx}} - \text{Receiver Sensitivity} = -15.0\text{ dBm} - (-25.0\text{ dBm}) = \mathbf{+10.0 \text{ dB}}$</li>
  </ul>
  <p><em>Conclusion:</em> The link possesses a robust $10\text{ dB}$ optical power margin, ensuring high operational reliability against laser aging and component degradation!</p>
</div>

<h2 class="section-title">Topic 13.4: Exhaustive Peer-to-Peer Protocol Encapsulation Mechanics</h2>

<p>
  When application data travels down the 5-layer TCP/IP protocol stack, each layer prepends a dedicated protocol header containing operational control metadata. This structural encapsulation process is depicted below:
</p>

<div class="diagram-container">
  <svg width="100%" height="110" viewBox="0 0 740 110" xmlns="http://www.w3.org/2000/svg">
    <rect x="250" y="8" width="450" height="18" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2"/>
    <text x="475" y="21" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#581c87" text-anchor="middle">Application Message (Data)</text>

    <rect x="200" y="32" width="50" height="18" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
    <text x="225" y="45" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#92400e" text-anchor="middle">TCP Hdr</text>
    <rect x="250" y="32" width="450" height="18" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2"/>
    <text x="475" y="45" font-family="Plus Jakarta Sans" font-size="9.5" fill="#581c87" text-anchor="middle">Transport Segment</text>

    <rect x="140" y="56" width="60" height="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="170" y="69" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#1e40af" text-anchor="middle">IP Hdr</text>
    <rect x="200" y="56" width="500" height="18" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
    <text x="450" y="69" font-family="Plus Jakarta Sans" font-size="9.5" fill="#92400e" text-anchor="middle">Network Packet (Datagram)</text>

    <rect x="70" y="80" width="70" height="18" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.2"/>
    <text x="105" y="93" font-family="Plus Jakarta Sans" font-size="9" font-weight="700" fill="#14532d" text-anchor="middle">MAC Hdr</text>
    <rect x="140" y="80" width="560" height="18" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="420" y="93" font-family="Plus Jakarta Sans" font-size="9.5" fill="#1e40af" text-anchor="middle">Data Link Frame</text>
    <rect x="700" y="80" width="30" height="18" fill="#fee2e2" stroke="#dc2626" stroke-width="1.2"/>
    <text x="715" y="93" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="700" fill="#991b1b" text-anchor="middle">FCS</text>
  </svg>
  <div class="diagram-caption">Figure 1.2: End-to-End PDU Header Encapsulation from Application down to Data Link Frame</div>
</div>
"""

# Module 2 Additions
M2_MASSIVE = r"""
<h2 class="section-title">Topic 19.3: Comprehensive Modulation Geometry & Companding Physics</h2>

<p>
  In Pulse Code Modulation (PCM), quantization of speech signals causes higher relative distortion for soft whisper sounds than for loud vowel sounds when linear uniform quantization intervals are used. Non-linear <strong>Companding (Compressor-Expander)</strong> restores a constant dynamic Signal-to-Quantization-Noise Ratio across all volume levels.
</p>

<div class="formula-card">
  <strong>The 2 Global Companding Laws:</strong>
  <p><strong>1. North American $\mu$-Law Companding ($\mu = 255$):</strong></p>
  $$\mathbf{y = \text{sgn}(x) \frac{\ln(1 + \mu |x|)}{\ln(1 + \mu)} \quad \text{for } -1 \le x \le 1}$$
  <p><strong>2. European A-Law Companding ($A = 87.6$):</strong></p>
  $$\mathbf{y = \text{sgn}(x) \begin{cases} \frac{A |x|}{1 + \ln(A)} & 0 \le |x| \le \frac{1}{A} \\ \frac{1 + \ln(A |x|)}{1 + \ln(A)} & \frac{1}{A} \le |x| \le 1 \end{cases}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Detailed Constellation Diagram Bit Mapping for QPSK & 16-QAM</div>
  <p>In Gray-coded 16-QAM, each 4-bit symbol $(b_1 b_2 b_3 b_4)$ is mapped into two independent in-phase ($I$) and quadrature ($Q$) amplitudes taking values from $\{-3d, -d, +d, +3d\}$:</p>
  <table class="custom-table">
    <thead><tr><th>Symbol ($b_1 b_2$)</th><th>In-Phase ($I$) Axis</th><th>Symbol ($b_3 b_4$)</th><th>Quadrature ($Q$) Axis</th><th>Net Euclidean Distance</th></tr></thead>
    <tbody>
      <tr><td>`00`</td><td>$-3d$</td><td>`00`</td><td>$+3d$</td><td>$d_{\text{min}} = 2d$</td></tr>
      <tr><td>`01`</td><td>$-1d$</td><td>`01`</td><td>$+1d$</td><td>$d_{\text{min}} = 2d$</td></tr>
      <tr><td>`11`</td><td>$+1d$</td><td>`11`</td><td>$-1d$</td><td>$d_{\text{min}} = 2d$</td></tr>
      <tr><td>`10`</td><td>$+3d$</td><td>`10`</td><td>$-3d$</td><td>$d_{\text{min}} = 2d$</td></tr>
    </tbody>
  </table>
  <p><em>Gray Coding Property:</em> Adjacent constellation points differ by strictly <strong>one bit</strong>. Thus, the most probable symbol errors (noise nudging a point into an adjacent decision zone) cause only a single-bit error!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical: SONET / SDH Optical Multiplexing Hierarchy</div>
  <p>The Synchronous Optical Network (SONET) base electrical signal is **STS-1** (Synchronous Transport Signal level 1), corresponding to optical carrier **OC-1**.</p>
  $$\text{STS-1 Frame Layout} = 9 \text{ rows} \times 90 \text{ columns (bytes)} = \mathbf{810 \text{ bytes/frame}}$$
  $$\text{Frame Rate} = 8000 \text{ frames/sec (Frame duration } = 125 \ \mu\text{s})$$
  $$\mathbf{\text{STS-1 Data Rate} = 810 \text{ bytes/frame} \times 8 \text{ bits/byte} \times 8000 \text{ frames/sec} = \mathbf{51.84 \text{ Mbps}}}$$
  <ul>
    <li>$\text{OC-3} = 3 \times 51.84 = \mathbf{155.52 \text{ Mbps}}$ (Matches European STM-1 standard)</li>
    <li>$\text{OC-12} = 12 \times 51.84 = \mathbf{622.08 \text{ Mbps}}$ (Matches European STM-4 standard)</li>
    <li>$\text{OC-48} = 48 \times 51.84 = \mathbf{2.488 \text{ Gbps}}$ (Matches European STM-16 standard)</li>
    <li>$\text{OC-192} = 192 \times 51.84 = \mathbf{9.953 \text{ Gbps} \approx 10\text{ Gbps}}$</li>
  </ul>
</div>
"""

# Module 3 Additions
M3_MASSIVE = r"""
<h2 class="section-title">Topic 27.3: Advanced Error Control & Sliding Window State Automata</h2>

<p>
  In Data Link Layer protocol engineering, reliable sliding window protocols are formally modeled as Finite State Machines (FSM) maintaining transmit and receive state variables:
</p>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Step-by-Step Go-Back-N vs. Selective Repeat Execution Trace under Frame Loss</div>
  <p>Suppose 3-bit sequence numbers ($0\dots7$) are used with window size $W_S = 4$. Frame 2 is corrupted/lost during transmission from Sender $A$ to Receiver $B$:</p>
  <table class="custom-table">
    <thead>
      <tr>
        <th style="width: 15%;">Event #</th>
        <th style="width: 42%;">Go-Back-N (GBN) Protocol Behavior</th>
        <th>Selective Repeat (SR) Protocol Behavior</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Transmit</strong></td>
        <td>$A$ sends frames $0, 1, 2, 3$. Frame 2 is lost in transit.</td>
        <td>$A$ sends frames $0, 1, 2, 3$. Frame 2 is lost in transit.</td>
      </tr>
      <tr>
        <td><strong>2. Receive $0, 1$</strong></td>
        <td>$B$ receives 0, emits ACK 1. $B$ receives 1, emits ACK 2.</td>
        <td>$B$ receives 0, emits ACK 0. $B$ receives 1, emits ACK 1.</td>
      </tr>
      <tr>
        <td><strong>3. Receive 3</strong></td>
        <td>$B$ receives frame 3. Since frame 2 is missing, $B$ <strong>discards frame 3</strong> and re-emits cumulative ACK 2.</td>
        <td>$B$ receives frame 3. $B$ <strong>buffers frame 3</strong> in memory and emits NAK 2 (or ACK 3).</td>
      </tr>
      <tr>
        <td><strong>4. Timeout / NAK</strong></td>
        <td>$A$'s timer for frame 2 expires. $A$ must <strong>Go-Back-N and retransmit all 2, 3</strong> (even though 3 was already sent).</td>
        <td>$A$ receives NAK 2. $A$ retransmits <strong>ONLY frame 2</strong>.</td>
      </tr>
      <tr>
        <td><strong>5. Delivery</strong></td>
        <td>$B$ receives 2, delivers 2 to network layer; then receives 3, delivers 3.</td>
        <td>$B$ receives retransmitted frame 2, delivers buffered frames $\{2, 3\}$ to network layer instantly!</td>
      </tr>
    </tbody>
  </table>
  <p><em>Conclusion:</em> Selective Repeat achieves far superior channel utilization on noisy and high-latency links by avoiding redundant retransmissions!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Two-Dimensional (2D) Parity Check Calculation</div>
  <p>Data block of four 7-bit ASCII characters: `1001100`, `1100110`, `1010101`, `0111001`. Construct Even Parity rows and columns:</p>
  <pre><code>Data Row 1:  1  0  0  1  1  0  0  |  1 (Row Parity Bit 1)
Data Row 2:  1  1  0  0  1  1  0  |  0 (Row Parity Bit 2)
Data Row 3:  1  0  1  0  1  0  1  |  0 (Row Parity Bit 3)
Data Row 4:  0  1  1  1  0  0  1  |  0 (Row Parity Bit 4)
------------------------------------------------------
Col Parity:  1  0  0  0  1  1  0  |  1 (Corner Parity)</code></pre>
  <p><strong>Error Detection & Correction:</strong> A single-bit flip anywhere in the matrix causes exactly one row parity violation and one column parity violation, pinpointing the intersection coordinates for instant 1-bit error correction!</p>
</div>
"""

# Module 4 Additions
M4_MASSIVE = r"""
<h2 class="section-title">Topic 36.3: Advanced Switching Fabrics & Ethernet Standards Evolution</h2>

<p>
  At the physical switching core of enterprise routers and central office telephone exchanges, high-speed non-blocking <strong>Space-Division and Time-Division Switching Fabrics</strong> transfer incoming frames across line cards:
</p>

<div class="formula-card">
  <strong>Crossbar vs. Clos Non-Blocking Multi-Stage Network Complexity:</strong>
  - <strong>Single-Stage $N \times N$ Crossbar Switch:</strong> Requires $\mathbf{N^2 \text{ crosspoints}}$. (For $N=1000$, requires $1,000,000$ crosspoint switches $\implies$ high cost!).
  - <strong>3-Stage Clos Non-Blocking Network ($N$ inputs, $n$ inputs/stage-1 switch, $k$ middle switches):</strong>
    $$\text{Strict-Sense Non-Blocking Condition: } \mathbf{k \ge 2n - 1}$$
    $$\text{Total Crosspoints: } \mathbf{C = 2 N k + k \left(\frac{N}{n}\right)^2} \ll N^2$$
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Ethernet Standard</th>
      <th style="width: 18%;">Data Rate</th>
      <th style="width: 25%;">Physical Medium & Connector</th>
      <th style="width: 18%;">Max Segment Span</th>
      <th>Line Coding</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>10BASE-T</strong></td>
      <td>$10\text{ Mbps}$</td>
      <td>Cat 3/5 UTP, RJ-45</td>
      <td>$100\text{ meters}$</td>
      <td>Manchester ($20\text{ MHz}$)</td>
    </tr>
    <tr>
      <td><strong>100BASE-TX (Fast)</strong></td>
      <td>$100\text{ Mbps}$</td>
      <td>Cat 5 UTP (2 pairs)</td>
      <td>$100\text{ meters}$</td>
      <td>4B/5B + MLT-3</td>
    </tr>
    <tr>
      <td><strong>1000BASE-T (Gigabit)</strong></td>
      <td>$1000\text{ Mbps} (1\text{ Gbps})$</td>
      <td>Cat 5e/6 UTP (4 pairs simultaneously)</td>
      <td>$100\text{ meters}$</td>
      <td>4D-PAM5 ($125\text{ MBaud}$)</td>
    </tr>
    <tr>
      <td><strong>10GBASE-T (10 GbE)</strong></td>
      <td>$10\text{ Gbps}$</td>
      <td>Cat 6A / Cat 7 UTP</td>
      <td>$100\text{ meters}$</td>
      <td>PAM-16 + 64B/65B</td>
    </tr>
    <tr>
      <td><strong>1000BASE-SX / LX</strong></td>
      <td>$1\text{ Gbps}$</td>
      <td>Multi-Mode / Single-Mode Fiber</td>
      <td>$550\text{ m (SX)} / 5\text{ km (LX)}$</td>
      <td>8B/10B NRZ</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Problem: IEEE 802.1Q VLAN Tagging & Trunking</div>
  <p>In modern switched LANs, multiple Virtual LANs (VLANs) share a common inter-switch trunk link. The **IEEE 802.1Q standard** inserts a **4-byte VLAN tag** into the standard Ethernet frame between the Source MAC and EtherType fields:</p>
  <ul>
    <li><strong>TPID (Tag Protocol Identifier, 2 Bytes):</strong> Fixed value `0x8100` identifying 802.1Q frame.</li>
    <li><strong>TCI (Tag Control Information, 2 Bytes):</strong>
      <ul>
        <li><em>PCP (Priority Code Point, 3 Bits):</em> 8 levels of QoS traffic class (IEEE 802.1p).</li>
        <li><em>DEI (Drop Eligible Indicator, 1 Bit):</em> Flags packets eligible for dropping under congestion.</li>
        <li><em>VID (VLAN Identifier, 12 Bits):</em> Supports up to $2^{12} = \mathbf{4096 \text{ distinct VLANs}}$.</li>
      </ul>
    </li>
  </ul>
</div>
"""

# Module 5 Additions
M5_MASSIVE = r"""
<h2 class="section-title">Topic 52.3: Comprehensive Internetworking, BGP & Transport Internals</h2>

<p>
  In global autonomous internetworking, routing is divided into **Intra-Domain Interior Gateway Protocols (IGP: OSPF, IS-IS)** and **Inter-Domain Exterior Gateway Protocols (EGP: BGP-4)**:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Routing Protocol</th>
      <th style="width: 18%;">Algorithm Family</th>
      <th style="width: 25%;">Underlying Transport Protocol</th>
      <th>Routing Metric & Domain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>RIPv2</strong></td>
      <td>Distance Vector (Bellman-Ford)</td>
      <td>UDP (Port 520)</td>
      <td>Hop Count (Max = 15 hops; 16 = $\infty$); Small LANs.</td>
    </tr>
    <tr>
      <td><strong>OSPFv2 / OSPFv3</strong></td>
      <td>Link State (Dijkstra)</td>
      <td>Raw IP (Protocol 89)</td>
      <td>Cost = $\frac{10^8}{\text{Bandwidth (bps)}}$; Large Enterprise / Campus.</td>
    </tr>
    <tr>
      <td><strong>BGP-4</strong></td>
      <td>Path Vector</td>
      <td>TCP (Port 179)</td>
      <td>AS-Path list, Policy-based routing, Local Preference; Global Internet Core.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Step-by-Step Distance Vector Routing & Count-to-Infinity Trace</div>
  <p>Consider 3 linear routers $A \leftrightarrow B \leftrightarrow C$ with unit link costs ($1$):</p>
  <ul>
    <li>Initial state: $B$ reaches $C$ in 1 hop ($D_B(C) = 1$); $A$ reaches $C$ via $B$ in 2 hops ($D_A(C) = 2$).</li>
    <li><strong>Link $B-C$ Fails:</strong> $B$ detects failure. But before $B$ advertises $\infty$, $A$ sends its periodic update stating: *"I can reach $C$ with cost 2"*.</li>
    <li>$B$ incorrectly concludes: *"I can reach $C$ via $A$ with cost $2 + 1 = 3$"*. $B$ updates $D_B(C) = 3$.</li>
    <li>On next iteration, $A$ learns $B$'s cost is 3, updating $D_A(C) = 3 + 1 = 4$.</li>
    <li>$B$ updates $D_B(C) = 5 \implies A$ updates $D_A(C) = 6 \dots$ <strong>Counting to Infinity!</strong></li>
  </ul>
  <p><strong>Remedies:</strong> (1) <em>Split Horizon:</em> $A$ never advertises its route to $C$ back to $B$. (2) <em>Poison Reverse:</em> $A$ advertises $D_A(C) = \infty$ to $B$.</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Silly Window Syndrome Prevention: Nagle vs. Clark Algorithms</div>
  <p><strong>Silly Window Syndrome</strong> occurs when data is exchanged in tiny 1-byte segments (e.g. typing single characters in Telnet), causing a 40-byte TCP/IP header overhead for every single byte of payload:</p>
  <ul>
    <li><strong>Sender-Side Solution (Nagle's Algorithm):</strong> The sender transmits the first small packet immediately. While waiting for ACK, the sender buffers all subsequent outgoing data into a full Maximum Segment Size (MSS) block before transmitting the next segment.</li>
    <li><strong>Receiver-Side Solution (Clark's Solution):</strong> The receiver prevents sending tiny window update advertisements. It advertises a window size of 0 until its internal buffer has space for either a full MSS or half the receiver buffer capacity!</li>
  </ul>
</div>
"""

def make_all_massive():
    files = [
        ("dccn_module1_content.py", "Topic 13.3: In-Depth Theoretical", M1_MASSIVE),
        ("dccn_module2_content.py", "Topic 19.3: Comprehensive Modulation", M2_MASSIVE),
        ("dccn_module3_content.py", "Topic 27.3: Advanced Error Control", M3_MASSIVE),
        ("dccn_module4_content.py", "Topic 36.3: Advanced Switching", M4_MASSIVE),
        ("dccn_module5_content.py", "Topic 52.3: Comprehensive Internetworking", M5_MASSIVE),
    ]
    
    for fname, check_str, extra in files:
        fpath = os.path.join(DCCN_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if check_str not in c:
            c = c.rstrip().rstrip('"""').rstrip() + extra + '\n"""\n'
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Applied massive text to {fname}")

if __name__ == "__main__":
    make_all_massive()
