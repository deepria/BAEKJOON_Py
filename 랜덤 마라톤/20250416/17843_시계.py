from sys import stdin, stdout

t = int(stdin.readline())
for _ in range(t):
    h, m, s = map(int, stdin.readline().split())

    ha = 30 * h + 0.5 * m + (0.5 / 60) * s
    ma = 6 * m + 0.1 * s
    sa = 6 * s

    angles = [ha, ma, sa]
    angles.sort()

    diffs = [
        angles[1] - angles[0],
        angles[2] - angles[1],
        360 - angles[2] + angles[0]
    ]

    stdout.write(str(min(diffs)) + '\n')
