import string


def sol():
    read = input().strip()
    uppercase_letters = list(string.ascii_uppercase)
    dic = {}

    i = 0
    while i < len(uppercase_letters):
        if i == 15 or i == 22:
            flag = 4
        else:
            flag = 3

        for ch in uppercase_letters[i:i + flag]:
            dic[ch] = ((i + 6) // 3) + 1
        i += flag

    result = 0
    for e in read:
        if e in dic:
            result += dic[e]

    print(result)


sol()
