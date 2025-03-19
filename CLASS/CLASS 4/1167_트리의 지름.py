import sys
from collections import deque


def bfs(start, n, tree):
    queue = deque([(start, 0)])
    visited = [-1] * (n + 1)
    visited[start] = 0
    max_dist = 0
    farthest_node = start
    while queue:
        node, dist = queue.popleft()
        for neighbor, weight in tree[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = dist + weight
                queue.append((neighbor, visited[neighbor]))

                if visited[neighbor] > max_dist:
                    max_dist = visited[neighbor]
                    farthest_node = neighbor
    return farthest_node, max_dist


def sol():
    read = sys.stdin.readline
    n = int(read())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n):
        data = list(map(int, read().split()))
        node = data[0]
        index = 1
        while data[index] != -1:
            neighbor, weight = data[index], data[index + 1]
            tree[node].append((neighbor, weight))
            tree[neighbor].append((node, weight))
            index += 2
    node_a, _ = bfs(1, n, tree)
    _, diameter = bfs(node_a, n, tree)
    print(diameter)


sol()
