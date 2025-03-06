import sys
from collections import deque


def bfs(n, m, grid):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    for j in range(m):
        if grid[0][j] == 0:
            queue.append((0, j))
            visited[0][j] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if x == n - 1:
            return "YES"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return "NO"


def sol():
    input = sys.stdin.read
    data = input().split("\n")
    n, m = map(int, data[0].split())
    grid = [list(map(int, list(data[i + 1]))) for i in range(n)]
    print(bfs(n, m, grid))


sol()
