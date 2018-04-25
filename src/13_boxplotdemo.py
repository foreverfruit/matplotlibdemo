import numpy as np
import matplotlib.pyplot as plt
import os

path = os.path.dirname(os.path.realpath(__file__))
sepal_length, sepal_width, petal_length, petal_width = np.loadtxt(path + '/../dataset/iris.data',
                                                                  delimiter=',',
                                                                  unpack=True, dtype=float, usecols=(0, 1, 2, 3))

# 画三种花的sepal_length的箱形图
x = sepal_length[:50], sepal_length[51:100], sepal_length[101:150]
labels = 'A', 'B', 'C'

plt.boxplot(x, labels=labels, whis=1, sym='bx')
plt.show()
