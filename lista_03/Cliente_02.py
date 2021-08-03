import socket


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))

    if not more:
        raise EOFError("Cliente não enviou todos os dadosesperados")
        data += more
    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 50000))
    print(" Socket: ", sock.getsockname())
    n1 = input("Digite um Numero : ")
    n2 = input("Digite outro Numero : ")
    sock.send(n1.encode())
    sock.send(n2.encode())

    msg = recvall(sock, 11)
    print("Mensagem recebida: ", msg.decode())


if __name__ == "__main__":
    main()
12
