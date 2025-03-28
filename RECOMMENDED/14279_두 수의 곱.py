import sys


def sol():
    a, b, c = map(int, sys.stdin.read().strip().split())
    min_cost = float('inf')
    for A in range(1, 2 * 10 ** 6 + 1):
        b_o = c // A
        for delta in [-1, 0, 1]:
            b_try = b_o + delta
            if b_try <= 0:
                continue
            c_o = A * b_try
            cost = abs(A - a) + abs(b_try - b) + abs(c_o - c)
            min_cost = min(min_cost, cost)

    print(min_cost)


sol()
