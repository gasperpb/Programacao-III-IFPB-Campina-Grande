import socket
from typing import Match


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))

        if not more:
            raise EOFError("Cliente não enviou todos os dados esperados")
        data += more
    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 50000))
    sock.listen(1)
    print("Ouvindo em", sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print("Aceitando conexão de ", sockname)
        print("  Nome do Socket: ", sc.getsockname())
        print("  Host Remoto: ", sc.getpeername())

        n1 = recvall(sc, 13)
        n2 = recvall(sc, 13)
        n1.decode()
        n2.decode()
        n3 = Match.min(n1, n2)

        sc.sendall("O Menor número é" + n3.encode())
        sc.close()

    return 0


if __name__ == "__main__":
    main()
