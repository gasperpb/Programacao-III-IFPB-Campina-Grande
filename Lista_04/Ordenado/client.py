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
    sock.connect(("127.0.0.1", 50000))

    print("socket: ", sock.getsockname())

    msg = [100, 200, 600, 0, 400, 100, 250, 900]
    print("lista enviada: ", msg)
    sock.sendall(pickle.dumps(msg))
    sock.shutdown(socket.SHUT_WR)

    res = recvall(sock)
    print("lista enviada: ", pickle.loads(res))

    sock.close()


if __name__ == "__main__":
    main()
