def switch(d, cnt):
    cnt += 1
    d = 0 if d == 3 else d + 1
    return d, cnt


def main():
    n, m = map(int, input().split())
    visited = [[False] * m for _ in range(n)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y, d, cnt = 0, 0, 0, 0

    for i in range(n * m):
        visited[x][y] = True
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x += direction[d][0]
            y += direction[d][1]
            cnt += 1

    print(cnt - 1)


if __name__ == "__main__":
    main()
