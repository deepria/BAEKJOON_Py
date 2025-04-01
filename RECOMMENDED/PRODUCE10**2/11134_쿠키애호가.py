from sys import stdin
from math import ceil


def sol():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, c = map(int, stdin.readline().strip().split())
        print(ceil(n / c))


sol()
