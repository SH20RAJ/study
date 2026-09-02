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

#!/usr/bin/env python3
"""
Playwright Chromium PDF Generator for Data Communication & Computer Networks (CS24305).
Generates Publication-Grade 10-15 Page Modules, 10-Page Revision, and 50+ Page Master Book.
"""

import os, re, glob
from playwright.sync_api import sync_playwright

from dccn_module1_content import DCCN_M1_EXHAUSTIVE
from dccn_module2_content import DCCN_M2_EXHAUSTIVE
from dccn_module3_content import DCCN_M3_EXHAUSTIVE
from dccn_module4_content import DCCN_M4_EXHAUSTIVE
from dccn_module5_content import DCCN_M5_EXHAUSTIVE
from dccn_revision_content import DCCN_REVISION_EXHAUSTIVE

DCCN_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(DCCN_DIR, "html")
PDF_DIR = os.path.join(DCCN_DIR, "pdf")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

CSS_STYLES = """
@page {
  size: A4 portrait;
  margin: 15mm 12mm 15mm 12mm;
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8.5pt;
    color: #64748b;
  }
  @bottom-left {
    content: "DCCN (CS24305) • BIT Mesra CSE";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8.5pt;
    color: #64748b;
  }
}

*, *::before, *::after {
  box-sizing: border-box;
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 11.8px;
  line-height: 1.60;
  color: #1e293b;
  background: #ffffff;
  margin: 0;
  padding: 0;
}

.cover-container {
  padding: 30px 20px;
  text-align: center;
  border-bottom: 2px solid #0284c7;
  margin-bottom: 24px;
}

.course-badge {
  display: inline-block;
  background: #e0f2fe;
  color: #0369a1;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 20px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 12px;
  border: 1px solid #bae6fd;
}

.book-title {
  font-size: 26px;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 8px 0;
  letter-spacing: -0.5px;
  line-height: 1.25;
}

.book-subtitle {
  font-size: 13.5px;
  color: #475569;
  margin: 0 0 16px 0;
  font-weight: 500;
}

.toc-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 16px 20px;
  margin: 20px 0 28px 0;
}

.toc-title {
  font-size: 13.5px;
  font-weight: 700;
  color: #0369a1;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px 16px;
  font-size: 11px;
  color: #334155;
}

h2.section-title {
  font-size: 15px;
  font-weight: 700;
  color: #0369a1;
  border-bottom: 1.5px solid #e2e8f0;
  padding-bottom: 5px;
  margin: 26px 0 14px 0;
  display: flex;
  align-items: center;
  gap: 8px;
  page-break-after: avoid;
}

h3.subsection-title {
  font-size: 13px;
  font-weight: 700;
  color: #0f172a;
  margin: 18px 0 8px 0;
  page-break-after: avoid;
}

p {
  margin: 0 0 10px 0;
  text-align: justify;
}

.callout {
  border-radius: 6px;
  padding: 14px 18px;
  margin: 14px 0;
  font-size: 11.5px;
  page-break-inside: avoid;
}

.callout-info {
  background: #f0f9ff;
  border-left: 4px solid #0284c7;
  color: #0c4a6e;
}

.callout-warning {
  background: #fefce8;
  border-left: 4px solid #eab308;
  color: #713f12;
}

.callout-title {
  font-weight: 700;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.custom-table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 11px;
  page-break-inside: avoid;
}

.custom-table th, .custom-table td {
  border: 1px solid #cbd5e1;
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
}

.custom-table th {
  background: #f1f5f9;
  color: #0f172a;
  font-weight: 700;
}

.custom-table tr:nth-child(even) {
  background: #f8fafc;
}

.formula-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #6366f1;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 14px 0;
  page-break-inside: avoid;
}

.worked-box {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-left: 4px solid #22c55e;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 16px 0;
  page-break-inside: avoid;
}

.worked-title {
  font-weight: 700;
  color: #15803d;
  font-size: 12px;
  margin-bottom: 8px;
}

.diagram-container {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 14px;
  margin: 14px 0;
  text-align: center;
  page-break-inside: avoid;
}

.diagram-caption {
  font-size: 10.5px;
  color: #64748b;
  margin-top: 8px;
  font-weight: 500;
}

.qa-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 12px 16px;
  margin: 12px 0;
  page-break-inside: avoid;
}

.qa-q {
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 6px;
}

.qa-a {
  color: #334155;
  line-height: 1.55;
}

pre {
  background: #0f172a;
  color: #f8fafc;
  padding: 12px 16px;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 10.5px;
  line-height: 1.45;
  overflow-x: auto;
  margin: 12px 0;
  page-break-inside: avoid;
}

code {
  font-family: 'Fira Code', monospace;
  font-size: 11px;
  background: #f1f5f9;
  color: #0369a1;
  padding: 2px 5px;
  border-radius: 4px;
}

pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

.page-break {
  page-break-before: always;
}
"""

