# s = input()
# if len(s) == 1:
#     print(s.upper())
# else:
#     arr = [0] * 100
#     for c in s:
#         arr[ord(c.upper())] += 1
#     sort = sorted(arr, reverse=True)
#     print('?' if sort[0] == sort[1] else chr(arr.index(max(arr))))


A = str(input())

a = A.upper()
cnt = []

alpha = [chr(i) for i in range(ord('A'),ord('Z')+1)]


for j in alpha:
    cnt.append(a.count(j))

if cnt.count(max(cnt)) >= 2:
    print("?")
else :
    result = cnt.index(max(cnt))
    print(chr(result+65))