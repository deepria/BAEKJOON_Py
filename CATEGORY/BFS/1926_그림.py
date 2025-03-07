import sys
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(n, m, grid, start_x, start_y):
    queue = deque([(start_x, start_y)])
    grid[start_x][start_y] = 0
    size = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                queue.append((nx, ny))
                grid[nx][ny] = 0
                size += 1

    return size


def sol():
    input = sys.stdin.read
    data = input().splitlines()
    n, m = map(int, data[0].split())

    grid = [list(map(int, data[i + 1].split())) for i in range(n)]

    max_size, count = 0, 0

    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                count += 1
                size = bfs(n, m, grid, x, y)
                if size > max_size:
                    max_size = size

    print(count)
    print(max_size)


sol()
