import sys


def sol():
    s = list(map(str,sys.stdin.read().strip().split('\n')))
    for e in s:
        sys.stdout.write(f'{e}\n')

sol()
