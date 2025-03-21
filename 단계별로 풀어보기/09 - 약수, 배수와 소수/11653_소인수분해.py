import sys


def sol():
    n = int(sys.stdin.read().strip())
    if n != 1:
        factors = []

        while n % 2 == 0:
            factors.append(2)
            n //= 2

        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i

        if n > 1:
            factors.append(n)

        print(*factors, sep='\n')


sol()
