import socket


def recvall(sock, delim):
    data = b""
    while True:
        more = sock.recv(1)

        if more == delim:
            break
        data += more
    return data


def atende_cliente(sc):
    print("Atendendo Cliente", sc.getpeername())

    msg = recvall(sc, b"\n").decode().upper() + "\n"
    sc.sendall(msg.encode())

    sc.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()

        atende_cliente(sc)

    return 0


if __name__ == "__main__":

    main()
