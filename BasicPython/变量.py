# -*- coding:utf-8 -*-
# @author=Hope
# @datetime=2022/2/11 18:42

"""
    变量
    定义：
        变量名 = 值
    变量名的命名规范：
        1. 变量名只能是 字母、数字或下划线的任意组合
        2. 变量名的第一个字符不能是数字
        3. 关键字不能声明为变量名
    变量值的三大特性:
        1. id(变量名) 可以查看变量名所指向变量值的内存地址
        2. type(变量名) 查看变量值的类型
        3. 变量值
    常量:在程序运行过程中不会变的量
        python没有专门语法定义常量，约定俗成使用全大写表示常量
"""

# 查看内置id()函数的作用
print(id.__doc__)
# 输出
"""
Return the identity of an object.

This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)
"""

# 查看内置的type()函数的作用
print(type.__doc__)  # 可以查看变量值的类型

# 定义变量
a = 15
b = 'python'
print("id(a):", id(a))
print("id(b):", id(b))

# 相同的数值在内存中占有同一块内存地址
a = 10
b = 10
print("数字10在内存中的地址:", id(10), id(10), id(a), id(b))

a = 'name'
b = 'name'
print("字符串'name'在内存中地址:", id("name"), id("name"), id(a), id(b))


# 相同的列表在内存中却占用不同的内存地址
a = [1, 2]
b = [1, 2]
print("列表[1,2]在内存中的地址:", id([1, 2]), id([1, 2]), id(a), id(b))
