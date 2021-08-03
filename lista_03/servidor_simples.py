import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()
        print("Aceitando conexão de ", sockname)
        print("  Nome do Socket: ", sc.getsockname())
        print("  Host Remoto: ", sc.getpeername())
        msg = sc.recv(20)
        print("Mensagem recebida: ", msg.decode())
        sc.sendall("Oi, Cliente".encode())
        sc.close()
    return 0


if __name__ == "__main__":
    main()
