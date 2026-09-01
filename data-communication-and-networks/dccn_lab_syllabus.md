# 🧪 Data Communication and Computer Networks Lab (CS24306)
**Practical Syllabus, Lab Assignments & Implementation Manual | BIT Mesra**

> **Course Code:** `CS24306`  
> **Course Title:** Data Communication and Computer Networks Lab  
> **Credits:** **1.5 Credits**  
> **Core Practical Platform:** Linux (Ubuntu / Debian), C / C++, Python, Wireshark, Cisco Packet Tracer

---

## 📌 Lab Index & Experiment Schedule

```
+-----------+-----------------------------------------------------------+----------------+
| Module    | Key Practical Focus Area                                  | Target Weeks   |
+-----------+-----------------------------------------------------------+----------------+
| Lab M1    | UNIX Networking Tools, Packet Capture, ARP Simulation     | Weeks 1 - 2    |
| Lab M2    | Data Link Framing, Bit-Stuffing, Hamming Code, Checksum   | Weeks 3 - 5    |
| Lab M3    | Cyclic Redundancy Check (CRC-16/32), Network Topologies   | Weeks 6 - 8    |
| Lab M4    | IP Subnetting, Dijkstra SPF, Distance Vector Routing      | Weeks 9 - 11   |
| Lab M5    | IPC (FIFO, Shm), Socket Programming (TCP/UDP Chat Server) | Weeks 12 - 14  |
+-----------+-----------------------------------------------------------+----------------+
```

---

## 🧪 Detailed Lab Module Breakdown & Code Assignments

### Lab Module I – Networking Basics & UNIX Command Suite
- [ ] **Task 1.1:** Study and execute fundamental network diagnostics tools in Linux/UNIX:
  - `ifconfig` / `ip addr show` (Interface configuration and MAC/IP display)
  - `ping -c 5 <host>` (ICMP Echo request/reply and RTT measurement)
  - `traceroute <host>` / `tracepath` (Hop-by-hop route discovery with TTL decrement)
  - `netstat -tulnp` / `ss -tulnp` (Active TCP/UDP listening ports and established sockets)
  - `nslookup <domain>` / `dig <domain> ANY` (DNS record querying)
  - `arp -a` (Viewing and flushing the kernel ARP cache)
  - `route -n` / `ip route` (Kernel routing table inspection)
- [ ] **Task 1.2:** Packet capture and analysis using **Wireshark**:
  - Capture 3-way TCP handshake (`SYN`, `SYN-ACK`, `ACK`).
  - Filter and inspect DNS queries/responses (`dns`).
  - Filter and inspect HTTP request/response headers (`http`).
  - Capture and analyze ICMP Echo packets (`icmp`).
- [ ] **Task 1.3:** Simulate ARP (Address Resolution Protocol) cache lookup and broadcast request/unicast reply in C/Python.

---

### Lab Module II – Data Link Layer Framing & Error Control
- [ ] **Task 2.1: Character (Byte) Stuffing:**
  - Implement byte stuffing with `FLAG = '@'` and `ESC = 'E'`.
  - Sender routine: Insert `ESC` before every occurrence of `FLAG` or `ESC` in the data stream.
  - Receiver routine: Strip `ESC` and reconstruct original message.
- [ ] **Task 2.2: Bit Stuffing & Destuffing (HDLC Framing):**
  - Delimiter flag: `01111110`.
  - Sender routine: After detecting five consecutive `1`s, automatically insert a `0` (`0111110`).
  - Receiver routine: After detecting five consecutive `1`s, inspect the next bit; if `0`, discard it; if `1`, check if next bit is `0` (Flag) or error.
- [ ] **Task 2.3: Internet Checksum:**
  - Sender routine: Divide data stream into 16-bit integers, compute 1's complement sum, and append 1's complement of the sum as the checksum.
  - Receiver routine: Compute 1's complement sum over received segments including checksum; verify result is all 1s (or 0 after inversion).
- [ ] **Task 2.4: Hamming Code $(7, 4)$:**
  - Generate 7-bit Hamming codeword for 4-bit input data $(d_7, d_6, d_5, d_3)$ using parity bits $(p_4, p_2, p_1)$.
  - Implement single-bit error injection.
  - Receiver routine: Calculate syndrome bits $(s_2, s_1, s_0)$, identify error bit location, and correct the inverted bit.

---

