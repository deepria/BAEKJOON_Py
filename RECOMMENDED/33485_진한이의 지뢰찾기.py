import sys


def solve_small(n0, m0):
    swap = False
    if n0 > m0:
        swap = True
        n, m = m0, n0
    else:
        n, m = n0, m0

    ALL = 1 << n
    cover_v = [0] * ALL
    for mask in range(ALL):
        cov = mask
        cov |= (mask << 1) & (ALL - 1)
        cov |= (mask >> 1)
        cover_v[mask] = cov

    INF = 10 ** 9
    dp = {(0, mask): mask.bit_count() for mask in range(ALL)}
    parent = [{} for _ in range(m)]
    for mask in range(ALL):
        parent[0][(0, mask)] = None

    for col in range(1, m):
        new_dp = {}
        for (prev, curr), val in dp.items():
            for nxt in range(ALL):
                if (cover_v[curr] | prev | nxt) != (ALL - 1):
                    continue
                cost = val + nxt.bit_count()
                key = (curr, nxt)
                if new_dp.get(key, INF) > cost:
                    new_dp[key] = cost
                    parent[col][key] = (prev, curr)
        dp = new_dp

    best = INF
    end_key = None
    for (prev, curr), val in dp.items():
        if (cover_v[curr] | prev) == (ALL - 1) and val < best:
            best = val
            end_key = (prev, curr)

    masks = [0] * m
    key = end_key
    for col in range(m - 1, 0, -1):
        masks[col] = key[1]
        key = parent[col][key]
    masks[0] = key[1]

    grid = [['.' for _ in range(m0)] for __ in range(n0)]
    for j in range(m):
        for i in range(n):
            if (masks[j] >> i) & 1:
                if not swap:
                    grid[i][j] = '#'
                else:
                    grid[j][i] = '#'
    return best, grid


def solve_large(n, m):
    grid = [['.' for _ in range(m)] for __ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if (2 * i + j) % 5 == 0:
                grid[i][j] = '#'
                cnt += 1
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '#':
                        break
                else:
                    grid[i][j] = '#'
                    cnt += 1
    return cnt, grid


def main():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []
    for _ in range(t):
        n, m = map(int, input().split())
        # if n <= 7 and m <= 7:
        #     cnt, grid = solve_small(n, m)
        # else:
        #     cnt, grid = solve_large(n, m)
        cnt, grid = solve_large(n, m)
        out.append(str(cnt))
        for row in grid:
            out.append(' '.join(row))
    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    main()

'''

. # . . . # . .
. . . # . . . #
# . . # . . . .
. . . . . # # .
. # # . . . . .
. . . . # . . #
# . . . # . . .
. . # . . . # .

1 # 1 1 1 # 1 1
1 1 1 # 1 1 1 #
# 1 1 # 1 1 1 1
1 1 1 1 1 # # 1
1 # # 1 1 1 1 1
1 1 1 1 # 1 1 #
# 1 1 1 # 1 1 1
1 1 # 1 1 1 # 1

'''
