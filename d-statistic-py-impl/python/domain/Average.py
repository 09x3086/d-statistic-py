import numpy

# -*- coding:utf-8 -*-
"""
平均値.
"""
__author__ = "09x3086"


# Averageクラスを定義
class Average:

    # コンストラクタを定義
    def __init__(self, name, year):
        # メンバ
        self.name = name
        self.year = year


N = [int(i) for i in input().split()]

print(N)
print(numpy.average(N))