### Lab Module III – Cyclic Redundancy Check & Network Simulation
- [ ] **Task 3.1: CRC Implementation in C/C++:**
  - Support arbitrary generator polynomials (CRC-12: $x^{12} + x^{11} + x^3 + x^2 + x + 1$, CRC-16: $x^{16} + x^{15} + x^2 + 1$, CRC-CCITT: $x^{16} + x^{12} + x^5 + 1$, CRC-32: IEEE 802.3).
  - Sender routine: Append $n$ zeros (where $n$ is polynomial degree), perform binary Modulo-2 division (XOR operations), and append remainder as FCS (Frame Check Sequence).
  - Receiver routine: Perform Modulo-2 division on received codeword; verify remainder is zero; test error detection by altering random bits.
- [ ] **Task 3.2: Cisco Packet Tracer / NS-2 Network Simulation:**
  - Design a star/mesh topology with 4 routers and 3 subnets.
  - Configure static IP routing and verify cross-subnet ping connectivity.
  - Simulate traffic generation, queue buffer buildup, and packet drop under congestion.

---

### Lab Module IV – IP Subnetting & Routing Algorithms
- [ ] **Task 4.1: IPv4 Subnet Calculator:**
  - Input: IPv4 address and required number of subnets / hosts per subnet.
  - Output: Network class, default mask, custom subnet mask, Network ID, First usable IP, Last usable IP, Directed broadcast address.
- [ ] **Task 4.2: Dijkstra's Shortest Path Algorithm:**
  - Represent network topology as an adjacency matrix with link costs/delays.
  - Compute shortest path from source node to all destinations; output routing forwarding table `[Destination, Next Hop, Cost]`.
- [ ] **Task 4.3: Distance Vector Routing (Bellman-Ford):**
  - Simulate distributed routing updates: Each node periodically shares its distance vector with direct neighbors.
  - Update routing table: $D_x(y) = \min_v \{ c(x, v) + D_v(y) \}$.
  - Demonstrate network link failure and trace the Count-to-Infinity problem; demonstrate Split Horizon mitigation.
- [ ] **Task 4.4: Traffic Shaping Algorithms:**
  - Implement Leaky Bucket algorithm with constant output leak rate.
  - Implement Token Bucket algorithm allowing controlled bursty traffic.

---

### Lab Module V – Socket Programming & Network Applications
- [ ] **Task 5.1: Inter-Process Communication (IPC) on Linux:**
  - Named Pipes (FIFO): Unidirectional client-server communication using `mkfifo()`.
  - Message Queues: `msgget()`, `msgsnd()`, `msgrcv()`.
  - Shared Memory with Semaphores: `shmget()`, `shmat()`, `shmdt()`.
- [ ] **Task 5.2: Iterative TCP Echo Server (BSD Sockets):**
  - Server: `socket()` $\rightarrow$ `bind()` $\rightarrow$ `listen()` $\rightarrow$ `accept()` $\rightarrow$ `recv()` $\rightarrow$ `send()` $\rightarrow$ `close()`.
  - Client: `socket()` $\rightarrow$ `connect()` $\rightarrow$ `send()` $\rightarrow$ `recv()` $\rightarrow$ `close()`.
- [ ] **Task 5.3: Multi-Client Concurrent TCP Chat Application:**
  - Multithreaded server using `pthread_create()` or I/O Multiplexing using `select()` / `epoll()`.
  - Broadcast messages from one client to all connected peers in real-time with username tagging.
- [ ] **Task 5.4: UDP Client-Server Communication:**
  - Implement connectionless file transfer / echo server using `sendto()` and `recvfrom()`.

---

## 📊 Lab Progress Tracker

| Module | Tasks Count | Completed | Status |
| :---: | :---: | :---: | :---: |
| **Lab M1** (Commands & Wireshark) | 8 | 0 | ⬜ Not Started |
| **Lab M2** (Framing, Stuffing, Hamming) | 9 | 0 | ⬜ Not Started |
| **Lab M3** (CRC & Packet Tracer) | 11 | 0 | ⬜ Not Started |
| **Lab M4** (Subnetting, Dijkstra, DVR) | 12 | 0 | ⬜ Not Started |
| **Lab M5** (IPC & Socket Programming) | 8 | 0 | ⬜ Not Started |
| **Total Practical Tasks** | **48** | **0** | **0% Complete** |

---
*Maintained for B.Tech CSE 5th Semester — CS24306 Data Communication and Computer Networks Lab.*
