# Project 2: IP Address Checker
# Created by Levin Vincent

import ipaddress

ip = input("Enter an IP address: ")

try:
    address = ipaddress.ip_address(ip)

    print("\nIP Address:", address)
    print("Version: IPv", address.version)

    if address.is_private:
        print("Type: Private IP Address")
    else:
        print("Type: Public IP Address")

    print("Valid IP Address!")

except ValueError:
    print("Invalid IP Address!")
