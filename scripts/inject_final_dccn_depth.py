#!/usr/bin/env python3
"""
Adds final polish and depth to M2, M3, M4.
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

M2_POLISH = r"""
<div class="qa-card">
  <div class="qa-q">Q10. Explain Spread Spectrum techniques: Direct Sequence Spread Spectrum (DSSS) and Frequency Hopping Spread Spectrum (FHSS). (10 Marks)</div>
  <div class="qa-a">
    <strong>Spread Spectrum</strong> expands the bandwidth of a narrowband message signal across a wide frequency band using a pseudo-random noise (PN) sequence to provide military-grade anti-jamming and multi-user CDMA capability:<br>
    • <strong>DSSS (Direct Sequence Spread Spectrum):</strong> Each data bit is multiplied ($\mathbf{XOR}$) by a high-rate $n$-bit pseudo-random **Chipping Sequence** (e.g. 11-bit Barker code `10110111000` in IEEE 802.11b Wi-Fi). Even if narrowband interference corrupts part of the band, the receiver cross-correlates with the known chipping code to recover the exact data with high processing gain ($G_p = 10 \log_{10}(B_{\text{ss}} / B_{\text{data}})$).<br>
    • <strong>FHSS (Frequency Hopping Spread Spectrum):</strong> The carrier frequency rapidly hops across a pseudo-random sequence of frequency channels (e.g. 79 channels in Bluetooth hopping 1600 times per second!). Eavesdroppers and narrow jammers cannot intercept or jam the transmission without knowing the exact hopping seed sequence!
  </div>
</div>
"""

M3_POLISH = r"""
<div class="qa-card">
  <div class="qa-q">Q10. Explain the High-Level Data Link Control (HDLC) operational modes: NRM, ABM, and ARM. (8 Marks)</div>
  <div class="qa-a">
    HDLC supports three distinct operational station configurations:<br>
    1. <strong>Normal Response Mode (NRM):</strong> Unbalanced configuration with 1 Primary station and $\ge 1$ Secondary stations. Secondary stations can transmit frames strictly in response to an explicit poll ($P=1$) from the primary.<br>
    2. <strong>Asynchronous Balanced Mode (ABM):</strong> Balanced point-to-point configuration with 2 Combined stations. Either station can initiate data transmission asynchronously at any time without asking permission (universal standard in Full-Duplex point-to-point links).<br>
    3. <strong>Asynchronous Response Mode (ARM):</strong> Unbalanced configuration where Secondary stations can initiate transmission asynchronously without waiting for a primary poll.
  </div>
</div>
"""

M4_POLISH = r"""
<div class="qa-card">
  <div class="qa-q">Q10. Explain Virtual LANs (VLANs, IEEE 802.1Q) and how Trunking and Inter-VLAN Routing operate. (8 Marks)</div>
  <div class="qa-a">
    • <strong>VLAN (Virtual LAN):</strong> Logically segments a single physical Layer 2 switch into multiple independent broadcast domains. Broadcast traffic from VLAN 10 (Finance) is completely isolated from VLAN 20 (Engineering) without requiring separate physical switches.<br>
    • <strong>Trunking (IEEE 802.1Q):</strong> A high-speed link carrying traffic for multiple VLANs simultaneously between switches. Each frame is tagged with a 4-byte 802.1Q header containing a 12-bit VLAN ID (VID).<br>
    • <strong>Inter-VLAN Routing:</strong> Because VLANs are isolated broadcast domains, communication between two different VLANs requires a Layer 3 Router (using "Router-on-a-Stick" subinterfaces) or a Multi-Layer Switch (SVI / Switched Virtual Interfaces).
  </div>
</div>
"""

def polish():
    files = [
        ("dccn_module2_content.py", "Topic 10. Spread Spectrum", M2_POLISH),
        ("dccn_module3_content.py", "Topic 10. HDLC operational modes", M3_POLISH),
        ("dccn_module4_content.py", "Topic 10. Virtual LANs", M4_POLISH),
    ]
    for fname, check_str, pol_text in files:
        fpath = os.path.join(DCCN_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if "Q10. Explain Spread Spectrum" not in c and "Q10. Explain the High-Level" not in c and "Q10. Explain Virtual LANs" not in c:
            c = c.rstrip().rstrip('"""').rstrip() + pol_text + '\n"""\n'
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Polished {fname}")

if __name__ == "__main__":
    polish()
