# DCCN Module 2 Exhaustive Content (6 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DCCN_M2_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module II: Transmission Media & Signal Encoding — Complete 6-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 14:</strong> Guided Media (Twisted Pair UTP/STP, Coaxial Cable, Optical Fiber)</div>
    <div><strong>Topic 15:</strong> Wireless Media & Propagation (Ground, Sky, LOS, Satellite Microwave)</div>
    <div><strong>Topic 16:</strong> Digital Signaling (Line Codes: NRZ-L, NRZ-I, Manchester, AMI)</div>
    <div><strong>Topic 17:</strong> Analog Signaling (Carrier Parameter Representations)</div>
    <div><strong>Topic 18:</strong> Encoding Techniques (Line Coding Comparison & Tradeoffs)</div>
    <div><strong>Topic 19:</strong> Modulation Techniques (ASK, FSK, PSK & Constellation QAM)</div>
  </div>
</div>

<h2 class="section-title">Topic 14: Guided Transmission Media</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 22%;">Guided Medium</th>
      <th style="width: 45%;">Physical Architecture & Transmission Physics</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Twisted Pair Cable</strong></td>
      <td>Two insulated copper wires twisted in a helical spiral. Twisting ensures both wires receive equal electromagnetic interference (EMI), which cancels out at the differential receiver. Available as <strong>UTP</strong> (Unshielded) and <strong>STP</strong> (Shielded with metal foil).</td>
      <td>Inexpensive, lightweight, easy to terminate with RJ-45 connectors. Limited bandwidth ($\le 10 \text{ Gbps}$ over short distances), prone to crosstalk.</td>
    </tr>
    <tr>
      <td><strong>2. Coaxial Cable</strong></td>
      <td>Solid central copper conductor surrounded by dielectric insulating layer, enclosed in a braided cylindrical wire mesh shield and outer protective plastic jacket.</td>
      <td>Better noise immunity and higher bandwidth than twisted pair. Bulkier, stiffer, harder to install. Used in Cable TV broadband (DOCSIS).</td>
    </tr>
    <tr>
      <td><strong>3. Optical Fiber</strong></td>
      <td>Ultra-pure cylindrical glass core ($n_1$) surrounded by concentric glass cladding ($n_2$) where refractive index $n_1 > n_2$. Transmits light pulses via <strong>Total Internal Reflection</strong> whenever incident angle $\theta > \theta_{\text{critical}}$.</td>
      <td>Enormous bandwidth (terabits/sec), ultra-low attenuation ($\approx 0.2 \text{ dB/km}$), zero EMI susceptibility, lightweight, highly secure against wiretapping. Expensive splicing and optical transceivers.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 15: Wireless Transmission & Propagation [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Propagation Mode</th>
      <th style="width: 45%;">Atmospheric Interaction & Frequency Band</th>
      <th>Representative Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Ground-Wave Propagation</strong></td>
      <td>Signals follow the curvature of the earth via diffraction over the conductive ground surface ($< 2 \text{ MHz}$).</td>
      <td>AM radio broadcasting, maritime navigation.</td>
    </tr>
    <tr>
      <td><strong>2. Sky-Wave Propagation</strong></td>
      <td>Signals bounce back and forth between earth's surface and the charged ionosphere ($2\text{–}30 \text{ MHz}$).</td>
      <td>Shortwave (SW) international radio broadcasting, amateur radio.</td>
    </tr>
    <tr>
      <td><strong>3. Line-of-Sight (LOS)</strong></td>
      <td>Straight-line path between transmitting and receiving directional horn antennas ($> 30 \text{ MHz}$). Antennas must have clear Fresnel zone.</td>
      <td>Terrestrial microwave links, cellular base stations, Wi-Fi.</td>
    </tr>
  </tbody>
</table>

<h3 class="subsection-title">Satellite Microwave vs. Terrestrial Microwave [UPLOADED PYQ]:</h3>
<ul>
  <li><strong>Terrestrial Microwave:</strong> Uses parabolic dish antennas mounted on high towers spaced $30\text{–}50 \text{ km}$ apart due to Earth's horizon curvature. Low propagation delay ($< 1 \text{ ms}$).</li>
  <li><strong>Satellite Microwave:</strong> Earth station beams signal to a geostationary satellite at $35,786 \text{ km}$ altitude (Uplink), which amplifies and retransmits it on a different downlink frequency. High round-trip latency ($\approx 270\text{–}540 \text{ ms}$), but provides massive continental coverage.</li>
</ul>

<h2 class="section-title">Topic 16 & 18: Digital Line Coding Schemes [UPLOADED PYQ]</h2>

<div class="callout callout-warning">
  <div class="callout-title">[UPLOADED PYQ] Step-by-Step Waveform Rules for Bit Stream `001110011`</div>
  <table class="custom-table">
    <thead><tr><th>Encoding Scheme</th><th>Bit Transition Invariant Rule</th><th>Waveform Encoding for `001110011`</th></tr></thead>
    <tbody>
      <tr><td><strong>NRZ-L (Level)</strong></td><td>Bit `0` = Positive voltage ($+V$), Bit `1` = Negative voltage ($-V$).</td><td>`+V, +V, -V, -V, -V, +V, +V, -V, -V`</td></tr>
      <tr><td><strong>NRZ-I (Invert)</strong></td><td>Bit `1` = Transition at start of bit interval; Bit `0` = No transition.</td><td>Maintains previous level on `0`, flips on `1`.</td></tr>
      <tr><td><strong>Bipolar AMI</strong></td><td>Bit `0` = Zero voltage ($0V$); Bit `1` = Alternating $+V$ and $-V$.</td><td>`0V, 0V, +V, -V, +V, 0V, 0V, -V, +V`</td></tr>
      <tr><td><strong>Manchester (802.3)</strong></td><td>Bit `0` = High-to-Low transition at bit center; Bit `1` = Low-to-High transition at center.</td><td>Guarantees a mid-bit clock transition in every single bit!</td></tr>
      <tr><td><strong>Differential Manchester</strong></td><td>Always transitions at center. Bit `0` = Transition at start; Bit `1` = No transition at start.</td><td>Token Ring standard; immune to wire polarity inversion.</td></tr>
    </tbody>
  </table>
</div>

<h2 class="section-title">Topic 17 & 19: Carrier Modulation Techniques (ASK, FSK, PSK, QAM)</h2>

<p>
  Digital modulation alters one or more parameters of a high-frequency analog sinusoidal carrier $c(t) = A \cos(2\pi f_c t + \phi)$:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Modulation</th>
      <th style="width: 25%;">Modulated Parameter</th>
      <th style="width: 30%;">Mathematical Signal Equation</th>
      <th>Key Advantages & Tradeoffs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>ASK</strong></td><td>Amplitude</td><td>$s(t) = A_1 \cos(2\pi f_c t)$ for `1`, $A_0 \cos(2\pi f_c t)$ for `0`</td><td>Simple; highly susceptible to noise and fading.</td></tr>
    <tr><td><strong>FSK</strong></td><td>Frequency</td><td>$s(t) = A \cos(2\pi f_1 t)$ for `1`, $A \cos(2\pi f_2 t)$ for `0`</td><td>High noise immunity; requires more channel bandwidth.</td></tr>
    <tr><td><strong>BPSK / QPSK</strong></td><td>Phase</td><td>$s(t) = A \cos(2\pi f_c t + \phi_i)$ where $\phi_i \in \{0, \pi\}$</td><td>Excellent bit error rate (BER); standard in modern wireless.</td></tr>
    <tr><td><strong>QAM (16/64/256)</strong></td><td>Amplitude + Phase</td><td>$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$</td><td>Enormous spectral efficiency ($\log_2 M$ bits/baud); used in Wi-Fi & 5G.</td></tr>
  </tbody>
</table>

<h2 class="section-title">🧠 M2 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Draw the line coding waveforms for bit stream `001110011` using NRZ-L, NRZ-I, Bipolar AMI, Manchester, and Differential Manchester. (10 Marks)</div>
  <div class="qa-a">
    1. <strong>NRZ-L:</strong> High for `0`, Low for `1` $\rightarrow$ `High, High, Low, Low, Low, High, High, Low, Low`.<br>
    2. <strong>NRZ-I:</strong> Invert signal level on every `1`; no change on `0`.<br>
    3. <strong>Bipolar AMI:</strong> Zero volts for all `0`s; alternating $+V$ and $-V$ for each successive `1` $\rightarrow$ `0, 0, +V, -V, +V, 0, 0, -V, +V`.<br>
    4. <strong>Manchester:</strong> Every bit has mid-interval transition. `0` = High-to-Low; `1` = Low-to-High.<br>
    5. <strong>Differential Manchester:</strong> Mandatory mid-bit transition. Start-of-bit transition for `0`; no start transition for `1`.
  </div>
</div>
"""
