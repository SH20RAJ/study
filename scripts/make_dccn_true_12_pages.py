#!/usr/bin/env python3
"""
True 12-Page Booster for DCCN (CS24305).
Injects deep, textbook-grade content into all 5 DCCN modules to ensure
every single module is solidly 38,000 - 45,000 characters and generates 11 to 14 pages!
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

# Module 1 Super Text
M1_ULTRA = r"""
<h2 class="section-title">Topic 13.6: Deep Layer-by-Layer Architectural Analysis & Standards Frameworks</h2>

<p>
  International network standards guarantee interoperability across heterogeneous hardware vendors, operating systems, and physical transmission media. The global standards architecture is governed by four preeminent bodies:
</p>
<ol>
  <li><strong>International Organization for Standardization (ISO):</strong> Promulgated the 7-layer Open Systems Interconnection (OSI) Basic Reference Model (ISO/IEC 7498-1).</li>
  <li><strong>Institute of Electrical and Electronics Engineers (IEEE):</strong> Governs physical and data link standards via the <strong>IEEE 802 LAN/MAN Standards Committee</strong> (802.1 Bridging & Architecture, 802.3 Ethernet, 802.11 Wireless LAN Wi-Fi, 802.15 Wireless PAN Bluetooth/Zigbee).</li>
  <li><strong>International Telecommunication Union (ITU-T):</strong> Promulgates global telecommunication recommendations (V-series for modem modulation, X-series for data networks like X.25, G-series for optical transmission like G.709 OTN).</li>
  <li><strong>Internet Engineering Task Force (IETF):</strong> Publishes <strong>Requests for Comments (RFCs)</strong> defining Internet protocols (RFC 791 IPv4, RFC 793 TCP, RFC 2616 HTTP/1.1, RFC 8200 IPv6).</li>
