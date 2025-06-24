import pprint


def sol(n0, m0):
    n, m, swapped = (n0, m0, False) if n0 <= m0 else (m0, n0, True)
    a = 1 << n
    full = a - 1

    cover_v = [0] * a
    for mask in range(a):
        c = mask
        c |= (mask << 1) & full
        c |= mask >> 1
        cover_v[mask] = c

    inf = 10 ** 9
    dp_prev = {(0, mask): mask.bit_count() for mask in range(a)}
    parent = [dict() for _ in range(m)]
    for mask in range(a):
        parent[0][(0, mask)] = None

    for col in range(1, m):
        dp_curr = {}
        par = {}
        for (prev, curr), val in dp_prev.items():
            cover_pc = cover_v[curr] | prev
            for nxt in range(a):
                if (cover_pc | nxt) != full:
                    continue
                cost = val + nxt.bit_count()
                key = (curr, nxt)
                if key not in dp_curr or cost < dp_curr[key]:
                    dp_curr[key] = cost
                    par[key] = (prev, curr)
        dp_prev = dp_curr
        parent[col] = par

    best = inf
    end = None
    for (prev, curr), val in dp_prev.items():
        if val < best and (cover_v[curr] | prev) == full:
            best = val
            end = (prev, curr)

    masks = [0] * m
    state = end
    for col in range(m - 1, 0, -1):
        masks[col] = state[1]
        state = parent[col][state]
    masks[0] = state[1]

    grid = [['.' for _ in range(m0)] for __ in range(n0)]
    for j in range(m):
        for i in range(n):
            if (masks[j] >> i) & 1:
                if not swapped:
                    grid[i][j] = '#'
                else:
                    grid[j][i] = '#'
    return best, [''.join(row) for row in grid]


def before_run():
    lut = {}
    for N in range(1, 13):
        lut[N] = {}
        for M in range(1, 13):
            cnt, g = sol(N, M)
            lut[N][M] = (cnt, g)
    pprint.pprint(lut, width=200)
