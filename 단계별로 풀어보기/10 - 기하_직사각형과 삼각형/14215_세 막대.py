import sys


def sol():
    arr = sorted(list(map(int, sys.stdin.read().strip().split())))
    print(2 * arr[0] + 2 * arr[1] - 1 if arr[2] >= arr[0] + arr[1] else sum(arr))


sol()
