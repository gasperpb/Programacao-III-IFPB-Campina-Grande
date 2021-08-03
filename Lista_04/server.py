import socket
import pickle


def recvall(sock):
    data = b""
    while True:
        more = sock.recv(1024)

        if not more:
            break
        data += more
    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 50000))
    sock.listen(3)

    print("Ouvindo em", sock.getsockname())

    while True:

        sc, sockname = sock.accept()
        sc.shutdown(socket.SHUT_WR)

        msg = recvall(sc)

        print("Dados recebidos: ", pickle.loads(msg))
        sc.close()

    return 0


main()
