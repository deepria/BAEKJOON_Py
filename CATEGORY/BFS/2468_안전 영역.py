import sys
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(copied_map, x, y, visited, n):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and copied_map[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))


def sol():
    read = sys.stdin.read().strip().split("\n")
    n = int(read[0])
    arr = [list(map(int, row.split())) for row in read[1:]]

    max_height = max(map(max, arr))
    max_safe_area = 1

    for height in range(max_height + 1):
        copied_map = [[arr[x][y] - height for y in range(n)] for x in range(n)]
        visited = [[False] * n for _ in range(n)]
        safe_area_count = 0

        for x in range(n):
            for y in range(n):
                if copied_map[x][y] > 0 and not visited[x][y]:
                    bfs(copied_map, x, y, visited, n)
                    safe_area_count += 1

        max_safe_area = max(max_safe_area, safe_area_count)

    print(max_safe_area)


sol()
