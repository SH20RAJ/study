# 📘 Data Communications & Computer Networks — Module I Notes
**Comprehensive 4-Page Revision Guide | BIT Mesra (CS24305)**

> **Module I:** Data Communications & Networking Overview  
> **Key Concepts:** Communications Model, Networks, OSI Model, TCP/IP, Transmission Impairments, Nyquist & Shannon Capacity Theorems.

---

## 📄 PAGE 1 – Data Communication Fundamentals

### 1. What is Data Communication?
**Definition:** Data communication is the exchange of data between two or more devices through a transmission medium.

```
Source → Sender → Transmission Medium → Receiver → Destination
                 ↑
              Protocol
```

| Component | Description |
| :--- | :--- |
| **Sender** | Device that originates and sends data (Computer, Workstation, Sensor) |
| **Receiver** | Device that accepts incoming data (Server, Printer, Mobile) |
| **Message** | Information (Text, Audio, Video, Binary) being transmitted |
| **Medium** | Physical transmission path (Twisted Pair, Coax, Fiber, Radio) |
| **Protocol** | Set of rules governing data communication syntax, semantics, and timing |

---

### 2. Characteristics of an Effective Data Communication System
- **Delivery:** Must deliver data to the correct destination and only to the intended user.
- **Accuracy:** Must deliver data accurately without corruption.
- **Timeliness:** Must deliver data in a timely manner (especially real-time audio/video).
- **Low Jitter:** Must maintain consistent packet arrival delay variation.

---

### 3. Types of Networks by Geographic Scope
| Network Type | Full Form | Geographic Coverage | Example |
| :--- | :--- | :--- | :--- |
| **PAN** | Personal Area Network | 1 – 10 meters | Bluetooth headset, smart watch |
| **LAN** | Local Area Network | Room, Building, Campus | Office Ethernet, University Wi-Fi |
| **MAN** | Metropolitan Area Network | Entire City (5 – 50 km) | Cable TV network, City Wi-Fi |
| **WAN** | Wide Area Network | Country, Continent, Worldwide | The Internet, Telecom backbones |

---

## 📄 PAGE 2 – Layered Architectures: OSI vs. TCP/IP

### 1. The OSI 7-Layer Reference Model
```
Layer 7: APPLICATION  ---> User interface, HTTP, FTP, SMTP, DNS
Layer 6: PRESENTATION ---> Encryption, Decryption, Compression, Data format conversion
Layer 5: SESSION      ---> Session checkpointing, Dialog control, Synchronization
Layer 4: TRANSPORT    ---> End-to-end reliable delivery, Port addressing, TCP, UDP
Layer 3: NETWORK      ---> Logical addressing (IP), Path determination, Routing
Layer 2: DATA LINK    ---> Framing, MAC addressing, Error detection (CRC), Flow control
Layer 1: PHYSICAL     ---> Bit transmission over physical wire/wireless medium
```

*Mnemonic:* **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing.

---

### 2. The TCP/IP Protocol Suite & Mapping to OSI
| TCP/IP Layer | OSI Equivalent Layers | Key Protocols & PDUs |
| :--- | :--- | :--- |
| **Application** | Application + Presentation + Session | HTTP, HTTPS, DNS, SMTP, FTP (Data / Messages) |
| **Transport** | Transport | TCP, UDP, SCTP (Segments / Datagrams) |
| **Internet** | Network | IPv4, IPv6, ICMP, ARP, OSPF, BGP (Packets) |
| **Network Access** | Data Link + Physical | Ethernet, IEEE 802.11, PPP, MAC (Frames & Bits) |

---

## 📄 PAGE 3 – Data Transmission, Impairments & Channel Capacity

### 1. Transmission Modes
- **Simplex:** Strictly unidirectional communication (e.g., Keyboard to CPU, Traditional TV broadcast).
- **Half-Duplex:** Bidirectional communication, but only one direction at a time (e.g., Walkie-Talkie).
- **Full-Duplex:** Simultaneous bidirectional communication on the same channel (e.g., Telephone call).

---

### 2. Transmission Impairments
1. **Attenuation:** Loss of signal strength over distance. Compensated using amplifiers (analog) or repeaters (digital). Decibel loss: $\text{dB} = 10 \log_{10}(P_2 / P_1)$.
2. **Delay Distortion:** Different frequency components travel through guided media at slightly different speeds, arriving out of phase at the receiver.
3. **Noise:** Unwanted electrical or thermal signals injected into the channel:
   - **Thermal (Johnson) Noise:** Agitation of electrons; unavoidable: $N_0 = kTB$.
   - **Intermodulation Noise:** Spurious sum/difference frequencies caused by non-linear components.
   - **Crosstalk:** Unwanted coupling between adjacent wire pairs.
   - **Impulse Noise:** Sudden non-continuous bursts of electromagnetic interference (lightning, power spikes).

---

### 3. Channel Capacity Theorems

#### Nyquist Capacity Theorem (For Noiseless Channels):
$$C = 2B \log_2(M) \text{ bps}$$
- $B$: Bandwidth of the channel in Hertz (Hz)
- $M$: Number of discrete signal levels (voltage levels)

#### Shannon Capacity Theorem (For Noisy Channels):
$$C = B \log_2(1 + \text{SNR}) \text{ bps}$$
- $\text{SNR} = \frac{\text{Signal Power}}{\text{Noise Power}}$ (linear ratio)
- $\text{SNR}_{\text{dB}} = 10 \log_{10}(\text{SNR}) \implies \text{SNR} = 10^{(\text{SNR}_{\text{dB}} / 10)}$

---

## 📄 PAGE 4 – Topologies & Quick Revision Cheat Sheet

### 1. Network Topologies Comparison
| Topology | Cabling Cost | Reliability | Bottleneck / Single Point of Failure |
| :--- | :--- | :--- | :--- |
| **Mesh** | Very High ($n(n-1)/2$ links) | Very High (Dedicated links) | High cost, complex port requirements |
| **Star** | Moderate ($n$ links) | Moderate | Central Hub / Switch failure disables network |
| **Bus** | Lowest (Single backbone) | Low | Backbone cable break halts entire network |
| **Ring** | Low ($n$ links) | Moderate | Single node or link failure breaks token ring |

---
*Created for B.Tech CSE 5th Semester — CS24305 Data Communication and Computer Networks.*
