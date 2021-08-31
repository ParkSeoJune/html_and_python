#else 사용하기
# else는 if 조건문 뒤에 오며 단독으로 사용할 수 없다.
# if와 마찬가지로 else도 :(콜론)을 붙이며 다음 줄에 실행할 코드가 온다.

# if 조건식:
#     코드1
# else:
#     코드2

x = 5
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')

# 실행결과: 참 거짓 거짓
# 알 수 있는 것: None은 False로 취급

#if 조건문에 숫자 지정하기
# 숫자는 정수(2진수, 10진수, 16진수), 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참이다.

#if 조건문에 문자열 지정하기
# 문자열은 내용이 있을 때 참, 빈 문자열은 거짓입니다.
if 'Hello':
    print('참')
else:
    print('거짓')

if '':
    print('참')
else:
    print('거짓')

#조건식을 여러 개 지정하기
x = 10
y = 20
if x == 10 and y == 20:
    print('참')
else:
    print('거짓')

#중첩 if 조건문과 논리 연산자
if x>0:
    if x<20:
        print('20보다 작은 양수입니다.')

if x>0 and x<20: # 논리 연산자 사용
    print('20보다 작은 양수입니다.')

if 0<x<20: # 부등호 연달아 사용
    print('20보다 작은 양수입니다.')