</ol>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 15%;">OSI Layer</th>
      <th style="width: 25%;">Primary Protocol Data Unit (PDU)</th>
      <th style="width: 30%;">Key Standards & Hardware Devices</th>
      <th>Security Mechanisms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Layer 7: Application</strong></td>
      <td>User Message / Stream Data</td>
      <td>HTTP/3, DNS, SMTP, SSH; Gateways, Application Load Balancers.</td>
      <td>Application-layer auth, OAuth2, PGP Email encryption.</td>
    </tr>
    <tr>
      <td><strong>Layer 6: Presentation</strong></td>
      <td>Formatted / Encoded Data</td>
      <td>ASCII, UTF-8, ASN.1, MIME, JPEG, MPEG.</td>
      <td>SSL / TLS 1.3 cryptographic record layer.</td>
    </tr>
    <tr>
      <td><strong>Layer 5: Session</strong></td>
      <td>Synchronized Dialogue Data</td>
      <td>RPC, NetBIOS, PPTP, ISO 8327 / ITU-T X.225.</td>
      <td>Session tokens, Mutual SSL handshake validation.</td>
    </tr>
    <tr>
      <td><strong>Layer 4: Transport</strong></td>
      <td>TCP Segment / UDP Datagram</td>
      <td>TCP (RFC 793), UDP (RFC 768), SCTP, QUIC; Layer 4 Firewalls.</td>
      <td>TLS transport encapsulation, TCP SYN cookies.</td>
    </tr>
    <tr>
      <td><strong>Layer 3: Network</strong></td>
      <td>IP Datagram (Packet)</td>
      <td>IPv4, IPv6, ICMP, ARP, OSPF, BGP; Layer 3 Routers.</td>
      <td>IPsec (AH / ESP), Access Control Lists (ACLs).</td>
    </tr>
    <tr>
      <td><strong>Layer 2: Data Link</strong></td>
      <td>Network Frame</td>
      <td>IEEE 802.3 Ethernet, IEEE 802.11 Wi-Fi, PPP, HDLC; Layer 2 Switches, Bridges.</td>
      <td>WPA3 Wi-Fi encryption, IEEE 802.1AE MACsec, Port Security.</td>
    </tr>
    <tr>
      <td><strong>Layer 1: Physical</strong></td>
      <td>Raw Binary Bitstream</td>
      <td>Cat 6A UTP, Single-Mode Fiber, RS-232, 1000BASE-T; Repeaters, Hubs, Modems.</td>
      <td>Physical conduit shielding, tamper-detection alarms.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 6: End-to-End Packet Delay Calculation (Transmission, Propagation, Queuing, Processing)</div>
  <p>A host transmits a packet of size $L = 1500\text{ bytes}$ across a path of $N = 4$ identical communication links. Each link has a transmission bandwidth of $R = 10\text{ Mbps}$, a physical length of $D = 250\text{ km}$, and propagation speed $v = 2 \times 10^8\text{ m/s}$. Each intermediate router introduces an average processing delay of $d_{\text{proc}} = 10 \ \mu\text{s}$ and queuing delay of $d_{\text{queue}} = 40 \ \mu\text{s}$. Calculate the total end-to-end latency from source to destination.</p>
  <p><strong>Solution:</strong> Total Latency $T_{\text{total}} = N \times (T_{\text{trans}} + T_{\text{prop}}) + (N - 1) \times (d_{\text{proc}} + d_{\text{queue}})$.</p>
  <ul>
    <li>Transmission Delay per link: $T_{\text{trans}} = \frac{1500 \times 8 \text{ bits}}{10 \times 10^6 \text{ bps}} = \frac{12,000}{10^7} = 0.0012\text{ s} = \mathbf{1.20 \text{ ms}}$.</li>
    <li>Propagation Delay per link: $T_{\text{prop}} = \frac{250 \times 10^3 \text{ m}}{2 \times 10^8 \text{ m/s}} = 0.00125\text{ s} = \mathbf{1.25 \text{ ms}}$.</li>
    <li>Nodal Delay per intermediate router: $d_{\text{nodal}} = 10 \ \mu\text{s} + 40 \ \mu\text{s} = 50 \ \mu\text{s} = \mathbf{0.05 \text{ ms}}$.</li>
    <li>There are $N=4$ links and $(N-1) = 3$ intermediate routers:</li>
    $$\mathbf{T_{\text{total}} = 4 \times (1.20\text{ ms} + 1.25\text{ ms}) + 3 \times (0.05\text{ ms}) = 4 \times 2.45\text{ ms} + 0.15\text{ ms} = 9.80\text{ ms} + 0.15\text{ ms} = \mathbf{9.95 \text{ ms}}}$$
  </ul>
</div>
"""

# Module 2 Super Text
M2_ULTRA = r"""
<h2 class="section-title">Topic 19.5: Mathematical Derivation of PCM Quantization Noise & Constellation Theory</h2>

<p>
  In Pulse Code Modulation (PCM), a continuous analog signal $x(t)$ with peak-to-peak voltage range $[-V_{\text{max}}, +V_{\text{max}}]$ (total voltage span $2 V_{\text{max}}$) is divided into $L = 2^n$ uniform quantization intervals of step width:
</p>

