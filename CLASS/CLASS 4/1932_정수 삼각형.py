import sys


def sol():
    read = sys.stdin.read().splitlines()
    n = int(read[0])

    if n == 1:
        print(read[1])
        return

    arr = [list(map(int, read[i].split())) for i in range(1, n + 1)]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                arr[i][j] += arr[i - 1][j]
            elif j == i:
                arr[i][j] += arr[i - 1][j - 1]
            else:
                arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

    print(max(arr[n - 1]))


sol()
