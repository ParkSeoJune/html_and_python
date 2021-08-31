print("hello world!")
print('Hello Python!')
print("""Hello""")
print('''Wow''')
print()

#sep사용
print('T','E','S','T', sep='')
print('2021', '07', '26', sep='-')
print('asdf', 'naver.com', sep='@')
print()

#end 사용
print('Welcome to ', end='')
print('Python World', end=' ')
print('!!')
print()

#format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{a} and {b}'.format(a='You', b='I'))
print()

#escape사용 \
print("'you'")
print('"I"')
print('\'me\'')
print('\n\t none')
print()

# %d: 정수, %s: 문자, %f: 실수
print("%s's favorite number is %d" %('PSJ', 3))
print("Test1: %5d, price: %4.2f" %(789, 1234.5678))
print("Test2: {0:5d}, price: {1:4.2f}".format(789, 1234.5678))
print("Test3: {a:5d}, price: {b:4.2f}".format(a=789, b=1234.5678))