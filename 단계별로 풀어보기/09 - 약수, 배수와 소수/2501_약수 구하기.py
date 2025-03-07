import sys


def sol():
    a, b = map(int, sys.stdin.readline().strip().split())
    for i in range(1, a + 1):
        if a % i == 0:
            b -= 1
        if b == 0:
            print(i)
            break
    if b != 0:
        print(0)


sol()
