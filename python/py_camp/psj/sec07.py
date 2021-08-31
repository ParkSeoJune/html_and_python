# 함수
def function_n(wolrd):
    val = "Hello" + str(wolrd)
    return val

str = function_n('pup')
print(str)

# 다중리턴

def func_mult(x):
    y1 = x * 10
    y2 = x*100
    y3= x*1000
    return y1, y2, y3

val1, val2, val3 = func_mult(5)
print(type(val1), val1, val2, val3)

def func_mult(x):
    y1 = x * 10
    y2 = x*100
    y3= x*1000
    return [y1, y2, y3]

lt = func_mult(5)
print(type(lt), lt)

def func_mult(x):
    y1 = x * 10
    y2 = x*100
    y3= x*1000
    return (y1, y2, y3)

tu = func_mult(5)
print(type(tu), tu)

def func_mult(x):
    y1 = x * 10
    y2 = x*100
    y3= x*1000
    return {'r1':y1, 'r2':y2, 'r3': y3}

di = func_mult(5)
print(type(di), di.items)

def args(*args):
    for i, v in enumerate(args):
        print(i, v)


args('Park', 'Lee')

def kwargs(**kwarg):
    print(kwarg)

kwargs(name1 = 'Kim')


# 혼합
def example(arg1, arg2, *args, **kk):
    print(arg1, arg2, args, kk)

example(10, 20, 'park', 'kim', 'lee', age1 = 33, age2 = 23)

# 중첩함수
def nested_func(num:int) -> int:
    def func_in_func(num):
        print('>>>',num)
        print("in func")
        func_in_func(num+100)

nested_func(20)


# 1. 입력한 숫자 n번만큼 *를 출력하는 함수를 작성하시오
# 함수명 starprint(n)
def starprint(n):
    print('*' * n)
s = int(input('숫자입력:'))
starprint(s)
# 2. 두수를 입력받아 합, 차, 곱을 저장하여 리스트로 출력하시오.
# 함수명 operator(a,b)
def operator(a, b):
    return [a+b, a-b, a*b]

s = operator(2,3)
print(s)    
# 3. 문장을 입력받아서 각 알파벳을 대문자로 바꾸어 출력하는 함수작성.
# 함수명: wordlist(string)
def wordlist(string):
    print(string.upper())

wordlist("hihi")
# 4. 두 자연수를 입력받아 최대공약수를 리턴하는 함수, 최소공배수를 리턴하는 함수를 완성하시오.
# 함수명: 최대공약수 gcd(n,m), 최소공배수 lcm(n,m)
n=int(input('n입력:'))
m=int(input('m입력:'))
for i in range(1,max(n,m)):
    if(n%i==0)&(m%i==0):
        gcd=i
print('gcd:',gcd)

for i in range(max(n,m),(n*m)+1):
    if i%n==0 and i%m==0:
       lcm=i 
       break
print('lcm:',lcm)
# 5 아래의 조건을 만족하면서, 100000보다 작은 자연수 중
# 3의 배수 또는 5의 배수를 모두 더한 합을 출력하는 프로그램을 작성하시오.
# 조건: 3의배수를 판정하는 함수-ismulThree(n), 
#       5의 배수를 판정하는 함수 - ismulfive(n),
#       전체코드는 15줄 내에서 완성하기
def ismulThree(n):
    if n % 3 == 0:
        return n
def ismulfive(n):
    if n % 5 == 0:
        return n
sum = 0
for i in range(1,100000):
    if ismulThree(i) or ismulfive(i):
        sum += i
print(sum)