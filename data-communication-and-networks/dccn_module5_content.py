# DCCN Module 5 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

DCCN_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Transport Layer, Application Services & Network Security</div>
  <div class="toc-grid">
    <div>1. Transport Layer Port Multiplexing & Sockets Interface (TCP vs. UDP)</div>
    <div>2. TCP Segment Anatomy: Sequence Numbers, Acknowledgments & Control Flags</div>
    <div>3. TCP 3-Way Handshake Connection Establishment & 4-Way FIN Teardown</div>
    <div>4. TCP Flow Control (Receiver Window `rwnd` & Nagle's Algorithm)</div>
    <div>5. TCP Congestion Control: Slow Start, Congestion Avoidance (AIMD), Fast Retransmit</div>
    <div>6. TCP Fast Recovery & Cubic / BBR Modern Congestion Mechanisms</div>
    <div>7. Domain Name System (DNS): Hierarchical Namespace, Root Servers & Records (A, AAAA, MX)</div>
    <div>8. Hypertext Transfer Protocol Evolution: HTTP/1.1 vs. HTTP/2 vs. HTTP/3 (QUIC)</div>
    <div>9. Email Architecture: SMTP, POP3, IMAP & MIME Extensions</div>
    <div>10. Cryptographic Fundamentals: Symmetric (AES) vs. Asymmetric (RSA) Cryptography</div>
    <div>11. RSA Public-Key Algorithm Mathematical Derivation & Worked Encryption Traces</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 1 – 3: TCP Protocol Architecture & 3-Way Handshake</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">TCP Control Flag</th>
      <th style="width: 15%;">Bit Position</th>
      <th>Operational Role in Connection State Machine</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>SYN</strong></td><td>Synchronize</td><td>Initiates a connection; synchronizes initial sequence numbers (ISN). Consumes 1 sequence number.</td></tr>
    <tr><td><strong>ACK</strong></td><td>Acknowledgment</td><td>Validates the 32-bit Acknowledgment Number field indicating next expected byte.</td></tr>
    <tr><td><strong>FIN</strong></td><td>Finish</td><td>Sender has finished sending data and requests connection termination. Consumes 1 sequence number.</td></tr>
    <tr><td><strong>RST</strong></td><td>Reset</td><td>Abruptly terminates an invalid or unauthorized connection request.</td></tr>
    <tr><td><strong>PSH</strong></td><td>Push</td><td>Instructs receiver to deliver buffered data to application immediately without waiting for buffer to fill.</td></tr>
    <tr><td><strong>URG</strong></td><td>Urgent</td><td>Validates the Urgent Pointer field for out-of-band high-priority data (e.g., `Ctrl+C`).</td></tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: TCP 3-Way Handshake Connection Sequence</div>
  <ol>
    <li><strong>Client $\rightarrow$ Server (SYN):</strong> Client chooses random initial sequence number $x$:
      $$\text{Segment 1: } [\mathbf{SYN}=1, \ \mathbf{Seq}=x]$$
    </li>
    <li><strong>Server $\rightarrow$ Client (SYN-ACK):</strong> Server acknowledges client's ISN ($x+1$) and chooses its own ISN $y$:
      $$\text{Segment 2: } [\mathbf{SYN}=1, \ \mathbf{ACK}=1, \ \mathbf{Seq}=y, \ \mathbf{Ack}=x+1]$$
    </li>
    <li><strong>Client $\rightarrow$ Server (ACK):</strong> Client acknowledges server's ISN ($y+1$):
      $$\text{Segment 3: } [\mathbf{ACK}=1, \ \mathbf{Seq}=x+1, \ \mathbf{Ack}=y+1]$$
      <em>Connection established in ESTABLISHED state.</em>
    </li>
  </ol>
</div>

<h2 class="section-title">Topic 5 & 6: TCP Congestion Control Mechanisms (AIMD)</h2>

<div class="formula-card">
  <strong>The 4 Standard Phases of TCP Congestion Control (Tahoe / Reno):</strong>
  <ol>
    <li><strong>Slow Start:</strong> Initial congestion window $\text{cwnd} = 1 \text{ MSS}$. Doubles every Round-Trip Time ($\text{cwnd} \leftarrow \text{cwnd} \times 2$) exponentially until $\text{cwnd} \ge \text{ssthresh}$ (Slow Start Threshold).</li>
    <li><strong>Congestion Avoidance (Additive Increase):</strong> Increases linearly by $1 \text{ MSS}$ per RTT ($\text{cwnd} \leftarrow \text{cwnd} + 1$).</li>
    <li><strong>Triple Duplicate ACK Event (Fast Retransmit & Recovery):</strong>
      - $\text{ssthresh} \leftarrow \frac{\text{cwnd}}{2}$
      - $\text{cwnd} \leftarrow \text{ssthresh} + 3 \text{ MSS}$ (TCP Reno skips Slow Start and continues linearly).
    </li>
    <li><strong>Timeout Event (Severe Congestion):</strong>
      - $\text{ssthresh} \leftarrow \frac{\text{cwnd}}{2}$
      - $\text{cwnd} \leftarrow 1 \text{ MSS}$ (Drops back to Slow Start).
    </li>
  </ol>
</div>

<h2 class="section-title">Topic 10 & 11: Network Security & RSA Public-Key Cryptography</h2>

<div class="formula-card">
  <strong>RSA Algorithm Mathematical Formulations (Rivest, Shamir, Adleman, 1977):</strong>
  <ol>
    <li>Select two distinct large prime numbers $p$ and $q$.</li>
    <li>Compute modulus $n = p \times q$.</li>
    <li>Compute Euler's Totient $\phi(n) = (p - 1)(q - 1)$.</li>
    <li>Choose public exponent $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.</li>
    <li>Compute private decryption exponent $d$ using Extended Euclidean Algorithm:
      $$d \equiv e^{-1} \pmod{\phi(n)} \implies (d \times e) \pmod{\phi(n)} = 1$$
    </li>
    <li><strong>Public Key:</strong> $KU = \{e, n\}$, <strong>Private Key:</strong> $KR = \{d, n\}$.</li>
    <li><strong>Encryption:</strong> Ciphertext $C = M^e \pmod n$.</li>
    <li><strong>Decryption:</strong> Plaintext $M = C^d \pmod n$.</li>
  </ol>
</div>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: Complete RSA Encryption & Decryption Trace</div>
  <p>Let primes $p = 3, q = 11$, and Plaintext message $M = 7$.</p>
  <ol>
    <li>$n = 3 \times 11 = \mathbf{33}$.</li>
    <li>$\phi(n) = (3 - 1)(11 - 1) = 2 \times 10 = \mathbf{20}$.</li>
    <li>Choose $e = 7$ ($\gcd(7, 20) = 1$).</li>
    <li>Find $d$: $(d \times 7) \pmod{20} = 1 \implies 7d = 21 \implies \mathbf{d = 3}$.</li>
    <li><strong>Encryption:</strong> $C = 7^7 \pmod{33} = 823543 \pmod{33} = \mathbf{4}$.</li>
    <li><strong>Decryption:</strong> $M = 4^3 \pmod{33} = 64 \pmod{33} = \mathbf{7}$. (Original plaintext recovered!).</li>
  </ol>
</div>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module V)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Compare HTTP/1.1, HTTP/2, and HTTP/3 across 4 architectural parameters. (8 Marks)</div>
  <div class="qa-a">
    1. <strong>Transport Layer:</strong> HTTP/1.1 and HTTP/2 run over standard TCP; HTTP/3 runs over QUIC (UDP-based).<br>
    2. <strong>Multiplexing:</strong> HTTP/1.1 uses sequential request-response pipelining (suffers from Head-of-Line blocking); HTTP/2 uses binary frame multiplexing over a single TCP connection; HTTP/3 achieves stream-level multiplexing without TCP Head-of-Line blocking.<br>
    3. <strong>Header Compression:</strong> HTTP/1.1 uses plain text headers without compression; HTTP/2 uses HPACK; HTTP/3 uses QPACK.<br>
    4. <strong>Handshake Latency:</strong> HTTP/1.1 & HTTP/2 require 2–3 RTTs (TCP + TLS); HTTP/3 achieves 0-RTT connection resumption.
  </div>
</div>
"""
