import sys

arr = []


def backtrack(depth, n, m):
    global arr
    if depth == m:
        sys.stdout.write(f"{' '.join(arr)}\n")
        return

    for i in range(1, n + 1):
        arr.append(str(i))
        backtrack(depth + 1, n, m)
        arr.pop()


def sol():
    read = sys.stdin.read().splitlines()
    n, m = map(int, read[0].split())
    backtrack(0, n, m)


sol()
