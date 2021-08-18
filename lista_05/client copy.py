import socket
import struct
import json
import zlib
import csv


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))

        if not more:
            raise EOFError("Falha ao receber os dados esperados.")
        data += more
    return data


def recvmsg(sock):
    tam = struct.unpack("!i", recvall(sock, 4))[0]
    return recvall(sock, tam)


def sendmsg(sock, msg):
    sock.sendall(struct.pack("!i", len(msg)))
    sock.sendall(msg)


def compress(msg):
    return zlib.compress(msg)


def decompress(msg):
    return zlib.decompress(msg)


def toJSON(msg):
    return json.dumps(msg)


def fromJSON(msg):
    return json.loads(msg)


def fromCSV(msg):
    csv = "", join(
        map(
            str,
        )
    )
    return msg.split(",")


def toCSV(msg):
    csv = ",".join(msg) + "\n"
    return csv


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 50000))

    notas = []

    while True:
        nome = input("Entre com o nome do Aluno: ")
        if not nome:
            break
        n1 = input("Entre com a Nota 1: ")
        n2 = input("Entre com a Nota 2: ")
        n3 = input("Entre com a Nota 3: ")
        notas = [nome, n1, n2, n3]

    sendmsg(sock, compress(toCSV(notas).encode()))

    res = fromCSV(decompress(recvmsg(sock)).decode())

    for nome, nota in res.items():
        print("Aluno ", nome, "obteve média ", nota[3])

    sock.close()

    return 0


if __name__ == "__main__":
    main()
