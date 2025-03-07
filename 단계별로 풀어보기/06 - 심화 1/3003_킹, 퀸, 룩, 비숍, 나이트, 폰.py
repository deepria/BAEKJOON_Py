import sys


def sol():
    arr = [1, 1, 2, 2, 2, 8]
    read = list(map(int, sys.stdin.read().strip().split()))
    for i in range(6):
        arr[i] = arr[i] - read[i]
    print(*arr)


sol()
