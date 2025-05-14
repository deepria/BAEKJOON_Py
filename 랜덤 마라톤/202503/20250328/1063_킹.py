import sys

move_dir = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1),
}


def in_board(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8


def sol():
    king, stone, t = sys.stdin.readline().split()
    kx, ky = ord(king[0]) - 64, int(king[1])
    sx, sy = ord(stone[0]) - 64, int(stone[1])
    for _ in range(int(t)):
        cmd = sys.stdin.readline().strip()
        dx, dy = move_dir[cmd]
        nkx, nky = kx + dx, ky + dy
        if in_board(nkx, nky):
            if nkx == sx and nky == sy:
                nsx, nsy = sx + dx, sy + dy
                if in_board(nsx, nsy):
                    kx, ky = nkx, nky
                    sx, sy = nsx, nsy
            else:
                kx, ky = nkx, nky
    print(f"{chr(kx + 64)}{ky}")
    print(f"{chr(sx + 64)}{sy}")


sol()
