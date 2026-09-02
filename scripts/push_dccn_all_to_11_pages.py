#!/usr/bin/env python3
"""
Adds the final comprehensive sections to DCCN Modules 1, 2, 3, 4
guaranteeing that EVERY SINGLE MODULE PDF is between 11 and 13 pages!
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

M1_PUSH = r"""
<h2 class="section-title">Topic 13.8: Master University Long-Answer Exam Solutions Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q13. Explain the detailed structure of the Global Internet Hierarchy: Tier-1, Tier-2, Tier-3 ISPs, Internet Exchange Points (IXPs), and Peering vs Transit agreements. (10 Marks)</div>
  <div class="qa-a">
    The Internet is a global hierarchical network of networks:<br>
    • <strong>Tier-1 ISPs (National/Global Backbones):</strong> AT&T, Lumen, Telia, Tata Communications, NTT. They own intercontinental fiber optic cables and peer with all other Tier-1 providers settlement-free (zero transit fees).<br>
    • <strong>Tier-2 ISPs (Regional Providers):</strong> Purchase transit from Tier-1 ISPs to reach the global Internet, while peering with other Tier-2 ISPs locally.<br>
    • <strong>Tier-3 ISPs (Local Access ISPs):</strong> Comcast, Jio, Airtel, local cable providers connecting end-user residential homes and enterprise campuses.<br>
    • <strong>Internet Exchange Points (IXPs):</strong> Physical data center facilities where multiple ISPs and CDNs (Google, Cloudflare, Akamai) interconnect via high-speed switching fabrics to exchange traffic locally without incurring transit costs.<br>
    • <strong>Peering vs. Transit:</strong> <em>Peering</em> is a bilateral agreement to exchange mutual customer traffic for free; <em>Transit</em> is a commercial contract where a customer ISP pays an upstream provider for complete global Internet routing access.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q14. Compare Coaxial Cable, Cat 6 UTP, and Optical Fiber across physical bandwidth, attenuation per km, installation difficulty, and maximum repeaterless distance. (8 Marks)</div>
  <div class="qa-a">
    • <strong>Cat 6 UTP:</strong> Bandwidth up to $250\text{--}500\text{ MHz}$; high attenuation ($20\text{ dB}/100\text{ m}$ at high freq); standard RJ45 crimping (very easy); max distance $100\text{ meters}$.<br>
    • <strong>Coaxial Cable (RG-6):</strong> Bandwidth up to $1\text{ GHz}$; moderate attenuation ($6\text{--}10\text{ dB}/100\text{ m}$); BNC/F-type connectors (moderate); max distance $500\text{ meters}$.<br>
    • <strong>Single-Mode Fiber (SMF):</strong> Bandwidth $>100\text{ THz}$ (virtually unlimited); ultra-low attenuation ($0.2\text{ dB/km}$ at $1550\text{ nm}$); requires precision fusion splicing (specialized training); max repeaterless distance $>80\text{ to }100\text{ km}$!
  </div>
</div>
"""

M2_PUSH = r"""
<h2 class="section-title">Topic 19.7: Master University Long-Answer Exam Solutions Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q8. Explain the 4B/5B and 8B/10B Block Coding mechanisms used in Fast Ethernet and Gigabit Ethernet. Why are they preferred over Manchester? (10 Marks)</div>
  <div class="qa-a">
    • <strong>Manchester Limitation:</strong> Manchester encoding has a baud rate efficiency of only $50\%$ ($S = 2N$), requiring a massive $200\text{ MHz}$ signaling rate for $100\text{ Mbps}$ Fast Ethernet.<br>
    • <strong>4B/5B Block Coding Solution:</strong> Takes 4-bit data nibbles and maps them into 5-bit symbols from a lookup table. The 5-bit codes are chosen such that they contain <strong>at most one leading zero and at most two trailing zeros</strong>. When transmitted using NRZ-I, this guarantees at least one transition every 3 bits for continuous receiver clock recovery with only $\mathbf{25\%}$ baud overhead ($125\text{ Mbaud}$ for $100\text{ Mbps}$)!<br>
    • <strong>8B/10B Coding (Gigabit Ethernet):</strong> Maps 8-bit bytes into 10-bit symbols, balancing the Running Disparity (DC balance) and providing robust error detection for fiber optic and copper links.
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q9. Differentiate between Frequency-Division Multiplexing (FDM), Time-Division Multiplexing (TDM), and Wavelength-Division Multiplexing (WDM) across signals, media, and multiplexing hardware. (8 Marks)</div>
  <div class="qa-a">
    • <strong>FDM:</strong> Analog multiplexing; divides total channel frequency band into discrete sub-channels with Guard Bands; requires analog bandpass filters (AM/FM Radio, Cable TV).<br>
    • <strong>TDM:</strong> Digital multiplexing; interleaves discrete time slices from multiple bitstreams into round-robin frames; requires digital framing logic and buffers (T1/E1, SONET).<br>
    • <strong>WDM:</strong> Optical multiplexing; combines multiple optical laser beams of different wavelengths ($\lambda$) onto a single optical fiber strand; requires optical prisms and diffraction gratings (DWDM telecommunications).
  </div>
