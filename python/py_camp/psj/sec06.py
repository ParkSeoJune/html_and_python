print(type(True))
if True:
    print('Yes')

if False:
    print('No')

if False:
    print("You can't reach here")
else:
    print('You are here')

# 관계연산자
# <, >, <=, >=, ==, !=
a= 10
b=0
print(a ==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

# 참: "내용", [내용], (내용), {내용}
# 거짓: "",[],(),{}

city="GJ"
if city:
    print("You are in: ", city)
else:
    print("Plz enter your city")

# 논리연산자
a=100
b=60
c=15

print('and:', a>b and b>c)
print('or:', a>b or b>c)
print('not:', not a>b)
print('not:', not b>c)
print(not True)
print(not False)

print('ex1:', 3 + 12 > 7+3)
print('ex2:', 5+10*3 > 7 + 3*20)
print('ex3:', 5+10 and 7 + 3==10)
print('ex4:', 5+10> 0 and not 7 + 3 == 10)


score1 = 90
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print("합격")
else:
    print("불합격")

id1='gold'
id2='admin'
grade='super'


if id1 == 'gold' or id2 == 'admin':
    print('관리자 로그인 성공')
if id2 == 'admin' and grade == 'super':
    print('최고 관리자 로그인 성공')


is_work = False

if not is_work:
    print("is work!")


num = 90

if num >= 90:
    print('A')
elif num>= 80:
    print('B')
else:
    print('C')

age = 27
height = 175
if age >= 20:
    if height >= 170:
        print('a지망 지원가능')
    elif height >= 160:
        print('B지망 지원가능')
    else:
        print('지원불가')
elif age < 20:
    print('20세 이상 지원 가능')


# in, not in

q = [1,2,3]
w = {7,8,9,10}
e = {'name':'Kim', 'city':'Gwangju', 'grade':'B'}
r = (10, 12, 14)

print(1 in q)
print(6 in w)
print( 12 not in r)
print("name" in e)
print('')


