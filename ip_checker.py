# Project 2: Network IP Checker
# Created by Levin Vincent

import ipaddress
import subprocess

ip = input("Enter an IP address: ")

try:
    address = ipaddress.ip_address(ip)

    print("\n--- IP ADDRESS INFORMATION ---")
    print("IP Address:", address)
    print("Version: IPv", address.version)

    if address.is_private:
        print("Type: Private IP Address")
    else:
        print("Type: Public IP Address")

    print("\n--- NETWORK CONNECTIVITY TEST ---")
    print("Checking connection...")

    result = subprocess.run(
        ["ping", "-n", "1", "-w", "2000", str(address)],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("Status: IP address is reachable!")
    else:
        print("Status: No ping response received.")

except ValueError:
    print("Invalid IP Address!")