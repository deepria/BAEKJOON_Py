import sys
from collections import defaultdict, deque


def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if parent[neighbor] == 0:
                parent[neighbor] = node
                queue.append(neighbor)


n = int(sys.stdin.readline().strip())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
bfs(1)

for i in range(2, n + 1):
    print(parent[i])
