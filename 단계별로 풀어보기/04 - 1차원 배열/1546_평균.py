import sys


def sol():
    data = sys.stdin.read().rstrip().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    m = max(arr)
    result = 0
    for i in range(n):
        result += arr[i] / m * 100
    print(result / n)


sol()
