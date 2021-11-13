import numpy

# -*- coding:utf-8 -*-
"""
不偏分散.
"""
__author__ = "09x3086"

N = [int(i) for i in input().split()]

print(N)
print(numpy.var(N, ddof=1))

# 495 502 510 512 505
# 51 75 80 65 73 58
