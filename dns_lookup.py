import socket
from banner import banner


def dns_lookup(domain):
    print("\nLooking up:", domain)
    print("-" * 50)

    # IPv4 Address
    try:
        ipv4 = socket.gethostbyname(domain)
        print(f"IPv4 Address : {ipv4}")
    except socket.gaierror:
        print("IPv4 Address : Not Found")

    # Hostname
    try:
        hostname = socket.getfqdn(domain)
        print(f"Hostname     : {hostname}")
    except:
        print("Hostname     : Not Found")

    # IPv6 Address
    try:
        ipv6 = socket.getaddrinfo(domain, None, socket.AF_INET6)
        print(f"IPv6 Address : {ipv6[0][4][0]}")
    except:
        print("IPv6 Address : Not Found")

    # Reverse DNS
    try:
        reverse = socket.gethostbyaddr(socket.gethostbyname(domain))
        print(f"Reverse DNS  : {reverse[0]}")
    except:
        print("Reverse DNS  : Not Found")


def main():
    banner()

    domain = input("Enter Domain (example: google.com): ").strip()

    dns_lookup(domain)


if __name__ == "__main__":
    main()
