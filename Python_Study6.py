# -*- coding: UTF-8 -*-
# Python IO

# Python 输入
# raw_input():括号中为提示的内容,去掉结尾的换行符
str = input("say something: ")
# print str

# input():input会假设你的输入是一个有效的Python表达式，并返回运算结果。
str = input("Enter your input: ");
# print "Received input is : ", str

# file对象
"""
file object = open(file_name [, access_mode][, buffering])
    file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
    access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
"""
"""
模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""
fo = open("filetest.py", "a")

# file.close():关闭文件
########
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
# python3已经去除 print("Softspace flag : ", fo.softspace)  # 如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

# write():写入文件
fo.write("ooooooooo\nxxxxxxxx\n")

# read():读取文件中的某一行
fo = open("Python_Study7.py", "r")
str = fo.read(4)
print(str)

# tell():当前光标所在位置，seek():移动光标所在位置
fo.tell()
fo.seek(6)
str = fo.read(fo.tell())
print(str)

# os模块
# 重命名和删除文件
import os

os.renames("filetest.py", "newfiletest.py")
os.remove("newfiletest.py")
# mkdir:在当前目录创建文件夹
# os.mkdir("xxx")#如果已经存在会报错
# getcwd()方法显示当前的工作目录。
print(os.getcwd())
# chdir()方法 :改变当前目录,该目录必须存在
# os.chdir("/Users/a1234/PycharmProjects/python/test")

# rmdir()方法删除目录，目录名称以参数传递。

#############
# Python异常：
# try...except
"""
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:(可以不指明异常类型)
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
"""
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

try:
    x = 1 / 0
except:
    print()
finally:
    print("go on")

# python3:
try:
    y = 1 / 0
except ZeroDivisionError as e:
    print("catch")
finally:
    print("....")
