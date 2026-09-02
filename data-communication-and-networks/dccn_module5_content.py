# DCCN Module 5 Exhaustive Content (16 Topics Complete)
# Neuroscience framework: Understand -> Visualize -> Connect -> Recall -> Apply -> Exam-Important Questions & [UPLOADED PYQ]

DCCN_M5_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module V: Ethernet, IP, Routing & Applications — Complete 16-Topic Tracker</div>
  <div class="toc-grid">
    <div><strong>Topic 39:</strong> Traditional Ethernet (IEEE 802.3 CSMA/CD at 10 Mbps)</div>
    <div><strong>Topic 40:</strong> High-Speed Ethernet (Fast 100M, Gigabit 1G, 10-Gigabit)</div>
    <div><strong>Topic 41:</strong> IEEE 802.11 Wi-Fi (CSMA/CA with RTS/CTS, Ethernet vs. Wi-Fi)</div>
    <div><strong>Topic 42:</strong> Internet Protocol (IPv4 20-Byte Header vs. IPv6 128-Bit)</div>
    <div><strong>Topic 43:</strong> IP Addressing & Subnetting ($2^{\text{borrowed}}$ & $2^{\text{host}}-2$)</div>
    <div><strong>Topic 44:</strong> Transport Protocols (TCP 3-Way Handshake vs. UDP Sockets)</div>
    <div><strong>Topic 45:</strong> Routing in Packet Networks (Hop Count, Cost, Bandwidth)</div>
    <div><strong>Topic 46:</strong> Distance Vector Routing (Bellman-Ford & RIP Count-to-Infinity)</div>
    <div><strong>Topic 47:</strong> Link State Routing (Dijkstra's Algorithm & OSPF Flooding)</div>
    <div><strong>Topic 48:</strong> Path Vector Routing (Border Gateway Protocol BGP-4)</div>
    <div><strong>Topic 49:</strong> Congestion Control (Leaky Bucket vs. Token Bucket Shaping)</div>
    <div><strong>Topic 50:</strong> Traffic Management & Quality of Service (QoS Dimensions)</div>
    <div><strong>Topic 51:</strong> Simple Mail Transfer Protocol (SMTP, POP3, IMAP)</div>
    <div><strong>Topic 52:</strong> Domain Name System (DNS Hierarchy & Records A, MX)</div>
    <div><strong>Topic 53:</strong> Hypertext Transfer Protocol (HTTP/1.1 vs. HTTP/2 & Statuses)</div>
    <div><strong>Topic 54:</strong> Dynamic Host Configuration Protocol (DHCP DORA Sequence)</div>
  </div>
</div>

<h2 class="section-title">Topic 39 – 41: Ethernet Evolution & Wireless LAN (IEEE 802.11)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Standard</th>
      <th style="width: 25%;">Data Rate</th>
      <th style="width: 25%;">Physical Media</th>
      <th>Medium Access Control (MAC)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Traditional Ethernet</strong></td><td>$10 \text{ Mbps}$</td><td>10Base5 (Thick coax), 10BaseT (UTP)</td><td>CSMA/CD (Half-Duplex)</td></tr>
    <tr><td><strong>Fast Ethernet</strong></td><td>$100 \text{ Mbps}$</td><td>100BaseTX (Cat 5 UTP), 100BaseFX</td><td>CSMA/CD / Switched Full-Duplex</td></tr>
    <tr><td><strong>Gigabit Ethernet</strong></td><td>$1 \text{ Gbps}$</td><td>1000BaseT (Cat 5e UTP), 1000BaseLX</td><td>Switched Full-Duplex</td></tr>
    <tr><td><strong>IEEE 802.11 (Wi-Fi)</strong></td><td>Up to $9.6 \text{ Gbps}$ (Wi-Fi 6)</td><td>$2.4 \text{ GHz} / 5 \text{ GHz} / 6 \text{ GHz}$ Radio</td><td>CSMA/CA with RTS/CTS Handshake</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 42 & 43: Internet Protocol (IPv4 Header & Subnetting) [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">IPv4 Header Field [UPLOADED PYQ]</th>
      <th style="width: 15%;">Bit Width</th>
      <th>Functional Operational Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Version</strong></td><td>4 bits</td><td>Identifies IP version (`0100` for IPv4).</td></tr>
    <tr><td><strong>Header Length (IHL)</strong></td><td>4 bits</td><td>Header length in 32-bit words (Minimum value $= 5 \implies 20 \text{ bytes}$).</td></tr>
    <tr><td><strong>Total Length</strong></td><td>16 bits</td><td>Total datagram length (Header + Payload) in bytes (Max $= 65,535 \text{ bytes}$).</td></tr>
    <tr><td><strong>Identification, Flags, Offset</strong></td><td>$16+3+13$ bits</td><td>Handles IP fragmentation. `DF`=Don't Fragment, `MF`=More Fragments. Offset in 8-byte units.</td></tr>
    <tr><td><strong>Time to Live (TTL)</strong></td><td>8 bits</td><td>Decremented at each router hop. When $\text{TTL}=0$, packet is dropped (prevents infinite loops).</td></tr>
    <tr><td><strong>Protocol</strong></td><td>8 bits</td><td>Demultiplexes to Transport layer (`6` for TCP, `17` for UDP, `1` for ICMP).</td></tr>
    <tr><td><strong>Header Checksum</strong></td><td>16 bits</td><td>1's complement sum of header fields recalculated at each router hop.</td></tr>
  </tbody>
</table>

<div class="formula-card">
  <strong>Subnetting Formulations:</strong>
  - Number of Created Subnets $= 2^{\text{borrowed bits}}$
  - Total IP Addresses per Subnet $= 2^{\text{host bits}}$
  - Usable Host Addresses per Subnet $= 2^{\text{host bits}} - 2$ (subtracting Subnet Network ID and Directed Broadcast Address).
</div>

<h2 class="section-title">Topic 44: Transport Protocols (TCP vs. UDP) [UPLOADED PYQ]</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">TCP (Transmission Control Protocol)</th>
      <th>UDP (User Datagram Protocol)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Connection Model</strong></td><td>Connection-Oriented (3-Way Handshake: SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK).</td><td>Connectionless (no handshake; sends datagrams immediately).</td></tr>
    <tr><td><strong>Reliability</strong></td><td>100% Reliable (Sequence numbers, ACKs, retransmissions on loss).</td><td>Unreliable Best-Effort (no ACKs, lost packets are not retransmitted).</td></tr>
    <tr><td><strong>Ordering & Streaming</strong></td><td>Guaranteed strictly in-order byte stream reassembly.</td><td>No ordering guarantee; datagram boundary preserved.</td></tr>
    <tr><td><strong>Flow & Congestion Control</strong></td><td>Full sliding window flow control + AIMD Congestion Control.</td><td>Zero flow control, zero congestion control.</td></tr>
    <tr><td><strong>Typical Applications</strong></td><td>Web (HTTP/HTTPS), Email (SMTP), File Transfer (FTP), SSH.</td><td>DNS queries, Video streaming (RTP), VoIP, DHCP, Online Gaming.</td></tr>
  </tbody>
</table>

<h2 class="section-title">Topic 45 – 48: Routing Protocols (Distance Vector vs. Link State vs. Path Vector)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 20%;">Routing Protocol</th>
      <th style="width: 30%;">Mathematical Algorithm</th>
      <th style="width: 25%;">Scope & Protocol</th>
      <th>Key Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Distance Vector</strong></td>
      <td>Bellman-Ford: $D_x(y) = \min_v \{ c(x, v) + D_v(y) \}$</td>
      <td>Intra-AS (RIP)</td>
      <td>Exchanges vector with neighbors; susceptible to Count-to-Infinity.</td>
    </tr>
    <tr>
      <td><strong>Link State</strong></td>
      <td>Dijkstra's Shortest Path Tree Algorithm</td>
      <td>Intra-AS (OSPF)</td>
      <td>Floods Link State Advertisements (LSA) globally; builds complete topological map.</td>
    </tr>
    <tr>
      <td><strong>Path Vector</strong></td>
      <td>Policy-based sequence of Autonomous System (AS) hops</td>
      <td>Inter-AS (BGP-4)</td>
      <td>Prevents loops by checking if local AS number is present in path vector.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 49 & 50: Congestion Control & Traffic Shaping (Leaky vs. Token Bucket)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Traffic Shaper</th>
      <th style="width: 45%;">Operating Mechanism</th>
      <th>Burst Handling Capability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Leaky Bucket</strong></td>
      <td>Input packet bursts fill a buffer with fixed capacity. Water (packets) leaks out at a <strong>strictly constant uniform output rate</strong>. Excess bursts overflow and are discarded.</td>
      <td>Completely eliminates bursts; outputs strictly smoothed constant bit-rate traffic.</td>
    </tr>
    <tr>
      <td><strong>2. Token Bucket</strong></td>
      <td>Tokens generate into the bucket at a constant rate $r$ up to capacity $b$. A packet can only transmit if it captures tokens.</td>
      <td>Allows controlled, regulated bursts up to bucket capacity $b$ while capping average rate at $r$.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">Topic 51 – 54: Application Layer Services (SMTP, DNS, HTTP, DHCP)</h2>

<div class="callout callout-info">
  <div class="callout-title">🧠 Summary of Core Application Protocols & Ports</div>
  <ul>
    <li><strong>SMTP (Port 25/587):</strong> Simple Mail Transfer Protocol; pushes email between client and server and between mail relays.</li>
    <li><strong>DNS (Port 53 - UDP/TCP):</strong> Hierarchical Domain Name System resolving domain names to IP addresses (Records: `A` for IPv4, `AAAA` for IPv6, `MX` for Mail Exchange, `CNAME` for Canonical Alias).</li>
    <li><strong>HTTP/HTTPS (Port 80/443):</strong> Stateless request-response web protocol. Status codes: `200 OK`, `301 Moved Permanently`, `404 Not Found`, `500 Internal Server Error`.</li>
    <li><strong>DHCP (Port 67/68 - UDP):</strong> Dynamic Host Configuration Protocol assigning IP addresses dynamically via the <strong>D-O-R-A</strong> sequence (<strong>D</strong>iscover $\rightarrow$ <strong>O</strong>ffer $\rightarrow$ <strong>R</strong>equest $\rightarrow$ <strong>A</strong>cknowledge).</li>
  </ul>
</div>

<div class="worked-box">
  <div class="worked-title">🌐 [UPLOADED PYQ] Complete Life Cycle: What Happens When You Type `https://example.com`?</div>
  <ol>
    <li><strong>Host IP Configuration (DHCP):</strong> Client uses DHCP DORA sequence to acquire local IP, Subnet Mask, Default Gateway, and DNS Server.</li>
    <li><strong>DNS Resolution:</strong> Browser queries local DNS cache, then queries Recursive Resolver $\rightarrow$ Root Server $\rightarrow$ TLD Server (`.com`) $\rightarrow$ Authoritative Server to obtain target IP for `example.com`.</li>
    <li><strong>ARP Translation:</strong> Host uses Address Resolution Protocol (ARP) to map Default Gateway IP to its physical 48-bit MAC address.</li>
    <li><strong>TCP 3-Way Handshake:</strong> Client sends `SYN` (Port 443) $\rightarrow$ Server replies `SYN-ACK` $\rightarrow$ Client confirms `ACK` (Connection Established).</li>
    <li><strong>TLS 1.3 Handshake:</strong> Client and server negotiate cipher suites, authenticate server X.509 certificate, and exchange ephemeral Diffie-Hellman keys to establish encrypted session.</li>
    <li><strong>HTTP GET Request & IP Routing:</strong> Browser transmits encrypted `GET / HTTP/2` request. Packet is encapsulated with IP header and routed across intermediate Autonomous Systems via OSPF and BGP-4.</li>
    <li><strong>Server Processing & Response:</strong> Web server processes request and returns HTTP `200 OK` response with HTML/CSS payload.</li>
    <li><strong>Browser Rendering:</strong> Browser parses HTML DOM tree, fetches CSS/JS, and renders the visual webpage!</li>
  </ol>
</div>

<h2 class="section-title">🧠 M5 Active Recall & Exam Questions [UPLOADED PYQ]</h2>

<div class="qa-card">
  <div class="qa-q">Q1. [UPLOADED PYQ] Explain the structure and working of the IPv4 Header with the purpose of all major fields. (10 Marks)</div>
  <div class="qa-a">
    The IPv4 header has a minimum size of 20 bytes (up to 60 bytes with options):<br>
    1. <em>Version (4b):</em> `4` for IPv4.<br>
    2. <em>IHL (4b):</em> Header length in 32-bit words (min 5).<br>
    3. <em>Total Length (16b):</em> Header + Data in bytes.<br>
    4. <em>Identification (16b), Flags (3b), Fragment Offset (13b):</em> Fragmentation management for MTU limits.<br>
    5. <em>TTL (8b):</em> Hop limit decremented at each router to prevent packet looping.<br>
    6. <em>Protocol (8b):</em> Transport demultiplexing (`6`=TCP, `17`=UDP).<br>
    7. <em>Header Checksum (16b):</em> Error detection across header fields.<br>
    8. <em>Source IP (32b) & Destination IP (32b):</em> Logical sender and receiver addresses.
  </div>
</div>
"""
