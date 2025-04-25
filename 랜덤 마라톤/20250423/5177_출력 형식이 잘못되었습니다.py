def sol(s):
    s = s.upper()
    while True:
        temp = s.replace('  ', ' ')
        if temp == s:
            break
        s = temp

    s = s.replace('{', '(')
    s = s.replace('}', ')')
    s = s.replace('[', '(')
    s = s.replace(']', ')')
    s = s.replace(',', ';')
    s = s.replace(' (', '(')
    s = s.replace('( ', '(')
    s = s.replace(' )', ')')
    s = s.replace(') ', ')')
    s = s.replace('. ', '.')
    s = s.replace(' .', '.')
    s = s.replace(': ', ':')
    s = s.replace(' :', ':')
    s = s.replace('; ', ';')
    s = s.replace(' ;', ';')

    return s


def main():
    from sys import stdin, stdout
    read = lambda: stdin.readline().strip()
    k = int(read())
    for i in range(1, k + 1):
        s1 = sol(read())
        s2 = sol(read())
        result = 'not equal' if s1 != s2 else 'equal'
        stdout.write(f'Data Set {i}: {result}\n\n')


if __name__ == "__main__":
    main()

'''

프로그램에 입력되는 문자열은 다음의 문자들로만 이루어져 있다.

대문자 혹은 소문자 영문 알파벳
숫자
공백 (탭이 아닌 스페이스바)
특수 부호
특수 부호의 목록은 아래와 같다.

( ) [ ] { } . , ; :

출력 형식만 다른 문자열인지는 아래의 규칙에 따라 판정한다.


    알파벳 대문자와 소문자는 구별하지 않는다. done
    
    공백이 하나 이상이라면, 공백의 크기는 관계없다. 물론 어떤 문자열엔 공백이 있고 어떤 문자열엔 공백이 없는 것, 
    즉 공백 유무의 차이 자체는 문제가 된다. done
    
    문자열의 맨 앞 혹은 맨 뒤에 나타나는 공백은 있으나 없으나 관계없다. done
    
    특수 부호의 바로 앞이나 바로 뒤에 나오는 공백도 있으나 없으나 상관없다. done
    
    여는 괄호끼리는 종류를 구별하지 않는다. done
    
    닫는 괄호끼리는 종류를 구별하지 않는다. done
    
    쉼표(",")와 세미콜론(";")은 구별하지 않는다. done


입력
첫 줄에 테스트 케이스의 수 K가 주어진다.

이어 두 줄에 걸쳐 문자열 s1과 문자열 s2가 주어진다.

각 문자열의 길이는 1000 이하이다.

개행 문자는 문자열에 포함되지 않는다.

출력
각 테스트 케이스마다, Data Set K: 를 출력한 뒤

만일 두 문자열이 출력 형식을 감안했을 때 동일한 문자열이라면 equal을, 출력 형식을 잘 조작해도 서로 다른 문자열이라면 not equal을 출력한다.

각 테스트 케이스의 사이엔 빈 줄을 하나 출력한다.

예제 입력 1
3
( 1, 4 ) (2,3) (2,4)
{ 1; 4 )   {2;3)  {2;4)
Data Set 1: equal
data   set 1 :  EQUAL
Data Set 1: equal
DataSet 1: equal

예제 출력 1
Data Set 1: equal

Data Set 2: equal

Data Set 3: not equal
'''
