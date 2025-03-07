import sys


def sol():
    case = list(map(int, sys.stdin.read().strip().split()))
    for c in case:
        if c == -1:
            break
        temp = [i for i in range(1, c) if c % i == 0]
        if sum(temp) == c:
            sys.stdout.write(f'{c} = ' + ' + '.join(map(str, temp)) + '\n')
        else:
            sys.stdout.write(f'{c} is NOT perfect.\n')


sol()
