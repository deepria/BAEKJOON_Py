import sys


def backtrack(depth, n, m, nums, current, used, results):
    if depth == m:
        results.append(current[:])
        return

    last = -1
    for i in range(n):
        if not used[i] and nums[i] != last:
            used[i] = True
            current.append(nums[i])
            backtrack(depth + 1, n, m, nums, current, used, results)
            current.pop()
            used[i] = False
            last = nums[i]


def sol():
    read = sys.stdin.read().splitlines()
    n, m = map(int, read[0].split())
    nums = [i for i in range(1,n+1)]
    results = []
    backtrack(0, n, m, nums, [], [False] * n, results)
    for result in results:
        print(' '.join(map(str, result)))


sol()
