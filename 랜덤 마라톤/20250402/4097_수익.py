import sys

data = sys.stdin.read().split()
index = 0
while True:
    n = int(data[index])
    index += 1
    if n == 0:
        break

    max_current = -10001
    max_global = -10001

    for _ in range(n):
        p = int(data[index])
        index += 1
        if max_current > 0:
            max_current += p
        else:
            max_current = p
        if max_current > max_global:
            max_global = max_current

    print(max_global)
