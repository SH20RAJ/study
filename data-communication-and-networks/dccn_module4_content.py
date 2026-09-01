# DCCN Module 4 Exhaustive Content (12-15 Pages Target)
# Neuroscience-backed formatting: High visual chunking, KaTeX equations, worked trace boxes, exam cards

DCCN_M4_EXHAUSTIVE = r"""
<div class="toc-box">
  <div class="toc-title"><i class="fa-solid fa-list-check"></i> Module IV: Network Layer, IP Addressing & Routing Algorithms</div>
  <div class="toc-grid">
    <div>1. Network Layer Service Models: Virtual-Circuit vs. Datagram Packet Switching</div>
    <div>2. IPv4 Header Format: 20-Byte Field Breakdown & Fragmentation Fields (Offset, Flags)</div>
    <div>3. Classful IP Addressing (Classes A, B, C, D, E & Special Loopback / Private Blocks)</div>
    <div>4. Subnetting & Classless Inter-Domain Routing (CIDR) Slash Notation ($/n$)</div>
    <div>5. Longest Prefix Match Algorithm in Forwarding Tables with Worked Lookups</div>
    <div>6. IPv6 Protocol Architecture: 40-Byte Fixed Base Header & Extension Headers</div>
    <div>7. IPv4 to IPv6 Transition Mechanisms: Dual-Stack, Tunneling & Header Translation</div>
    <div>8. Unicast Routing Principles: Intra-AS (IGP) vs. Inter-AS (EGP) Autonomous Systems</div>
    <div>9. Distance Vector Routing (DVR): Bellman-Ford Equation & Count-to-Infinity Problem</div>
    <div>10. Solutions to Count-to-Infinity: Split Horizon & Poisoned Reverse Mechanisms</div>
    <div>11. Link State Routing (LSR): Link State Advertisements & Dijkstra's Algorithm Tree</div>
    <div>12. Comprehensive Solved BIT Mesra & GATE Exam Question Bank (8 Questions)</div>
  </div>
</div>

<h2 class="section-title">Topic 2 – 4: IPv4 Datagram Format & CIDR Subnetting</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">IPv4 Header Field</th>
      <th style="width: 15%;">Bit Width</th>
      <th>Functional Purpose & Transmission Invariant</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Version</strong></td>
      <td>4 bits</td>
      <td>Identifies IP version (`0100` for IPv4).</td>
    </tr>
    <tr>
      <td><strong>Header Length (IHL)</strong></td>
      <td>4 bits</td>
      <td>Length of header in 32-bit (4-byte) words. Minimum value is $5$ ($20$ bytes).</td>
    </tr>
    <tr>
      <td><strong>Total Length</strong></td>
      <td>16 bits</td>
      <td>Entire datagram length (Header + Data) in bytes. Max size $= 65,535$ bytes.</td>
    </tr>
    <tr>
      <td><strong>Identification, Flags, Offset</strong></td>
      <td>$16 + 3 + 13$ bits</td>
      <td>Handles MTU packet fragmentation. Fragment Offset is measured in 8-byte units. `DF`=Don't Fragment, `MF`=More Fragments.</td>
    </tr>
    <tr>
      <td><strong>Time to Live (TTL)</strong></td>
      <td>8 bits</td>
      <td>Hop counter decremented by 1 at each router to prevent infinite forwarding loops. Discarded with ICMP Time Exceeded when $\text{TTL} = 0$.</td>
    </tr>
    <tr>
      <td><strong>Protocol</strong></td>
      <td>8 bits</td>
      <td>Demultiplexing to transport layer (`6` for TCP, `17` for UDP, `1` for ICMP).</td>
    </tr>
    <tr>
      <td><strong>Header Checksum</strong></td>
      <td>16 bits</td>
      <td>1's complement sum of header fields recalculated at every router as TTL decrements.</td>
    </tr>
  </tbody>
</table>

<div class="worked-box">
  <div class="worked-title">🏛️ Step-by-Step Solved Problem: CIDR Subnet Allocation</div>
  <p><strong>Problem:</strong> An organization is assigned the network block `200.10.20.0/24`. It needs to divide this block into 4 equal subnets for 4 departments.</p>
  <ol>
    <li>
      <strong>Step 1: Determine Additional Subnet Bits ($k$):</strong>
      $$2^k \ge 4 \implies k = 2 \text{ bits}$$
      New Subnet Mask: $/24 + 2 = \mathbf{/26} \implies \mathbf{255.255.255.192}$.
    </li>
    <li>
      <strong>Step 2: Compute Total and Usable Host Addresses per Subnet:</strong>
      $$\text{Total Addresses per Subnet} = 2^{32 - 26} = 2^6 = \mathbf{64}$$
      $$\text{Usable Host Addresses} = 64 - 2 = \mathbf{62} \quad (\text{subtracting Network ID and Directed Broadcast})$$
    </li>
    <li>
      <strong>Step 3: Subnet Allocation Table:</strong>
      <table class="custom-table">
        <tr><th>Subnet</th><th>Network Address</th><th>Usable Host IP Range</th><th>Broadcast Address</th></tr>
        <tr><td>Dept 1</td><td>`200.10.20.0/26`</td><td>`200.10.20.1` – `200.10.20.62`</td><td>`200.10.20.63`</td></tr>
        <tr><td>Dept 2</td><td>`200.10.20.64/26`</td><td>`200.10.20.65` – `200.10.20.126`</td><td>`200.10.20.127`</td></tr>
        <tr><td>Dept 3</td><td>`200.10.20.128/26`</td><td>`200.10.20.129` – `200.10.20.190`</td><td>`200.10.20.191`</td></tr>
        <tr><td>Dept 4</td><td>`200.10.20.192/26`</td><td>`200.10.20.193` – `200.10.20.254`</td><td>`200.10.20.255`</td></tr>
      </table>
    </li>
  </ol>
</div>

<h2 class="section-title">Topic 9 – 11: Routing Algorithms (Distance Vector vs. Link State)</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Feature</th>
      <th style="width: 37%;">Distance Vector Routing (DVR — RIP)</th>
      <th>Link State Routing (LSR — OSPF)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Mathematical Algorithm</strong></td>
      <td><strong>Bellman-Ford Equation:</strong>
        $$D_x(y) = \min_v \{ c(x, v) + D_v(y) \}$$
      </td>
      <td><strong>Dijkstra's Shortest Path Algorithm:</strong> Computes full shortest-path tree from source.</td>
    </tr>
    <tr>
      <td><strong>Information Exchanged</strong></td>
      <td>Vector of estimated distances to all destinations.</td>
      <td>Exact state and cost of directly attached links (LSA).</td>
    </tr>
    <tr>
      <td><strong>Destination of Updates</strong></td>
      <td>Sent only to directly adjacent neighbors.</td>
      <td>Flooded globally to all routers in the entire network area.</td>
    </tr>
    <tr>
      <td><strong>Convergence & Stability</strong></td>
      <td>Slow convergence; prone to <strong>Count-to-Infinity</strong> routing loops.</td>
      <td>Fast convergence; completely immune to routing loops.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">🏛️ Top BIT Mesra Exam Questions & Answers (Module IV)</h2>

<div class="qa-card">
  <div class="qa-q">Q1. Explain the Count-to-Infinity problem in Distance Vector Routing and how Split Horizon with Poison Reverse resolves it. (8 Marks)</div>
  <div class="qa-a">
    - <strong>Count-to-Infinity Problem:</strong> When a link $A-B$ goes down, router $A$ sets its cost to $\infty$. However, neighbor $C$ may still advertise that it has a path to $A$ via $B$ with cost 2. Router $B$ receives this and updates its cost to $A$ as $2 + 1 = 3$, advertising it back to $C$. $C$ updates to $3 + 1 = 4$, and both routers slowly increment their distance vectors step-by-step up to $\infty$ (16 in RIP).<br>
    - <strong>Split Horizon with Poison Reverse:</strong> If router $C$ routes traffic to destination $X$ through neighbor $B$, $C$ advertises its distance to $X$ back to $B$ as $\infty$ ($\text{Poisoned Reverse}$). This prevents $B$ from wrongly routing traffic back through $C$ during link failures.
  </div>
</div>
"""
