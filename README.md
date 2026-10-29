
# Project Title

A brief description of what this project does and who it's for

# 🚀 SQL Injection Log Analyzer

A high-performance, native Python command-line utility designed for application security engineers and incident responders. This script parses web server access logs line-by-line, isolates malicious IP addresses, and leverages regular expression pattern matching to flag SQL Injection (SQLi) attack signatures.

## ✨ Key Features
* **Line-by-Line Stream Parsing:** Engineered to read large log files efficiently without exhausting system RAM.
* **Granular Signature Engine:** Matches diverse SQLi attack vectors including classic tautologies (`OR 1=1`), comments, UNION statements, and stored procedure execution.
* **Attacker IP Isolation:** Uses native string boundaries to correctly map attack signatures back to their originating source IP address.
* **Instant Signal Interception:** Hooks cleanly into `SIGINT` (Ctrl+C) via kernel-level process teardown (`os._exit`) for immediate termination.


## 🛠️ Installation & Setup

1. **Clone or download the project script files** into your working directory.
2. Ensure you have **Python 3.6 or higher** installed:
   ```bash
   python --version

No external dependencies are required. The script uses standard internal Python engine modules.



## 🕹️ Usage Guide Command


| Flag | Long Flag     | Required                | Description |
| :-------- | :------- | :------------------------- | :-----------|
| -f | --file | Yes | Path to the target web access log file to analyze. |
| -h | --help | No | Displays the automated help menu overview. |

## Running the Analyzer 
To execute a scan against a local log file, open your terminal and run:
    
    python log_analyzer.py -f access.log

## 🛡️ Security Considerations
This utility is designed for defensive incident response and educational workflows. It runs entirely locally. However, when handling real-world access logs, ensure that you sanitize any sensitive PII (Personally Identifiable Information) or valid session tokens before sharing those logs outside of your secure environment.

## Known Limitations
**Regex-Based Constraints:** The tool relies on pattern matching. It will not catch highly obfuscated zero-day SQLi payloads or blind time-based injections that avoid standard SQL meta-characters.

**Encoding:** Currently, the tool assumes standard URL-encoded payloads (like %27 for '). Attackers using double-encoding or non-standard character sets may bypass the current signature list.

## Future Improvements
-   Add dynamic URL decoding (e.g., using urllib.parse.unquote) before running the regex to catch multi-encoded attacks.
-   Add an export feature to save the final summary to a .csv or .json file for easier ingestion into reporting dashboards.
-  Expand the signature database to include NoSQL injection patterns.
