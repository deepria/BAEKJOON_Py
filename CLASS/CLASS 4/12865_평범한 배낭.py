import sys


def sol():
    read = sys.stdin.read
    n, k, *rest = map(int, read().split())
    items = [(rest[i], rest[i + 1]) for i in range(0, len(rest), 2)]
    dp = [0] * (k + 1)
    for weight, value in items:
        for w in range(k, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    print(max(dp))


sol()


def sol_how():
    read = sys.stdin.read
    n, k, *rest = map(int, read().split())
    items = [(rest[i], rest[i + 1]) for i in range(0, len(rest), 2)]
    dp = [0] * (k + 1)

    for weight, value in items:
        print(f'weight : {weight} , value : {value}')
        print()

        # 뒤에서부터 갱신해야 1개씩만 사용하는 0-1 Knapsack이 됨
        for w in range(k, weight - 1, -1):
            print(f'w : {w}')
            print(f'dp[w] : {dp[w]} , dp[w - weight ({w - weight})] : {dp[w - weight]} + {value}')
            dp[w] = max(dp[w], dp[w - weight] + value)
            print(dp)
            print()

        print()

    print(max(dp))
