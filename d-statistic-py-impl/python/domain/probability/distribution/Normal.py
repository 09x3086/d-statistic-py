from infrastructure.ReadCsv import ReadCsv
from scipy.stats import norm
import numpy
import matplotlib.pyplot as plt
import statistics

# -*- coding:utf-8 -*-
"""
正規分布.
"""
__author__ = "nyo"

df = ReadCsv.read("../../../../resource/20220613.csv")

lowPrice = df.LowPrice
highPrice = df.HighPrice

lowPriceNegative2Sigma = numpy.average(lowPrice) - 2 * numpy.std(lowPrice)
lowPriceNegativeSigma = numpy.average(lowPrice) - numpy.std(lowPrice)
lowPricePositiveSigma = numpy.average(lowPrice) + numpy.std(lowPrice)

highPriceNegative2Sigma = numpy.average(highPrice) - 2 * numpy.std(highPrice)
highPriceNegativeSigma = numpy.average(highPrice) - numpy.std(highPrice)
highPricePositiveSigma = numpy.average(highPrice) + numpy.std(highPrice)

print(df.LowPrice)
print(numpy.average(lowPrice))
print(numpy.std(lowPrice))
print("--------------------------------------------------")
print("LowPrice")
print("-2σ : " + str(lowPriceNegative2Sigma))
print("-σ : " + str(lowPriceNegativeSigma))
print("+σ : " + str(lowPricePositiveSigma))
print("+2σ : " + str(numpy.average(lowPrice) + 2 * numpy.std(lowPrice)))
print("+median : " + str(statistics.median(lowPrice)))
print("--------------------------------------------------")
print("HighPrice")
print("-2σ : " + str(highPriceNegative2Sigma))
print("-σ : " + str(highPriceNegativeSigma))
print("+σ : " + str(highPricePositiveSigma))
print("+2σ : " + str(numpy.average(highPrice) + 2 * numpy.std(highPrice)))
print("+median : " + str(statistics.median(highPrice)))
print("--------------------------------------------------")
print("Buy : " + str((lowPriceNegativeSigma + highPriceNegativeSigma) / 2))
print("Cell : " + str((lowPricePositiveSigma + highPricePositiveSigma) / 2))

X = numpy.arange(lowPrice.min() - 1, highPrice.max() + 1, 0.01)
yLowPrice = norm.pdf(X, numpy.average(lowPrice), numpy.std(lowPrice))
yHighPrice = norm.pdf(X, numpy.average(highPrice), numpy.std(highPrice))

plt.plot(X, yLowPrice, color='b')
plt.plot(X, yHighPrice, color='r')
plt.axvline(x=numpy.average(lowPrice), color='b')
plt.axvline(x=numpy.average(numpy.average(lowPrice) - numpy.std(lowPrice)), color='b')
plt.axvline(x=numpy.average(numpy.average(lowPrice) + numpy.std(lowPrice)), color='b')
plt.grid()
# plt.show()
