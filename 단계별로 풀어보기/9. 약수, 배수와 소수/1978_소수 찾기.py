import sys


def sol():
    read = list(map(int, sys.stdin.read().strip().split()))
    cnt = 0
    for e in read[1:]:
        if e == 1:
            continue
        temp = [i for i in range(1, e+1) if e % i == 0]
        cnt += 1 if len(temp) == 2 else 0
    print(cnt)


sol()
