"""
一元配置分散分析.
"""
__author__ = "09x3086"

import pandas as pandas

listA = ['AAA', 'BBB', 'CCC', 'DDD']
listB = ['EEE', 'FFF', 'GGG', 'HHH']
listC = ['III', 'JJJ', 'KKK', 'LLL']
listD = ['MMM', 'NNN', 'OOO', 'PPP']

lists = [listA, listB, listC, listD]
data = pandas.DataFrame(lists)

print(data)
