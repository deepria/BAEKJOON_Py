from sys import stdin
from math import ceil
import heapq

read = stdin.read().splitlines()
n, h_centi, t = map(int, read[0].split())
heap = []
for i in range(1, n + 1):
    heapq.heappush(heap, -int(read[i]))
cnt = 0
isYes = False
while t != 0:
    for hp in heap:
        if hp > -h_centi:
            isYes = True
        else:
            isYes = False
            break
    if isYes:
        break
    h = heapq.heappop(heap)
    h_harf = ceil(h / 2)
    heapq.heappush(heap, h if h == -1 else h_harf)
    t -= 1
    cnt += 1
    for hp in heap:
        if hp > -h_centi:
            isYes = True
        else:
            isYes = False
            break
    if isYes:
        break


print('YES' if isYes else 'NO')
print(cnt if isYes else -heapq.heappop(heap))
