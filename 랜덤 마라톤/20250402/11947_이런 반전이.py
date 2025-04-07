from sys import stdin, stdout
from math import pow


def sol():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        c = n
        cnt = 0
        while c >= 10:
            c //= 10
            cnt += 1
        l = pow(10, cnt + 1) / 2
        n = n if n <= l else int(l)
        r = ''
        for s in str(n):
            r += str(9 - int(s))
        stdout.write(str(int(r) * n) + '\n')


sol()
