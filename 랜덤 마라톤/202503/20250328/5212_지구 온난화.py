from sys import stdin, stdout


def sol():
    r, c = map(int, stdin.readline().split())
    earth = [[False] * c for _ in range(r)]

    for i in range(r):
        read = stdin.readline()
        for j in range(c):
            if read[j] == 'X':
                earth[i][j] = True

    four_direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    after_earth = [[earth[i][j] for j in range(c)] for i in range(r)]

    for i in range(r):
        for j in range(c):
            if earth[i][j]:
                sea_cnt = 0
                for dx, dy in four_direction:
                    if 0 <= i + dx <= r - 1 and 0 <= j + dy <= c - 1:
                        if not earth[i + dx][j + dy]:
                            sea_cnt += 1
                    else:
                        sea_cnt += 1
                if sea_cnt >= 3:
                    after_earth[i][j] = False

    x1, y1 = r, c
    x2, y2 = 0, 0

    for i in range(r):
        for j in range(c):
            if after_earth[i][j]:
                x1 = min(x1, i)
                y1 = min(y1, j)
                x2 = max(x2, i)
                y2 = max(y2, j)

    if x1 <= x2 and y1 <= y2:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                stdout.write('X' if after_earth[i][j] else '.')
            stdout.write('\n')



sol()
