from sys import stdin, stdout


def ccw(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


def segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    cross = dx1 * dy2 - dy1 * dx2

    if cross == 0:
        if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
            stdout.write('LINE\n')
        else:
            stdout.write('NONE\n')
        return
    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1
    a2 = y4 - y3
    b2 = x3 - x4
    c2 = a2 * x3 + b2 * y3
    det = a1 * b2 - a2 * b1
    if det == 0:
        stdout.write('NONE\n')
    else:
        x = (b2 * c1 - b1 * c2) / det
        y = (a1 * c2 - a2 * c1) / det
        x = round(x + 1e-10, 2)
        y = round(y + 1e-10, 2)
        stdout.write(f'POINT {x:.2f} {y:.2f}\n')


def main():
    read = lambda: stdin.readline().rstrip()
    for _ in range(int(read())):
        segment_intersection(*map(int, read().split()))


if __name__ == "__main__":
    main()
