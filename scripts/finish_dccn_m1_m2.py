#!/usr/bin/env python3
"""
Final Polish for DCCN M1 and M2 to achieve 100% PASS across all DCCN modules!
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

M1_FINISH = r"""
<h2 class="section-title">Topic 13.9: Advanced Communication Systems & Electromagnetic Wave Spectrum</h2>

<p>
  The electromagnetic spectrum extends from low-frequency radio waves to high-frequency gamma rays. Telecommunications allocates specific spectrum bands governed by international treaty (ITU-R Radio Regulations):
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Band Name</th>
      <th style="width: 20%;">Frequency Range</th>
      <th style="width: 25%;">Propagation Mode</th>
      <th>Primary Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>VLF (Very Low)</strong></td><td>$3\text{ to }30\text{ kHz}$</td><td>Ground Wave (surface wave)</td><td>Submarine communication, navigation beacons</td></tr>
    <tr><td><strong>LF (Low)</strong></td><td>$30\text{ to }300\text{ kHz}$</td><td>Ground Wave</td><td>Longwave radio, RFID, aeronautical beacons</td></tr>
    <tr><td><strong>MF (Medium)</strong></td><td>$300\text{ kHz to }3\text{ MHz}$</td><td>Sky Wave (ionospheric reflection)</td><td>AM Radio broadcasting ($530\text{--}1700\text{ kHz}$)</td></tr>
    <tr><td><strong>HF (High)</strong></td><td>$3\text{ to }30\text{ MHz}$</td><td>Sky Wave (skip distance reflection)</td><td>Shortwave international radio, amateur radio</td></tr>
    <tr><td><strong>VHF (Very High)</strong></td><td>$30\text{ to }300\text{ MHz}$</td><td>Line-of-Sight (LOS)</td><td>FM Radio ($88\text{--}108\text{ MHz}$), VHF Television, Air traffic control</td></tr>
    <tr><td><strong>UHF (Ultra High)</strong></td><td>$300\text{ MHz to }3\text{ GHz}$</td><td>Line-of-Sight (LOS)</td><td>Cellular mobile (4G LTE, 5G sub-6), Wi-Fi ($2.4\text{ GHz}$), GPS ($1.575\text{ GHz}$)</td></tr>
    <tr><td><strong>SHF (Super High)</strong></td><td>$3\text{ to }30\text{ GHz}$</td><td>Line-of-Sight (Microwave dish)</td><td>Satellite communication, Radar, Wi-Fi ($5\text{ GHz} / 6\text{ GHz}$)</td></tr>
    <tr><td><strong>EHF (Extremely High)</strong></td><td>$30\text{ to }300\text{ GHz}$</td><td>Millimeter Wave (mmWave)</td><td>5G mmWave ($28\text{--}39\text{ GHz}$), Automotive radar ($77\text{ GHz}$)</td></tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Satellite Link Up-Link and Down-Link Frequency Planning</div>
  <p>Geostationary communication satellites operate in paired frequency bands where the <strong>Up-Link frequency ($f_{\text{up}}$) is intentionally higher than the Down-Link frequency ($f_{\text{down}}$)</strong>:</p>
  <ul>
    <li><strong>C-Band:</strong> Up-Link $= 5.925\text{--}6.425\text{ GHz}$ ($6\text{ GHz}$); Down-Link $= 3.700\text{--}4.200\text{ GHz}$ ($4\text{ GHz}$).</li>
    <li><strong>Ku-Band:</strong> Up-Link $= 14.0\text{--}14.5\text{ GHz}$ ($14\text{ GHz}$); Down-Link $= 11.7\text{--}12.2\text{ GHz}$ ($12\text{ GHz}$).</li>
    <li><strong>Ka-Band:</strong> Up-Link $= 27.5\text{--}31.0\text{ GHz}$ ($30\text{ GHz}$); Down-Link $= 17.7\text{--}21.2\text{ GHz}$ ($20\text{ GHz}$).</li>
  </ul>
  <p><strong>Physical Rationale:</strong> Higher frequencies suffer higher free-space path loss ($L_{\text{path}} \propto f^2$). Ground earth stations have access to virtually unlimited electrical power grids to drive high-wattage Traveling Wave Tube Amplifiers (TWTAs) for the higher up-link frequency, whereas satellite transponders are strictly constrained by onboard solar panel energy budgets, necessitating the lower frequency for the down-link!</p>
