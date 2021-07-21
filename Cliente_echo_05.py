import socket
MAXBYTES = 65535


def main():
    # 1.cria um soquete e define o modo de uso dele como udc
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        nota1 = input("Nota 1 : ")
        nota2 = input("Nota 2 : ")
        notas = nota1+'x'+nota2
        sock.sendto(notas.encode(), ('127.0.0.1', 50000))
        print("Meu endereço e:  ", sock.getsockname())
        data, address = sock.recvfrom(MAXBYTES)
        if sock.recvfrom < 7:
            final = input("Nota da final : ")
            sock.sendto(final.encode(), ('127.0.0.1', 50000))
        print("Servidor responde: {}".format(data.decode()))
    sock.close()
    return 0


if __name__ == '__main__':
    main()
