import sys
from collections import deque, defaultdict


def bfs(n, k, x, graph):
    queue = deque([(x, 0)])
    visited = [-1] * (n + 1)
    visited[x] = 0
    result = []

    while queue:
        node, dist = queue.popleft()

        if dist == k:
            result.append(node)

        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))

    return sorted(result) if result else [-1]


def sol():
    input = sys.stdin.read
    data = input().split("\n")

    n, m, k, x = map(int, data[0].split())

    graph = defaultdict(list)
    for i in range(1, m + 1):
        a, b = map(int, data[i].split())
        graph[a].append(b)

    result = bfs(n, k, x, graph)

    sys.stdout.write("\n".join(map(str, result)) + "\n")


sol()
