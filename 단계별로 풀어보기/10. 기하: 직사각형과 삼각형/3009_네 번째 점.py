import sys
from collections import Counter


def sol():
    arr = list(map(int, sys.stdin.read().strip().split()))
    x_a, y_a = arr[0::2], arr[1::2]
    x = x_a[0] if x_a[1] == x_a[2] else x_a[1] if x_a[0] == x_a[2] else x_a[2]
    y = y_a[0] if y_a[1] == y_a[2] else y_a[1] if y_a[0] == y_a[2] else y_a[2]
    print(x, y)

sol()


def sol_counter():
    arr = list(map(int, sys.stdin.read().strip().split()))
    x, y = arr[0::2], arr[1::2]
    x_res = Counter(x).most_common()[-1][0]
    y_res = Counter(y).most_common()[-1][0]
    print(x_res, y_res)

sol_counter()
