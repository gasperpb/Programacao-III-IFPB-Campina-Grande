import socket
MAXBYTES = 65535


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 50000))
    while True:
        data, address = sock.recvfrom(MAXBYTES)
        new_data = data.decode()
        a = int(new_data)
        qtd = 0
        for x in range(1, a + 1):
            resto = a % x
            if resto == 0:
                qtd += 1
        if qtd == 2:
            n = 'O número é primo '
        else:
            n = 'O número não é primo'
        sock.sendto(str(n).encode(), address)
    sock.close()
    return 0


if __name__ == '__main__':
    main()
