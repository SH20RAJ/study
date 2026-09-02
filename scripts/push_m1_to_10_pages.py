#!/usr/bin/env python3
"""
Adds the final push to DCCN Module 1 to make it 10-11 pages.
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

M1_ONE_MORE = r"""
<h2 class="section-title">Topic 13.12: Master Solved Numerical on Shannon Capacity & Eb/N0</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 10: Energy-per-Bit to Noise Power Spectral Density Ratio ($E_b/N_0$)</div>
  <p>In digital communications, Signal-to-Noise Ratio (SNR) is related to the normalized parameter $\frac{E_b}{N_0}$ (energy per bit to noise power spectral density) by:</p>
  $$\mathbf{\frac{E_b}{N_0} = \text{SNR} \times \frac{B}{R}}$$
  <p>Where $B$ is channel bandwidth in Hz, and $R$ is bit rate in bps. If a satellite channel requires a bit rate $R = 2\text{ Mbps}$ over bandwidth $B = 1\text{ MHz}$ with $\text{SNR} = 15$ ($11.76\text{ dB}$):</p>
  $$\mathbf{\frac{E_b}{N_0} = 15 \times \frac{10^6 \text{ Hz}}{2 \times 10^6 \text{ bps}} = 15 \times 0.5 = \mathbf{7.5}}$$
  $$\mathbf{\left(\frac{E_b}{N_0}\right)_{\text{dB}} = 10 \log_{10}(7.5) \approx \mathbf{8.75 \text{ dB}}}$$
  <p><strong>Shannon's Ultimate Limit:</strong> As bandwidth $B \rightarrow \infty$, the minimum theoretical threshold for error-free transmission is the famous <strong>Shannon Limit</strong>:</p>
  $$\mathbf{\left(\frac{E_b}{N_0}\right)_{\text{min}} = \ln(2) \approx 0.693 = \mathbf{-1.59 \text{ dB}}}$$
</div>

<div class="qa-card">
  <div class="qa-q">Q16. Explain Baud Rate (Modulation Rate) vs. Bit Rate (Data Rate) with formula and modulation examples. (6 Marks)</div>
  <div class="qa-a">
    • <strong>Bit Rate ($R$):</strong> The number of binary bits ($0, 1$) transmitted per second (bps).<br>
    • <strong>Baud Rate ($S$):</strong> The number of distinct signal units (symbols) transmitted per second (baud).<br>
    $$\mathbf{R = S \times r = S \times \log_2(L)}$$
    Where $L$ is the number of constellation points/levels and $r = \log_2(L)$ is bits/symbol. In 256-QAM ($L=256 \implies r=8$), a baud rate of $S = 1000\text{ baud}$ produces a bit rate of $R = 8000\text{ bps}$!
  </div>
</div>
"""

def push_m1():
    with open(os.path.join(DCCN_DIR, "dccn_module1_content.py"), "r", encoding="utf-8") as f:
        m1 = f.read()
    if "Topic 13.12: Master Solved Numerical" not in m1:
        m1 = m1.rstrip().rstrip('"""').rstrip() + M1_ONE_MORE + '\n"""\n'
        with open(os.path.join(DCCN_DIR, "dccn_module1_content.py"), "w", encoding="utf-8") as f:
            f.write(m1)
        print("Pushed M1.")

if __name__ == "__main__":
    push_m1()
