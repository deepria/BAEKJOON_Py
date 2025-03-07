import sys


def sol():
    arr = map(int, sys.stdin.read().rstrip().split())
    s = set()
    for e in arr:
        s.add(e % 42)
    sys.stdout.write(str(len(s)))


sol()
