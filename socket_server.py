import socket
MAXBYTES = 65535


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 50000))
    data, address = sock.recvfrom(MAXBYTES)
    print("Cliente {} transmitiu {}".format(address, data.decode()))
    sock.sendto("Olá, Cliente UDP".encode(), address)
    sock.close()
    return 0
main()