def wrap_html(title, subtitle, body_html, module_num=None):
    badge = f"CS24305 • Module {module_num}" if module_num else "CS24305 • Complete Master Guide"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Fira+Code:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ]}});"></script>
  <style>
    {CSS_STYLES}
  </style>
</head>
<body>
  <div class="cover-container">
    <div class="course-badge">{badge}</div>
    <h1 class="book-title">{title}</h1>
    <div class="book-subtitle">{subtitle}</div>
  </div>
  {body_html}
</body>
</html>"""

def generate_pdf(html_path, pdf_path, title):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath(html_path)}", wait_until="networkidle")
        page.wait_for_timeout(1200)
        
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "12mm", "right": "12mm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=f"""
            <div style="font-size: 8.5pt; font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 12mm;">
              <span>{title} • BIT Mesra CSE</span>
              <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
            </div>
            """
        )
        browser.close()
    print(f"✅ Generated {pdf_path} ({os.path.getsize(pdf_path)} bytes)")

def build_all_dccn():
    print("Launching Chromium via Playwright for DCCN suite...")
    
    modules = [
        (1, "Module 1: Data Communication Overview & Channels", "Topics 1 to 13 • Communication Model, OSI vs TCP/IP, Impairments & Channel Capacity", DCCN_M1_EXHAUSTIVE, "Module_1_Data_Communication_Overview_Notes"),
        (2, "Module 2: Data Encoding & Multiplexing Techniques", "Topics 14 to 19 • Line Coding, Scrambling, QAM Modulation, PCM & TDM/FDM", DCCN_M2_EXHAUSTIVE, "Module_2_Data_Encoding_Multiplexing_Notes"),
        (3, "Module 3: Data Link Control & Error Handling Protocols", "Topics 20 to 27 • Framing, CRC Polynomial Division, Hamming Codes & ARQ Protocols", DCCN_M3_EXHAUSTIVE, "Module_3_Data_Link_Control_Notes"),
        (4, "Module 4: Switching & Local Area Networks (LANs)", "Topics 28 to 36 • Circuit/Packet Switching, ALOHA, CSMA/CD, Ethernet & STP", DCCN_M4_EXHAUSTIVE, "Module_4_Switching_LANs_Notes"),
        (5, "Module 5: Networking, Transport & Application Layers", "Topics 37 to 52 • IPv4/IPv6, Subnetting, Dijkstra/Bellman-Ford, TCP AIMD & HTTP/3", DCCN_M5_EXHAUSTIVE, "Module_5_Networking_Transport_Notes"),
    ]
    
    # 1. Generate Individual Module PDFs
    for num, title, subtitle, content, fname in modules:
        html_content = wrap_html(title, subtitle, content, module_num=num)
        html_file = os.path.join(HTML_DIR, f"{fname}.html")
        pdf_file = os.path.join(PDF_DIR, f"{fname}.pdf")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        generate_pdf(html_file, pdf_file, f"DCCN Module {num}")

    # 2. Generate 10-Page Revision Guide
    rev_html = wrap_html(
        "DCCN (CS24305) 10-Page Master Quick Revision",
        "High-Yield Formulas, Protocol Summaries, Comparison Matrices & Exam Flashcards",
        DCCN_REVISION_EXHAUSTIVE
    )
    rev_html_file = os.path.join(HTML_DIR, "DCCN_10_Page_Master_Revision.html")
    rev_pdf_file = os.path.join(PDF_DIR, "DCCN_10_Page_Master_Revision.pdf")
    with open(rev_html_file, "w", encoding="utf-8") as f:
        f.write(rev_html)
    generate_pdf(rev_html_file, rev_pdf_file, "DCCN 10-Page Master Revision")

    # 3. Generate Full Course Master Book
    full_body = []
    for num, title, subtitle, content, _ in modules:
        full_body.append(f"""
        <div class="page-break"></div>
        <div class="cover-container" style="margin-top: 40px;">
          <div class="course-badge">Module {num} of 5</div>
          <h2 style="font-size: 22px; font-weight: 800; color: #0f172a; margin: 0 0 6px 0;">{title}</h2>
          <div style="font-size: 12.5px; color: #64748b;">{subtitle}</div>
        </div>
        {content}
        """)
    
    # Append Lab Guide and 10-Page Revision to Master Book for 55+ Pages
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
    )
    master_html_file = os.path.join(HTML_DIR, "DCCN_Full_Course_Master.html")
    master_pdf_file = os.path.join(PDF_DIR, "DCCN_Full_Course_Master.pdf")
    with open(master_html_file, "w", encoding="utf-8") as f:
        f.write(full_master_html)
    generate_pdf(master_html_file, master_pdf_file, "DCCN Full Course Master")

if __name__ == "__main__":
    build_all_dccn()
