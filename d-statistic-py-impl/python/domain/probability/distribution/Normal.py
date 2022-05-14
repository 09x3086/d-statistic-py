import numpy

# -*- coding:utf-8 -*-
"""
正規分布.
"""
__author__ = "09x3086"


# NormalDistributionクラスを定義
class Normal:

    # コンストラクタ
    def __init__(self, data):
        # メンバ
        self.data: list[float] = data

    # 平均値計算
    def calculate(self):
        print(numpy.average(self.data))
        return numpy.average(self.data)
