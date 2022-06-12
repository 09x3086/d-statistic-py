import sympy

# -*- coding:utf-8 -*-
"""
対数尤度.
"""
__author__ = "nyo"


# Logarithmクラスを定義
class Logarithm:

    # コンストラクタ
    def __init__(self, data):
        # メンバ
        self.data: list[float] = data

    # 対数尤度
    def calculate(self):
        # 変数を定義（v=σ**2としておく）
        sympy.var('μ v y')
        # 尤度p(パラメータ|x)を定義
        fe = (1 / sympy.sqrt(2 * sympy.pi * v)) * sympy.exp(-(y - μ) ** 2 / (2 * v))
        # 対数化
        logf = sympy.log(fe)
        # fを偏微分して、式を展開
        pdff1 = sympy.expand(sympy.diff(logf, μ))  # μについて偏微分
        pdff2 = sympy.expand(sympy.diff(logf, v))  # vについて偏微分