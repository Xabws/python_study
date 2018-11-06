# -*- coding: UTF-8 -*-
# Python 数据结构

# Python有五个标准的数据类型：

#  Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）

# NUmber
#    int（有符号整型）

#   long（长整型[也可以代表八进制和十六进制]）

#  float（浮点型）

#    complex（复数）:复数由实数部分和虚数部分构成
number1 = 1
number2 = 2
number3 = 3.0
number4 = 3e+26J

# String

message = "1234567"

print (message[2]) # 截取字符串，留头不留尾
print (message[2:])
print (message * 2)
print (message + "0000")
print ("23" in message)

# List:列表用[ ]标识。是python最通用的复合数据类型。:有序
List = [000, "111", 1.05, 45343, 3e+26J]
print (List)
List[4] = "asdqw"
print (List)

# Tuple:只读列表
myTuple = (000, "111", 1.05, 3434334)
print (myTuple)

# Dictionary:字典是无序的对象集合。字典当中的元素是通过键来存取的，而不是通过偏移存取。'
myDict = {"SIX": 6, "FIVE": 5, "FOUR": 4}  # 前面为键，后面为值

print (myDict)
print (myDict.keys())  # 所有的键
print (myDict.values())  # all value

dict = {}
dict["one"] = "This is one"
dict[2] = "This is two"
print (dict["one"])  # 输出键为"one" 的值
print (dict[2])  # 输出键为 2 的值

# 运算符
print (1 ** 3)  # **取幂：1的3次幂
print (1 // 3 ) # //	取整除 :返回商的整数部分

# 逻辑运算符
# and	布尔"与" - 如果x为False，x and y返回False，否则它返回y的计算值。	(a and b) 返回 true。----->&&a
# or	布尔"或" - 如果x是True，它返回True，否则它返回y的计算值。	(a or b) 返回 true。       ------->||a
# not	布尔"非" - 如果x为True，返回False。如果x为False，它返回True。	not(a and b) 返回 false。---->!a

x = True
y = False
print( x and y)
print (x or y)
print( not y)
print ("--------")

# 成员运算符
# 运算符	描述	实例
# in	如果在指定的序列中找到值返回True，否则返回False。	x 在 y序列中 , 如果x在y序列中返回True。
# not in	如果在指定的序列中没有找到值返回True，否则返回False。	x 不在 y序列中 , 如果x不在y序列中返回True。
a = 10
b = 20
list = [1, 2, 3, 4, 5];
print (a in list)
print (a not in list)

# 条件语句
# Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
if 1 == 2:
    print ("1==2")
elif 1 < 2:
    print ("1<2")
else:
    print ("1>2")
# 循环语句
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1
print ("Good bye!")
#在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
# while … else 也是一样。
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

#for循环
for letter in "Python":
    print (letter)

count =[1,2,3,4,5]

for number in count:
    print (number)

numlist = [11,12,13,14,15,16]
for number in range(len(numlist)):#range:范围，len：list的size
    print (numlist[number])
else:#在循环自然结束后执行
    print ("end")
print ("-----------------")
List1 = ['zi', 'qiang', 'xue', 'tang']
List2 = [1, 2]

new_list = []

for m in List1:
    for n in List2:
        new_list.append([m, n])

print (new_list)
print ("-----------------")
n = 20
for i in range(1, n):
    for j in range(2, int(i ** 0.5)):
        if i % j == 0:
            break
    else:
        print (i, '是素数')

