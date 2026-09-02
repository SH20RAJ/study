Absolutely. I’ll make your **DCCN (CS24305) Master Notes** in the same style as CD: **complete M1–M5 coverage, no syllabus topic intentionally skipped, exam-focused explanations, formulas, diagrams, active-recall prompts, memory hooks, and actual uploaded-paper questions clearly separated from syllabus/question-bank questions.**

Your uploaded study guide lists **52 DCCN topics: 13 + 6 + 8 + 9 + 16**. 

One important distinction: the uploaded papers include **AI323/IT365 DCCN papers**, including 2025 mid/end papers, but they are not labelled CS24305 CSE papers. I’ll therefore mark those as **[UPLOADED PYQ]**, rather than pretending they are your exact CSE paper. Your uploaded study guide also contains a DCCN question bank covering the syllabus.

# 📘 DCCN — COMPLETE MASTER NOTES

### CS24305 | Data Communication & Computer Networks

---

# 🧠 0. THE ONE BIG PICTURE

Before memorizing anything, build this mental model:

```text
DATA
 ↓
SIGNAL
 ↓
TRANSMISSION MEDIA
 ↓
ENCODING / MODULATION
 ↓
DATA LINK
 ↓
SWITCHING
 ↓
NETWORK / IP
 ↓
ROUTING
 ↓
TRANSPORT
 ↓
APPLICATION
```

Or think:

> **Send → Encode → Carry → Detect Errors → Control → Switch → Route → Deliver → Application**

This single chain connects almost the entire syllabus.

---

# MODULE I — DATA COMMUNICATION & NETWORKING OVERVIEW

### 13 topics

Your syllabus covers Communication Model, Data Communication, Networks, Internet, OSI, TCP/IP, standards/layers, applications, transmission concepts, analog/digital transmission, impairments and channel capacity. 

---

# 1. Communication Model

Basic communication:

```text
Sender
  │
  ▼
Encoder
  │
  ▼
Transmission Medium
  │
  ▼
Decoder
  │
  ▼
Receiver
```

### Components

| Component | Meaning                          |
| --------- | -------------------------------- |
| Sender    | Generates data                   |
| Receiver  | Receives data                    |
| Message   | Information being transmitted    |
| Medium    | Physical/wireless path           |
| Encoder   | Converts information into signal |
| Decoder   | Recovers information             |
| Protocol  | Rules governing communication    |

### Protocol

A protocol defines:

* syntax
* semantics
* timing
* sequence
* error handling

### Memory hook

**S-M-M-P**

**S**ender → **M**essage → **M**edium → **P**rotocol

---

# 2. Data Communications

Data communication = exchange of data between devices through a communication medium.

### Characteristics

Good communication should provide:

* delivery
* accuracy
* timeliness
* low jitter

### Data representation

Data can represent:

* text
* numbers
* images
* audio
* video

### Transmission modes

#### Simplex

```text
A ─────────► B
```

One direction only.

Example: traditional television broadcasting.

#### Half-duplex

```text
A ─────────► B
A ◄───────── B
```

Both directions, but not simultaneously.

Example: walkie-talkie.

#### Full-duplex

```text
A ◄────────► B
```

Both directions simultaneously.

Example: telephone.

**[UPLOADED PYQ]** asks for the main transmission modes. 

---

# 3. Networks

A computer network is a collection of interconnected devices that communicate and share resources.

## Types by geographical size

```text
PAN → LAN → MAN → WAN
```

### PAN

Personal Area Network.

Small personal range.

Example:

```text
Phone ↔ Earbuds ↔ Smartwatch
```

### LAN

Local Area Network.

* building/campus
* high speed
* usually privately managed

### MAN

Metropolitan Area Network.

Covers a city/metropolitan region.

### WAN

Wide Area Network.

Covers large geographical regions.

Example: Internet.

### Comparison

| PAN        | LAN             | MAN    | WAN           |
| ---------- | --------------- | ------ | ------------- |
| Personal   | Building/campus | City   | Country/world |
| Very small | Small           | Medium | Huge          |

---

# 4. Internet

The Internet is a global **network of interconnected networks** using the TCP/IP protocol suite.

```text
Device
  ↓
LAN
  ↓
Router
  ↓
ISP
  ↓
Internet
  ↓
Server
```

Important ideas:

* packet switching
* routers
* IP addressing
* TCP/UDP
* DNS
* application protocols

---

# 5. OSI Model

The OSI model contains **7 layers**.

```text
7  Application
6  Presentation
5  Session
4  Transport
3  Network
2  Data Link
1  Physical
```

### Memory trick

> **All People Seem To Need Data Processing**

A → P → S → T → N → D → P

---

## Layer 7 — Application

Provides network services to applications.

Examples:

* HTTP
* FTP
* SMTP
* DNS

---

## Layer 6 — Presentation

Deals with:

* translation
* encryption/decryption
* compression

Example:

```text
ASCII ↔ another representation
```

---

## Layer 5 — Session

Manages sessions/dialogues.

Functions:

* establish session
* maintain session
* terminate session
* synchronization

---

## Layer 4 — Transport

End-to-end delivery.

Important concepts:

* segmentation
* reassembly
* flow control
* error control
* reliability

Protocols:

* TCP
* UDP

---

## Layer 3 — Network

Responsible for:

* logical addressing
* routing
* packet forwarding

Protocol:

* IP

Device:

* router

---

## Layer 2 — Data Link

Responsible for:

* framing
* MAC addressing
* error detection
* flow control
* medium access

Devices:

* switches/bridges

---

## Layer 1 — Physical

Transmits raw bits.

Deals with:

* voltage
* connectors
* cables
* bit transmission
* signal characteristics

---

# 6. TCP/IP Protocol Architecture

Your syllabus specifically includes TCP/IP architecture. 

Common 4-layer representation:

```text
Application
     ↓
Transport
     ↓
Internet
     ↓
Network Access
```

### Application

HTTP, DNS, SMTP, FTP, DHCP etc.

### Transport

TCP / UDP.

### Internet

IP, ICMP etc.

### Network Access

Physical transmission + data-link functionality.

---

## OSI vs TCP/IP

