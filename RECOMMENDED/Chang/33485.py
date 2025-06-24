import sys
import math
import itertools


def compute_domination_number(n, m):
    if n > m:
        n, m = m, n
    if n == 1:
        return math.ceil(m / 3)
    elif n == 2:
        return math.ceil((m + 1) / 2)
    elif n == 3:
        return math.ceil((3 * m + 1) / 4)
    elif n == 4:
        if m in [5, 6, 9]:
            return m + 1
        else:
            return m
    elif n == 5:
        if m == 7:
            return math.ceil((6 * m + 4) / 5) - 1
        else:
            return math.ceil((6 * m + 4) / 5)
    elif n == 6:
        return math.ceil((10 * m + 4) / 7)
    elif n == 7:
        return math.ceil((5 * m + 1) / 3)
    elif n == 8:
        return math.ceil((15 * m + 7) / 8)
    elif n == 9:
        return math.ceil((23 * m + 10) / 11)
    elif n == 10:
        if m % 13 == 10 or m in [13, 16]:
            return math.ceil((30 * m + 15) / 13) - 1
        else:
            return math.ceil((30 * m + 15) / 13)
    elif n == 11:
        if m in [11, 18, 20, 22, 33]:
            return math.ceil((38 * m + 22) / 15) - 1
        else:
            return math.ceil((38 * m + 22) / 15)
    elif n == 12:
        return math.ceil((80 * m + 38) / 29)
    elif n == 13:
        if m % 33 in [13, 16, 18, 19]:
            return math.ceil((98 * m + 54) / 33) - 1
        else:
            return math.ceil((98 * m + 54) / 33)
    elif n == 14:
        if m % 22 == 7:
            return math.ceil((35 * m + 20) / 11) - 1
        else:
            return math.ceil((35 * m + 20) / 11)
    elif n == 15:
        if m % 26 == 5:
            return math.ceil((44 * m + 28) / 13) - 1
        else:
            return math.ceil((44 * m + 28) / 13)
    elif n >= 16:
        return math.floor(((n + 2) * (m + 2)) / 5) - 4
    else:
        raise NotImplementedError("?")


def dominates(grid, n, m):
    covered = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        covered[ni][nj] = True
    return all(all(row) for row in covered)


def build_known_pattern(n, m):
    count = compute_domination_number(n, m)
    grid = [['.' for _ in range(m)] for _ in range(n)]
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_dominated(dom_grid):
        return all(all(cell for cell in row) for row in dom_grid)

    def apply_domination(dom_grid, i, j):
        new_grid = [row[:] for row in dom_grid]
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m:
                new_grid[ni][nj] = True
        return new_grid

    result = []

    def dfs(pos, placed, dom_grid):
        if placed > count:
            return False
        if placed == count and is_dominated(dom_grid):
            result.append([row[:] for row in grid])
            return True
        for idx in range(pos, n * m):
            i, j = divmod(idx, m)
            grid[i][j] = '#'
            new_dom = apply_domination(dom_grid, i, j)
            if dfs(idx + 1, placed + 1, new_dom):
                return True
            grid[i][j] = '.'
        return False

    initial_dom = [[False] * m for _ in range(n)]
    dfs(0, 0, initial_dom)
    return [''.join(row) for row in result[0]] if result else ['IMPOSSIBLE']


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        count = compute_domination_number(n, m)
        print(count)
        grid = build_known_pattern(n, m)
        for row in grid:
            print(row)


if __name__ == "__main__":
    main()
