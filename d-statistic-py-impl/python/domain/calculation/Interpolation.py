# -*- coding:utf-8 -*-

"""
補間(Interpolation).
"""
__author__ = "09x3086"

# print("自由度A : ")
# a: float = float(input())
#
# print("自由度B : ")
# b: float = float(input())
#
# print("自由度C : ")
# c: float = float(input())
#
# print("確率A : ")
# a2: float = float(input())
#
# print("確率C : ")
# c2: float = float(input())

# calculate
# answer = a2 - ((a2 - c2) * (((1 / a) - (1 / c)) / ((1 / a) - (1 / b))))

answer = 1.98 - ((1.98 - 1.97) * (((1 / 120) - (1 / 149)) / ((1 / 120) - (1 / 240))))


print(answer)