| OSI                             | TCP/IP                              |
| ------------------------------- | ----------------------------------- |
| 7 layers                        | 4-layer representation              |
| Reference model                 | Protocol architecture               |
| Developed by ISO                | Developed around Internet protocols |
| Session & Presentation separate | Usually part of Application         |
| Data Link + Physical separate   | Often combined as Network Access    |

**[UPLOADED PYQ]** directly asks to compare OSI and TCP/IP. 

**[UPLOADED PYQ]** also asks TCP/IP architecture and layer functions. 

---

# 7. Standards and Protocol Layers

Layering divides networking into manageable functions.

```text
Application
────────────
Transport
────────────
Network
────────────
Data Link
────────────
Physical
```

### Why layering?

* modularity
* easier design
* easier troubleshooting
* interoperability
* independent development

### Encapsulation

Sender:

```text
Application Data
      ↓
Transport Segment
      ↓
Network Packet
      ↓
Data-Link Frame
      ↓
Bits
```

Receiver performs reverse:

```text
Bits
 ↓
Frame
 ↓
Packet
 ↓
Segment
 ↓
Data
```

---

# 8. Internet Applications

| Application          | Protocol   |
| -------------------- | ---------- |
| Web                  | HTTP/HTTPS |
| Email sending        | SMTP       |
| Email retrieval      | POP3/IMAP  |
| File transfer        | FTP        |
| Name resolution      | DNS        |
| Automatic addressing | DHCP       |
| Secure remote login  | SSH        |

---

# 9. Data Transmission Concepts & Terminology

## Bit rate

Bits transmitted per second.

```text
bps
```

## Baud rate

Symbols transmitted per second.

If each symbol carries one bit:

```text
baud = bit/s
```

Otherwise:

```text
Bit rate = Baud rate × bits/symbol
```

## Bandwidth

Frequency range available to a channel.

For analog channel:

```text
Bandwidth = f_high − f_low
```

## Throughput

Actual achieved data rate.

Usually:

```text
Throughput ≤ theoretical data rate
```

## Latency

Total delay experienced by data.

Major components:

```text
Transmission delay
+
Propagation delay
+
Processing delay
+
Queuing delay
```

### Transmission delay

Time to push bits onto link:

```text
Ttrans = Packet size / Data rate
```

### Propagation delay

Time for signal to travel:

```text
Tprop = Distance / Propagation speed
```

### Jitter

Variation in packet delay.

Especially important for:

* voice
* video
* real-time applications

---

# 10. Analog Data Transmission

Analog signal varies continuously.

```text
Amplitude
   │    /‾\      /‾\
   │   /   \    /   \
───┼──/─────\──/─────\──► time
```

Parameters:

* amplitude
* frequency
* phase

---

# 11. Digital Data Transmission

Digital signal uses discrete levels.

```text
1 ────┐    ┌────
      │    │
0     └────┘
```

Typically represented using binary values.

### Analog vs Digital

| Analog                                | Digital                     |
| ------------------------------------- | --------------------------- |
| Continuous                            | Discrete                    |
| More susceptible to accumulated noise | Better noise regeneration   |
| Uses continuous waveform              | Uses discrete signal levels |
| Traditional radio/voice systems       | Computers/data networks     |

---

# 12. Transmission Impairments

Three major impairments:

```text
Attenuation
Distortion
Noise
```

## Attenuation

Signal loses strength with distance.

Measured commonly in decibels.

```text
Received power < Transmitted power
```

## Distortion

Signal shape changes.

Different frequency components may experience different delays/attenuation.

## Noise

Unwanted signal added to desired signal.

Types:

* thermal
* intermodulation
* crosstalk
* impulse

**[UPLOADED PYQ]** asks specifically about major transmission impairments and their effect on signal quality. 

---

# 13. Channel Capacity

Maximum theoretical rate at which information can be transmitted reliably.

## Nyquist theorem

For a noiseless channel:

```text
C = 2B log₂L
```

where:

* B = bandwidth
* L = number of signal levels

## Shannon theorem

For noisy channel:

```text
C = B log₂(1 + S/N)
```

where:

* C = capacity
* B = bandwidth
* S/N = signal-to-noise ratio

If SNR is in dB:

```text
SNRlinear = 10^(SNRdB/10)
```

### Key distinction

> **Nyquist → noiseless**

> **Shannon → noisy**

**[UPLOADED PYQ]** asks Shannon capacity directly. 

---

# 🧠 M1 ACTIVE RECALL

Without looking:

1. What are the five basic components of data communication?
2. Simplex vs half-duplex vs full-duplex?
3. PAN/LAN/MAN/WAN?
4. Name all seven OSI layers.
5. What does each OSI layer do?
6. OSI vs TCP/IP?
7. What is encapsulation?
8. Bit rate vs baud rate?
9. Transmission vs propagation delay?
10. Attenuation vs distortion vs noise?
11. Nyquist formula?
12. Shannon formula?

---

# MODULE II — TRANSMISSION MEDIA & SIGNAL ENCODING

### 6 topics

The uploaded syllabus lists Guided Media, Wireless Transmission & Propagation, Digital Signaling, Analog Signaling, Encoding and Modulation. 

---

# 14. Guided Transmission Media

Signals travel through physical media.

```text
Guided
├── Twisted Pair
├── Coaxial
└── Optical Fiber
```

---

## Twisted Pair

Two insulated copper wires twisted together.

### Types

**UTP**

Unshielded Twisted Pair.

**STP**

Shielded Twisted Pair.

### Advantages

* inexpensive
* easy installation
* widely available

### Disadvantages

* electromagnetic interference
* lower bandwidth than fiber
* attenuation

---

## Coaxial Cable

Structure:

```text
Outer Jacket
 ┌───────────────┐
 │ Shield        │
 │ ┌───────────┐ │
 │ │ Insulator │ │
 │ │  ┌─────┐  │ │
 │ │  │Core │  │ │
 │ │  └─────┘  │ │
 │ └───────────┘ │
 └───────────────┘
```

Better shielding than twisted pair.

Applications:

* cable TV
* broadband
* older Ethernet

---

## Optical Fiber

