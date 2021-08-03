import socket


def recvall(sock, delim):
    data = b""
    while True:
        more = sock.recv(1)

        if more == delim:
            break
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

        print(recvall(sc, b"\n").decode())
        sc.sendall("É sim!\n".encode())

        print(recvall(sc, b"\n").decode())
        sc.sendall("É sim!\n".encode())

        print(recvall(sc, b"\n").decode())
        sc.sendall("É sim!\n".encode())

        sc.close()
    return 0


main()
