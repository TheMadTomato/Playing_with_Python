import socket
import requests
import uuid

def get_internal_ip():
    return socket.gethostbyname(socket.gethostname())

def get_external_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    data = response.json()
    return data['ip']

def get_subnet_mask():
    return socket.gethostbyname(socket.gethostname())

def get_mac_address():
    return ':'.join(format(b, '02x') for b in uuid.getnode().to_bytes(6, 'big'))

def get_ipv6_address():
    try:
        ipv6_addresses = [addr[0] for addr in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)]
        return ipv6_addresses[0] if ipv6_addresses else "No IPv6 address found"
    except socket.gaierror:
        return "No IPv6 address found"

def main():
    while True:
        print("Menu:")
        print("1. Show Internal IP")
        print("2. Show External IP")
        print("3. Show Subnet Mask")
        print("4. Show MAC Address")
        print("5. Show IPv6 Address")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Internal IP: " + get_internal_ip())
        elif choice == "2":
            print("External IP: " + get_external_ip())
        elif choice == "3":
            print("Subnet Mask: " + get_subnet_mask())
        elif choice == "4":
            print("MAC Address: " + get_mac_address())
        elif choice == "5":
            print("IPv6 Address: " + get_ipv6_address())
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

