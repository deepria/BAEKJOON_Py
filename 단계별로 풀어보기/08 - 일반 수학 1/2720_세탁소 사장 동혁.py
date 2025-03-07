import sys


def sol():
    read = list(map(int, sys.stdin.read().strip().split()))
    for e in read[1:]:
        sys.stdout.write(f'{e // 25} {e % 25 // 10} {e % 25 % 10 // 5} {e % 25 % 10 % 5}\n')


sol()
