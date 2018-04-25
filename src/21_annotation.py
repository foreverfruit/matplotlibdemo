import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 11)
y = x ** 2
plt.plot(x, y, 'b-')
# xy表示箭头的位置，xytext表示注释文本的坐标
# arrowprops字典类型的关于箭头的属性设置。
# facecolor颜色，frac箭头百分百，arrowstyle是一个内置样式，查看文档具体的props设置
plt.annotate('this is bottom', xy=(0, 1), xytext=(-3, 20),
             arrowprops={'arrowstyle': '->'})
plt.show()