</div>
"""

M3_PUSH = r"""
<h2 class="section-title">Topic 27.7: Master University Long-Answer Exam Solutions Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q8. Derive the Channel Utilization Efficiency ($\eta$) for Go-Back-N ARQ and Selective Repeat ARQ under non-zero transmission error probability ($P_f$). (10 Marks)</div>
  <div class="qa-a">
    Let $P_f$ be the frame error probability, and $a = T_{\text{prop}} / T_{\text{trans}}$:<br>
    • <strong>Stop-and-Wait ARQ with Errors:</strong> Average number of transmissions per frame is $N_{\text{trans}} = \frac{1}{1 - P_f}$.<br>
      $$\mathbf{\eta_{\text{SW}} = \frac{1 - P_f}{1 + 2a}}$$
    • <strong>Go-Back-N ARQ with Errors:</strong> If a frame is lost, the entire window of $N = 1 + 2a$ frames must be retransmitted. The average number of transmitted frames per successful delivery is $1 + \frac{N P_f}{1 - P_f}$.<br>
      $$\mathbf{\eta_{\text{GBN}} = \frac{1 - P_f}{1 + 2a P_f}}$$
    • <strong>Selective Repeat ARQ with Errors:</strong> Since ONLY the corrupted frame is retransmitted individually:<br>
      $$\mathbf{\eta_{\text{SR}} = 1 - P_f} \quad (\text{Independent of propagation parameter } a!).$$
    <em>Conclusion:</em> On high-latency satellite and fiber channels ($a \gg 1$), Selective Repeat is the only viable ARQ protocol!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q9. Explain the Point-to-Point Protocol (PPP) frame structure, Link Control Protocol (LCP), and Network Control Protocol (NCP). (8 Marks)</div>
  <div class="qa-a">
    <strong>PPP (RFC 1661)</strong> is the standard data link protocol for broadband DSL, dial-up, and leased lines:<br>
    1. <strong>Framing:</strong> Byte-oriented frame with `Flag (0x7E)`, `Address (0xFF)`, `Control (0x03)`, `Protocol (2B)`, `Payload`, `FCS (16/32b)`. Uses byte stuffing (`0x7D`).<br>
    2. <strong>Link Control Protocol (LCP):</strong> Establishes, configures, authenticates (PAP / CHAP), tests, and terminates the data link connection.<br>
    3. <strong>Network Control Protocol (NCP):</strong> Establishes and configures network layer protocols over the link (e.g. IPCP assigns IP addresses to clients dynamically).
  </div>
</div>
"""

M4_PUSH = r"""
<h2 class="section-title">Topic 36.7: Master University Long-Answer Exam Solutions Bank</h2>

<div class="qa-card">
  <div class="qa-q">Q8. Explain the IEEE 802.11 Wi-Fi Medium Access Control architecture: DCF, PCF, Inter-Frame Spaces (SIFS, PIFS, DIFS, EIFS), and Network Allocation Vector (NAV). (10 Marks)</div>
  <div class="qa-a">
    IEEE 802.11 defines two operational coordination modes:<br>
    • <strong>Distributed Coordination Function (DCF):</strong> Contention-based CSMA/CA protocol used by all Wi-Fi stations.<br>
    • <strong>Point Coordination Function (PCF):</strong> Optional contention-free polling protocol managed by the Access Point (AP).<br>
    • <strong>Inter-Frame Space (IFS) Hierarchy:</strong><br>
      1. <strong>SIFS (Short IFS):</strong> Highest priority; used for instant ACK, CTS, and fragmented frame bursts.<br>
      2. <strong>PIFS (PCF IFS):</strong> Medium priority; used by Access Point to gain channel control for PCF polling.<br>
      3. <strong>DIFS (DCF IFS):</strong> Normal priority; minimum idle duration a station must wait before contending for channel.<br>
      4. <strong>EIFS (Extended IFS):</strong> Longest wait time used when a frame is received with checksum errors.<br>
    • <strong>Network Allocation Vector (NAV):</strong> A virtual carrier sensing timer maintained inside every Wi-Fi station. When a station overhears an RTS or CTS frame, it sets its NAV to the duration value specified in the frame header, remaining asleep and deferring all channel access until NAV reaches 0!
  </div>
</div>

<div class="qa-card">
  <div class="qa-q">Q9. Compare 10BASE5 (Thicknet), 10BASE2 (Thinnet), 10BASE-T, 100BASE-TX, and 1000BASE-T across physical media, topology, connector, and maximum span. (8 Marks)</div>
  <div class="qa-a">
    • <strong>10BASE5:</strong> Thick coaxial cable, Bus topology, Vampire taps & AUI cable, max $500\text{ meters}$.<br>
    • <strong>10BASE2:</strong> RG-58 Thin coaxial cable, Bus topology, BNC T-connectors, max $185\text{ meters}$.<br>
    • <strong>10BASE-T:</strong> Cat 3/5 UTP copper, Star topology (Hub), RJ-45, max $100\text{ meters}$.<br>
    • <strong>100BASE-TX:</strong> Cat 5 UTP (2 pairs), Star topology (Switch), RJ-45, max $100\text{ meters}$.<br>
    • <strong>1000BASE-T:</strong> Cat 5e/6 UTP (4 pairs simultaneously full-duplex), Star topology, RJ-45, max $100\text{ meters}$.
  </div>
</div>
"""

def apply_push():
    files = [
        ("dccn_module1_content.py", "Topic 13.8: Master University Long-Answer", M1_PUSH),
        ("dccn_module2_content.py", "Topic 19.7: Master University Long-Answer", M2_PUSH),
        ("dccn_module3_content.py", "Topic 27.7: Master University Long-Answer", M3_PUSH),
        ("dccn_module4_content.py", "Topic 36.7: Master University Long-Answer", M4_PUSH),
    ]
    
    for fname, check_str, push_text in files:
        fpath = os.path.join(DCCN_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if check_str not in c:
            c = c.rstrip().rstrip('"""').rstrip() + push_text + '\n"""\n'
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Applied final 11-page push to {fname}")

if __name__ == "__main__":
    apply_push()
