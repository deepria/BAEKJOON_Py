import sys
from collections import deque


def bfs(graph, start, end, n):
    queue = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        node, depth = queue.popleft()

        if node == end:
            return depth

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))

    return -1


n = int(sys.stdin.readline().strip())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(graph, start, end, n))
