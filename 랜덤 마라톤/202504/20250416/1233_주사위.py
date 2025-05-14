a, b, c = map(int, input().split())
arr = [0 for _ in range(a + b + c + 1)]
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            arr[i + j + k] += 1
print(arr.index(max(arr)))
