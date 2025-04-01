from sys import stdin, stdout


def sol():
    r, c = map(int, stdin.readline().split())
    earth = [[False] * c for _ in range(r)]
    print(earth)

    for i in range(r):
        read = stdin.readline()
        for j in range(c):
            if read[j] == 'X':
                earth[i][j] = True

    print(earth)

    four_direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    after_earth = [[earth[i][j] for j in range(c)] for i in range(r)]

    for i in range(r):
        for j in range(c):
            if earth[i][j]:
                sea_cnt = 0
                for dx, dy in four_direction:
                    if 0 <= i + dx <= r-1 and 0 <= j + dy <= c-1:
                        if not earth[i + dx][j + dy]:
                            sea_cnt += 1
                if sea_cnt >= 3:
                    after_earth[i][j] = False

    print(after_earth)


sol()
