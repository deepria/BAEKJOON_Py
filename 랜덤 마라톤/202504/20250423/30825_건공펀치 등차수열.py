def sol():
    from sys import stdin
    input = stdin.read
    data = list(map(int, input().split()))
    n, k = data[0], data[1]
    a = data[2:]

    min_punch = float('inf')

    print(*a, sep='  ')
    print()

    for i in range(n):
        start = a[i] - i * k
        punch = 0
        possible = True
        for j in range(n):
            target = start + j * k
            if a[j] > target:  # ❗ 줄여야 하는 상황 = 불가능
                possible = False
                break
            punch += target - a[j]
        if possible:
            min_punch = min(min_punch, punch)
            print(f"✅ valid start {start}: punch = {punch}")
        else:
            print(f"❌ invalid start {start}: a[{j}] = {a[j]} > target = {target}")

    print(min_punch)


def main():
    from sys import stdin
    read = [*map(int, stdin.read().split())]
    n, k, a = read[0], read[1], read[2:]
    min_punch = float('inf')
    for i in range(n):
        start = a[i] - i * k
        punch = 0
        possible = True
        for j in range(n):
            target = start + j * k
            if a[j] > target:
                possible = False
                break
            punch += target - a[j]
        if possible:
            min_punch = min(min_punch, punch)
    print(min_punch)


if __name__ == "__main__":
    main()

'''
문제
서울시립대학교의 마스코트와도 같은 존재인 건공이는 어떤 수열을 주더라도 공차가 
K인 등차수열로 만들어 버리는 버릇이 있다.

건공이는 주어진 수열을 등차수열로 만들기 위해, 
건공펀치를 1회 사용하여 수열의 한 원소의 값을 1 증가시킬 수 있다.

건공이는 건공펀치를 최소로 사용하고 싶어하지만, 
수열의 길이가 너무 길어 건공펀치의 최소 사용 횟수를 구하는 데 어려움을 겪고 있다.

건공이를 대신하여 주어진 수열을 등차수열로 만드는 데 필요한 건공펀치의 최소 사용 횟수를 구해보자.

입력
첫 번째 줄에 수열의 길이 
N과 공차 
K가 공백으로 구분되어 주어진다. 
(2 <= N <= 200 000 , 1 <= K <= 200 000)

두 번째 줄에 수열 
A_1, A_2, ..., A_N이 공백으로 구분되어 주어진다. 
(1 <= A_i <= 100 000)

출력
주어진 수열을 공차가 
K인 등차수열로 만드는 데 필요한 건공펀치의 최소 사용 횟수를 출력한다.

예제 입력 1 
4 5
3 5 6 1

예제 출력 1
27


6 1
5 10 5 20 5 30
Answer: 90
Output: -6
// 25 26 27 28 29 30이 건공펀치를 최소한 사용하여 만들 수 있는 수열입니다


4 5
49 36 100 5
Answer: 200
Output: 36
// 90 95 100 105가 건공펀치를 최소한 사용하여 만들 수 있는 수열입니다


'''
