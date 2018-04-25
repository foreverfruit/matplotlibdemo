import numpy as np
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))
sepal_length, sepal_width, petal_length, petal_width = np.loadtxt(cur_dir + '/../dataset/iris.data',
                                                                  delimiter=',',
                                                                  unpack=True, dtype=float, usecols=(0, 1, 2, 3))

# 三种花的统计值，简单的统计
print(sepal_length[:50].mean())
print(sepal_length[:50].var())

print(sepal_length[51:100].mean())
print(sepal_length[51:100].var())

print(sepal_length[101:150].mean())
print(sepal_length[101:150].var())
