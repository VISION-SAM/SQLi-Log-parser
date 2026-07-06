import argparse
import sys
import os
import re
import signal

def graceful_exit(sig, frame):
    print("\n[!] Exiting gracefully...")
    os._exit(0)

signal.signal(signal.SIGINT, graceful_exit)

# Regular expression to find potential SQL injection patterns
sqli_patterns = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",  # SQL meta-characters
    r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))",  # SQL meta-characters with equal sign
    r"\w*((\%27)|(\'))(\s)*((\%6F)|o|(\%4F))((\%72)|r|(\%52))",  # SQL 'or' statements
    r"((\%27)|(\'))union",  # SQL union statements
    r"exec(\s|\+)+(s|x)p\w+",  # SQL exec statements
]

ip_pattern = r"\d{1,3}(\.\d{1,3}){3}"

parser = argparse.ArgumentParser(description="SQL Injection Log Analyzer")
parser.add_argument("-f", "--file", required=True, help="Path to the log file")
args = parser.parse_args()  
file = args.file

print(f'[*] Initializing Scan on File: {file}')
print("=" * 60)

potential_sqli = []
suspect_log = []
suspected_ips = []

if not os.path.isfile(file):
    print(f"[!] The file '{file}' does not exist.")
    sys.exit(1)

try:
    with open(file, 'r', encoding='utf-8', errors='ignore') as log_file:
        for line in log_file:
            line = line.strip()
            if not line:
                continue

            # We use this variable to capture the text snippet that triggered the alert
            attack_snippet = None
            matched_signature = False
            
            for pattern in sqli_patterns:
                matches = re.search(pattern, line, re.IGNORECASE)
                if matches:
                    potential_sqli.append(pattern)
                    matched_signature = True
                    # FIXED: Instead of printing the match object, capture the clean string match
                    attack_snippet = matches.group(0)

            if matched_signature:
                suspect_log.append(line)

                ip_match = re.search(ip_pattern, line, re.IGNORECASE)
                line_ip = ip_match.group(0) if ip_match else "Unknown IP"
                suspected_ips.append(line_ip)
                
                # --- CLEAN LIVE ALERT PRINTING ---
                print(f"[💥] SQLi ALERT")
                print(f"    ├── Attacker IP : {line_ip}")
                print(f"    └── Attack Text : {attack_snippet}")
                print("-" * 40)

except Exception as e:
    print(f'[ERROR!] : {e}')

# --- Final Summary Dashboard ---
print("\n" + "=" * 60)
print(f"[!] ANALYSIS COMPLETE. Total Malicious Entries Found: {len(suspect_log)}")
print("=" * 60)

if potential_sqli:
    print("\n[+] Summary of Unique Attack Vectors Identified:")
    for pat in set(potential_sqli):
        print(f"  └── Signature: {pat}")
    
    print("\n[+] Source Malicious IPs Blocklist:")
    for ip in set(suspected_ips):
        print(f"  └── {ip}")
else:
    print("\n[+] No malicious SQL Injection patterns found.")