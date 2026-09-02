#!/usr/bin/env python3
"""
Adds comprehensive, university-level deep exam banks and worked derivations
to ensure all DCCN modules are solidly 36,000+ characters and generate 11 to 14 pages each!
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

# Module 1 Super Boost
M1_BOOST = r"""
<h2 class="section-title">Topic 13.5: Master University Solved Examination Numerical Bank</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 4: Nyquist Multi-Level Constellation Design</div>
  <p>A TV broadcast channel has a bandwidth of $B = 6\text{ MHz}$. We wish to transmit a digital HDTV stream at a data rate of $R = 30\text{ Mbps}$ over this noiseless channel.</p>
  <ol>
    <li>What is the minimum number of discrete signal voltage levels ($L$) required by the signaling hardware?</li>
    <li>If each discrete level is represented by $k$ bits, what is the value of $k$?</li>
  </ol>
  <p><strong>Solution:</strong></p>
  $$R = 2 B \log_2(L) \implies 30 \times 10^6 = 2 \times (6 \times 10^6) \times \log_2(L)$$
  $$\log_2(L) = \frac{30}{12} = 2.5 \implies L = 2^{2.5} \approx 5.657$$
  <p>Since the number of physical signal levels $L$ must be an integer power of 2 ($2^k$), we round up to the next power of 2:</p>
  $$\mathbf{k = 3 \text{ bits/symbol} \implies L = 2^3 = \mathbf{8 \text{ signal levels}}}$$
  <p><em>Actual Max Bit Rate with $L=8$:</em> $R_{\text{actual}} = 2 \times 6\text{ MHz} \times 3 = \mathbf{36 \text{ Mbps}}$ (exceeds the required $30\text{ Mbps}$).</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 5: Shannon Limit on Deep Space Satellite Channel</div>
  <p>A deep space satellite probe transmits telemetry data over a microwave radio channel with bandwidth $B = 10\text{ MHz}$ and Signal-to-Noise Ratio $\text{SNR}_{\text{dB}} = -3\text{ dB}$ (noise power exceeds signal power!). Calculate the maximum theoretical bit rate.</p>
  <p><strong>Solution:</strong></p>
  $$\text{SNR}_{\text{dB}} = -3\text{ dB} \implies -3 = 10 \log_{10}(\text{SNR}) \implies \text{SNR} = 10^{-0.3} \approx 0.5012$$
  $$\mathbf{C = B \log_2(1 + \text{SNR}) = 10 \times 10^6 \times \log_2(1 + 0.5012) = 10^7 \times \log_2(1.5012)}$$
  $$\text{Since } \log_2(1.5012) \approx 0.5861: \quad \mathbf{C = 10^7 \times 0.5861 = \mathbf{5,861,000 \text{ bps} \approx \mathbf{5.86 \text{ Mbps}}}}$$
  <p><em>Significance:</em> Shannon's theorem proves that reliable, error-free communication is mathematically possible even when noise is greater than signal power ($\text{SNR} < 1$), provided robust error-correcting codes are utilized!</p>
</div>
"""

# Module 2 Super Boost
M2_BOOST = r"""
<h2 class="section-title">Topic 19.4: Master University Solved Examination Numerical Bank</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 2: Line Coding Baud Rate & Bandwidth Requirements</div>
  <p>A digital bitstream of rate $R = 10\text{ Mbps}$ is transmitted using: (a) NRZ-L, (b) Manchester, (c) 4B/5B Block Coding with NRZ-I. Calculate the signal baud rate ($S$) and minimum Nyquist bandwidth ($B_{\text{min}}$) for each scheme.</p>
  <p><strong>Solution:</strong> $\text{Baud Rate } S = c \times R \times \frac{1}{r}, \quad B_{\text{min}} = \frac{S}{2}$ (for average factor $c = 1/2$).</p>
  <ul>
    <li><strong>(a) NRZ-L ($r=1$):</strong> Baud rate $S = 10\text{ Mbaud} \implies B_{\text{min}} = \frac{10}{2} = \mathbf{5 \text{ MHz}}$.</li>
    <li><strong>(b) Manchester ($r=0.5$):</strong> Baud rate $S = 20\text{ Mbaud} \implies B_{\text{min}} = \frac{20}{2} = \mathbf{10 \text{ MHz}}$ (Requires $2\times$ the bandwidth of NRZ!).</li>
    <li><strong>(c) 4B/5B with NRZ-I ($r = 4/5 = 0.8$):</strong> Baud rate $S = \frac{10}{0.8} = 12.5\text{ Mbaud} \implies B_{\text{min}} = \frac{12.5}{2} = \mathbf{6.25 \text{ MHz}}$ (Only $25\%$ bandwidth overhead with guaranteed clock synchronization!).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 3: Pulse Code Modulation (PCM) of Video Signals</div>
  <p>A television video signal has a maximum frequency bandwidth of $f_{\text{max}} = 4.5\text{ MHz}$. The signal is sampled at $20\%$ above the Nyquist rate and quantized into 1024 discrete levels ($L = 1024$). Calculate: (1) Sampling rate, (2) Bits per sample, (3) Output digital bit rate, and (4) Minimum channel bandwidth.</p>
  <p><strong>Solution:</strong></p>
  $$\text{1. Nyquist Rate } = 2 \times 4.5\text{ MHz} = 9\text{ MHz} \implies f_s = 1.20 \times 9\text{ MHz} = \mathbf{10.8 \text{ MHz (10.8 million samples/sec)}}$$
  $$\text{2. Bits per Sample } n = \log_2(1024) = \mathbf{10 \text{ bits/sample}}$$
  $$\text{3. Bit Rate } R = f_s \times n = 10.8\text{ MHz} \times 10 = \mathbf{108 \text{ Mbps}}$$
  $$\text{4. Minimum Bandwidth } B_{\text{min}} = \frac{R}{2} = \frac{108}{2} = \mathbf{54 \text{ MHz}}$$