Uses light instead of electrical signals.

```text
Light
  ↓
Core
──────────
Cladding
──────────
Jacket
```

Principle:

> **Total Internal Reflection**

### Advantages

* huge bandwidth
* low attenuation
* EMI immunity
* lightweight
* secure against electromagnetic interception

### Disadvantages

* installation complexity
* higher equipment cost
* fragile compared with copper

### Memory

> **Copper carries electrons; fiber carries light.**

---

# 15. Wireless Transmission & Propagation

Unguided media:

```text
Radio
Microwave
Infrared
Satellite
```

### Propagation methods

#### Ground wave

Follows Earth's surface.

#### Sky wave

Signal reflected/refracted by ionospheric region.

#### Line-of-sight

Direct path between antennas.

```text
A ───────────────► B
```

Used heavily by microwave communication.

---

## Satellite Communication

```text
Earth Station
     ↑
     │ uplink
     ▼
 Satellite
     │
     │ downlink
     ▼
Earth Station
```

### Advantages

* huge coverage
* useful for remote regions
* broadcasting

### Disadvantages

* high propagation delay
* expensive
* weather effects for some bands
* requires satellite infrastructure

**[UPLOADED PYQ]** asks the physical description/transmission characteristics of satellite microwave and satellite-vs-terrestrial microwave.

---

# 16. Digital Signaling

Digital data must be represented by physical signal patterns.

Important line codes:

* NRZ-L
* NRZ-I/NRZI
* Manchester
* Differential Manchester
* Bipolar AMI

---

## NRZ-L

Signal level represents bit value.

Convention depends on specification.

Key issue:

> Long sequences of same bits can cause synchronization problems.

---

## NRZ-I

A transition represents one binary value; no transition represents the other.

The exact convention must be stated.

**[UPLOADED PYQ]** asks NRZI and Differential Manchester waveforms. 

---

## Manchester

Every bit has a transition in the middle.

This provides synchronization.

Typical convention:

```text
1 → high-to-low
0 → low-to-high
```

But always follow the convention specified by your teacher/question.

### Key advantage

Self-clocking.

---

## Differential Manchester

There is always a transition in the middle.

The transition at the beginning determines the bit value.

Again, conventions may differ.

---

## Bipolar AMI

```text
0 → zero level
1 → alternating +V and −V
```

Example:

```text
1 0 1 1 0 1
+ 0 - + 0 -
```

---

# 17. Analog Signaling

Digital data can be represented by changing a carrier wave.

Carrier:

```text
c(t) = Ac cos(2πfct + φ)
```

Three fundamental parameters:

* amplitude
* frequency
* phase

Changing one creates modulation.

---

# 18. Encoding Techniques

### Encoding

Maps data into a signal suitable for transmission.

```text
Bits → Line Code → Signal
```

Important techniques:

| Technique               | Main idea                                   |
| ----------------------- | ------------------------------------------- |
| NRZ-L                   | Level represents data                       |
| NRZ-I                   | Transition represents data                  |
| Manchester              | Mid-bit transition                          |
| Differential Manchester | Mid-bit transition + differential beginning |
| AMI                     | Bipolar representation                      |

### **[UPLOADED PYQ]**

For `001110011`, the paper asks you to draw:

* NRZ-L
* NRZ-I
* Bipolar AMI
* Manchester
* Differential Manchester



This is a **must-practice waveform question**.

---

# 19. Modulation Techniques

Modulation changes a carrier according to information.

## ASK

Amplitude Shift Keying.

```text
1 → carrier present
0 → carrier absent/different amplitude
```

## FSK

Frequency Shift Keying.

```text
1 → f1
0 → f2
```

## PSK

Phase Shift Keying.

```text
1 → phase φ1
0 → phase φ2
```

## QAM

Quadrature Amplitude Modulation.

Changes:

* amplitude
* phase

simultaneously.

### General comparison

| ASK       | FSK       | PSK                    | QAM                |
| --------- | --------- | ---------------------- | ------------------ |
| Amplitude | Frequency | Phase                  | Amplitude + phase  |
| Simple    | Robust    | Good noise performance | High data capacity |

---

# 🧠 M2 ACTIVE RECALL

1. Twisted pair vs coaxial vs fiber?
2. Why is fiber resistant to EMI?
3. What is total internal reflection?
4. Ground vs sky vs LOS propagation?
5. Satellite vs terrestrial microwave?
6. NRZ-L vs NRZ-I?
7. Why does Manchester help synchronization?
8. What happens in AMI?
9. ASK/FSK/PSK/QAM?
10. Encoding vs modulation?

---

# MODULE III — ERROR HANDLING, DATA LINK CONTROL & MULTIPLEXING

### 8 topics

The syllabus contains errors, detection, correction, flow/error control, HDLC, FDM and TDM. 

---

# 20. Types of Errors

## Single-bit error

Only one bit changes.

```text
Sent:     101101
Received:101001
```

## Burst error

Multiple bits in a sequence are affected.

```text
Sent:     1100110011
Received:1101001011
```

Burst errors are particularly important in practical communication channels.

---

# 21. Error Detection Techniques

Goal:

> Detect whether received data has been corrupted.

Main techniques:

```text
Parity
Checksum
CRC
```

---

## Parity

Add one bit.

### Even parity

Total number of 1s becomes even.

### Odd parity

Total number of 1s becomes odd.

### Limitation

A single parity bit is not sufficient for detecting every possible error pattern.

**[UPLOADED PYQ]** directly asks what a parity bit is and how it detects errors. 

---

# 22. Checksum

Basic idea:

```text
Data words
   ↓
Add
   ↓
Complement
   ↓
Checksum
```

Receiver performs corresponding calculation.

Used historically/in various network protocols including transport/network contexts.

---

# 23. CRC

**Cyclic Redundancy Check** is one of the most important DCCN numerical topics.

Given:

```text
Data = D
Generator = G
```

If generator degree = r:

1. Append r zeros to data.
2. Perform modulo-2 division.
3. Remainder = CRC.
4. Append remainder to original data.

```text
Transmitted frame = Data + CRC
```

### Modulo-2 arithmetic