<div class="formula-card">
  <strong>Quantization Step Size & Quantization Noise Power Derivation:</strong>
  $$\mathbf{\Delta = \frac{2 V_{\text{max}}}{L} = \frac{2 V_{\text{max}}}{2^n}}$$
  Assuming the quantization error $e = x - x_q$ is uniformly distributed over $\left[-\frac{\Delta}{2}, +\frac{\Delta}{2}\right]$ with probability density function $f_E(e) = \frac{1}{\Delta}$:
  $$\mathbf{\sigma_q^2 = \int_{-\Delta/2}^{+\Delta/2} e^2 f_E(e) \, de = \frac{1}{\Delta} \left[ \frac{e^3}{3} \right]_{-\Delta/2}^{+\Delta/2} = \frac{1}{\Delta} \left( \frac{\Delta^3}{24} - \left(-\frac{\Delta^3}{24}\right) \right) = \mathbf{\frac{\Delta^2}{12}}}$$
  $$\mathbf{\text{Signal-to-Quantization-Noise Ratio: } \text{SQNR}_{\text{dB}} = 10 \log_{10}\left(\frac{P_{\text{signal}}}{\sigma_q^2}\right) = \mathbf{6.02 n + 1.76 \text{ dB}}}$$
  <em>Engineering Axiom:</em> Every additional bit added to each PCM sample increases the Signal-to-Noise Ratio by exactly $\mathbf{6.02 \text{ dB}}$!
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Complete Comparison Matrix: Digital Line Coding Spectral Properties</div>
  <table class="custom-table">
    <thead>
      <tr>
        <th style="width: 18%;">Coding Scheme</th>
        <th style="width: 20%;">Baud Rate ($S$)</th>
        <th style="width: 20%;">DC Component?</th>
        <th style="width: 22%;">Synchronization Quality</th>
        <th>Primary Real-World Standard</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>NRZ-L</strong></td><td>$S = N$ baud</td><td>Severe DC bias</td><td>Poor (loses clock on 0s & 1s)</td><td>RS-232 Serial COM Ports</td></tr>
      <tr><td><strong>NRZ-I</strong></td><td>$S = N$ baud</td><td>Severe DC bias</td><td>Partial (syncs on 1s only)</td><td>USB 1.1/2.0 (with Bit Stuffing)</td></tr>
      <tr><td><strong>Bipolar AMI</strong></td><td>$S = N$ baud</td><td><strong>Zero DC Bias</strong></td><td>Partial (syncs on 1s only)</td><td>ISDN Primary Rate, DS1 lines</td></tr>
      <tr><td><strong>Manchester</strong></td><td>$S = 2N$ baud</td><td><strong>Zero DC Bias</strong></td><td><strong>100% Guaranteed</strong></td><td>IEEE 802.3 10BASE-T Ethernet</td></tr>
      <tr><td><strong>Diff. Manchester</strong></td><td>$S = 2N$ baud</td><td><strong>Zero DC Bias</strong></td><td><strong>100% Guaranteed</strong></td><td>IEEE 802.5 Token Ring LANs</td></tr>
      <tr><td><strong>4B/5B + NRZ-I</strong></td><td>$S = 1.25N$ baud</td><td>Low DC bias</td><td><strong>100% Guaranteed</strong></td><td>100BASE-TX Fast Ethernet, FDDI</td></tr>
      <tr><td><strong>8B/10B Coding</strong></td><td>$S = 1.25N$ baud</td><td>Zero DC bias</td><td><strong>100% Guaranteed</strong></td><td>Gigabit Ethernet (1000BASE-X), PCIe, SATA</td></tr>
    </tbody>
  </table>
</div>
"""

# Module 3 Super Text
M3_ULTRA = r"""
<h2 class="section-title">Topic 27.5: HDLC Protocol Architecture & Mathematical Error Analysis</h2>

<p>
  <strong>High-Level Data Link Control (HDLC)</strong> is the foundational bit-oriented Data Link Layer standard (ISO 13239) governing synchronous point-to-point and multipoint communication lines.
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">HDLC Frame Type</th>
      <th style="width: 38%;">Control Field Encoding</th>
      <th>Operational Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>I-Frame (Information)</strong></td>
      <td>`0 | N(S) [3 bits] | P/F | N(R) [3 bits]`</td>
      <td>Carries user network payload data with piggybacked sequence numbers $N(S)$ and acknowledgments $N(R)$.</td>
    </tr>
    <tr>
      <td><strong>S-Frame (Supervisory)</strong></td>
      <td>`1 0 | Type [2 bits] | P/F | N(R) [3 bits]`</td>
      <td>Flow and error control when no payload is ready: `00`=Receive Ready (RR), `01`=Receive Not Ready (RNR), `10`=Reject (REJ GBN), `11`=Selective Reject (SREJ).</td>
    </tr>
    <tr>
      <td><strong>U-Frame (Unnumbered)</strong></td>
      <td>`1 1 | Modifier [5 bits] | P/F`</td>
      <td>Link connection establishment and teardown: `SABM` (Set Asynchronous Balanced Mode), `DISC` (Disconnect), `UA` (Unnumbered Ack).</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Comprehensive CRC-16 Polynomial Division Trace</div>
  <p>Compute the CRC checksum for 16-bit dataword $D = \text{0xC4D1} = 1100010011010001$ using standard CRC-16-CCITT polynomial $G(x) = x^{16} + x^{12} + x^5 + 1 \implies 10001000000100001$ (degree $r=16$).</p>
  <ul>
    <li>Append $r=16$ zeros to $D$: $D \cdot 2^{16} = 11000100110100010000000000000000$.</li>
    <li>Perform Modulo-2 XOR binary division by the 17-bit divisor $G$.</li>
    <li>The 16-bit remainder generated is appended to $D$ to produce the exact 32-bit transmitted codeword.</li>
    <li><em>Error Detection Capability of CRC-16:</em> Detects $100\%$ of single-bit errors, $100\%$ of double-bit errors, $100\%$ of odd-numbered bit errors, and $100\%$ of burst errors of length $\le 16$ bits!</li>
  </ul>
