import sys


def sol():
    n, m = map(int, sys.stdin.readline().strip().split())
    arr = [i + 1 for i in range(n)]
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().strip().split())
        a,b,c = arr[:i-1],arr[i-1:j][::-1],arr[j:]
        arr = a + b + c

    print(*arr)


sol()
