# -*- coding:utf-8 -*-
# @author=Hope
# @datetime=2022/2/11 19:11
"""
    python基本的数据结构:
        1. 数字类型
            (1) int
            (2) float
        2. 字符串string
            字符串是不可变对象(immutable)
            支持单引号、双引号和多引号
            字符串只支持加号和乘号
            支持切片索引
        3. 列表 list
            用于包含一系列复合数据类型
        4. 字典 dict
            一种包含键值对(keys:values)的集合
            字典用一个花括号表示，内部元素用逗号分隔，键和值之间使用冒号分隔
            每一个字典中的键都是独一无二的,不可以重复,且键必须是不可变对象，如字符串、数字等


"""

# int 型变量
a = 10
b = 3

print(a / b)

# 字符串
s1 = "learn"
s2 = "python"

# 字符串相加表示两个字符串进行拼接
print(s1 + s2)
# 字符串乘以一个数字n，表示重复显示该字符串n次
print(s2 * 3)

# 列表
list1 = [1, 2, 3, 44]
print(list1)
print(list1[1])
print("列表切片1:3", list1[1:3])

# 字典
dict1 = {'age': 18, 'score': 99, 'name6': 'jin', 1: 500}

print(dict1)
