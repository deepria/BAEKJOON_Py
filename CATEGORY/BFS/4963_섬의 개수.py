import sys

directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
sys.setrecursionlimit(10 ** 6)


def dfs(grid, visited, x, y, w, h):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
            if grid[nx][ny] == 1:
                visited[nx][ny] = True
                dfs(grid, visited, nx, ny, w, h)


def solve():
    read = sys.stdin.read().strip().splitlines()
    w, h = map(int, read[0].split())
    line = 1
    while w != 0 and h != 0:
        grid = [list(map(int, read[line + i].split())) for i in range(h)]
        visited = [[False] * w for _ in range(h)]
        islands = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    dfs(grid, visited, x, y, w, h)
                    islands += 1
        sys.stdout.write(str(islands) + '\n')

        line += h
        w, h = map(int, read[line].split())
        line += 1


solve()
