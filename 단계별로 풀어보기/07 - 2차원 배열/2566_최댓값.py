import sys


def sol():
    read = list(map(int, sys.stdin.read().strip().split()))
    m = max(read)
    row, col = divmod(read.index(m), 9)
    print(f'{m}\n{row + 1} {col + 1}')


sol()
