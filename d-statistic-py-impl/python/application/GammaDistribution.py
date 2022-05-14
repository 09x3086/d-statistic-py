import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sps

shape, scale = 1., 1
s = np.random.gamma(shape, scale, 10000)

count, bins, ignored = plt.hist(s, 50, density=True)
y = bins ** (shape - 1) * (np.exp(-bins / scale) /
                           (sps.gamma(shape) * scale ** shape))
plt.plot(bins, y, linewidth=2, color='r')
plt.show()
