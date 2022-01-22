# -*- coding:utf-8 -*-

"""
共分散.
"""
__author__ = "09x3086"

print("標本数 : ")
a: float = float(input())

print("平均平方和1 : ")
b: float = float(input())

print("平均平方和2 : ")
c: float = float(input())

# calculate
answer = (1 / a) * (b * c)

print(answer)
