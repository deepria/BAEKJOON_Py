import sys


def comb(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result


def main():
    read = sys.stdin.readline
    n, m, r = map(int, read().split())
    s = r - n * m
    if s < 0:
        print(0)
        return
    print(comb(s + n - 1, n - 1))


if __name__ == "__main__":
    sys.exit(main())

'''
컴퓨터 공학에 흥미를 잃은 상근이는 로드샵을 열었다.
로드샵의 주력상품은 구슬 목걸이다.
상근이네 집에는 구슬이 무한히 많다.
색상은 총 n가지이고,
이들을 각각 m개 이상씩 뽑아서 r개의 구슬로 된 목걸이를 만들려고 한다.
상근이는 여성들의 유니크함을 이해하는 남자이다.
따라서, 색 조합이 다른 목걸이를 하나씩 다 만들려고 한다.
상근이가 만들 수 있는 목걸이의 종류는 몇 가지 일까?

입력
첫째 줄에 n, m, r이 주어진다.

출력
첫째 줄에 만들 수 있는 목걸이가 총 몇 종류나 있는지 출력한다.
제한
0 ≤ m＜n ≤ r ≤ 10000

예제 입력 1 
2 0 3

예제 출력 1 
4

예제 입력 2 
3 1 4

예제 출력 2 
3

예제 입력 3 
4 2 5

예제 출력 3 
0

'''
