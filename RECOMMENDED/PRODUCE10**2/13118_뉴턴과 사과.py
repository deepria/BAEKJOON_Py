pa = input().split()
x, _, _ = input().split()
flag = False
for i in range(4):
    if x == pa[i]:
        print(i + 1)
        flag = True
if not flag:
    print(0)