</div>
"""

# Module 4 Super Text
M4_ULTRA = r"""
<h2 class="section-title">Topic 36.5: Mathematical MAC Throughput & Wireless Protocol States</h2>

<div class="formula-card">
  <strong>Carrier Sense Multiple Access with Collision Detection (CSMA/CD) Efficiency Formula:</strong>
  $$\mathbf{\eta = \frac{1}{1 + 5 \times a} \quad \text{where } a = \frac{T_{\text{prop}}}{T_{\text{trans}}}}$$
  As network cable length increases or transmission data rate increases, parameter $a$ grows, dramatically reducing channel efficiency. This is why 10-Gigabit and 100-Gigabit Ethernet completely abandon CSMA/CD in favor of <strong>Switched Full-Duplex Point-to-Point Links</strong>!
</div>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">IEEE 802.11 Standard</th>
      <th style="width: 18%;">Frequency Band</th>
      <th style="width: 22%;">Modulation & Physical Layer</th>
      <th style="width: 20%;">Max Physical Data Rate</th>
      <th>MIMO Stream Count</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>802.11b (Wi-Fi 1)</strong></td><td>$2.4\text{ GHz}$</td><td>DSSS / CCK</td><td>$11\text{ Mbps}$</td><td>$1 \times 1$ (SISO)</td></tr>
    <tr><td><strong>802.11g (Wi-Fi 3)</strong></td><td>$2.4\text{ GHz}$</td><td>OFDM (64-QAM)</td><td>$54\text{ Mbps}$</td><td>$1 \times 1$</td></tr>
    <tr><td><strong>802.11n (Wi-Fi 4)</strong></td><td>$2.4\text{ GHz} / 5\text{ GHz}$</td><td>MIMO-OFDM (64-QAM)</td><td>$600\text{ Mbps}$</td><td>Up to $4 \times 4$ MIMO</td></tr>
    <tr><td><strong>802.11ac (Wi-Fi 5)</strong></td><td>$5\text{ GHz}$ only</td><td>256-QAM ($160\text{ MHz}$ channels)</td><td>$3.46\text{ Gbps}$</td><td>Up to $8 \times 8$ MU-MIMO</td></tr>
    <tr><td><strong>802.11ax (Wi-Fi 6)</strong></td><td>$2.4 / 5 / 6\text{ GHz}$</td><td>OFDMA + 1024-QAM</td><td>$9.6\text{ Gbps}$</td><td>$8 \times 8$ Target Wake Time</td></tr>
    <tr><td><strong>802.11be (Wi-Fi 7)</strong></td><td>$2.4 / 5 / 6\text{ GHz}$</td><td>4096-QAM ($320\text{ MHz}$ channels)</td><td>$46\text{ Gbps}$</td><td>$16 \times 16$ Multi-Link MLO</td></tr>
  </tbody>
