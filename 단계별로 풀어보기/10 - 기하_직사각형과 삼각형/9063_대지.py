import sys


def sol():
    read = list(map(int, sys.stdin.read().strip().split()))
    x_a, y_a = read[1::2], read[2::2]
    print((max(x_a) - min(x_a)) * (max(y_a) - min(y_a)))


sol()
