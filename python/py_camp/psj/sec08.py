# # 클래스 
# # 선언
# # class 클래스명 : 첫글자: 대문자, ex/Stu, StuInfo
# #       함수
# # class UserInfo:
# #     def __init__(self, name):
# #         self.name = name
# #         print('Name:', self.name)

# # user1 = UserInfo('Kim')
# # user2 = UserInfo('Park')

# # print(id(user1))
# # print(id(user2))

# # print('user1:', user1.__dict__)
# # print('user2:', user2.__dict__)

# class Student:
#     name = 'student'
#     age = 0
#     def __init__(self, name, age) -> None:
#         print('객체 초기화')
#         self.name = name
#         self.age = age

#     def __del__(self) -> None:
#         print('객체삭제')
#     def info(self):
#         print('My name is', self.name)
#         print('I am', self.age, 'years old')

# s =Student('Jane', 22)
# s.info()
# del s
# print(type(s))


# class Student1:
#     def __init__(self, name, age) -> None:
#         self.university = "SNU"
#         self.name = name
#         self.age = age
#         self.isStudying = True
#         self.studyHour = 0

#     def study(self):
#         if self.isStudying:
#             self.isStudying += 1
#     def hourofstudy(self):
#         print('{} 현재 공부시간: {}시간'.formmat(self.name, self.studyHour))

result = 0

def add(num):
    global result
    result += num
    return num

print(add(5))
print(add(7))

class Cal:
    def __init__(self) -> None:
        self.result = 0

    def add(self, num):
        self.result += num
        return num

cal1 = Cal()
cal2 = Cal()

print(cal1.add(3))
print(cal1.add(5))
print(cal2.add(7))
print(cal2.add(10))

class FourCal:
    # def setdata(self, first, second) -> None:
    #     self.first = first
    #     self.second = second

    def __init__(self, first, second) -> None:
         self.first = first
         self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.frist * self.second
        return result

a = FourCal()
b = FourCal()

print(a.add(2, 3))
print(a.mul(2, 3))

a.setdata(3,5)
print(a.add())
print(a.mul())


class MorefourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MorefourCal(5,5)
b = FourCal(4, 7)

print(a.add())
print(a.mul())
print(b.add())
print(b.mul())
print(a.pow())


