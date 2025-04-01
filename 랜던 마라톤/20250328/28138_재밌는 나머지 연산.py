from sys import stdin

def sol():
    n, r = map(int, stdin.readline().split())
    diff = n - r
    total = 0
    i = 1
    while i * i <= diff:
        if diff % i == 0:
            j = diff // i
            if i > r:
                total += i
            if j != i and j > r:
                total += j
        i += 1

    print(total)

sol()