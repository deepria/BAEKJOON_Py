import sys


def main() -> None:
    read = sys.stdin.readlines()
    n = int(read[0])
    cross = list(map(int, read[1].split()))
    left_line = list(map(int, read[2].split()))
    right_line = list(map(int, read[3].split()))
    left = [0] * n
    for i in range(1, n):
        left[i] = left[i - 1] + left_line[i - 1]
    right = [0] * n
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] + right_line[i]
    distance = [left[i] + cross[i] + right[i] for i in range(n)]
    mn = min(distance)
    print(distance.index(mn) + 1, mn)


if __name__ == "__main__":
    sys.exit(main())

'''


숭실 대학교 정보 과학관은 숭실 대학교 건물 중 제일 높은 곳에 있다.
민주는 평소에 버스를 타고 이 언덕을 오르지만,
이 문제에 등장하기 위하여 오늘 하루만 걸어서 올라간다.

정보 과학관을 오르는 길은 왼쪽 길과 오른쪽 길이 있다.
민주는 처음에 왼쪽 길 맨 아래에 있고 정보 과학관을 오른쪽 길 맨 위에 있다.
정보 과학관을 오르는 길은 매우 구불구불하다.
또, 길의 중간 중간에는 횡단보도가 있다.
민주는 횡단보도를 한번만 건널 수 있다.
최소한으로 걷기 위해서 민주가 건너야 하는 횡단 보도의 번호와 걸어야 할 거리를 구해 더운 여름 민주를 도와주자!

입력
첫 번째 줄에는 지점의 개수 n 이 주어진다.
(2 ≤ n ≤ 100,000)

횡단보도는 1번 지점부터 n 번 지점까지 한 개 씩 있고,
왼쪽 1번 지점에는 민주가,
오른쪽 n 번 지점에는 정보 과학관이 위치한다.
다음 줄에는 i 번째 지점에 있는 횡단보도의 거리 (0 < cross ≤ 100,000) 가 주어진다.
(1 ≤ i ≤ n)
다음 줄에는 i 번째 지점에서 i+1번째 지점까지 왼쪽 길의 거리 (0 < left ≤ 100,000) 가 주어진다.
(1 ≤ i ≤ n-1)
다음 줄에는 i 번째 지점에서 i+1번째 지점까지 오른쪽 길의 거리(0 < right ≤ 100,000) 가 주어진다.
(1 ≤ i ≤ n-1)
출력
민주가 최소 길로 가기 위해 건널 횡단보도는 몇 번째 지점에 있는지 출력하고,
민주가 최소 길로 가기 위해 걸어야 하는 거리를 출력한다.
만약,
최소 거리로 갈 수 있는 지점이 여러곳이라면 번호가 낮은 지점을 출력한다.
예제 입력 1 
4
2 3 1 4
1 2 3
2 5 6
예제 출력 1 
3 10

'''
