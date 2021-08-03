import socket
MAXBYTES = 65535


def main():
    # 1.cria um soquete e define o modo de uso dele como udc
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        nota1 = input("Nota 1 : ")
        nota2 = input("Nota 2 : ")
        sock.sendto(nota1.encode(), ('127.0.0.1', 50000))
        sock.sendto(nota2.encode(), ('127.0.0.1', 50000))
        data, address = sock.recvfrom(MAXBYTES)
        final = data.encode()
        if float(final) < 7:
            input("Nota da final : ")
            sock.sendto(final.encode(), ('127.0.0.1', 50000))
        print("Servidor responde: {}".format(data.decode()))
    sock.close()
    return 0


if __name__ == '__main__':
    main()
