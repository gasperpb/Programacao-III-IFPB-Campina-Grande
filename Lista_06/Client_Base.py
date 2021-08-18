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
    sock.connect(("127.0.0.1", 50000))

    print(" Socket: ", sock.getsockname())

    msg = input("Entre com uma mensagem: ") + "\n"

    sock.sendall(msg.encode())
    print(recvall(sock, b"\n").decode())

    sock.close()

    return 0


if __name__ == "__main__":
    main()
