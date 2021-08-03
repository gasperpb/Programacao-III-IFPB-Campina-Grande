import socket
import struct


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))

        if not more:
            raise EOFError("Falha ao receber os dados esperados.")
        data += more
    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 50000))

    print(" Socket: ", sock.getsockname())

    number_1 = int(input("Enter your first number: "))
    operation = input(
        """
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    """
    )
    number_2 = int(input("Enter your second number: "))

    msg = struct.pack("!iic", number_1, number_2, operation.encode())

    sock.sendall(msg)
    res = recvall(sock, 4)
    print("Result! ", struct.unpack("!i", res)[0])

    sock.close()

    return 0


main()
