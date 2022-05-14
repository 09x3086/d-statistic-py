import numpy

# -*- coding:utf-8 -*-
"""
平均値.
"""
__author__ = "09x3086"


# Averageクラスを定義
class Average:

    # コンストラクタ
    def __init__(self, data):
        # メンバ
        self.data: list[float] = data

    # 平均値計算
    def calculate(self):
        print(numpy.average(self.data))
        return numpy.average(self.data)
