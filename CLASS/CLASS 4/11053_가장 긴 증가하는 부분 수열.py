import sys


def sol():
    read = list(map(int, sys.stdin.read().strip().split()))
    a = read[0]
    arr = read[1:]
    dp = [1] * a

    for i in range(a):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


sol()
