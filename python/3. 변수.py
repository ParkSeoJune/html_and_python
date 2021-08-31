#변수 만들기
# 변수이름 = 값 또는 문자열
# 영문 문자와 숫자 사용 가능
# 대소문자 구분
# 문자부터 시작해야함 숫자부터 시작하면 안됨
# _(밑줄문자)로 시작할 수 있음
# 특수문자(+,-,*,/,$ 등)는 사용할 수 없음
# 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없음

#변수의 자료형 알아내기
# type(변수)
# y='Hello'일 때 type(y)의 결과는 <class 'str'>

#변수 여려 개를 한 번에 만들기
x, y, z = 10, 20, 30
# 서로 값이 같다면 
x = y = z = 10

#변수 삭제
# del이용
del x

#빈 변수 만들기
x = None

#변수로 계산하기
a=10
b=20
c=a+b
print(c) # 30출력

#산술 연산 후 할당 연산자 사용하기
a=10
a+=20 # a와 20을 더한 후 결과를 다시 a에 저장
print(a) # 30 출력

#부호 붙이기
x=-10
print(+x) # -10 출력
print(-x) # 10 출력

#입력 값을 변수에 저장하기
# input()함수를 사용
# 변수 = input()
x=input()
x=input('문자열을 입력하세요: ') # 입력받는 값의 용도를 미리 알려줄 수 있음

#두 숫자의 합 구하기
a = input('첫 번째 숫자를 입력하세요: ') # 10입력
b = input('두 번째 숫자를 입력하세요: ') # 20입력
print(a+b) # 값은 1020으로 나온다
# 1020으로 나오는 이유 input에서 입력받은 값은 항상 문자열 형태이기 때문 type(a)를 해보면 str로 나온다
# 그러므로 정수로 쓸 때에는 변환을 해줘야함

#입력 값을 정수로 변환하기
# 변수=int(input()), 변수=int(input('문자열'))
a = int(input('첫 번째 숫자를 입력하세요: ')) # 10입력
b = int(input('두 번째 숫자를 입력하세요: ')) # 20입력
print(a+b) #이렇게 해줘야 30으로 나온다
# 정수형 말고 실수형으로 쓰고 싶을 때는 int자리에 float을 쓰면 된다

#입력 값을 변수 두 개에 저장하기
# 변수1, 변수2 = input().split()
# 변수1, 변수2 = input().split('기준문자열')
# 변수1, 변수2 = input('문자열').split()
# 변수1, 변수2 = input('문자열').split('기준문자열')
# .split()이 입력받은 값을 공백을 기준으로 분리

a,b = input('문자열 두 개를 입력하세요: ').split()
# Hello Python을 입력
print(a)
print(b)

#입력 값을 정수로 변환하기
a, b =input('숫자 두 개를 입력하세요: ').split() # 입력받은 값을 공백을 기준으로 분리
a = int(a) # 변수를 정수로 변환한 뒤 다시 저장
b = int(b) # 변수를 정수로 변환한 뒤 다시 저장

print(a+b) # 실행 결과 : 숫자 두 개를 입력하세요: 10 20 (입력)
           # 30
print(int(a)+int(b)) # 이렇게 줄여 쓸 수도 있다.

#map을 사용하여 정수로 변환하기
# 변수1, 변수2 = map(int, input().split())
# 변수1, 변수2 = map(int, input().split('기준문자열'))
# 변수1, 변수2 = map(int, input('문자열').split())
# 변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
# 정수 말고 실수를 쓰고 싶을 때에는 int대신 float을 쓰면 된다.
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())

print(a+b)
# 실행 결과
# 숫자 두 개를 입력하세요: 10 20 (입력)
# 30

#입력받은 값을 콤마를 기준으로 분리하기
a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) #입력받은 값을 콤마(,)를 기준으로 분리

print(a+b)
# 실행 결과
# 숫자 두 개를 입력하세요: 10,20 (입력)
# 30

#map을 사용하여 정수로 변환하기
# 변수1, 변수2 = map(int, input().split())
# 변수1, 변수2 = map(int, input().split('기준문자열'))
# 변수1, 변수2 = map(int, input('문자열').split())
# 변수1, 변수2 = map(int, input('문자열').split('기준문자열'))

a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a+b)
숫자 두 개를 입력하세요: 10 20
30

#입력받은 값을 콤마를 기준으로 분리하기
a, b = map(int, input('숫자 두 개를 입력하세요: ').split(','))
print(a+b)
숫자 두 개를 입력하세요: 10,20
30

#값을 여러 개 출력하기
# print(값1, 값2, 값3)
# print(변수1, 변수2, 변수3)
print(1,2,3)
1 2 3
print('Hello','Python')
Hello Python

#sep로 값 사이에 문자 넣기
# print('값1, 값2, sep='문자 또는 문자열')
# print(변수1, 변수2, sep='문자 또는 문자열')
print(1,2,3, sep=', ')  # sep에 콤마와 공백을 지정
1, 2, 3
print(4,5,6, sep=',')   # sep에 콤마만 지정
4,5,6
print('Hello', 'Python', sep='')  # sep에 빈 문자열을 지정
HelloPython
print(1920, 1080, sep='x')  # sep에 x를 지정
1920x1080

#줄바꿈 활용하기
print(1, 2, 3)
1 2 3 
print(1, 2, 3, sep='\n')
1
2
3
print('1\n2\n3')
1
2
3

#end 사용하기
# print는 기본적으로 출력하는 값 끝에 \n을 붙입니다.
print(1)
print(2)
print(3)
1
2
3

print(1, end='') # end에 빈 문자열을 지정하면 다음번 출력이 바로 뒤에 오게 됨
print(2, end='')
print(3)
123

print(1, end=' ')
print(2, end=' ')
print(3)
1 2 3

