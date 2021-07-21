import socket
MAXBYTES = 65535


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 50000))
    while True:
        data, address = sock.recvfrom(MAXBYTES)
        new_data = data.decode()
        notas = new_data.split("x")
        media = (float(notas[0])+float(notas[1]))/2
        if media < 7:
            mfinal = (float(media)+float(new_data))/2
            sock.sendto(float(mfinal).encode(), address)
        else:
            sock.sendto(float(media).encode(), address)
    sock.close()
    return 0


if __name__ == '__main__':
    main()