Subtraction = XOR.

```text
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0
```

### Receiver

Divide received frame by generator.

```text
remainder = 0
```

means no detected error under the CRC test.

**[UPLOADED PYQ]** asks CRC for:

```text
Data = 1010011110
Generator = 1011
```



Another uploaded paper asks:

```text
Data = 1101011011
Generator = 10011
```

and requests the complete calculation and transmitted message. 

### 🚨 Must practice

Do not memorize CRC.

**Do the binary division repeatedly.**

---

# 24. Error Correction Techniques

Error correction means recovering/correcting corrupted data.

Two broad approaches:

### Forward Error Correction

Receiver corrects error without retransmission.

Useful when retransmission is expensive or slow.

### Hamming Code

Adds redundant bits at carefully selected positions.

---

## Hamming Code

For `m` data bits and `r` parity bits:

```text
2^r ≥ m + r + 1
```

Parity positions:

```text
1, 2, 4, 8, 16, ...
```

These are powers of two.

Example:

```text
Position:
1 2 3 4 5 6 7
P P D P D D D
```

Parity bits cover different position groups.

### Syndrome

The received parity-check results form a binary number.

If syndrome:

```text
000
```

→ no detected single-bit error.

If:

```text
101
```

→ error at decimal position 5.

### Memory

> **Hamming parity lives at powers of 2.**

---

# 25. Flow Control

Flow control prevents a fast sender from overwhelming a slow receiver.

```text
Fast Sender ─────────► Slow Receiver
             CONTROL
```

Important methods:

* Stop-and-Wait
* Sliding Window

---

## Stop-and-Wait

```text
Sender ── Frame 0 ──► Receiver
Sender ◄──── ACK ──── Receiver
Sender ── Frame 1 ──►
```

Only one outstanding frame.

### Advantage

Simple.

### Disadvantage

Poor link utilization on long-delay networks.

---

## Sliding Window

Multiple frames can be outstanding.

```text
[0][1][2][3][4] →→→
```

Window moves as acknowledgements arrive.

Benefits:

* better utilization
* higher throughput
* supports pipelining

---

# 26. Error Control

Flow control:

> **How fast?**

Error control:

> **Was it received correctly?**

Error control uses:

* error detection
* acknowledgements
* retransmission
* sequence numbers
* timers

### ARQ

Automatic Repeat reQuest.

Important forms:

1. Stop-and-Wait ARQ
2. Go-Back-N
3. Selective Repeat

---

## Go-Back-N

If frame k is lost:

```text
0 ✓
1 ✓
2 ✗
3
4
```

sender retransmits from frame 2 onward.

---

## Selective Repeat

Only damaged/missing frames are retransmitted.

```text
0 ✓
1 ✓
2 ✗
3 ✓
4 ✓
```

Retransmit only 2.

### Comparison

| GBN                           | Selective Repeat            |
| ----------------------------- | --------------------------- |
| Retransmits from error onward | Retransmits selected frames |
| Simpler                       | More complex                |
| More waste                    | More efficient              |

**[UPLOADED PYQ]** explicitly asks Sliding Window and Stop-and-Wait ARQ vs Go-Back-N. 

---

# 27. HDLC

**High-Level Data Link Control**

A bit-oriented data-link protocol.

Basic frame:

```text
┌─────┬────────┬────────┬──────┬─────┬─────┐
│Flag │Address │Control │Data  │ FCS │Flag │
└─────┴────────┴────────┴──────┴─────┴─────┘
```

### Flag

Identifies frame boundaries.

Common flag pattern:

```text
01111110
```

### Address

Identifies station.

### Control

Defines frame type/control information.

### Data

Payload.

### FCS

Frame Check Sequence for error detection.

---

## HDLC frame types

### I-frame

Information.

Carries user data.

### S-frame

Supervisory.

Used for control/acknowledgement.

### U-frame

Unnumbered.

Used for management/control functions.

### Memory

> **I = Information**
> **S = Supervisory**
> **U = Unnumbered**

---

# 28. FDM

**Frequency Division Multiplexing**

Channel bandwidth is divided into frequency bands.

```text
Frequency
│
├── Ch1 ──┤
├── Guard ┤
├── Ch2 ──┤
├── Guard ┤
├── Ch3 ──┤
```

Each signal gets a different frequency band.

Applications:

* radio
* television
* analog communication

### Guard bands

Prevent interference between adjacent channels.

---

# 29. TDM

**Time Division Multiplexing**

Users share the channel by taking turns in time.

```text
Time →
| A | B | C | A | B | C |
```

### Synchronous TDM

Fixed time slot allocated to each source.

Even if source has no data, slot may remain allocated.

### Statistical TDM

Slots dynamically allocated to active sources.

Better utilization but requires more control.

**[UPLOADED PYQ]** asks TDM and explicitly asks synchronous vs asynchronous/statistical TDM. 

---

# 🧠 M3 ACTIVE RECALL

1. Single-bit vs burst error?
2. Parity vs checksum vs CRC?
3. CRC steps?
4. What is `2^r ≥ m+r+1` used for?
5. Where are Hamming parity bits placed?
6. Flow control vs error control?
7. Stop-and-Wait?
8. GBN vs Selective Repeat?
9. HDLC frame?
10. I/S/U frames?
11. FDM vs TDM?
12. Synchronous vs statistical TDM?

---

# MODULE IV — WAN & LAN

### 9 topics

Your syllabus lists switching, circuit/packet switching, cellular networks, generations, topologies, LAN architecture and VLANs. 

---

# 30. Switching Network

Switching allows information to move through intermediate network nodes.

Main approaches:

```text
Switching
├── Circuit Switching
└── Packet Switching
```

---

# 31. Circuit-Switching Networks

A dedicated path is established before communication.

```text
A ── S1 ── S2 ── S3 ── B
      dedicated circuit
```

Three phases:

```text
Setup
 ↓
Data transfer
 ↓
Teardown
```

Advantages:

* predictable path
* predictable delay after setup
* suitable for continuous traffic

Disadvantages:

* setup time
* inefficient for bursty traffic
* dedicated resources may remain unused

---

# 32. Circuit-Switching Concepts

