# 🌐 Data Communication and Computer Networks (CS24305) — Syllabus & Study Guide

> **Academic Program:** B.Tech in Computer Science & Engineering  
> **Scheme:** NEP Scheme (2024–25) | BIT Mesra  
> **Semester:** 5th Semester  
> **Course Code:** `CS24305` (Theory) — **3.0 Credits**  
> **Co-requisite Lab:** `CS24306` (Practical) — **1.5 Credits**  
> **Total Credits:** **4.5 Credits**

---

## 📌 Table of Contents
1. [Course Overview & Learning Outcomes](#-course-overview--learning-outcomes)
2. [Theory Syllabus (Modules I – V)](#-theory-syllabus-cs24305)
   - [Module I: Data Communications & Networking Overview](#module-i--data-communications--networking-overview)
   - [Module II: Transmission Media & Signal Encoding Techniques](#module-ii--transmission-media--signal-encoding-techniques)
   - [Module III: Error Handling, Data Link Control & Multiplexing](#module-iii--error-handling-data-link-control--multiplexing)
   - [Module IV: Wide Area Networks & Local Area Networks](#module-iv--wide-area-networks--local-area-networks)
   - [Module V: Internetworking, Routing & Application Protocols](#module-v--internetworking-routing--application-protocols)
3. [Lab Syllabus (CS24306)](#-lab-syllabus-cs24306)
4. [Standard Reference Books & Recommended Reading](#-recommended-textbooks--references)
5. [Key Exam Topics & High-Yield Questions](#-high-yield-exam-topics--question-bank)
6. [Interactive Study Tracker](#-interactive-study-tracker)

---

## 🎯 Course Overview & Learning Outcomes

This course provides a comprehensive foundation in the principles, architectures, protocols, and mechanisms of modern computer networks and data communication systems. It covers the complete network protocol stack from the physical layer signaling and data link protocols to network routing and application layer architectures.

```
+-------------------------------------------------------------+
| APPLICATION LAYER : HTTP, DNS, SMTP, DHCP, FTP             |
+-------------------------------------------------------------+
| TRANSPORT LAYER   : TCP (Reliable/Flow/Congestion), UDP     |
+-------------------------------------------------------------+
| NETWORK LAYER     : IPv4/IPv6 Addressing, Subnetting, OSPF, |
|                     BGP, Distance Vector / Dijkstra Routing |
+-------------------------------------------------------------+
| DATA LINK LAYER   : Framing, CRC, Hamming, Flow/Error ARQ,  |
|                     HDLC, Ethernet MAC, CSMA/CD, VLANs      |
+-------------------------------------------------------------+
| PHYSICAL LAYER    : Guided/Wireless Media, Digital NRZ/Man, |
|                     Analog ASK/FSK/PSK, Multiplexing (TDM)  |
+-------------------------------------------------------------+
```

---

## 📖 Theory Syllabus: CS24305

### Module I – Data Communications & Networking Overview
*Focus: Communication models, transmission concepts, transmission impairments, and layered protocol architectures.*

- [ ] **Communications Model:** Source, Transmitter, Transmission System, Receiver, Destination
- [ ] **Data Communications:** Digital vs. Analog data, Signals, Line configurations (Point-to-Point, Multipoint), Transmission modes (Simplex, Half-Duplex, Full-Duplex)
- [ ] **Networks & The Internet:** Network topologies (Mesh, Star, Bus, Ring, Hybrid), Network types (LAN, MAN, WAN), Internet architecture & history
- [ ] **Layered Protocol Architectures:**
  - **OSI 7-Layer Model:** Physical, Data Link, Network, Transport, Session, Presentation, Application layers (functions, services, encapsulation)
  - **TCP/IP Protocol Suite:** 4/5-layer model, mapping with OSI model
  - Protocol data units (PDUs), Service data units (SDUs), and Header overheads
- [ ] **Data Transmission Concepts & Impairments:**
  - Time domain vs. Frequency domain concepts of signals, Bandwidth vs. Spectrum
  - **Transmission Impairments:** Attenuation, Delay Distortion, Thermal Noise, Intermodulation Noise, Crosstalk, Impulse Noise
  - Signal-to-Noise Ratio ($SNR$) and Decibel ($dB$) calculations
- [ ] **Channel Capacity Theorems:**
  - **Nyquist Maximum Data Rate (Noiseless Channel):** $C = 2B \log_2(M) \text{ bps}$
  - **Shannon Channel Capacity (Noisy Channel):** $C = B \log_2(1 + SNR) \text{ bps}$
  - Trade-off between Bandwidth and Signal-to-Noise Ratio

---

### Module II – Transmission Media & Signal Encoding Techniques
*Focus: Guided and wireless physical media, digital baseband encoding, and analog modulation schemes.*

- [ ] **Guided Transmission Media:**
  - **Twisted Pair Cable:** Unshielded (UTP Category 3/5e/6), Shielded (STP), Characteristic impedance, Attenuation vs. Frequency
  - **Coaxial Cable:** Baseband vs. Broadband, Construction, Velocity factor
  - **Optical Fiber:** Step-Index vs. Graded-Index Multimode fiber, Single-Mode fiber, Total Internal Reflection, Critical angle, Dispersion, Attenuation characteristics
- [ ] **Wireless Transmission & Propagation:**
  - Terrestrial Microwave, Satellite Microwave, Broadcast Radio, Infrared
  - Propagation modes: Ground-wave ($< 2 \text{ MHz}$), Sky-wave ($2 - 30 \text{ MHz}$), Line-of-sight ($> 30 \text{ MHz}$)
- [ ] **Digital Signal Encoding Techniques (Data $\rightarrow$ Digital Signal):**
  - Non-Return to Zero-Level (NRZ-L) & Non-Return to Zero-Invert (NRZI)
  - Multilevel Binary: Bipolar-AMI (Alternate Mark Inversion), Pseudoternary
  - Biphase / Self-Clocking: **Manchester** (Ethernet), **Differential Manchester** (Token Ring)
  - Scrambling techniques: B8ZS (North America), HDB3 (Europe)
- [ ] **Analog Modulation Techniques (Data $\rightarrow$ Analog Carrier Signal):**
  - **Amplitude Shift Keying (ASK)** & Binary ASK
  - **Frequency Shift Keying (FSK)** & Multiple FSK (MFSK)
  - **Phase Shift Keying (PSK):** Binary PSK (BPSK), Quadrature PSK (QPSK), Offset QPSK
  - **Quadrature Amplitude Modulation (QAM):** 16-QAM, 64-QAM, Constellation diagrams
- [ ] **Analog Data to Digital Signals:** Pulse Code Modulation (PCM), Sampling theorem (Nyquist rate $f_s \ge 2f_{\max}$), Quantization noise, Delta Modulation (DM), Slope overload distortion

---

### Module III – Error Handling, Data Link Control & Multiplexing
*Focus: Error detection and correction mathematics, sliding window ARQ protocols, HDLC, and multiplexing.*

- [ ] **Types of Transmission Errors:** Single-bit errors, Burst errors (Burst length definition)
- [ ] **Error Detection Techniques:**
  - Simple Parity Check (Even/Odd parity, Longitudinal Redundancy Check)
  - Internet Checksum algorithm (One's complement arithmetic and verification)
  - **Cyclic Redundancy Check (CRC):** Polynomial representation, Modulo-2 binary division, Generator polynomial properties, CRC-12, CRC-16, CRC-CCITT, CRC-32
- [ ] **Error Correction Techniques:**
  - Hamming Distance ($d_{\min}$), Minimum distance requirements ($d_{\min} \ge 2t + 1$ for correcting $t$ errors)
  - **Hamming Code:** Parity bit position formula ($2^k \ge m + k + 1$), Error syndrome decoding and single-bit correction
- [ ] **Data Link Flow Control & Error Control (ARQ Protocols):**
  - **Stop-and-Wait Flow Control:** Efficiency $\eta = \frac{T_{\text{frame}}}{T_{\text{frame}} + 2T_{\text{prop}}} = \frac{1}{1 + 2a}$, where $a = \frac{T_{\text{prop}}}{T_{\text{trans}}}$
  - **Sliding Window Protocol:** Sender and Receiver window mechanics, Sequence numbers
  - **Stop-and-Wait ARQ:** Handling lost frames and lost ACKs with timeouts
  - **Go-Back-N (GBN) ARQ:** Sliding window size $W_s \le 2^k - 1, W_r = 1$, Cumulative ACKs, Retransmission upon timeout
  - **Selective Repeat (SR) ARQ:** Sliding window size $W_s = W_r \le 2^{k-1}$, Individual ACKs, Negative Acknowledgement (NAK), Buffering out-of-order frames
  - Efficiency derivations and bandwidth-delay product implications
- [ ] **High-Level Data Link Control (HDLC):** Frame format, Bit-stuffing (0-insertion after five consecutive 1s: `0111110`), Frame types (I-Frames, S-Frames, U-Frames)
- [ ] **Multiplexing Techniques:** Frequency Division Multiplexing (FDM), Time Division Multiplexing (Synchronous TDM vs. Statistical / Asynchronous TDM), Wavelength Division Multiplexing (WDM)

---

### Module IV – Wide Area Networks & Local Area Networks
*Focus: Circuit vs packet switching, cellular networks, Ethernet MAC, and VLANs.*

- [ ] **Switching Paradigms:**
  - **Circuit Switching:** Three phases (Circuit establishment, Data transfer, Circuit disconnect), Dedicated channel, Zero queuing delay during transfer
  - **Packet Switching:** Store-and-forward mechanism, Datagram approach (Connectionless, dynamic routing, packets can arrive out-of-order) vs. Virtual Circuit approach (Connection-oriented, logical channel, fixed path, in-order delivery)
  - Comparison of Circuit Switching, Datagram Packet Switching, and Virtual Circuit Packet Switching (Delay analysis)
- [ ] **Cellular Network Principles & Generations:**
  - Frequency reuse concept, Cluster size ($N = i^2 + ij + j^2$), Cellular geometry (Hexagonal cells), Co-channel interference ($Q = \sqrt{3N}$)
  - Handoff strategies (Hard handoff vs. Soft handoff), Cell splitting, Cell sectoring
  - Cellular evolution: 1G (AMPS, analog), 2G (GSM, CDMA, digital voice), 3G (UMTS, CDMA2000, mobile data), 4G (LTE, all-IP, OFDM), 5G (mmWave, Massive MIMO, Network Slicing)
- [ ] **Local Area Network (LAN) Technologies:**
  - IEEE 802 Architecture, Media Access Control (MAC) and Logical Link Control (LLC)
  - **Traditional Ethernet (IEEE 802.3):** 10BASE-T, 10BASE-2, 10BASE-5, CSMA/CD protocol (Carrier Sense, Collision Detection, Binary Exponential Backoff Algorithm)
  - **High-Speed Ethernet:** Fast Ethernet (100BASE-TX), Gigabit Ethernet (1000BASE-T), 10-Gigabit Ethernet, Full-duplex Ethernet without collisions
  - **Wireless LAN (IEEE 802.11 / Wi-Fi):** Architecture (BSS, ESS, AP), CSMA/CA protocol, Interframe Spaces (DIFS, SIFS, PIFS), RTS/CTS mechanism for Hidden Terminal & Exposed Terminal problems
  - **Virtual LANs (VLANs):** IEEE 802.1Q tag, Broadcast domain segmentation, Port-based vs Tag-based VLANs

---

### Module V – Internetworking, Routing & Application Protocols
*Focus: IP addressing, subnetting, transport layer protocols, dynamic routing algorithms, and application protocols.*

- [ ] **Internet Protocol & Addressing:**
  - **IPv4 Protocol:** Header format, Fields (IHL, ToS, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Header Checksum), Fragmentation & Reassembly
  - **Classful Addressing:** Class A, B, C, D, E boundaries, Network ID, Host ID, Default subnet masks
  - **Classless Inter-Domain Routing (CIDR) & Subnetting:** Subnet masks, Variable Length Subnet Masking (VLSM), Slash notation (`/24`, `/28`), Subnet calculation exercises (Network address, Broadcast address, Usable host range)
  - **IPv6 Overview:** 128-bit address space, Header format simplification, Transition mechanisms (Dual-stack, Tunneling)
- [ ] **Transport Layer Protocols:**
  - **User Datagram Protocol (UDP):** Connectionless, Unreliable, 8-byte minimal header, Use cases (DNS, Video streaming, VoIP)
  - **Transmission Control Protocol (TCP):** Connection-oriented, Stream-oriented, Reliable data transfer, Header format (Seq Num, Ack Num, Flags: SYN, ACK, FIN, RST, PSH, URG), Three-Way Handshake connection establishment (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`), Connection teardown (4-way FIN handshake)
  - **TCP Flow Control:** Sliding Window mechanism, Silly Window Syndrome & Nagle's Algorithm
  - **TCP Congestion Control:** Additive Increase Multiplicative Decrease (AIMD), Slow Start ($cwnd$ doubles every RTT until $ssthresh$), Congestion Avoidance (linear growth), Fast Retransmit (3 duplicate ACKs), Fast Recovery (TCP Tahoe vs. TCP Reno)
- [ ] **Unicast Routing Algorithms:**
  - Autonomous Systems (AS), Interior Gateway Protocols (IGP) vs. Exterior Gateway Protocols (EGP)
  - **Distance Vector Routing:** Bellman-Ford algorithm, Routing Information Protocol (RIP), Count-to-Infinity problem, Split Horizon and Poison Reverse solutions
  - **Link State Routing:** Dijkstra's Shortest Path First (SPF) algorithm, Link State Advertisements (LSAs), Open Shortest Path First (OSPF) protocol
  - **Path Vector Routing:** Border Gateway Protocol (BGP-4), Policy-based inter-domain routing
- [ ] **Application Layer Protocols:**
  - **Domain Name System (DNS):** Hierarchical domain namespace, Recursive vs. Iterative queries, Resource records (A, AAAA, CNAME, MX, NS, PTR)
  - **Dynamic Host Configuration Protocol (DHCP):** DORA process (Discover, Offer, Request, Acknowledge), Lease management
  - **Hypertext Transfer Protocol (HTTP):** HTTP/1.0, HTTP/1.1 (Persistent connections, Pipelining), HTTP/2 (Multiplexing, Header compression), HTTP/3 (QUIC), Methods (`GET`, `POST`, `PUT`, `DELETE`), Status codes
  - **Email Protocols:** Simple Mail Transfer Protocol (SMTP), Post Office Protocol (POP3), Internet Message Access Protocol (IMAP4)

---

## 🧪 Lab Syllabus: CS24306

| Lab Module | Core Practical Objectives & Tasks |
| :--- | :--- |
| **Lab Module I** | **UNIX/Linux Network Tools & Basic Simulations**<br>• Network inspection commands: `ifconfig`, `ip addr`, `ping`, `traceroute`, `netstat`, `nslookup`, `dig`, `arp`, `route`.<br>• Packet capture using Wireshark / `tcpdump`.<br>• Simulation of ARP resolution and LAN packet forwarding. |
| **Lab Module II** | **Data Link Framing & Error Control Implementation**<br>• Implement Character Stuffing and Bit Stuffing / Destuffing algorithms in C/C++.<br>• Implement 1D Parity, 2D Longitudinal Parity, and Internet Checksum.<br>• Implement Hamming Code $(7, 4)$ generation, error injection, and single-bit correction. |
| **Lab Module III** | **CRC & Network Topology Simulation**<br>• Implement CRC-12, CRC-16, CRC-CCITT, and CRC-32 with custom generator polynomials in C/C++.<br>• Build multi-node subnets and simulated queues in NS-2 / NS-3 / Cisco Packet Tracer.<br>• Measure packet drop rates, throughput, and end-to-end latency under variable traffic loads. |
| **Lab Module IV** | **Routing Algorithms & IP Calculations**<br>• Implement IPv4 address classification and subnet calculation utility in C/C++ / Python.<br>• Implement Dijkstra's Shortest Path routing algorithm on graph representations.<br>• Implement Distance Vector Routing (Bellman-Ford) simulation with step-by-step routing table convergence.<br>• Simulate Leaky Bucket and Token Bucket traffic shaping algorithms. |
| **Lab Module V** | **Socket Programming & Client-Server Applications**<br>• IPC Mechanisms in C: Named Pipes (FIFO), Message Queues, Shared Memory.<br>• Implement iterative TCP Echo Client-Server using BSD Sockets (`socket`, `bind`, `listen`, `accept`, `connect`, `send`, `recv`).<br>• Implement multi-client Concurrent TCP Chat Server using `fork()` / multithreading `pthread` / `select()`.<br>• Implement UDP Client-Server application (`sendto`, `recvfrom`). |

---

## 📚 Recommended Textbooks & References

1. **"Data Communications and Networking with TCP/IP Protocol Suite"**  
   *Behrouz A. Forouzan* — McGraw Hill Education (6th / 5th Edition).  
   *(Primary text for data communications, physical layer encoding, data link protocols, and subnetting).*
2. **"Computer Networks"**  
   *Andrew S. Tanenbaum, David J. Wetherall, Nick Feamster* — Pearson (6th Edition).  
   *(Standard reference for layered architecture, MAC protocols, routing algorithms, transport protocols, and applications).*
3. **"Data and Computer Communications"**  
   *William Stallings* — Pearson Education (10th Edition).  
   *(In-depth theoretical analysis of transmission impairments, channel capacity, cellular networks, and ARQ protocols).*
4. **"Computer Networking: A Top-Down Approach"**  
   *James F. Kurose & Keith W. Ross* — Pearson (8th Edition).  
   *(Excellent reference for TCP congestion control, DNS, HTTP, socket programming, and Wireshark lab exercises).*

---

## 🌟 High-Yield Exam Topics & Question Bank

### Top Numerical & Analytical Problems
1. **Channel Capacity:** Calculate Nyquist maximum data rate and Shannon capacity for a channel with given bandwidth and SNR (in dB).
2. **Signal Encoding Waveforms:** Draw the digital waveforms for a given binary bit sequence (e.g., `01001110`) using NRZ-L, NRZI, Bipolar-AMI, Manchester, and Differential Manchester.
3. **CRC Calculation:** Given data word $D(x) = 1010001101$ and generator polynomial $G(x) = x^5 + x^4 + x^2 + 1$, compute the transmitted codeword and verify error detection at receiver.
4. **Hamming Code:** Compute the 7-bit Hamming codeword for a 4-bit data word `1011`. Given a received word with an error (e.g., `1001110`), calculate the error syndrome and correct the corrupted bit.
5. **ARQ Protocol Efficiency:** Derive the maximum throughput / link utilization for Stop-and-Wait ARQ, Go-Back-N ARQ ($N=7$), and Selective Repeat ARQ ($N=4$) given frame size, bit rate, propagation delay, and frame error probability.
6. **Subnetting & IP Calculations:** Given an IP block (e.g., `192.168.10.0/24`), design subnets for 4 departments requiring 60, 30, 14, and 6 hosts respectively using VLSM. Determine subnet masks, network IDs, and broadcast addresses.
7. **Dijkstra & Distance Vector Routing:** Trace step-by-step routing table updates for a given weighted network graph using Dijkstra's algorithm and Bellman-Ford algorithm.

### Critical Theoretical Questions
- Compare the OSI 7-Layer Model and TCP/IP 4-Layer Architecture with layer functionalities and data units.
- Explain the hidden terminal and exposed terminal problems in wireless LANs and how RTS/CTS resolves them.
- Compare Go-Back-N ARQ and Selective Repeat ARQ with sliding window mechanics and buffer requirements.
- Explain TCP Congestion Control mechanisms (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery) with a $cwnd$ vs. RTT graph.
- Differentiate between Distance Vector Routing and Link State Routing with convergence characteristics and count-to-infinity problem.

---

## 📊 Interactive Study Tracker

| Module | Core Concept | Topics Count | Status |
| :---: | :--- | :---: | :---: |
| **M1** | OSI vs TCP/IP, Signal Impairments, Nyquist & Shannon Capacity | 13 | ⬜ Not Started |
| **M2** | Guided/Wireless Media, NRZ, Manchester, ASK/FSK/PSK, QAM, PCM | 6 | ⬜ Not Started |
| **M3** | Checksum, CRC, Hamming Code, Stop-and-Wait, GBN, Selective Repeat, HDLC | 8 | ⬜ Not Started |
| **M4** | Circuit/Packet Switching, Cellular Reuse & Handoff, CSMA/CD, Wi-Fi CSMA/CA, VLAN | 9 | ⬜ Not Started |
| **M5** | IPv4/IPv6, VLSM Subnetting, TCP 3-Way Handshake & Congestion, Routing (Dijkstra/DVR), DNS/HTTP | 16 | ⬜ Not Started |
| **LAB** | Linux Commands, Framing, Hamming, Checksum, CRC, Dijkstra, DVR, TCP/UDP Socket Chat | 48 Tasks | ⬜ Not Started |

---
*Created for B.Tech 5th Semester CSE — Data Communication and Computer Networks (`CS24305` & `CS24306`).*
