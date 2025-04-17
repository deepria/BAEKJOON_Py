from sys import stdin, stdout


def sol():
    read = stdin.read().splitlines()
    n, m = map(int, read[0].split())
    arr = [[*map(int, read[i].split())] for i in range(1, n + 1)]
    k = int(read[n + 1])
    for i in range(n + 2, k + n + 2):
        a, b, x, y = map(int, read[i].split())
        s = 0
        for q in arr[a - 1:x]:
            s += sum(q[b - 1:y])
        stdout.write(str(s) + '\n')


# sol()


# 누적합 최적화
def sol_prefix_sum():
    read = stdin.read().splitlines()
    n, m = map(int, read[0].split())
    arr = [[*map(int, read[i].split())] for i in range(1, n + 1)]
    print(arr)

    # 누적합 배열 생성 (1-based index)
    sums = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sums[i][j] = (
                    sums[i - 1][j] + sums[i][j - 1]
                    - sums[i - 1][j - 1] + arr[i - 1][j - 1]
            )
    print(sums)

    k = int(read[n + 1])
    for i in range(n + 2, n + 2 + k):
        a, b, x, y = map(int, read[i].split())
        s = (
                sums[x][y] - sums[a - 1][y]
                - sums[x][b - 1] + sums[a - 1][b - 1]
        )
        stdout.write(str(s) + '\n')


sol_prefix_sum()