Important characteristics:

* dedicated resources
* call setup
* fixed path
* circuit release

Traditional telephone systems are the classic example.

---

# 33. Packet-Switching Principles

Data is divided into packets.

```text
Message
 ↓
Packet 1
Packet 2
Packet 3
 ↓
Network
 ↓
Destination
```

Packets may share links with other traffic.

Two major approaches:

### Datagram

Each packet independently routed.

### Virtual Circuit

Logical path established; packets follow that logical route.

---

## Circuit vs Packet

| Circuit                     | Packet                     |
| --------------------------- | -------------------------- |
| Dedicated path              | Shared network             |
| Setup                       | Usually no dedicated setup |
| Predictable path            | Dynamic                    |
| Good for continuous traffic | Good for bursty traffic    |
| Traditional telephony       | Internet                   |

**[UPLOADED PYQ]** explicitly asks circuit vs packet switching. 

Another uploaded paper asks datagram vs virtual-circuit packet switching. 

---

# 34. Principles of Cellular Networks

A cellular network divides a geographical region into cells.

```text
       ◯
    ◯     ◯
       ◯
    ◯     ◯
```

Each cell has a base station.

### Frequency reuse

Same frequency can be reused in sufficiently separated cells.

Goal:

> Increase capacity without requiring unique frequencies everywhere.

---

## Handoff

When a mobile moves from one cell to another:

```text
Cell A ─────► Cell B
       handoff
```

The connection is transferred to another base station.

---

# 35. Cellular Network Generations

### 1G

* analog
* voice

### 2G

* digital
* voice
* SMS
* improved capacity

### 3G

* higher data rates
* mobile Internet

### 4G

* broadband mobile data
* LTE
* IP-oriented services

### 5G

* very high capacity
* low-latency applications
* massive device connectivity
* IoT-oriented use cases

### Memory

> **1 Voice → 2 Digital → 3 Internet → 4 Broadband → 5 Massive Connectivity**

---

# 36. Network Topologies

## Bus

```text
A ── B ── C ── D
───────────────
```

Cheap but backbone failure can affect network.

---

## Star

```text
    A
    |
B──Switch──C
    |
    D
```

Easy to manage.

Central device is critical.

---

## Ring

```text
A ─ B
|   |
D ─ C
```

Nodes form a ring.

---

## Mesh

Every node has multiple connections.

```text
A────B
|\  /|
| \/ |
| /\ |
|/  \|
C────D
```

Very reliable but expensive.

---

## Tree

Hierarchical arrangement.

```text
        Core
       /    \
     SW1    SW2
    / \     / \
   A   B   C   D
```

### Comparison

| Topology | Major strength        | Major weakness            |
| -------- | --------------------- | ------------------------- |
| Bus      | Cheap                 | Backbone failure          |
| Star     | Easy management       | Central-device dependency |
| Ring     | Predictable structure | Break can affect ring     |
| Mesh     | Reliability           | Cost                      |
| Tree     | Scalable hierarchy    | More complex              |

---

# 37. LAN Protocol Architecture

IEEE LAN architecture is associated with the data-link layer and physical layer.

Data Link is commonly divided into:

```text
Data Link
├── LLC
└── MAC
```

### LLC

Logical Link Control.

Provides higher-level link services.

### MAC

Medium Access Control.

Deals with:

* addressing
* access to shared medium
* frame handling

---

# 38. VLAN

**Virtual LAN**

A VLAN logically divides a physical LAN.

```text
Physical Switch
 ├── VLAN 10 → Students
 ├── VLAN 20 → Faculty
 └── VLAN 30 → Admin
```

Devices can be physically connected to the same switches but logically separated.

### Benefits

* segmentation
* security
* broadcast-domain reduction
* easier management
* flexibility

### Memory

> **VLAN = logical LAN, not necessarily physical LAN.**

---

# 🧠 M4 ACTIVE RECALL

1. What is switching?
2. Circuit vs packet switching?
3. Datagram vs virtual circuit?
4. Three phases of circuit switching?
5. Why does packet switching suit bursty data?
6. What is frequency reuse?
7. What is handoff?
8. 1G → 5G evolution?
9. Five network topologies?
10. LLC vs MAC?
11. Why VLAN?

---

# MODULE V — ETHERNET, IP, ROUTING & APPLICATIONS

### 16 topics

The syllabus contains Traditional Ethernet, High-Speed Ethernet, Wi-Fi, IP, addressing, transport, routing, three routing approaches, congestion, traffic management and SMTP/DNS/HTTP/DHCP. 

---

# 39. Traditional Ethernet

Ethernet is standardized under **IEEE 802.3**.

Traditional Ethernet:

```text
10 Mbps
```

Historically used:

* coaxial cable
* twisted pair

Traditional shared-medium Ethernet used **CSMA/CD**.

---

# 40. High-Speed Ethernet

Important generations:

```text
Ethernet       → 10 Mbps
Fast Ethernet  → 100 Mbps
Gigabit        → 1 Gbps
10 Gigabit     → 10 Gbps
```

Higher-speed Ethernet improves:

* throughput
* latency
* network capacity

---

# 41. IEEE 802.11 — Wi-Fi

Wireless LAN standard.

Common generations include:

* 802.11b
* 802.11a
* 802.11g
* 802.11n
* 802.11ac
* 802.11ax

Advantages:

* mobility
* easy deployment
* no cable to every endpoint

Challenges:

* interference
* shared medium
* security concerns
* variable performance

### Ethernet vs Wi-Fi

| Ethernet                                | Wi-Fi                       |
| --------------------------------------- | --------------------------- |
| Wired                                   | Wireless                    |
| IEEE 802.3                              | IEEE 802.11                 |
| Dedicated physical connection typically | Shared radio medium         |
| Generally more stable                   | More interference-sensitive |

---

# 42. Internet Protocol — IP

IP provides logical addressing and packet delivery across interconnected networks.

Main versions:

```text
IPv4
IPv6
```

---

## IPv4

32-bit address.

Example:

```text
192.168.1.10
```

IPv4 header includes fields such as:

