#!/usr/bin/env python3
"""
Finalizes DCCN Suite:
1. Pushes Module 1 over 10 pages.
2. Expands Full Course Master Book with Socket Programming Lab Guide & Master Revision to achieve 55+ pages!
"""

import os

DCCN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-communication-and-networks"))

M1_FINAL_PUSH = r"""
<h2 class="section-title">Topic 13.11: Comprehensive Protocol Architectures & Network Performance Metrics</h2>

<div class="worked-box">
  <div class="worked-title">🏛️ Solved Numerical 9: Packetization Delay vs. Propagation Latency in Real-Time Voice (VoIP)</div>
  <p>In a Voice-over-IP (VoIP) network, human speech is encoded at $64\text{ kbps}$ using G.711 PCM. The voice encoder generates $20\text{ ms}$ voice sample frames before encapsulating into RTP/UDP/IP packets ($40\text{ bytes}$ header). The packet travels across a $2000\text{ km}$ fiber optic link ($v = 2 \times 10^8\text{ m/s}$) with transmission bandwidth $100\text{ Mbps}$. Calculate: (1) Payload size per VoIP packet in bytes, (2) Packetization delay, (3) Transmission delay, (4) Propagation delay, and (5) Total one-way latency.</p>
  <p><strong>Solution:</strong></p>
  <ul>
    <li>Payload size per $20\text{ ms}$ voice block: $\text{Payload} = \frac{64,000 \text{ bps} \times 0.020\text{ s}}{8 \text{ bits/byte}} = \mathbf{160 \text{ bytes}}$.</li>
    <li>Total Packet Size (Header + Data): $40 + 160 = \mathbf{200 \text{ bytes (1600 bits)}}$.</li>
    <li><strong>Packetization Delay:</strong> The time required to accumulate $20\text{ ms}$ of continuous human speech = $\mathbf{20.0 \text{ ms}}$.</li>
    <li><strong>Transmission Delay:</strong> $T_{\text{trans}} = \frac{1600 \text{ bits}}{100 \times 10^6 \text{ bps}} = 0.000016\text{ s} = \mathbf{0.016 \text{ ms}}$.</li>
    <li><strong>Propagation Delay:</strong> $T_{\text{prop}} = \frac{2000 \times 10^3 \text{ m}}{2 \times 10^8 \text{ m/s}} = 0.010\text{ s} = \mathbf{10.0 \text{ ms}}$.</li>
    <li><strong>Total One-Way Voice Latency:</strong> $20.0\text{ ms} + 0.016\text{ ms} + 10.0\text{ ms} = \mathbf{30.016 \text{ ms}}$ (Well within ITU-T G.114 target of $< 150\text{ ms}$ for crystal-clear interactive voice!).</li>
  </ul>
</div>

<div class="qa-card">
  <div class="qa-q">Q15. Explain Network Reliability, Mean Time Between Failures (MTBF), and Mean Time to Repair (MTTR) with Availability formula. (6 Marks)</div>
  <div class="qa-a">
    Network Availability measures the percentage of operational uptime in a communication infrastructure:<br>
    $$\mathbf{\text{Availability } A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\%}$$
    Where $\text{MTBF}$ is Mean Time Between Failures, and $\text{MTTR}$ is Mean Time to Repair. A telecom-grade "Five Nines" ($99.999\%$) network allows no more than <strong>5.26 minutes of unscheduled downtime per year</strong>, necessitating redundant hot-standby routers, dual-homed BGP links, and rapid failover protocols!
  </div>
</div>
"""

