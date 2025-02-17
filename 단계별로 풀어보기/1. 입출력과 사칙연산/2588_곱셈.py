a = int(input())
b = int(input())
print(f"{a * (b % 10)}\n{a * ((b // 10) % 10)}\n{a * (b//100)}\n{a * b}")
