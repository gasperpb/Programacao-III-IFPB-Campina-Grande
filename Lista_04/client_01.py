import socket
import pickle


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 50000))
    sock.shutdown(socket.SHUT_RD)

    print(" Socket: ", sock.getsockname())

    msg = {"Dia 1": "30C", "Dia 2": "29C", "Dia 3": "42C"}
    sock.sendall(pickle.dumps(msg))

    sock.close()

    return 0


if __name__ == "__main__":
    main()
