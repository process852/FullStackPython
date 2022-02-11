# -*- coding:utf-8 -*-
# @author=Hope
# @datetime=2022/2/11 20:00
"""
    交互的本质：输入和输出
        输入：
            input()
        输出:
            print()
        格式化显示：占位符如%s,%d等
"""

# 输入函数input()
print(help(input))
username = input("请输入您的用户名:")
password = input("请输入您的密码:")

# 输出函数print()
print(username, password, sep='####')

# 格式化输出
age = 20
print("Mary's age is %d" % (age))
