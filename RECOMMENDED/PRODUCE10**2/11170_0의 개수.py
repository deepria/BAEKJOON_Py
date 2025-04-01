import sys


def count_zeros(n):
    total_zeros = 0
    if n == 0:
        total_zeros += 1
    else:
        while n > 0:
            if n % 10 == 0:
                total_zeros += 1
            n //= 10
    return total_zeros


def sol():
    read = sys.stdin.read().splitlines()
    t = int(read[0])
    for i in range(1, t + 1):
        n, m = map(int, read[i].split())
        cnt = 0
        for j in range(n, m + 1):
            cnt += count_zeros(j)
        print(cnt)


sol()