* Version
* Header Length
* Total Length
* Identification
* Flags
* Fragment Offset
* TTL
* Protocol
* Header Checksum
* Source Address
* Destination Address

**[UPLOADED PYQ]** asks the structure and working of IPv4 and purpose of major header fields. 

---

## IPv6

128-bit addressing.

Example:

```text
2001:db8::1
```

Advantages:

* enormous address space
* simplified base header
* better support for modern networking requirements
* extension-header architecture

### IPv4 vs IPv6

| IPv4                                | IPv6                                                    |
| ----------------------------------- | ------------------------------------------------------- |
| 32-bit                              | 128-bit                                                 |
| Dotted decimal                      | Hexadecimal                                             |
| Smaller address space               | Huge address space                                      |
| Broadcast exists                    | No conventional broadcast; multicast/anycast mechanisms |
| More dependence on NAT historically | Designed for vastly larger address space                |

---

# 43. IP Addressing

An IP address identifies a network interface logically.

### Classful IPv4 addressing

Traditional classes:

| Class | First octet range | Default mask |
| ----- | ----------------: | ------------ |
| A     |             1–126 | /8           |
| B     |           128–191 | /16          |
| C     |           192–223 | /24          |
| D     |           224–239 | Multicast    |
| E     |           240–255 | Experimental |

### Important special addresses

Private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

---

## Subnetting

Splits a network into smaller networks.

Example:

```text
192.168.1.0/24
```

If changed to:

```text
/26
```

then:

```text
2^(26-24) = 4 subnets
```

Each `/26` has:

```text
2^(32-26) = 64 addresses
```

Traditionally:

```text
62 usable host addresses
```

per ordinary subnet, excluding network and broadcast addresses.

### Must know

```text
Number of subnets = 2^borrowed_bits
Addresses/subnet = 2^host_bits
```

---

# 44. Transport Protocols

Main transport protocols:

```text
TCP
UDP
```

---

## TCP

Transmission Control Protocol.

Properties:

* connection-oriented
* reliable
* ordered
* byte-stream
* flow control
* congestion control

### Three-way handshake

```text
Client                 Server

   SYN  ─────────────►
        ◄──────────── SYN + ACK
   ACK  ─────────────►
```

Connection established.

---

## UDP

User Datagram Protocol.

Properties:

* connectionless
* low overhead
* no built-in reliability
* no ordering guarantee
* useful for real-time/latency-sensitive applications

### TCP vs UDP

| TCP                               | UDP                                                          |
| --------------------------------- | ------------------------------------------------------------ |
| Connection-oriented               | Connectionless                                               |
| Reliable                          | Best-effort                                                  |
| Ordered                           | No ordering guarantee                                        |
| More overhead                     | Low overhead                                                 |
| Flow/congestion control           | No TCP-style mechanisms                                      |
| Web/secure web/file transfer etc. | DNS, streaming/real-time uses, etc. depending on application |

The uploaded DCCN question bank identifies **TCP vs UDP** as one of the highest-priority Module V questions. 

---

# 45. Routing in Packet-Switching Networks

Routing determines a path from source to destination.

```text
Source
  ↓
Router
  ↓
Router
  ↓
Router
  ↓
Destination
```

Routing algorithms use metrics such as:

* hop count
* delay
* bandwidth
* cost
* reliability

---

# 46. Distance Vector Routing

Each router maintains distance estimates to destinations.

Basic idea:

> Router knows the distance through neighbors.

A classic recurrence is based on:

```text
Dₓ(y) = minᵥ { c(x,v) + Dᵥ(y) }
```

### Characteristics

* neighbor-based information
* iterative updates
* simpler
* slower convergence in some situations

Example protocol:

> **RIP**

### Problem

Count-to-infinity.

---

# 47. Link State Routing

Every router builds a map of the network.

Steps:

```text
Discover neighbors
       ↓
Measure link costs
       ↓
Create link-state information
       ↓
Flood information
       ↓
Build topology database
       ↓
Run shortest-path algorithm
```

Common algorithm:

> **Dijkstra**

Example protocol:

> **OSPF**

### Memory

> **Link State = Know the map.**

---

# 48. Path Vector Routing

Used especially for routing between autonomous systems.

Instead of simply advertising a distance, routers advertise path information.

Example:

```text
AS1 → AS3 → AS7
```

A router can use policy and path information to select routes.

Main protocol:

> **BGP**

### Memory

```text
Distance Vector → RIP
Link State      → OSPF
Path Vector     → BGP
```

---

# 49. Congestion Control

Congestion occurs when offered traffic exceeds network capacity.

```text
Traffic in
   ↓
Router Queue
   ↓
████████████
   ↓
Overflow
   ↓
Packet loss
```

Effects:

* delay
* packet loss
* retransmissions
* reduced throughput

### Congestion vs Flow Control

**Flow control**

Protects the receiver.

**Congestion control**

Protects the network.

---

## Congestion-control approaches

* traffic shaping
* admission control
* queue management
* congestion avoidance
* rate control

### Leaky Bucket

Controls output at a relatively fixed rate.

```text
Incoming bursts
      ↓
 ┌──────────┐
 │  Bucket  │
 └────┬─────┘
      ↓
Fixed-rate output
```

### Token Bucket

Tokens accumulate at a controlled rate.

Packets require tokens to transmit.

Allows controlled bursts.

---

# 50. Traffic Management

Goal:

> Use network resources efficiently while maintaining acceptable service quality.

Includes:

* QoS
* queue management
* scheduling
* traffic shaping
* admission control
* congestion avoidance

### QoS dimensions

* bandwidth
* delay
* jitter
* packet loss

### Memory

> **QoS = Bandwidth + Delay + Jitter + Loss**

---

# 51. SMTP

**Simple Mail Transfer Protocol**

Used primarily for sending/relaying email.

Typical ports:

```text
25  → SMTP relay
587 → message submission
```

Basic flow:

```text
Sender
  ↓
Mail Server
  ↓
Internet
  ↓
Recipient Mail Server
```

SMTP is primarily a **sending/transfer** protocol.

---

# 52. DNS

**Domain Name System**

Maps domain names to network information, especially IP addresses.