DCCN_LAB_GUIDE = r"""
<div class="page-break"></div>
<div class="cover-container" style="margin-top: 40px;">
  <div class="course-badge">Hands-On Practical Lab Master Appendix</div>
  <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">DCCN Socket Programming & Packet Analysis Master Guide</h2>
  <div style="font-size: 12.5px; color: #64748b;">Complete C & Python Socket Implementations, Wireshark Protocol Traces & Simulation Architectures</div>
</div>

<h2 class="section-title">Lab Topic 1: Berkeley Socket API & POSIX System Call Architecture</h2>

<p>
  A <strong>Socket</strong> is an endpoint for process-to-process network communication across the transport layer. In UNIX and Linux operating systems, sockets are represented as standard integer file descriptors manipulated via system calls:
</p>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 25%;">Socket System Call</th>
      <th style="width: 45%;">Operating System Action</th>
      <th>Client vs. Server</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>`socket(AF_INET, SOCK_STREAM, 0)`</td><td>Creates an IPv4 TCP communication endpoint and returns a socket descriptor.</td><td>Both Client and Server</td></tr>
    <tr><td>`bind(sockfd, &addr, sizeof(addr))`</td><td>Binds the socket to a specific local IP address and 16-bit Port number.</td><td>Server Routine</td></tr>
    <tr><td>`listen(sockfd, backlog)`</td><td>Transitions TCP socket into passive listening state with incoming connection queue.</td><td>Server Routine</td></tr>
    <tr><td>`accept(sockfd, &client_addr, &len)`</td><td>Blocks until incoming SYN arrives; completes 3-way handshake, returns new active socket.</td><td>Server Routine</td></tr>
    <tr><td>`connect(sockfd, &serv_addr, len)`</td><td>Initiates TCP 3-Way Handshake with remote server socket.</td><td>Client Routine</td></tr>
    <tr><td>`send()` / `recv()` (or `read`/`write`)</td><td>Transfers stream data across the established full-duplex TCP socket buffer.</td><td>Both Client and Server</td></tr>
    <tr><td>`close(sockfd)`</td><td>Initiates TCP 4-Way connection teardown (FIN/ACK) and frees kernel descriptor.</td><td>Both Client and Server</td></tr>
  </tbody>
</table>

<h2 class="section-title">Lab Topic 2: Complete Production-Grade TCP Echo Server in C</h2>

<pre><code class="language-c">#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;unistd.h&gt;
#include &lt;arpa/inet.h&gt;

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    socklen_t addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    // 1. Create TCP Socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) &lt; 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 2. Set Socket Options (SO_REUSEADDR prevents "Address already in use" errors)
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    // 3. Configure Server Address Structure
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY; // Bind to all local interfaces (0.0.0.0)
    address.sin_port = htons(PORT);       // Host-to-Network Short byte order conversion

    // 4. Bind Socket to Address & Port
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) &lt; 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // 5. Listen for incoming connections (Queue backlog = 5)
    if (listen(server_fd, 5) &lt; 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("TCP Echo Server listening on port %d...\n", PORT);

    // 6. Accept incoming client connection
    while (1) {
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, &addrlen)) &lt; 0) {
            perror("Accept error");
            continue;
        }
        printf("Client connected: %s:%d\n", inet_ntoa(address.sin_addr), ntohs(address.sin_port));

        // 7. Echo Loop: Read from client and write back identical data
        ssize_t valread;
        while ((valread = read(new_socket, buffer, BUFFER_SIZE)) &gt; 0) {
            write(new_socket, buffer, valread);
            memset(buffer, 0, BUFFER_SIZE);
        }
        close(new_socket);
        printf("Client disconnected.\n");
    }
    close(server_fd);
    return 0;
}</code></pre>

<h2 class="section-title">Lab Topic 3: High-Performance Concurrent UDP Server in Python</h2>

<pre><code class="language-python">import socket

HOST = "0.0.0.0"
PORT = 9090
BUFFER_SIZE = 2048

# Create Datagram Socket (UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"UDP Server active on {HOST}:{PORT}...")

while True:
    data, client_addr = sock.recvfrom(BUFFER_SIZE)
    message = data.decode('utf-8', errors='ignore')
    print(f"Received from {client_addr}: {message.strip()}")
    
    # Send UDP reply
    reply = f"ACK: {message}".encode('utf-8')
    sock.sendto(reply, client_addr)
</code></pre>

<h2 class="section-title">Lab Topic 4: Wireshark Packet Sniffing & Protocol Dissection Trace</h2>

<table class="custom-table">
  <thead>
    <tr>
      <th style="width: 18%;">Filter Syntax</th>
      <th style="width: 40%;">Wireshark Display Action</th>
      <th>Network Troubleshooting Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>`tcp.port == 80`</td><td>Filters all unencrypted HTTP traffic.</td><td>Inspecting web requests, response headers, status codes.</td></tr>
    <tr><td>`dns`</td><td>Displays all DNS queries and authoritative responses.</td><td>Diagnosing domain name resolution latency.</td></tr>
    <tr><td>`icmp`</td><td>Shows Ping request/replies and ICMP error reports.</td><td>Verifying network connectivity and MTU path discovery.</td></tr>
    <tr><td>`tcp.flags.syn == 1 && tcp.flags.ack == 0`</td><td>Isolates initial TCP connection establishment requests.</td><td>Detecting TCP SYN Flood Distributed Denial of Service (DDoS) attacks.</td></tr>
    <tr><td>`ip.addr == 192.168.1.1`</td><td>Filters all packets originating from or destined to gateway router.</td><td>Monitoring local default gateway traffic.</td></tr>
    <tr><td>`tcp.analysis.retransmission`</td><td>Highlights duplicate TCP retransmission segments.</td><td>Detecting physical link degradation, buffer overflow, and high packet loss.</td></tr>
  </tbody>
</table>
"""

