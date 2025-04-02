import sys


def get_divisors(n):
    if n < 1:
        return []

    small_divisors = []
    large_divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            small_divisors.append(i)
            if i != n // i:
                large_divisors.append(n // i)

    return small_divisors + large_divisors[::-1]


def sol():
    read = list(map(int, sys.stdin.read().strip().split()[1:]))
    for y in read:
        divs = get_divisors(y)
        if (sum(divs) - y) <= y:
            sys.stdout.write('BOJ 2022\n')
            continue
        else:
            is_boj = False
            for d in divs:
                if d == y:
                    continue
                else:
                    divdivs = get_divisors(d)
                    if (sum(divdivs) - d) > d:
                        is_boj = False
                        sys.stdout.write('BOJ 2022\n')
                        break
                    else:
                        is_boj = True
            if is_boj:
                sys.stdout.write('Good Bye\n')


sol()