```text
www.example.com
        ↓
      DNS
        ↓
     IP address
```

### Hierarchy

```text
Root
 ↓
TLD
 ↓
Authoritative domain
 ↓
Host
```

### Important records

| Record | Purpose        |
| ------ | -------------- |
| A      | IPv4 address   |
| AAAA   | IPv6 address   |
| MX     | Mail server    |
| CNAME  | Canonical name |
| NS     | Name server    |
| TXT    | Text/metadata  |

Port:

```text
53
```

DNS commonly uses UDP for ordinary queries, with TCP also used in situations such as zone transfers and responses requiring it.

---

# 53. HTTP

**HyperText Transfer Protocol**

Used for web communication.

Basic model:

```text
Client ── HTTP Request ──► Server
Client ◄─ HTTP Response ── Server
```

### Common methods

```text
GET
POST
PUT
DELETE
```

### Common status codes

```text
2xx → Success
3xx → Redirection
4xx → Client error
5xx → Server error
```

Examples:

```text
200 → OK
301/302 → Redirect
404 → Not Found
500 → Server Error
```

Ports:

```text
HTTP  → 80
HTTPS → 443
```

---

# 54. DHCP

**Dynamic Host Configuration Protocol**

Automatically provides configuration such as:

* IP address
* subnet mask
* gateway
* DNS server

### DORA

```text
Client
  │
  │ DISCOVER
  ▼
Server
  │
  │ OFFER
  ▼
Client
  │
  │ REQUEST
  ▼
Server
  │
  │ ACK
  ▼
Client configured
```

### Memory

> **DORA = Discover → Offer → Request → Acknowledge**

Ports:

```text
Server → UDP 67
Client → UDP 68
```

---

# 🌐 THE MOST IMPORTANT INTEGRATED CONCEPT

## What happens when you type a URL?

Suppose:

```text
https://example.com
```

### Step 1 — Device needs network configuration

DHCP can provide:

```text
IP
Subnet Mask
Gateway
DNS server
```

### Step 2 — DNS resolution

```text
example.com
     ↓
DNS
     ↓
Server IP
```

### Step 3 — Transport connection

For HTTPS over TCP:

```text
TCP 3-way handshake
```

```text
SYN
SYN + ACK
ACK
```

### Step 4 — HTTP/HTTPS request

```text
GET /...
```

### Step 5 — IP routing

Packet travels:

```text
Host
 ↓
Default Gateway
 ↓
Routers
 ↓
Server
```

### Step 6 — Link-layer transmission

Locally:

```text
Ethernet / Wi-Fi
```

### Step 7 — Server response

```text
HTTP response
 ↓
TCP
 ↓
IP
 ↓
Ethernet/Wi-Fi
 ↓
Browser
```

### Step 8 — Browser renders webpage

```text
HTML
CSS
JavaScript
Images
etc.
```

This single scenario connects **M1 + M4 + M5**.

The uploaded question bank specifically asks for this complete URL → webpage journey. 

---

# 🔥 ACTUAL UPLOADED PYQ PATTERNS

These are not invented; they come from the DCCN papers available in your uploaded files.

### 2025 AI323 Mid

* Port vs logical vs physical address
* TCP/IP architecture
* Eb/No
* Half vs full duplex
* LAN vs WAN
* Communication vs transmission
* Transmission impairments
* Shannon capacity
* Satellite microwave
* NRZ-L / NRZ-I / AMI / Manchester / Differential Manchester 

### 2025 AI323 End

* IPv4 header
* TCP/IP architecture
* PCM
* Satellite microwave
* Sliding window
* Stop-and-Wait ARQ vs Go-Back-N
* CRC numerical
* Multiplexing/access methods
* LLC
* Internetworking
* Circuit vs packet switching 

### 2025 IT365 Mid

* Transmission modes
* Data communication components
* Data Link Layer
* OSI vs TCP/IP
* SNR
* Transmission impairments
* Guided vs unguided media
* Delta Modulation vs PCM
* Parity
* CRC 

### 2025 IT365 End

* OSI vs TCP/IP
* Noise
* NRZI
* Differential Manchester
* PCM
* Unguided media
* CRC numerical
* TDM
* Synchronous vs statistical TDM
* Datagram vs virtual circuit
* Dijkstra
* ATM 

---

# 🧠 ULTRA-HIGH-YIELD 20

Your uploaded study guide itself identifies these as the **20 highest-priority questions/topics**. 

### ⭐⭐⭐⭐⭐

1. OSI Model
2. TCP/IP Architecture
3. OSI vs TCP/IP
4. Guided Transmission Media
5. Analog vs Digital Signal
6. Manchester Encoding
7. ASK/FSK/PSK/QAM
8. CRC
9. Hamming Code
10. Stop-and-Wait vs Sliding Window
11. HDLC Frame
12. FDM vs TDM
13. Circuit vs Packet Switching
14. Cellular Networks / 1G–5G
15. Network Topologies
16. VLAN
17. IPv4 vs IPv6
18. TCP vs UDP
19. Routing — RIP/OSPF/BGP
20. DNS/HTTP/SMTP/DHCP

---

# 📊 FORMULA SHEET

## Transmission

```text
Bandwidth = fH − fL
```

```text
Transmission Delay = Packet Size / Data Rate
```

```text
Propagation Delay = Distance / Propagation Speed
```

---

## Nyquist

```text
C = 2B log₂L
```

---

## Shannon

```text
C = B log₂(1 + S/N)
```

---

## SNR conversion

```text
SNR(dB) = 10 log₁₀(S/N)
```

---

## Subnetting

```text
Number of subnets = 2^borrowed bits
```

```text
Addresses/subnet = 2^host bits
```

---

## Hamming

```text
2^r ≥ m + r + 1
```

---

## CRC

```text
Append r zeros
→ modulo-2 divide
→ remainder = CRC
→ append CRC
```

---

# 🧠 MASTER MEMORY MAP

You should be able to reconstruct the whole course from this:

