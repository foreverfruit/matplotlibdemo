# histogram
import numpy as np
import matplotlib.pyplot as plt
import os

path = os.path.dirname(os.path.realpath(__file__))
sepal_length, sepal_width, petal_length, petal_width = np.loadtxt(path + '/../dataset/iris.data',
                                                                  delimiter=',',
                                                                  unpack=True, dtype=float, usecols=(0, 1, 2, 3))

# 直方图
plt.hist(sepal_length, bins=50, normed=False, color='green')
plt.show()
