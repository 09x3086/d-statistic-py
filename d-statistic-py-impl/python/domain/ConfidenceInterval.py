# -*- coding:utf-8 -*-
import math

"""
信頼区間.
"""
__author__ = "09x3086"

print("平均 : ")
a: float = float(input())

print("確率 : ")
b: float = float(input())

print("分散 : ")
c: float = float(input())

print("母集団数 : ")
d: float = float(input())

# calculate
answer = b * math.sqrt(c / d)

print(a)
print(answer)