def finalize_dccn():
    with open(os.path.join(DCCN_DIR, "dccn_module1_content.py"), "r", encoding="utf-8") as f:
        m1 = f.read()
    if "Topic 13.11: Comprehensive Protocol" not in m1:
        m1 = m1.rstrip().rstrip('"""').rstrip() + M1_FINAL_PUSH + '\n"""\n'
        with open(os.path.join(DCCN_DIR, "dccn_module1_content.py"), "w", encoding="utf-8") as f:
            f.write(m1)
        print("Finalized M1 content.")

    # Update generate_dccn_suite.py to append Lab guide & Revision into master book
    with open(os.path.join(DCCN_DIR, "generate_dccn_suite.py"), "r", encoding="utf-8") as f:
        gen_code = f.read()
    
    # Include LAB Guide in generate_dccn_suite
    if "DCCN_LAB_GUIDE =" not in gen_code:
        gen_code = f'DCCN_LAB_GUIDE = r"""{DCCN_LAB_GUIDE}"""\n\n' + gen_code
        
        # Replace full master construction
        old_master_body = """    full_master_html = wrap_html(
        "Data Communication & Computer Networks (CS24305) Full Course Master",
        "Exhaustive 52-Topic Textbook & Solved University Question Bank (Modules I–V)",
        "".join(full_body)
    )"""
        new_master_body = """    # Append Lab Guide and 10-Page Revision to Master Book for 55+ Pages
    full_body.append(DCCN_LAB_GUIDE)
    full_body.append(f'''
    <div class="page-break"></div>
    <div class="cover-container" style="margin-top: 40px;">
      <div class="course-badge">Comprehensive Revision Appendix</div>
      <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">10-Page Master Quick Revision Guide</h2>
      <div style="font-size: 12.5px; color: #64748b;">High-Yield Formulas, Protocol Checklists & Solved Exam Cards</div>
    </div>
    {DCCN_REVISION_EXHAUSTIVE}
    ''')
    full_master_html = wrap_html(
        "Data Communication & Computer Networks (CS24305) Full Course Master",
        "Exhaustive 52-Topic Textbook, Lab Socket Manual & Solved University Question Bank",
        "".join(full_body)
    )"""
        gen_code = gen_code.replace(old_master_body, new_master_body)
        with open(os.path.join(DCCN_DIR, "generate_dccn_suite.py"), "w", encoding="utf-8") as f:
            f.write(gen_code)
        print("Updated generate_dccn_suite.py with Master Lab & Revision Book integration.")

if __name__ == "__main__":
    finalize_dccn()
