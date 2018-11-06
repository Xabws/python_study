# -*- coding: UTF-8 -*-
# python的默认编码文件是用的ASCII码,此处申明用U8编码

import time

print("Hello Python!")


def file_append(file, data):
    file.write(data)
    file.write('\r\n')


# 在python里，标识符有字母、数字、下划线组成。
# 在python中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
# python中的标识符是区分大小写的。
# 以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
# 以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。

file = open('fw1.txt', 'a')
# file = open('fw1.txt')
# file.seek(5)
# file.write('hello, hello\r\n')
file_append(file, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
file_append(file, 'hello, hello')
file_append(file, 'hello, hello')
file.close()

if True:
    print("True")
else:
    print("false")

# Python语句中一般以新行作为为语句的结束符。

# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示,语句中包含[], {} 或 () 括号就不需要使用多行连接符

print("HELLO" \
      "WORLD")

week = ["monday", "tuesday", "wednesday",
        "thursday", "friday"]
print(week)
# Python 引号

# Python 接收单引号(' )，双引号(" )，三引号(''' """) 来表示字符串，引号的开始与结束必须的相同类型的。

# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。

word = 'one'
word2 = "two"
word3 = """three"""
print(word + word2 + word3)

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys;

x = 'foo';
sys.stdout.write(x + '\n')

# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。
if 5 / 2 == 3:
    print
    "3"
elif 5 / 2 == 2:
    print
    '2'
else:
    print
    '1'

# 多个变量赋值：
a, b, c = 1, 1.2, "hello"
print
a
print
b
print
c


def xxx(a, b):
    return a + b
