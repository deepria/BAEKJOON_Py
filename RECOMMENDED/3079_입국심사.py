import sys


def is_possible(gate, m, time_limit):
    total = 0
    for g in gate:
        total += time_limit // g
    return total >= m


def sol():
    n, m, *gate = map(int, sys.stdin.read().split())
    gate.sort()

    left = 0
    right = gate[-1] * m

    answer = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible(gate, m, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


sol()
