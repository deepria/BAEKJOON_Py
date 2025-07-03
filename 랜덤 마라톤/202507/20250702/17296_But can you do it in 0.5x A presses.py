import sys


def main():
    read = sys.stdin.readlines()
    n = int(read[0])
    arr = [*map(float, read[1].split())]
    v = []

    for i in range(n):
        t = arr[i]
        int_part = int(t)
        half_flag = 1 if t - int_part > 0.1 else 0
        v.append((int_part, half_flag))

    ans = v[0][0]
    if v[0][1] == 1:
        ans += 1

    for i in range(1, n):
        if v[i][1] == 1 and ans == 0:
            ans += 1
        ans += v[i][0]

    print(ans)


if __name__ == "__main__":
    sys.exit(main())

'''


'''
