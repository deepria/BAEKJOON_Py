import sys


def sol():
    n, m = map(int, sys.stdin.readline().strip().split())
    arr = [0 for _ in range(n)]
    for _ in range(m):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        for x in range(i-1,j,1):
            arr[x] = k

    sys.stdout.write(" ".join(map(str, arr)))

def sol_opt():
    n, m = map(int, sys.stdin.readline().strip().split())
    arr = [0] * n
    for _ in range(m):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        for x in range(i-1,j):
            arr[x] = k
    print(*arr)


# sol()

sol_opt()