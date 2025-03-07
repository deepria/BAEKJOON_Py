import sys, math


def sol():
    a, b, v = map(int, sys.stdin.read().strip().split())
    print(math.ceil((v - b) / (a - b)))


sol()
