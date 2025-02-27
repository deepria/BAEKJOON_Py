import math
import sys


def sol():
    n, b = sys.stdin.read().strip().split()
    r = 0
    b = int(b)
    l = len(n) - 1
    for i in range(l + 1):
        e = ord(n[i]) - 55
        if e < 10:
            r += int(n[i]) * math.pow(b, l - i)
        else:
            r += e * math.pow(b, l - i)
    print(int(r))


sol()