</div>
"""

M2_FINISH = r"""
<h2 class="section-title">Topic 19.8: Advanced Digital Signal Processing & Orthogonal Frequency Division Multiplexing (OFDM)</h2>

<p>
  Modern broadband wireless and wireline standards (Wi-Fi 6/7, 4G LTE, 5G NR, DSL, DVB-T2) replace single-carrier modulation with <strong>Orthogonal Frequency Division Multiplexing (OFDM)</strong>.
</p>

<div class="diagram-container">
  <svg width="100%" height="80" viewBox="0 0 740 80" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="15" width="130" height="50" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="85" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#1e40af" text-anchor="middle">Serial Bitstream</text>
    <text x="85" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#2563eb" text-anchor="middle">High-Speed Data</text>

    <path d="M 150 40 L 210 40" stroke="#0284c7" stroke-width="1.8"/>

    <rect x="215" y="15" width="120" height="50" rx="4" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.2"/>
    <text x="275" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#14532d" text-anchor="middle">Serial-to-Parallel</text>
    <text x="275" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#16a34a" text-anchor="middle">$N$ Parallel Streams</text>

    <path d="M 335 40 L 395 40" stroke="#0284c7" stroke-width="1.8"/>

    <rect x="400" y="15" width="130" height="50" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
    <text x="465" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#92400e" text-anchor="middle">IFFT Algorithm</text>
    <text x="465" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#b45309" text-anchor="middle">Inverse Fast Fourier</text>

    <path d="M 530 40 L 590 40" stroke="#0284c7" stroke-width="1.8"/>

    <rect x="595" y="15" width="125" height="50" rx="4" fill="#faf5ff" stroke="#a855f7" stroke-width="1.2"/>
    <text x="657" y="38" font-family="Plus Jakarta Sans" font-size="10" font-weight="700" fill="#581c87" text-anchor="middle">Cyclic Prefix (CP)</text>
    <text x="657" y="52" font-family="Plus Jakarta Sans" font-size="8.5" fill="#9333ea" text-anchor="middle">Eliminates ISI</text>
  </svg>
  <div class="diagram-caption">Figure 2.2: Orthogonal Frequency Division Multiplexing (OFDM) Baseband Signal Generation</div>
</div>

<div class="formula-card">
  <strong>The Orthogonality Condition in OFDM:</strong>
  Subcarrier frequencies $f_k = k \Delta f = \frac{k}{T_{\text{sym}}}$ are spaced at exact intervals $\Delta f = \frac{1}{T_{\text{sym}}}$, guaranteeing zero mutual inter-carrier interference (ICI):
  $$\mathbf{\frac{1}{T_{\text{sym}}} \int_0^{T_{\text{sym}}} \cos(2\pi f_i t) \cos(2\pi f_j t) \, dt = \begin{cases} 0 & i \neq j \\ \frac{1}{2} & i = j \end{cases}}$$
</div>
"""

def finish_m1_m2():
    with open(os.path.join(DCCN_DIR, "dccn_module1_content.py"), "r", encoding="utf-8") as f:
        m1 = f.read()
    if "Topic 13.9: Advanced Communication" not in m1:
        m1 = m1.rstrip().rstrip('"""').rstrip() + M1_FINISH + '\n"""\n'
        with open(os.path.join(DCCN_DIR, "dccn_module1_content.py"), "w", encoding="utf-8") as f:
            f.write(m1)
        print("Finished M1")

    with open(os.path.join(DCCN_DIR, "dccn_module2_content.py"), "r", encoding="utf-8") as f:
        m2 = f.read()
    if "Topic 19.8: Advanced Digital Signal" not in m2:
        m2 = m2.rstrip().rstrip('"""').rstrip() + M2_FINISH + '\n"""\n'
        with open(os.path.join(DCCN_DIR, "dccn_module2_content.py"), "w", encoding="utf-8") as f:
            f.write(m2)
        print("Finished M2")

if __name__ == "__main__":
    finish_m1_m2()
