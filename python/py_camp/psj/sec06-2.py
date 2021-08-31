# # 반복문
# # for, while
# v1 =1
# while v1<11:
#     print('v1:', v1)
#     v1 +=1
    
# for i in range(1,10):
#     print('i is:', i)
    
# for i in range(1,11):
#     print('i is:', i)

# for i in range(1,11,2):
#     print('i is:', i)

# sum=0
# for p in range(1, 101):
#     sum += p
# print(sum)

# a = int(input('enter 1st number:'))
# print(a)
# b = int(input('enter 2st number:'))
# print('두수의 합:', a+b)

a = int(input('숫자를 입력:'))
b = 0

for i in range(2, a):
    if a%i==0:
        b=1
if b==1 or a==1 or a==0:
    print("소수x")
else:
    print("소수")

names =['Kim', 'Park', 'cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print("U are ", name)

lotto_numbers = [11, 25, 43,28, 36, 37]

for number in lotto_numbers:
    print("your number", number)

word ='Dreams'
for s in word:
    print('word:', s)


my_info= {'name':'Kim', 'age':30, 'city':'Gwangju'}

for key in my_info:
    print(key, ':', my_info[key])

for val in my_info.values():
    print(val)

name = "Li"

for n in name:
    if n.isupper():
        print(n, end='')
    else:
        print(n.upper(), end='')


numbers = [14, 3, 4, 5, 18, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print('찾았다', num)
        break
    else:
        print("못찾았다",num)

lt = ["1", 2, 5, True, 4.3, complex(4)]

for floa in lt:
    if type(floa) is float:
        print('type:', type(floa))

f = True
numbers = [14, 3, 4, 5, 18, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:
            print("found",v)
        f = False