import socket
MAXBYTES = 65535


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto("Olá, Cliente UDP".encode(), ("localhost", 50000))
    data, address = sock.recvfrom(MAXBYTES)
    print("servidor  {} responde com{}".format(address, data.decode()))

    sock.close()
    return 0


if __name__ == '__main__':
    main()
