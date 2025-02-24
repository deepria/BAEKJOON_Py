s = input()
r = 1
for i in range(1, len(s) // 2 + 1):
    if s[i - 1] != s[-i]:
        r = 0
        break
print(r)
