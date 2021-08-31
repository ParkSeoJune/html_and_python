# # 리스트, 튜플
# # 리스트(순서o, 중복o, 수정o, 삭제o)
# # 선언
# a =[]
# b = list()
# c = [1,2,3,4]
# d = [1, 100, 'Pen', 'Cap', 'Plate']
# e = [1, 100, ['Pen', 'Cap', 'Plate']]

# print(d[3])
# print(d[-1])
# print(d[0]+d[1])
# print(d[3]+d[4])
# print(e[2][1])
# print(e[-1][-3])

# print('===='*20)
# print(d[0:3])
# print(d[:3])
# print(d[2:])
# print(e[2][0:2])

# print(c+d)
# print(c*3)
# print('ball'+d[2])
# print('hi'+str(c[2]))
# c[0]=5
# print(c)
# c[1:2]=['a','b','c']
# print(c)
# c[1]=['a','b','c']
# print(c)
# c[1:3]=[]
# print(c)
# del c[3]
# print(c)
# c = [1,2,3]

# c[2]=1
# print(c)
# c[0:1]=[2,5,4,8]
# print(c)

# c.append(6)
# print(c)

# c.sort()
# print(c)
# c.reverse()
# print(c)
# c.insert(2, 9)
# print(c)

# c.remove(1)
# print(c)
# c.pop()
# print(c)

# print(c.count(6))
# ex =[10,11]
# c.append(ex)
# print(c)
# c.extend(ex)
# print(c)

# 튜플(수정, 삭제x)
a =()
b =(1,)
c = (1,2,3,4)
d = (10, 100, 'banana', 'pineapple', 'apple')
e = (10,100, ('banana', 'pineapple', 'apple'))

# 인덱싱
print(d[1])
print(d[0]+d[1])

# 슬라이싱
print(d[:3])
print(type(d))
print(e[2][:2])
# 연산
print('hi' +e[2][1])
print('hi'+str(e[1]))
print(c+d)
print(c*3)
