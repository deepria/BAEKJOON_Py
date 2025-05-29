def main():
    from sys import stdin, stdout
    read = lambda: stdin.readline().strip()
    n, m = map(int, read().split())
    arr = [*map(int, read().split())]
    for t in range(m):
        a, b = map(int, read().split())
        if a == b:
            stdout.write('0\n')
            continue
        s = 0
        for i in range(a, b):
            s += abs(arr[i] - arr[i - 1])
        stdout.write(str(s) + '\n')


if __name__ == "__main__":
    main()

'''
    
4 3
100 101 382 573
1 1
1 3
2 4

0
282
472
    
첫 번째 구간 [1, 1]의 구간 변화량의 합은 0이다.

두 번째 구간 [1, 3]의 구간 변화량 합은 |101-100| + |382-101| = 1 + 281 = 282이다.

세 번째 구간 [2, 4]의 구간 변화량 합은 |382-101| + |573-382| = 281 + 191 = 472이다.


5 3
1 0 1 0 -11
1 5
3 5
2 4

14
12
2


첫 번째 구간 [1, 5]의 구간 변화량의 합은 |0-1| + |1-0| + |0-1| + |(-11)-0| = 1 + 1 + 1 + 11 = 14이다.

두 번째 구간 [3, 5]의 구간 변화량의 합은 |0-1| + |(-11)-0| = 1 + 11 = 12이다.

세 번째 구간 [2, 4]의 구간 변화량의 합은 |1-0| + |0-1| = 1 + 1 = 2이다.
'''
