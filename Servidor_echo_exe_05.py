import socket
MAXBYTES = 65535


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 50000))
    while True:
        data, address = sock.recvfrom(MAXBYTES)
        nota1 = data.decode()
        nota2 = data.decode()
        media = (float(nota1)+float(nota2))/2
        sock.sendto(media.encode(), address)
    sock.close()
    return 0


if __name__ == '__main__':
    main()
