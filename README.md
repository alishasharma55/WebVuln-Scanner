🔍 Web Vulnerability Scanner using WMAP (Metasploit) & Python
🎯 Project Objective

A security testing project that performs web service discovery, crawling, vulnerability scanning and report generation on a purposely vulnerable machine.
This tool helps identify common vulnerabilities like SQL Injection, XSS, WebDAV misconfigurations and weak database authentication.

🧪 Testing Environment

Target Virtual Machine: ****

Attacking System: ****

Web Server Detected: ****

Scanner Module: ****

Target IP: 192.168.60.129

Scanned Web Labs:

🛠 Tools & Libraries Used
Tool / Library	Purpose
****	Web vulnerability scanning using WMAP
****	Service and port reconnaissance
****	Custom scanner automation
****	Web request handling
****	Automating Nmap scans
****	CLI highlighting
****	Scan progress display
🚀 Features

✅ Discovers active services and versions
✅ Crawls available web endpoints
✅ Detects web vulnerabilities with payload testing
✅ Generates structured scan report (wmap‑report.txt)
✅ Provides basic remediation suggestions

⚠️ Vulnerabilities Detected
Vulnerability	Risk
SQL Injection	HIGH
Reflected XSS	MEDIUM
WebDAV PUT Enabled	MEDIUM
phpinfo.php Exposed	HIGH
MySQL Root login without password	CRITICAL
🧾 Sample Output Report

Report file stored as: wmap‑report.txt

📥 How to Run the Scanner

Clone the repository

git clone <your-repo-url>


Give execute permission (if script requires)

chmod +x scanner.py


Install dependencies

pip3 install -r requirements.txt


Run the scanner

python3 scanner.py
