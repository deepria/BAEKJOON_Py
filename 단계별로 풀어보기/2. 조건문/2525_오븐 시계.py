a, b = map(int, input().split())
c = int(input())
e = (b + c) // 60
b = (b + c) % 60
a = a + e if a + e < 24 else a + e - 24
print(f"{a} {b}")
