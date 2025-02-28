import sys


def sol():
    a, b = map(int, sys.stdin.readline().strip().split())
    while a != 0 and b != 0:
        if b % a == 0:
            sys.stdout.write('factor')
        elif a % b == 0:
            sys.stdout.write('multiple')
        else:
            sys.stdout.write('neither')
        sys.stdout.write('\n')
        a, b = map(int, sys.stdin.readline().strip().split())


sol()