</div>
"""

# Module 3 Super Boost
M3_BOOST = r"""
<h2 class="section-title">Topic 27.4: Master University Solved Examination Numerical Bank</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 4: CRC Hardware Shift-Register Circuit Implementation</div>
  <p>Design the Linear Feedback Shift Register (LFSR) hardware circuit for generating CRC-4 with polynomial $G(x) = x^4 + x + 1$.</p>
  <ul>
    <li>The circuit consists of 4 D-Flip-Flops ($FF_3, FF_2, FF_1, FF_0$) initialized to zero.</li>
    <li>$\mathbf{XOR}$ gates are placed at positions corresponding to non-zero coefficients of $G(x)$ (specifically before $FF_0$ and between $FF_0$ and $FF_1$).</li>
    <li>Data bits are shifted in MSB first. After $k$ shifts of data and $r=4$ shifts of zeros, the contents of the 4 flip-flops contain the exact 4-bit CRC remainder!</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 5: Go-Back-N Window Size Optimization under High Propagation Delay</div>
  <p>A $100\text{ Mbps}$ fiber-optic link connects two data centers separated by $D = 2000\text{ km}$ ($v = 2 \times 10^8\text{ m/s}$). Frame size $L = 1500\text{ bytes}$ ($12,000\text{ bits}$). What is the minimum number of sequence number bits ($k$) required for Go-Back-N ARQ to achieve $100\%$ link utilization?</p>
  <p><strong>Solution:</strong></p>
  $$T_{\text{prop}} = \frac{2000 \times 10^3\text{ m}}{2 \times 10^8\text{ m/s}} = 0.010\text{ s} = 10\text{ ms}$$
  $$T_{\text{trans}} = \frac{12,000\text{ bits}}{100 \times 10^6\text{ bps}} = 0.00012\text{ s} = 0.12\text{ ms}$$
  $$a = \frac{T_{\text{prop}}}{T_{\text{trans}}} = \frac{10\text{ ms}}{0.12\text{ ms}} = 83.33 \implies 1 + 2a = 1 + 2(83.33) = \mathbf{167.67}$$
  $$\text{For } 100\% \text{ utilization, sender window must satisfy: } W_S \ge 1 + 2a = 168$$
  $$\text{In GBN, } W_S = 2^k - 1 \ge 168 \implies 2^k \ge 169 \implies \mathbf{k = 8 \text{ bits}} \quad (2^8 - 1 = 255 \ge 168)$$
</div>
"""

# Module 4 Super Boost
M4_BOOST = r"""
<h2 class="section-title">Topic 36.4: Master University Solved Examination Numerical Bank</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 4: CSMA/CD Maximum Cable Distance Calculation</div>
  <p>A 10 Mbps Standard Ethernet network transmits frames with minimum size 64 bytes (512 bits) over coaxial cable with propagation velocity $v = 2 \times 10^8\text{ m/s}$. The network includes 4 repeaters, each introducing an internal processing delay of $1.5 \ \mu\text{s}$. Calculate the maximum permissible cable distance between the two furthest stations.</p>
  <p><strong>Solution:</strong></p>
  $$T_{\text{trans}} = \frac{512\text{ bits}}{10 \times 10^6\text{ bps}} = 51.2 \ \mu\text{s}$$
  $$\text{Condition: } T_{\text{trans}} \ge 2 \times T_{\text{prop\_total}} = 2 \times (T_{\text{cable}} + 4 \times T_{\text{repeater}})$$
  $$51.2 \ \mu\text{s} \ge 2 \times (T_{\text{cable}} + 4 \times 1.5 \ \mu\text{s}) = 2 T_{\text{cable}} + 12 \ \mu\text{s}$$
  $$2 T_{\text{cable}} \le 51.2 - 12 = 39.2 \ \mu\text{s} \implies T_{\text{cable}} \le 19.6 \ \mu\text{s}$$
  $$\mathbf{\text{Max Cable Distance } D = T_{\text{cable}} \times v = 19.6 \times 10^{-6}\text{ s} \times (2 \times 10^8\text{ m/s}) = \mathbf{3920 \text{ meters (3.92 km)}}}$$
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 5: Pure ALOHA vs. Slotted ALOHA Station Scaling</div>
  <p>A broadcast channel is shared by $N$ independent stations, each generating a $1000\text{-bit}$ frame on average every $10\text{ seconds}$. The channel bandwidth is $50\text{ kbps}$. How many stations can be supported by: (a) Pure ALOHA, and (b) Slotted ALOHA?</p>
  <p><strong>Solution:</strong> Frame duration $T_{\text{fr}} = \frac{1000\text{ bits}}{50,000\text{ bps}} = 0.020\text{ s} = 20\text{ ms}$.</p>
  $$\text{Each station generation rate } \lambda = \frac{1 \text{ frame}}{10\text{ s}} = 0.1 \text{ frames/s}$$
  $$\text{Normalized frame rate per station } g = \lambda \times T_{\text{fr}} = 0.1 \times 0.020 = 0.002 \text{ frames/slot}$$
  <ul>
    <li><strong>(a) Pure ALOHA ($G_{\text{max}} = 0.5$):</strong> $N \times g \le 0.5 \implies N \le \frac{0.5}{0.002} = \mathbf{250 \text{ stations}}$.</li>
    <li><strong>(b) Slotted ALOHA ($G_{\text{max}} = 1.0$):</strong> $N \times g \le 1.0 \implies N \le \frac{1.0}{0.002} = \mathbf{500 \text{ stations}}$ ($2\times$ the capacity of Pure ALOHA!).</li>
  </ul>
