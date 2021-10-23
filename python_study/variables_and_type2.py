#-*-coding:utf-8-*-
#coding=tuf-8

'''
1、变量的定义
在程序中，用于存储某值的结构。例如，我们去曹氏买东西，我们需要菜篮子，用来存储物品。菜篮子就是变量，里面物品就是值。
2、变量的三要素：变量的名称，变量的类型，变量的值
3、变量的类型
为了更加充分的利用内存空间以及更有效的管理内存，变量是有不同的类型。
python的对象分类
对象Obejct：
1、Fundamental对象:Type类型
2、Numeric对象:
    1)布尔型：True、False两种值,可以用and、or、not运算
    2)浮点型:小数，可以直接是小数或者科学计数法（很大或很小的浮点数），浮点型可能存在四舍五入的误差。
    3)整形:1，100，-8080，0,计算机由于使用二进制，有时候用十六进制表示,用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。
3、Sequence对象
    1)String:
    a、以单引号或双引号括起来。若字符串里面含有引号，需要用\来进行转义。注意转义的层数,java,python,hive可能涉及到多层
    b、r"字符串内容"表示里面字符串不转义
    c、允许使用''''''将内容括起来，表示多行内容。'第一行\n第二行\n第三行\n'
    2)List
    3)tuple
4、Mapping对象：dict类型
5、Internal对象
    1)function
    2)code
    3)frame
    4)module
    5)method
注意点:
空值:空值是python里面一个特殊的值，用None表示。空值不能理解为0，因为0是有意义的，而空值是一个特殊的空值。
python中若定义了变量，并且有数据，那么我们无需主动去说明他的类型，系统自动辨别。可以用type（变量名），来查看变量的类型
'''

print('第一行1\n第二行2\n第三行3')

print('''
第一行
第二行
第三行
''')
a = 1
b = 2.2
c = True
d = 'I love python'
type(a)
type(b)
type(c)
type(d)
print(type(a))
print(b)
print(c)
print(d)

#常用的数据类型转换
'''
函数                          说明
int(x[,base])               将x转换为一个整数
long(x,[,base])             将x转换为一个长整数
float(x)                    将x转换到一个浮点数
complex(real[,imag])        创建一个复数
str(x)                      将x转换成字符串
repr(x)                     将对象x转换成表达式字符串
eval(str)                   用来计算字符串中的有效python表达式并返回一个对象
tuple(s)                    将序列s转换成一个元组
list(s)                     将序列转换成一个列表
chr(x)                      将一个整数转换成一个子凡
unichr(x)                   将一个字符转换成一个unicode字符
ord(x)                      将字符转换成他的整数值
hex(x)                      将一个整数转换为一个十六进制的字符串
oct(x)                      将一个整数转换为一个八进制字符串

'''
