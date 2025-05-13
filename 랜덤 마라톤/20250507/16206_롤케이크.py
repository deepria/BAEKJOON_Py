def main():
    import sys
    read = lambda: sys.stdin.readline().split()
    n, m = map(int, read())
    role = [*map(int, read())]
    ten = []
    not_ten = []
    for r in role:
        if r % 10 == 0:
            ten.append(r)
        else:
            not_ten.append(r)
    cnt = 0
    ten.sort()
    for r in ten:
        if r == 10:
            cnt += 1
        else:
            if m >= r // 10:
                use = r // 10 - 1
                m -= use
                cnt += r // 10
            else:
                use = m
                cnt += m
                if r - 10 * m == 10:
                    cnt += 1
                m -= use
    for r in not_ten:
        use = min(r // 10, m)
        cnt += use
        m -= use
    print(cnt)


if __name__ == "__main__":
    main()

'''
예제 입력 1 
3 1
10 10 10

예제 출력 1 
3

예제 입력 2 
3 1
10 10 20

예제 출력 2 
4

예제 입력 3 
3 3
20 20 20

예제 출력 3 
6

예제 입력 4 
5 7
10 20 30 40 50

예제 출력 4 
11

예제 입력 5 
5 8
34 45 56 12 23

예제 출력 5 
8
'''
