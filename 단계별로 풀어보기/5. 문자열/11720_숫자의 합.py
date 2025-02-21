import sys


def sol():
    read = sys.stdin.read().rstrip().split()
    arr = [int(c) for c in read[1]]
    print(sum(arr))


sol()
