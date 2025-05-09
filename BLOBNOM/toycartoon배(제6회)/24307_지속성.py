from collections import deque


def pers(n):
    cnt = 0
    while n >= 10:
        prod = 1
        for d in str(n):
            prod *= int(d)
        n = prod
        cnt += 1
    return cnt


def bfs_min(p):
    if p == 0:
        return 0

    q = deque()
    for d in range(1, 10):
        q.append((str(d), d))

    while q:
        s, last = q.popleft()
        n = int(s)
        if pers(n) == p:
            return n
        if len(s) >= 16:
            continue
        for d in range(last, 10):
            q.append((s + str(d), d))


def main():
    p = int(input())
    print(bfs_min(p) if p != 1 else 10)


if __name__ == "__main__":
    main()
