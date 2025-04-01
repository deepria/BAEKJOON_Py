from sys import stdin, stdout


def sol():
    t = int(stdin.readline())
    for _ in range(t):
        _ = stdin.readline()
        result = sum(list(map(int, stdin.readline().split())))
        if result == 0:
            stdout.write('Equilibrium\n')
        elif result>0:
            stdout.write('Right\n')
        else:
            stdout.write('Left\n')



sol()
