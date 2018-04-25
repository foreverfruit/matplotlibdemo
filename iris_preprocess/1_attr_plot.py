import numpy as np
import matplotlib.pyplot as plt
import os

path = os.path.dirname(os.path.realpath(__file__))
sl, sw, pl, pw = np.loadtxt(path + '/../dataset/iris.data',
                            delimiter=',',
                            unpack=True, dtype=float, usecols=(0, 1, 2, 3))
datarray = np.array([sl, sw, pl, pw])
attr_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
class_names = ['setosa', 'versicolor', 'virginica']

bins = 150
x1 = np.linspace(sl.min(), sl.max(), bins)
x2 = np.linspace(sw.min(), sw.max(), bins)
x3 = np.linspace(pl.min(), pl.max(), bins)
x4 = np.linspace(pw.min(), pw.max(), bins)
x = (x1, x2, x3, x4)
colors = ('r', 'g', 'b', 'y')

# plot
plt.style.use('ggplot')
figure = plt.figure()
for i, data in enumerate(datarray):
    axe = figure.add_subplot(221 + i)
    axe.scatter(x[i], data, color=colors[i], alpha=0.5)

plt.show()
