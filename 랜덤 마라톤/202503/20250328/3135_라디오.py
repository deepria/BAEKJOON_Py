import sys


def sol():
    read = sys.stdin.read().splitlines()
    now, to = map(int, read[0].split())
    n = int(read[1])
    with_favorites = min([abs(int(read[i]) - to) + 1 for i in range(2, 2 + n)])
    direct = abs(to - now)
    print(min(with_favorites, direct))


sol()