</table>
"""

# Module 5 Super Text
M5_ULTRA = r"""
<h2 class="section-title">Topic 52.5: Comprehensive Transport State Machines & Variable Length Subnetting (VLSM)</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 5: Complete Variable-Length Subnet Masking (VLSM) Design</div>
  <p>An enterprise organization is assigned address block `172.16.0.0/16`. Design an optimal VLSM subnetting plan for 4 distinct departments:</p>
  <ul>
    <li>Department A: Requires 4000 host addresses</li>
    <li>Department B: Requires 2000 host addresses</li>
    <li>Department C: Requires 1000 host addresses</li>
    <li>Department D: Requires 500 host addresses</li>
  </ul>
  <p><strong>VLSM Allocation Plan:</strong></p>
  <table class="custom-table">
    <thead><tr><th>Department</th><th>Hosts Needed</th><th>Bits Needed ($2^h - 2 \ge N$)</th><th>Prefix Mask</th><th>Assigned Network Address</th><th>Usable Host Range</th></tr></thead>
    <tbody>
      <tr><td><strong>Dept A</strong></td><td>4000</td><td>$h=12 \ (4094)$</td><td>$/20 \ (255.255.240.0)$</td><td>`172.16.0.0/20`</td><td>`172.16.0.1 - 172.16.15.254`</td></tr>
      <tr><td><strong>Dept B</strong></td><td>2000</td><td>$h=11 \ (2046)$</td><td>$/21 \ (255.255.248.0)$</td><td>`172.16.16.0/21`</td><td>`172.16.16.1 - 172.16.23.254`</td></tr>
      <tr><td><strong>Dept C</strong></td><td>1000</td><td>$h=10 \ (1022)$</td><td>$/22 \ (255.255.252.0)$</td><td>`172.16.24.0/22`</td><td>`172.16.24.1 - 172.16.27.254`</td></tr>
      <tr><td><strong>Dept D</strong></td><td>500</td><td>$h=9 \ (510)$</td><td>$/23 \ (255.255.254.0)$</td><td>`172.16.28.0/23`</td><td>`172.16.28.1 - 172.16.29.254`</td></tr>
    </tbody>
  </table>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step TCP Jacobson's RTO Calculation Algorithm</div>
  <p>Given initial $\text{SRTT} = 100\text{ ms}$, $\text{RTTVAR} = 10\text{ ms}$, and $\alpha = 0.125, \beta = 0.25$. If a new sample RTT measurement $R = 140\text{ ms}$ arrives, compute the updated Retransmission Timeout ($\text{RTO}$):</p>
  $$\text{Error } E = R - \text{SRTT} = 140 - 100 = \mathbf{+40 \text{ ms}}$$
  $$\text{Updated SRTT} \leftarrow \text{SRTT} + \alpha \times E = 100 + 0.125(40) = 100 + 5 = \mathbf{105 \text{ ms}}$$
  $$\text{Updated RTTVAR} \leftarrow \text{RTTVAR} + \beta \times (|E| - \text{RTTVAR}) = 10 + 0.25(40 - 10) = 10 + 7.5 = \mathbf{17.5 \text{ ms}}$$
  $$\mathbf{\text{New RTO} = \text{SRTT} + 4 \times \text{RTTVAR} = 105 + 4(17.5) = 105 + 70 = \mathbf{175 \text{ ms}}}$$
</div>
"""

def make_true_12():
    files = [
        ("dccn_module1_content.py", "Topic 13.6: Deep Layer-by-Layer", M1_ULTRA),
        ("dccn_module2_content.py", "Topic 19.5: Mathematical Derivation", M2_ULTRA),
        ("dccn_module3_content.py", "Topic 27.5: HDLC Protocol", M3_ULTRA),
        ("dccn_module4_content.py", "Topic 36.5: Mathematical MAC", M4_ULTRA),
        ("dccn_module5_content.py", "Topic 52.5: Comprehensive Transport", M5_ULTRA),
    ]
    
    for fname, check_str, extra in files:
        fpath = os.path.join(DCCN_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if check_str not in c:
            c = c.rstrip().rstrip('"""').rstrip() + extra + '\n"""\n'
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Applied 12-page ultra content to {fname}")

if __name__ == "__main__":
    make_true_12()
