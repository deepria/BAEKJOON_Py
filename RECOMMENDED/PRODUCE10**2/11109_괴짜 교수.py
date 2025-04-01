from sys import stdin, stdout


def sol():
    t = int(stdin.readline().strip())
    for _ in range(t):
        d, n, s, p = map(int, stdin.readline().strip().split())
        result = (n * p + d) - n * s
        if result == 0:
            stdout.write('does not matter\n')
        elif result > 0:
            stdout.write('do not parallelize\n')
        else:
            stdout.write('parallelize\n')


sol()
