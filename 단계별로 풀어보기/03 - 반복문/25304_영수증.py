x = int(input())
n = int(input())
result = 0
for i in range(0, n, +1):
    a, b = map(int, input().split())
    result += a * b
print('Yes' if x == result else 'No')
