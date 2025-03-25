import sys


def backtrack(depth, n, m, nums, current, last, results):
    if depth == m:
        results.append(current[:])
        return

    for i in range(n):
        if nums[i] != last and last <= nums[i]:
            current.append(nums[i])
            backtrack(depth + 1, n, m, nums, current, last, results)
            current.pop()
            last = nums[i]


def sol():
    read = sys.stdin.read().splitlines()
    n, m = map(int, read[0].split())
    nums = sorted(list(map(int, read[1].split())))
    results = []
    backtrack(0, n, m, nums, [], 0, results)
    for result in results:
        print(' '.join(map(str, result)))


sol()
