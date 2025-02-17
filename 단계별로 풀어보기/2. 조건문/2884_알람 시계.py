a, b = map(int, input().split())
c = b - 45 >= 0
b = b - 45 if c else (b - 45) + 60
if not c and a == 0:
    a = 23
elif not c and a != 0:
    a = a - 1
print(f"{a} {b}")
