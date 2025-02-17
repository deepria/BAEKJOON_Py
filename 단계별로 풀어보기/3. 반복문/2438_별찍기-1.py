import sys


def sol():
    n = int(sys.stdin.readline().rstrip())
    result = ['*' * (i + 1) for i in range(n)]
    print('\n'.join(result))


def sol2():
    n = int(sys.stdin.readline().rstrip())
    result = ''
    for i in range(n):
        for j in range(n):
            if j <= i:
                result += '*'
        result += '\n'
    print(result)


sol()
