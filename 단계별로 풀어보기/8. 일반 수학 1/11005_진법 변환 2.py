import sys


def sol():
    n, b = map(int, sys.stdin.read().strip().split())
    r = ''
    while n != 0:
        x, y = divmod(n, b)
        r += str(y) if y < 10 else chr(y + 55)
        n = x

    print(r[::-1])


sol()