```text
                    DCCN
                     │
       ┌─────────────┼─────────────┐
       │             │             │
      DATA         SIGNAL        NETWORK
       │             │             │
 Communication    Encoding       OSI
 Components       Modulation     TCP/IP
 Transmission     Media          IP
       │             │             │
       └──────┬──────┘             │
              ▼                    │
          DATA LINK                │
              │                    │
      ┌───────┼────────┐           │
      │       │        │           │
    Errors  Flow     HDLC          │
      │     Control                │
     CRC      │                    │
   Hamming  Sliding                 │
              │                    │
              └──────────┬─────────┘
                         ▼
                     SWITCHING
                         │
              ┌──────────┴─────────┐
              │                    │
           Circuit              Packet
                                   │
                                   ▼
                                ROUTING
                                   │
                     ┌─────────────┼─────────────┐
                     │             │             │
                    DV            LS            PV
                    RIP          OSPF           BGP
                                   │
                                   ▼
                               TRANSPORT
                                   │
                              ┌────┴────┐
                              TCP      UDP
                                   │
                                   ▼
                              APPLICATION
                                   │
                   ┌───────┬──────┬──────┬──────┐
                  DNS     HTTP   SMTP   DHCP
```

---

# 🧠 NEUROSCIENCE-BASED STUDY SYSTEM FOR DCCN

Don't read this entire thing repeatedly.

Use:

### 1. Retrieval before rereading

Close the notes and answer:

> "What are the 7 OSI layers?"

Then check.

---

### 2. Generation

Before seeing a solution, try:

```text
Data = 1010011110
Generator = 1011
```

and perform CRC yourself.

---

### 3. Dual coding

For every major concept, **draw it**.

Especially:

* OSI
* TCP/IP
* communication model
* satellite
* Manchester
* CRC division
* Hamming positions
* HDLC
* FDM/TDM
* switching
* cellular cells
* topologies
* VLAN
* Ethernet
* TCP handshake
* routing

---

### 4. Interleaving

Don't study:

```text
CRC → CRC → CRC → CRC
```

Instead:

```text
CRC
OSI
Hamming
TCP
Manchester
CRC
Routing
```

This improves discrimination between similar concepts.

---

### 5. Spaced repetition

```text
Day 0 → Learn
Day 1 → Recall
Day 3 → Recall
Day 7 → Recall
Day 14 → Recall
Day 30 → Recall
```

---

# 🎯 DCCN EXAM ANSWER FORMULA

For a **5/10-mark theory question**, use:

```text
Definition
   ↓
Diagram
   ↓
Working
   ↓
Components / Steps
   ↓
Advantages
   ↓
Disadvantages
   ↓
Application
   ↓
Comparison / conclusion
```

For a **numerical**:

```text
Given
↓
Formula / rule
↓
Substitution
↓
Step-by-step calculation
↓
Final answer boxed
```

For a **comparison**:

```text
Definition
↓
Table
↓
Example
↓
When to use which
```

---

# 🚨 TOP NUMERICALS YOU MUST MASTER

If your goal is high marks, don't treat DCCN as only theory.

Practice these **from scratch**:

1. ⭐⭐⭐⭐⭐ CRC
2. ⭐⭐⭐⭐⭐ Hamming Code
3. ⭐⭐⭐⭐⭐ Nyquist
4. ⭐⭐⭐⭐⭐ Shannon
5. ⭐⭐⭐⭐ Subnetting
6. ⭐⭐⭐⭐ Transmission delay
7. ⭐⭐⭐⭐ Propagation delay
8. ⭐⭐⭐⭐ Line-code waveform generation
9. ⭐⭐⭐ Dijkstra
10. ⭐⭐⭐ Sliding-window calculations

---

# ✅ COMPLETE 52-TOPIC TRACKER

### M1 — 13/13

* [ ] Communication Model
* [ ] Data Communications
* [ ] Networks
* [ ] Internet
* [ ] OSI Model
* [ ] TCP/IP Architecture
* [ ] Standards & Protocol Layers
* [ ] Internet Applications
* [ ] Data Transmission Concepts
* [ ] Analog Data Transmission
* [ ] Digital Data Transmission
* [ ] Transmission Impairments
* [ ] Channel Capacity

### M2 — 6/6

* [ ] Guided Transmission Media
* [ ] Wireless Transmission & Propagation
* [ ] Digital Signaling
* [ ] Analog Signaling
* [ ] Encoding Techniques
* [ ] Modulation Techniques

### M3 — 8/8

* [ ] Types of Errors
* [ ] Error Detection
* [ ] Error Correction
* [ ] Flow Control
* [ ] Error Control
* [ ] HDLC
* [ ] FDM
* [ ] TDM

### M4 — 9/9

* [ ] Switching Network
* [ ] Circuit-Switching Networks
* [ ] Circuit-Switching Concepts
* [ ] Packet-Switching Principles
* [ ] Cellular Network Principles
* [ ] Cellular Generations
* [ ] Network Topologies
* [ ] LAN Protocol Architecture
* [ ] VLAN

### M5 — 16/16

* [ ] Traditional Ethernet
* [ ] High-Speed Ethernet
* [ ] IEEE 802.11
* [ ] IP
* [ ] IP Addressing
* [ ] Transport Protocols
* [ ] Routing
* [ ] Distance Vector
* [ ] Link State
* [ ] Path Vector
* [ ] Congestion Control
* [ ] Traffic Management
* [ ] SMTP
* [ ] DNS
* [ ] HTTP
* [ ] DHCP

**Total: 52/52 topics.** 

### The most important thing

For **DCCN**, your learning should be much more **problem-oriented** than CD:

> **Understand → draw → derive → calculate → recall → solve PYQ.**

And the highest-value sequence is:

**M1:** OSI/TCP-IP + transmission + Nyquist/Shannon
→ **M2:** waveforms + media + modulation
→ **M3:** CRC + Hamming + ARQ + HDLC + TDM
→ **M4:** switching + cellular + topology + VLAN
→ **M5:** IP + subnetting + TCP/UDP + routing + application protocols.

Your uploaded material independently highlights essentially the same high-priority cluster, particularly **OSI/TCP-IP, CRC, Hamming, flow control, HDLC, FDM/TDM, switching, cellular networking, IP/TCP/UDP, routing and DNS/HTTP/SMTP/DHCP**.
