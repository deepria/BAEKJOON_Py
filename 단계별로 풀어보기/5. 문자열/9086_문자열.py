import sys


def sol():
    read = sys.stdin.read().rstrip().split()
    arr = read[1:]
    for s in arr:
        sys.stdout.write(s[0] + s[-1] + '\n')


sol()
