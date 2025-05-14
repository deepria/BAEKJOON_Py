import sys


def sol():
    read = sys.stdin.read().splitlines()
    n = int(read[0])
    for i in range(1, n + 1):
        a, b = map(int, read[i].split())
        sys.stdout.write('1\n' if b % a == 0 and b // a >= 2 else '0\n')


sol()
