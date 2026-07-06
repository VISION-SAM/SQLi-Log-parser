# 🚀 SQL Injection Log Analyzer

A high-performance, native Python command-line utility designed for application security engineers and incident responders. This script parses web server access logs line-by-line, isolates malicious IP addresses, and leverages regular expression pattern matching to flag SQL Injection (SQLi) attack signatures.

## ✨ Key Features
* **Line-by-Line Stream Parsing:** Engineered to read large log files efficiently without exhausting system RAM.
* **Granular Signature Engine:** Matches diverse SQLi attack vectors including classic tautologies (`OR 1=1`), comments, UNION statements, and stored procedure execution.
* **Attacker IP Isolation:** Uses native string boundaries to correctly map attack signatures back to their originating source IP address.
* **Instant Signal Interception:** Hooks cleanly into `SIGINT` (Ctrl+C) via kernel-level process teardown (`os._exit`) for immediate termination.

---

## 🛠️ Installation & Setup

1. **Clone or download the project script files** into your working directory.
2. Ensure you have **Python 3.6 or higher** installed:
   ```bash
   python --version

No external dependencies are required. The script uses standard internal Python engine modules.

🕹️ Usage Guide Command 
Flag   | Long Flag | Required | Description 
-f     | --file    | Yes      | Path to the target web access log file to analyze.
-h     | --help    | No       | Displays the automated help menu overview.

## Running the Analyzer 
To execute a scan against a local log file, open your terminal and run:
    Bash
    python log_analyzer.py -f access.log

## 📊 Example Console OutputWhen a signature matches, the tool formats a clean, scannable dashboard:Plaintext[*] Initializing Scan on File: access.log

============================================================
[💥] SQLi ALERT
    ├── Attacker IP : 192.168.1.45
    └── Attack Text : =admin%27%20OR%20%271%27=%271&pass=secret HTTP/1.
----------------------------------------
[💥] SQLi ALERT
    ├── Attacker IP : 10.0.4.11
    └── Attack Text : =corporate%27%20UNION%20SELECT%201,2,version(),4%

============================================================
[!] ANALYSIS COMPLETE. Total Malicious Entries Found: 2
============================================================

[+] Summary of Unique Attack Vectors Identified:
  └── Signature: (\%27)|(\')|(\-\-)|(\%23)|(#)
  └── Signature: ((\%27)|(\'))union

[+] Source Malicious IPs Blocklist:
  └── 192.168.1.45
  └── 10.0.4.11

## 🛡️ Security Disclaimer
This utility is designed strictly for educational, defensive, and authorized incident response security workflows. Always ensure you have explicit permission before processing proprietary corporate application logs.