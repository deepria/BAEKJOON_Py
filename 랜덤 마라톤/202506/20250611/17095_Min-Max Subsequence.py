def main():
    n = int(input())
    a = list(map(int, input().split()))

    global_max = max(a)
    global_min = min(a)
    last_max = last_min = -1
    ans = n

    for i, v in enumerate(a):
        if v == global_max:
            last_max = i
            if last_min != -1:
                ans = min(ans, i - last_min + 1)
        if v == global_min:
            last_min = i
            if last_max != -1:
                ans = min(ans, i - last_max + 1)

    print(ans)


if __name__ == "__main__":
    main()

'''
수열의 부분수열을 그 수열의 연속한 일부 항을 원래 순서대로 나열해 얻을 수 있는 수열이라고 하자.
(원래 부분수열의 정의는 이것이 아니다) 
길이 N의 수열 A가 주어지면,
수열 A의 부분수열 중 (부분수열 내 최댓값)-(부분수열 내 최솟값)이 최대가 되는 부분수열 중 가장 짧은 수열의 길이를 구하여라.

입력
첫 줄에 N이 주어진다.
(1 ≤ N ≤ 10^5)

다음 줄에 N개의 수가 공백으로 구분되어 주어지며,
i번째 수는 Ai를 뜻한다.
(1 ≤ Ai ≤ 10^5)

출력
문제의 답인 하나의 정수를 출력한다.

예제 입력 1 
5
1 1 1 1 1

예제 출력 1 
1

예제 입력 2 
5
1 1 2 3 3

예제 출력 2 
3

'''
