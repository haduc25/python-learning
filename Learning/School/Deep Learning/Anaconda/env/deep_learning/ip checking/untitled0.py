# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:01:16 2023

@author: Admin
"""
import socket

# Get the hostname of the current machine
hostname = socket.gethostname()

# Get the IP address associated with the hostname
ip_address = socket.gethostbyname(hostname)

# Print the IP address
print(ip_address)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 0))
print('listening on port:', sock.getsockname()[1])



# Set the IP address and port number for the hotspot
host_ip = "192.168.137.1" # Change to the IP address of your hotspot network
port_num = 54066  # Change to the port number used by your hotspot

# Create a socket and bind it to the hotspot IP address and port number
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host_ip, port_num))

# Listen for incoming connections
sock.listen()

# Print a message indicating that the script is running
print("Listening for incoming connections...")

# Loop forever and wait for incoming connections
while True:
    # Accept the incoming connection
    conn, addr = sock.accept()

    # Get the IP address of the connected device
    ip_address = addr[0]

    # Print the IP address of the connected device
    print("Device connected: ", ip_address)

    # Exit the loop if a device has connected
    if ip_address != host_ip:
        break

