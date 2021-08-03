import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 50000))

    print(" Socket: ", sock.getsockname())

    sock.sendall("Oi, Servidor!".encode())

    msg = sock.recv(11)
    print("Mensagem recebida: ", msg.decode())

    sock.close()
    return 0


if __name__ == "__main__":
    main()
