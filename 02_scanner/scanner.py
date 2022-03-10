#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<------------------------------------------------------>")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""")
print("You have selected option: ", resp)


if resp == '1':
    scanFlags = '-v -sS'
    portTypes = 'tcp'
elif resp == '2':
    scanFlags = '-v -sU'
    portTypes = 'udp'
elif resp == '3':
    scanFlags = '-v -sS -sV -sC -A -O'
    portTypes = 'tcp'
else:
    print("Please enter a valid option")
    exit 

print("Nmap Version: ", scanner.nmap_version())
scanner.scan(ip_addr, '1-1024', scanFlags)
print(scanner.scaninfo())
print("Ip Status: ", scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())
print("Open Ports: ", scanner[ip_addr][portTypes].keys())