# Python IP Address Checker

Created by: Levin Vincent

## Project Overview

A Python-based networking tool that validates IP addresses, identifies their IP version, determines whether they are public or private, and tests network connectivity using the ping command.

## Features

- Validates IPv4 and IPv6 addresses.
- Identifies IP address versions.
- Classifies addresses as public or private.
- Tests network reachability using ping.
- Handles invalid IP address inputs.

## Technologies Used

- Python 3
- "ipaddress" module
- "subprocess" module
- Windows Command Prompt

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code or Command Prompt.
4. Run:

python ip_checker.py

5. Enter an IP address when prompted.

## Example

Enter an IP address: 8.8.8.8

IP Address: 8.8.8.8
Version: IPv 4
Type: Public IP Address

NETWORK CONNECTIVITY TEST
Status: IP address is reachable!

Note: A failed ping does not necessarily mean an IP address is offline. Some networks block ping requests.

## Purpose

This project was developed to strengthen practical Python programming and computer networking skills.ip-address-checker.
