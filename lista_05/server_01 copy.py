""" Altere o código apresentado no material de modo que, ao invés de JSON, o Cliente/Servidor 
passem a trabalhar com CSV. Você não precisará manipular arquivos, pode usar uma string para
armazenar os dados CSV. Você pode separar as linhas com um 
\n ou, se preferir, pode enviar linha por linha para o Servidor. 
Caso opte por enviar linha a linha, crie um mecanismo para que o Servidor saiba quando todos os dados chegarem. """

import socket
import struct
import json
import zlib


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
    return msg.split(",")


def toCSV(msg):
    str_csv = ",".join(msg)
    return str_csv


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        notas = fromCSV(decompress(recvmsg(sc)).decode())
        for aluno in notas.values():
            n1 = float(aluno[1])
            n2 = float(aluno[2])
            n3 = float(aluno[3])
            aluno.append((n1 + n2 + n3) / 3)
        sendmsg(sc, compress(toCSV(notas).encode()))
        sc.close()

    return 0


main()
