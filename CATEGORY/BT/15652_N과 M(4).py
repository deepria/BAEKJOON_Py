import sys

arr = []


def backtrack(start, n, m):
    global arr
    if len(arr) == m:
        sys.stdout.write(f"{' '.join(arr)}\n")
        return

    for i in range(start, n + 1):
        arr.append(str(i))
        backtrack(i + 1, n, m)
        arr.pop()


def sol():
    n, m = map(int, sys.stdin.read().strip().split())
    backtrack(1, n, m)


sol()
