import sys


def sol():
    read = list(map(int, sys.stdin.read().strip().split()[1:]))
    for y in read:
        sys.stdout.write('Good\n' if (y + 1) % (y % 100) == 0 else 'Bye\n')


sol()
