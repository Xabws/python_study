# -*- coding: UTF-8 -*-

"""
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


def mprint(string):
    print string


mprint("hello Python");


def person(name, age):
    print "name:", name
    print "age:", age


person(18, "lily")
person(age=18, name="ff")  # 与传入顺序无关


def person2(name, age=16):  # age不传时设置为缺省
    print "name:", name
    print "age:", age


person2(name="qqq")


# 加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。如下实例：
# !/usr/bin/python

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数
msum = lambda arg1, arg2: arg1 + arg2
print "sum:", msum(10, 15)


# return 只需在函数中使用return即可
def multiply(x, y):
    return x * y


print  multiply(4, 6)

# Python模块
# 模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码。相当于类
# import :倒入其他模块，一个模块只会被导入一次
import Python_Study1

print Python_Study1.xxx(56, 65)
# 只引用部分：
from Python_Study1 import xxx

print xxx(4, 2)

# Python会先查找局部变量后查找全局变量，要想使用全局变量，在使用时加上global
Money = 2000
def AddMoney():
    global Money

Money = Money + 1

print Money
AddMoney()
print Money

#dir(模块名)将一个模块的所有模块，变量和函数名放在一个list中
print dir(Python_Study1)

#globals()和locals()函数
"""
根据调用地方的不同，globals()和locals()函数可被用来返回全局和局部命名空间里的名字。
如果在函数内部调用locals()，返回的是所有能在该函数里访问的命名。
如果在函数内部调用globals()，返回的是所有在该函数里能访问的全局名字。
两个函数的返回类型都是字典。所以名字们能用keys()函数摘取。
"""

#reload:reload()函数
#当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
#因此，如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。语法如下：
reload(Python_Study1)




