import socket
MAXBYTES = 65535


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 50000))
    while True:
        data, address = sock.recvfrom(MAXBYTES)
        new_data = data.decode().upper()
        if new_data == 'SAIR':
            Client.emit('disconnect')
        sock.sendto(new_data.encode(), address)

    sock.close()
    return 0


if __name__ == '__main__':
    main()