</div>
"""

# Module 5 Super Boost
M5_BOOST = r"""
<h2 class="section-title">Topic 52.4: Master University Solved Examination Numerical Bank</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 3: Hierarchical CIDR Route Aggregation & Supernetting</div>
  <p>A regional ISP router receives routing updates for four contiguous IP address blocks:</p>
  <ul>
    <li>Block 1: `200.16.0.0/24` (Binary: `11001000.00010000.00000000.00000000`)</li>
    <li>Block 2: `200.16.1.0/24` (Binary: `11001000.00010000.00000001.00000000`)</li>
    <li>Block 3: `200.16.2.0/24` (Binary: `11001000.00010000.00000010.00000000`)</li>
    <li>Block 4: `200.16.3.0/24` (Binary: `11001000.00010000.00000011.00000000`)</li>
  </ul>
  <p><strong>Route Aggregation (Supernetting) Solution:</strong></p>
  <p>Comparing the 3rd octets in binary: `00000000`, `00000001`, `00000010`, `00000011`. All 4 blocks share the identical first 22 bits (`11001000.00010000.000000xx`).</p>
  $$\mathbf{\text{Single Aggregated Supernet Route} = \mathbf{200.16.0.0/22} \quad (\text{Subnet Mask: } 255.255.252.0)}$$
  <p><em>Benefit:</em> Replaces 4 independent routing table entries with 1 consolidated entry, reducing router BGP memory table size by $75\%$!</p>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 4: TCP Maximum Throughput & Mathis Equation</div>
  <p>A cross-continental $10\text{ Gbps}$ TCP link has an RTT of $100\text{ ms}$ and standard MSS of $1460\text{ bytes}$. If the packet loss rate is $p = 0.0001$ ($0.01\%$), calculate the maximum achievable TCP throughput according to the <strong>Mathis Formula</strong>.</p>
  <p><strong>Solution (Mathis Formula):</strong></p>
  $$\mathbf{\text{Throughput} \le \frac{\text{MSS}}{\text{RTT}} \times \frac{1.22}{\sqrt{p}}}$$
  $$\text{Throughput} \le \frac{1460 \times 8 \text{ bits}}{0.100\text{ s}} \times \frac{1.22}{\sqrt{0.0001}} = 116,800 \times \frac{1.22}{0.01} = 116,800 \times 122 = \mathbf{14,249,600 \text{ bps} \approx \mathbf{14.25 \text{ Mbps}}}$$
  <p><em>Critical Engineering Insight:</em> Even on a $10\text{ Gbps}$ physical pipe, a tiny $0.01\%$ packet drop throttles standard TCP Reno throughput down to $14.25\text{ Mbps}$ due to aggressive AIMD window halving!</p>
</div>
"""

def boost_all():
    files = [
        ("dccn_module1_content.py", "Topic 13.5: Master University Solved", M1_BOOST),
        ("dccn_module2_content.py", "Topic 19.4: Master University Solved", M2_BOOST),
        ("dccn_module3_content.py", "Topic 27.4: Master University Solved", M3_BOOST),
        ("dccn_module4_content.py", "Topic 36.4: Master University Solved", M4_BOOST),
        ("dccn_module5_content.py", "Topic 52.4: Master University Solved", M5_BOOST),
    ]
    
    for fname, check_str, extra in files:
        fpath = os.path.join(DCCN_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if check_str not in c:
            c = c.rstrip().rstrip('"""').rstrip() + extra + '\n"""\n'
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Boosted {fname}")

if __name__ == "__main__":
    boost_all()
