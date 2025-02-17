import sys


def sol():
    data = sys.stdin.read().splitlines()
    for line in data:
        a, b = map(int, line.split())
        print(a + b)


sol()
