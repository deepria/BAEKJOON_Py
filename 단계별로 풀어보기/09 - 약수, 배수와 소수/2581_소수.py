import sys


# 브르투포스
def sol_bf():
    m, n = map(int, sys.stdin.read().strip().split())
    arr = []
    for e in range(m, n + 1):
        if e == 1:
            continue
        temp = [i for i in range(1, e + 1) if e % i == 0]
        if len(temp) == 2:
            arr.append(temp[1])
    if len(arr) == 0:
        print(-1)
    else:
        print(f'{sum(arr)}\n{arr[0]}')


# sol_bf()

# 에라토스테네스의 체
def sol():
    m, n = map(int, sys.stdin.read().strip().split())

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    primes = [i for i in range(m, n + 1) if prime[i]]

    if primes:
        print(f'{sum(primes)}\n{primes[0]}')
    else:
        print(-1)


sol()
