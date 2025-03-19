import sys
import heapq


def solve():
    read = sys.stdin.read
    data = list(map(int, read().split()))
    n, l = data[0], data[1]
    icicles = data[2:n + 2]
    pq = []
    time_map = [0] * n
    for i in range(n):
        if (i == 0 and icicles[i] > icicles[i + 1]) or (i == n - 1 and icicles[i] > icicles[i - 1]) or (
                0 < i < n - 1 and icicles[i] > icicles[i - 1] and icicles[i] > icicles[i + 1]):
            disappear_time = l - icicles[i]
            heapq.heappush(pq, (disappear_time, i))
            time_map[i] = disappear_time

    time = 0
    while pq:
        time, i = heapq.heappop(pq)
        if icicles[i] == 0:
            continue
        icicles[i] = 0
        for ni in [i - 1, i + 1]:
            if 0 <= ni < n and icicles[ni] > 0:
                if (ni == 0 and icicles[ni] > icicles[ni + 1]) or (ni == n - 1 and icicles[ni] > icicles[ni - 1]) or (
                        0 < ni < n - 1 and icicles[ni] > icicles[ni - 1] and icicles[ni] > icicles[ni + 1]):
                    new_time = time + (l - icicles[ni])
                    if time_map[ni] == 0 or new_time < time_map[ni]:
                        heapq.heappush(pq, (new_time, ni))
                        time_map[ni] = new_time
    print(time)


solve()
