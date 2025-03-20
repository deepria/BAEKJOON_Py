import sys


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def solve():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    watcher_info = list(map(int, data[1].split()))
    watcher_count = watcher_info[0]
    watcher_set = set(watcher_info[1:]) if watcher_count > 0 else set()

    uf = UnionFind(n)
    parties = []
    for i in range(m):
        party_members = list(map(int, data[i + 2].split()[1:]))
        first_person = party_members[0]
        for person in party_members[1:]:
            uf.union(first_person, person)
        parties.append(party_members)
    watcher_leaders = {uf.find(person) for person in watcher_set}

    lie_possible_count = 0
    for party in parties:
        if uf.find(party[0]) not in watcher_leaders:
            lie_possible_count += 1
    print(lie_possible_count)


solve()
