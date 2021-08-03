import socket
import struct


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("Falha ao receber os dadosesperados.")
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
        msg = recvall(sc, 9)
        nums = struct.unpack("!iic", msg)
        print(nums)

        if nums[2] == b"+":
            sc.sendall(struct.pack("!i", nums[0] + nums[1]))
        elif nums[2] == b"-":
            sc.sendall(struct.pack("!i", nums[0] - nums[1]))
        elif nums[2] == b"*":
            sc.sendall(struct.pack("!i", nums[0] * nums[1]))
        elif nums[2] == b"/":
            sc.sendall(struct.pack("!i", nums[0] / nums[1]))
    """    else:
            sc.sendall(struct.pack("!ii", "Valor errado!")) """

    sc.close()

    return 0


main()
