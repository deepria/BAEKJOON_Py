def main():
    from sys import stdin
    read = stdin.readline
    n = int(read())
    arr = list(map(int, read().split()))
    cnt = [0] * 64

    for x in arr:
        if x == 0:
            continue
        k = x.bit_length() - 1
        cnt[k] += 1

    for k in range(63):
        merge = cnt[k] // 2
        cnt[k] -= merge * 2
        cnt[k + 1] += merge

    ans_k = max(i for i, v in enumerate(cnt) if v > 0)
    print(1 << ans_k)


if __name__ == '__main__':
    main()



'''

20
512 32 64 0 32 32 32 64 64 0 32 0 0 0 512 0 0 256 256 256

'''
