from sys import stdin, stdout, exit
from math import log


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, v in enumerate(is_prime) if v]


def main():
    read = stdin.readlines()
    n = int(read[0])
    nn = n * n
    board = [[*map(int, read[i].split())] for i in range(1, nn + 1)]
    blanks = sum(1 for i in range(nn) for j in range(nn) if board[i][j] == 0)
    forbidden = set()
    trial_primes = sieve(1000)
    for i in range(nn):
        for j in range(nn):
            x = board[i][j]
            if x > 1:
                tmp = x
                for p in trial_primes:
                    if p * p > tmp:
                        break
                    if tmp % p == 0:
                        forbidden.add(p)
                        while tmp % p == 0:
                            tmp //= p
                if tmp > 1:
                    forbidden.add(tmp)
    forbidden_count = len(forbidden)
    need = blanks + forbidden_count

    if need < 6:
        upper = 15
    else:
        upper = int(need * (log(need) + log(log(need)))) + 1000
    primes = sieve(upper)
    available = []
    for p in primes:
        if len(available) >= blanks:
            break
        if p not in forbidden:
            available.append(p)
    idx = 0
    for i in range(nn):
        for j in range(nn):
            if board[i][j] == 0:
                board[i][j] = available[idx]
                idx += 1
    for row in board:
        stdout.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    exit(main())
