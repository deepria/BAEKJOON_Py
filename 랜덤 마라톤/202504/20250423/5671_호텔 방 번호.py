from sys import stdin, stdout


def main():
    read = stdin.read().splitlines()
    for r in read:
        n, m = map(int, r.split())
        cnt = 0
        for i in range(n, m + 1):
            if len({*str(i)}) == len(str(i)):
                cnt += 1
        stdout.write(str(cnt) + '\n')


main()
