from sys import stdin, stdout

n = int(stdin.readline())
metrix = [[] * n for _ in range(n)]

for i in range(n):
    metrix[i] = list(map(int, stdin.readline().split()))

cut_metrix = []
new_n = n // 2

while new_n != 0:
    cut_metrix = [[0] * new_n for _ in range(new_n)]

    mi, mj = 0, 0
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            arr = sorted([metrix[i][j], metrix[i + 1][j], metrix[i][j + 1], metrix[i + 1][j + 1]], reverse=True)
            cut_metrix[mi][mj] = arr[1]
            mj += 1
        mi += 1
        mj = 0
    n //= 2
    new_n //= 2
    metrix = [e for e in cut_metrix]

print(cut_metrix[0][0])
