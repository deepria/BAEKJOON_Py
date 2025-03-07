import sys


def sol():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        r, s = map(str, sys.stdin.readline().strip().split())
        for s in [e for e in s]:
            for _ in range(int(r)):
                sys.stdout.write(s)
        sys.stdout.write('\n')


sol()
