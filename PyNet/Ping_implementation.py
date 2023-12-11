"""
Another day of learning computer networks. i was reading about the well known ping command, and thought to myself,
why not try to implement it in python? so here i am.

while working on ping there is a few things to keep in mind:
1. the ping command is a command line command, so i will have to use the subprocess module.
2. the ping command is a system command, so it will be different on different operating systems.
3. the ping command is a network command, so i will have to use the socket module. https://docs.python.org/3/library/socket.html
4. the ping's echo request and echo reply are ICMP packets, so i will have to use the ICMP protocol.
   the exchange of echos happens between a source and a destination, so i will have to use the IP protocol.
5. echo request are should be 32 bytes or 100 bytes on cisco devices.
6. the echo request and reply should have the same id and sequence number.
7. the echo request and reply should have the same checksum.
8. the echo request and reply should have the same data.
9. the echo request and reply should have the same ttl.
10. the echo request and reply should have the same source and destination.
11. RTT is the time it takes for the echo request to reach the destination and the echo reply to reach the source.
12. TTl is the number of hops the echo request took to reach the destination. on windows the default ttl is 128 and
    on linux the default ttl is 64. on cisco devices the default ttl is 255. the ttl is decremented by 1 on each hop.

so let's start working on pingo, my implementation of the ping command.
"""
# import the modules
import subprocess
import socket
import struct
import random
import time
import sys

# define the functions
def random_ip(class_choice):
    # if the ip is class A, the first octet will be between 1 and 126
    # if the ip is class B, the first octet will be between 128 and 191
    # if the ip is class C, the first octet will be between 192 and 223
    # if the ip is class D, the first octet will be between 224 and 239
    # if the ip is class E, the first octet will be between 240 and 255
    if class_choice == "A":
        ip = f"{random.randint(1, 126)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        return ip
    elif class_choice == "B":
        ip = f"{random.randint(128, 191)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        return ip
    elif class_choice == "C":
        ip = f"{random.randint(192, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        return ip
    elif class_choice == "D":
        ip = f"{random.randint(224, 239)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        return ip
    elif class_choice == "E":
        ip = f"{random.randint(240, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        return ip
    else:
        print("Invalid class, please try again.")

