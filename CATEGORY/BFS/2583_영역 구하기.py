import sys
from collections import deque

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(grid, x, y, w, h):
    queue = deque([(x, y)])
    grid[x][y] = 0
    a = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 1:
                queue.append((nx, ny))
                grid[nx][ny] = 0
                a += 1
    return a


def sol():
    read = sys.stdin.read().splitlines()
    m, n, k = map(int, read[0].split())
    grid = [[1] * n for _ in range(m)]
    for i in range(1, k + 1):
        y1, x1, y2, x2 = map(int, read[i].split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x][y] = 0

    areaCnt = 0
    areaArr = []
    for x in range(m):
        for y in range(n):
            if grid[x][y] == 1:
                areaArr.append(bfs(grid, x, y, n, m))
                areaCnt += 1

    print(areaCnt)
    print(*sorted(areaArr))


sol()
