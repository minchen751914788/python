
#1、单行注释：以#开头
#2、多行注释：三个单引号括起来。 '''多行注释 '''
#3、python的乱码问题
'''
由于python源代码也是文本文件。所以，当你的源码中包含中文的时候，在保存源码时候，就需要无比指定保存为utf-8编码。
当python解释器读取源代码时候，为了让他按utf-8读取，我们通常需要在文件开头加上这两行
	# -*- coding:utf-8 -*-
	# coding=utf-8

'''
print("python的注释和解决乱码问题")