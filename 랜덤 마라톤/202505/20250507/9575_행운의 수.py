def main():
    from sys import stdin
    read = lambda: stdin.readline().strip()
    t = int(read())
    for _ in range(t):
        _ = read()
        arr = [*map(int, read().split())]
        _ = read()
        brr = [*map(int, read().split())]
        _ = read()
        crr = [*map(int, read().split())]
        cnt = 0
        lucky = []
        for ar in arr:
            for br in brr:
                for cr in crr:
                    temp = str(ar + br + cr)
                    flag = True
                    for tmp in temp:
                        if tmp != '8' and tmp != '5':
                            flag = False
                            break
                    if not flag:
                        continue
                    elif temp not in lucky:
                        cnt += 1
                        lucky.append(temp)
        print(cnt)


if __name__ == "__main__":
    main()
