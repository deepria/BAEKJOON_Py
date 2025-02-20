import sys
from collections import deque

dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

def bfs_tomato(box, h, n, m):
    queue = deque()

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if box[z][x][y] == 1:
                    queue.append((z, x, y, 0))

    max_days = 0

    while queue:
        z, x, y, days = queue.popleft()
        max_days = max(max_days, days)

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = 1
                    queue.append((nz, nx, ny, days + 1))

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if box[z][x][y] == 0:
                    return -1

    return max_days


def sol():
    m, n, h = map(int, sys.stdin.readline().split())
    box = [[[0] * m for _ in range(n)] for _ in range(h)]

    for z in range(h):
        for x in range(n):
            box[z][x] = list(map(int, sys.stdin.readline().split()))

    print(bfs_tomato(box, h, n, m))


sol()
