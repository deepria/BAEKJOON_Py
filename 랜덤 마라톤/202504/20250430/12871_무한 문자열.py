def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def main():
    s = input()
    t = input()
    ls, lt = len(s), len(t)
    l = lcm(ls, lt)
    fs = s * (l // ls)
    ft = t * (l // lt)
    print(1 if fs == ft else 0)


if __name__ == "__main__":
    main()

'''
문제
문자열 s가 있을 때, f(s)는 s를 무한번 붙인 문자열로 정의한다. 
예를 들어, s = "abc" 인 경우에 f(s) = "abcabcabcabc..."가 된다.

다른 문자열 s와 t가 있을 때, f(s)와 f(t)가 같은 문자열인 경우가 있다. 
예를 들어서, s = "abc", t = "abcabc"인 경우에 f(s)와 f(t)는 같은 문자열을 만든다.

s와 t가 주어졌을 때, f(s)와 f(t)가 같은 문자열을 만드는지 아닌지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 s, 둘째 줄에 t가 주어진다. 
두 문자열 s와 t의 길이는 50보다 작거나 같은 자연수이고, 알파벳 소문자로만 이루어져 있다. 

출력
첫째 줄에 f(s)와 f(t)가 같으면 1을, 다르면 0을 출력한다.

예제 입력 1 
ab
abab

예제 출력 1 
1

예제 입력 2 
abc
bca

예제 출력 2 
0
'''
