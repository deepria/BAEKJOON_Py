import sys
from collections import deque

directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


def bfs(l, start_x, start_y, target_x, target_y):
    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * l for _ in range(l)]
    visited[start_x][start_y] = True

    while queue:
        x, y, moves = queue.popleft()

        if x == target_x and y == target_y:
            return moves

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))


def sol():
    read = sys.stdin.read().strip().splitlines()
    t = int(read[0])
    index = 1

    for _ in range(t):
        l = int(read[index])
        start_x, start_y = map(int, read[index + 1].split())
        target_x, target_y = map(int, read[index + 2].split())
        index += 3

        if (start_x, start_y) == (target_x, target_y):
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(bfs(l, start_x, start_y, target_x, target_y)) + '\n')


sol()
