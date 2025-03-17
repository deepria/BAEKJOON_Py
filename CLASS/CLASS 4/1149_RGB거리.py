import sys

def sol():
    read = sys.stdin.read().splitlines()
    n = int(read[0])
    cost = [list(map(int, line.split())) for line in read[1:]]

    r, g, b = cost[0]

    for i in range(1, n):
        new_r = min(g, b) + cost[i][0]
        new_g = min(r, b) + cost[i][1]
        new_b = min(r, g) + cost[i][2]
        r, g, b = new_r, new_g, new_b

    print(min(r, g, b))

sol()