import sys

input = sys.stdin.read
sys.setrecursionlimit(10 ** 6)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = 0, 0
grid = []
max_result = 0


def dfs(x, y, depth, total):
    global max_result

    if total + max_remain * (4 - depth) <= max_result:
        return

    if depth == 4:
        max_result = max(max_result, total)
        return

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + grid[nx][ny])
            visited[nx][ny] = False


def check_extra_shapes(x, y):
    global max_result
    shapes = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        [(1, 0), (1, 1), (1, 2), (0, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 1)]
    ]
    for shape in shapes:
        try:
            total = sum(grid[x + dx][y + dy] for dx, dy in shape)
            max_result = max(max_result, total)
        except IndexError:
            continue


def solve():
    global n, m, grid, max_remain, visited
    data = input().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(map(int, data[i + 1].split())) for i in range(n)]

    max_remain = max(max(row) for row in grid)
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, grid[i][j])
            visited[i][j] = False
            check_extra_shapes(i, j)

    print(max_result)


solve()
