import sys


def sol():
    read = list(map(int, sys.stdin.read().strip().split()))
    n, m, e = read[0], read[1], read[2:]
    for i in range(n * m):
        sys.stdout.write(f"{e[i] + e[i + n * m]}")
        if (i + 1) % n != 0:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('\n')


sol()
