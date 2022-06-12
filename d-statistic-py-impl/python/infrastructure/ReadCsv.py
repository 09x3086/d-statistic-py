import pandas

# -*- coding:utf-8 -*-
"""
正規分布.
"""
__author__ = "nyo"


# Averageクラスを定義
class ReadCsv:

    # 平均値計算
    @staticmethod
    def read(path):
        f = pandas.read_csv(path, encoding="shift-jis")
        return f
