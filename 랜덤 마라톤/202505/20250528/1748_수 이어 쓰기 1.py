def main():
    n = input()
    rb = [(1, 9)]
    for i in range(2, 10):
        rb.append((i, (rb[i - 2][1] + i * int('9' + '0' * (i - 1)))))

    nl = len(n)
    base = '1' + '0' * (nl - 1)
    mod = int(n) - int(base) + 1
    if nl == 1:
        print(n)
    else:
        print(str(rb[nl - 2][1] + mod * rb[nl - 1][0]))


if __name__ == "__main__":
    main()
'''

1~9         9       *   1    
10~99       89      *   2
100~999     899     *   3
1000~9999   8999    *   4

100,000,000
187 60 247
120 252

123456789 10 11 12 13 14 15
'''
