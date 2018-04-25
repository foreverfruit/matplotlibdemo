"""
累计条形图，stacked bar graph
"""
import numpy as np
import matplotlib.pyplot as plt
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))
sepal_length, sepal_width, petal_length, petal_width = np.loadtxt(cur_dir + '/../dataset/iris.data',
                                                                  delimiter=',',
                                                                  unpack=True, dtype=float, usecols=(0, 1, 2, 3))

# data
sun_sepal_length = [np.sum(sepal_length[0:50]), np.sum(sepal_length[51:100]), np.sum(sepal_length[101:150])]
sun_sepal_width = [np.sum(sepal_width[0:50]), np.sum(sepal_width[51:100]), np.sum(sepal_width[101:150])]
sun_petal_length = [np.sum(petal_length[0:50]), np.sum(petal_length[51:100]), np.sum(petal_length[101:150])]
sun_petal_width = [np.sum(petal_width[0:50]), np.sum(petal_width[51:100]), np.sum(petal_width[101:150])]

# plot
pos = np.arange(3)
width = 0.5
# 这里有大量重复的矩阵计算，需要优化
bar1 = plt.bar(pos, sun_sepal_length, width, yerr=sun_sepal_length, align='center', color='red')
bar2 = plt.bar(pos, sun_sepal_width, width, yerr=sun_sepal_width, bottom=sun_sepal_length, align='center',
               color='green')
bar3 = plt.bar(pos, sun_petal_length, width, yerr=sun_petal_length, bottom=np.add(sun_sepal_length, sun_sepal_width),
               align='center', color='blue')
bar4 = plt.bar(pos, sun_petal_width, width, yerr=sun_petal_width,
               bottom=np.add(np.add(sun_sepal_length, sun_sepal_width), sun_petal_length), align='center',
               color='black')
# 坐标轴美化
plt.ylabel('value')
plt.title('this is title')
plt.xticks(pos, ('typeA', 'typeB', 'typeC'))
# 图例标注
plt.legend((bar1, bar2, bar3, bar4), ('sepal_length1', 'sepal_width2', 'petal_length3', 'petal_width4'))
plt.show()
