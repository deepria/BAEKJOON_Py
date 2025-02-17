import sys


def sol():
    n = int(sys.stdin.readline().rstrip())
    result = [' ' * (n - i - 1) + '*' * (i + 1) for i in range(n)]
    print('\n'.join(result))


sol()
