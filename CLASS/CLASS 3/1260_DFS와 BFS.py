import sys
from collections import deque, defaultdict


def dfs(graph, start, visited):
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(str(node))
            stack.extend(reversed(graph[node]))

    return " ".join(result)


def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    result = []

    while queue:
        node = queue.popleft()
        result.append(str(node))

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return " ".join(result)


input = sys.stdin.read
data = input().split("\n")
n, m, start = map(int, data[0].split())

graph = defaultdict(list)
for i in range(1, m + 1):
    a, b = map(int, data[i].split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

visited = set()
dfs_result = dfs(graph, start, visited)

bfs_result = bfs(graph, start)

print(dfs_result)
print(bfs_result)
