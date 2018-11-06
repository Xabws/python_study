# -*- coding: UTF-8 -*-
import operator
# 类型转换
print(float(1000000000))
# str:转换会去掉换行符
name = ('My name is Jmilk\n')
print(str(name))
print(repr(name))

# 数学符号：
print(abs(-200))

# Python格式化字符串
#  符   号	描述
#      %c	 格式化字符及其ASCII码
#      %s	 格式化字符串
#      %d	 格式化整数
#      %u	 格式化无符号整型
#      %o	 格式化无符号八进制数
#      %x	 格式化无符号十六进制数
#      %X	 格式化无符号十六进制数（大写）
#      %f	 格式化浮点数字，可指定小数点后的精度
#      %e	 用科学计数法格式化浮点数
#      %E	 作用同%e，用科学计数法格式化浮点数
#      %g	 根据值的大小决定使用%f活%e
#      %G	 作用同%g，根据值的大小决定使用%f活%e
#      %p	 用十六进制数格式化变量的地址

str = "String is: %s ,int is: %d ,float is: %f" % ("STRING", 12345, 44.44)
print(str)

# Python三引号（triple quotes）
# python中三引号可以将复杂的字符串进行复制:
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
# 三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。

longstr = """
qweqewqefqwrqwfqwereqrqwrtqdewqrqwerfeqwrqw
ewqrqwerwqerqwtwgrtnenrymkrutjyshtearw435467u6jtnhregwfdq
"""

# string.capitalize()

'''
string.capitalize()
把字符串的第一个字符大写

string.center(width)
返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

string.count(str, beg=0, end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

string.decode(encoding='UTF-8', errors='strict')
以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'

string.endswith(obj, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

string.expandtabs(tabsize=8)
把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.

string.find(str, beg=0, end=len(string))
检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1

string.index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在 string中会报一个异常.

string.isalnum()
如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

string.isalpha()
如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

string.isdecimal()
如果 string 只包含十进制数字则返回 True 否则返回 False.

string.isdigit()
如果 string 只包含数字则返回 True 否则返回 False.

string.islower()
如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

string.isnumeric()
如果 string 中只包含数字字符，则返回 True，否则返回 False

string.isspace()
如果 string 中只包含空格，则返回 True，否则返回 False.

string.istitle()
如果 string 是标题化的(见 title())则返回 True，否则返回 False

string.isupper()
如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

string.join(seq)
Merges (concatenates)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

string.ljust(width)
返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

string.lower()
转换 string 中所有大写字符为小写.

string.lstrip()
截掉 string 左边的空格

string.maketrans(intab, outtab])
maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)
返回字符串 str 中最大的字母。

min(str)
返回字符串 str 中最小的字母。

string.partition(str)
有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.

string.replace(str1, str2,  num=string.count(str1))
把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

string.rfind(str, beg=0,end=len(string) )
类似于 find()函数，不过是从右边开始查找.

string.rindex( str, beg=0,end=len(string))
类似于 index()，不过是从右边开始.

string.rjust(width)
返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

string.rpartition(str)
类似于 partition()函数,不过是从右边开始查找.

string.rstrip()
删除 string 字符串末尾的空格.

string.split(str="", num=string.count(str))
以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串

string.splitlines(num=string.count('\n'))
按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.

string.startswith(obj, beg=0,end=len(string))
检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

string.strip([obj])
在 string 上执行 lstrip()和 rstrip()

string.swapcase()
翻转 string 中的大小写

string.title()
返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

string.translate(str, del="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中

string.upper()
转换 string 中的小写字母为大写

string.zfill(width)
返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0,isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。 
'''
# Python列表：
"""
1	cmp(list1, list2)
比较两个列表的元素
2	len(list)
列表元素个数
3	max(list)
返回列表元素最大值
4	min(list)
返回列表元素最小值
5	list(seq)
将元组转换为列表

Python包含以下方法:
序号	方法
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort([func])
对原列表进行排序
"""
# Python 字典
"""
序号	函数及描述
1	cmp(dict1, dict2)
比较两个字典元素,如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
比较list时：
如果比较的元素是同类型的,则比较其值,返回结果。

如果两个元素不是同一种类型,则检查它们是否是数字。

    如果是数字,执行必要的数字强制类型转换,然后比较。
    如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
    否则,通过类型名字的字母顺序进行比较。

如果有一个列表首先到达末尾,则另一个长一点的列表"大"。

如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。
2	len(dict)
计算字典元素个数，即键的总数。
3	str(dict)
输出字典可打印的字符串表示。
4	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。

Python字典包含了以下内置函数：
序号	函数及描述
1	radiansdict.clear()
删除字典内所有元素
2	radiansdict.copy()
返回一个字典的浅复制
3	radiansdict.fromkeys(seq[, value]))
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	radiansdict.has_key(key)
如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
以列表返回一个字典所有的键
8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
10	radiansdict.values()
以列表返回字典中的所有值
"""

sdd = {"1111": "A", "2222": "B", "3333": "C"}
sddd = sdd.items();
print(sddd)
print(sdd.keys())

mlist = ("A", "B", "C", "D")
dic = {}
dic = dic.fromkeys(mlist, "letter")
print(dic.get("F", "NULL"))
print(dic.setdefault("E", "NULL"))
print(dic)

mlist2 = ("D", "E", "F", "G")
print(operator.concat(mlist, mlist2))
