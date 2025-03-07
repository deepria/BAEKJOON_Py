import sys


def sol():
    in_arr = set(map(int, sys.stdin.read().rstrip().split()))
    arr = {i + 1 for i in range(30)}
    missing = arr - in_arr
    print(*sorted(missing), sep='\n')


sol()
