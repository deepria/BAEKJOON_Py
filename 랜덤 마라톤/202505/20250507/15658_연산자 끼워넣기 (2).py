n = int(input())
numbers = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())

max_val = -1e9
min_val = 1e9


def dfs(idx, current, plus, minus, mul, div):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return

    if plus:
        dfs(idx + 1, current + numbers[idx], plus - 1, minus, mul, div)
    if minus:
        dfs(idx + 1, current - numbers[idx], plus, minus - 1, mul, div)
    if mul:
        dfs(idx + 1, current * numbers[idx], plus, minus, mul - 1, div)
    if div:
        if current < 0:
            dfs(idx + 1, -(-current // numbers[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, current // numbers[idx], plus, minus, mul, div - 1)


dfs(1, numbers[0], pl, mi, mu, di)
print(max_val)
print(min_val)
