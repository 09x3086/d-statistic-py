import matplotlib.pyplot as plt
import numpy
import requests
import pprint
from scipy.stats import norm

headers = {'Authorization': 'Bearer {}'.format('6f0cc851-a033-4fd4-ac0a-1638ff78c2a1')}
X = list()
for i in range(1):
    r_get = requests.get('https://simplefx.com/utils/instruments.json', headers=headers)

    # print(r_get.status_code)
    # 200

    # pprint.pprint(r_get.json())
    pprint.pprint(r_get.json()['80'])
    # pprint.pprint(r_get.json()['80']['quote'])

    X.append(float(r_get.json()['80']['quote']['b'] - (i * 0.01)))

print(X)

ave = numpy.average(X)
stddd = numpy.std(X)

start = ave - stddd * 5
end = ave + stddd * 5

# X軸
wide = numpy.arange(start, end, 0.001)

Y = norm.pdf(wide, ave, stddd)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(color='gray')
ax.plot(wide, Y, color='r')
plt.show()
