def mat_mult(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % 1000
    return result


def mat_pow(matrix, power):
    n = len(matrix)
    result = [[int(i == j) for j in range(n)] for i in range(n)]

    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, matrix)
        matrix = mat_mult(matrix, matrix)
        power //= 2
    return result


def main():
    from sys import stdin
    read = stdin.read().splitlines()
    n, b = map(int, read[0].split())
    base = [[*map(int, read[i].split())] for i in range(1, n + 1)]
    result = mat_pow(base, b)
    for r in result:
        print(*r)


if __name__ == "__main__":
    main()
