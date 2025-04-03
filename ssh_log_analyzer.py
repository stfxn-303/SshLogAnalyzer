import os
import re
from collections import defaultdict
#imports

#The path to the authentication log file
LOG_FILE_PATH = "/var/log/auth.log"

#Set the limit for failed login attempts before blocking
THRESHOLD = 5

#Dictionary that stores failed login attempts per IP
failed_attempts = defaultdict(int)

#Read log file and analyze failed login attempts
with open(LOG_FILE_PATH, "r") as log_file:
    for line in log_file:
        match = re.search(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

#Print summary of detected failed logins
print("\nFailed SSH Login Attempts: ")
for ip, count in failed_attempts.items():
    print(f"IP: {ip} | Failed Attempts: {count}")

#Block IPs that exceed the threshold
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"Blocking IP: {ip} (Failed Attempts: {count})")
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
