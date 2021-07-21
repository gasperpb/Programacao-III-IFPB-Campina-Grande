
import math


def isPrime(n):
    start = 2

    while start <= math.sqrt(n):
        if n % start < 1:
            return False
        start += 1

    return n > 1


print(isPrime(12))
print(isPrime(13))
