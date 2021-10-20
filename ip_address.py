import socket


def get_ip_address(domain):
    return socket.gethostbyname(domain)

print(get_ip_address("sitenum.com"))