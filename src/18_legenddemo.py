import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
f = plt.figure()
ax = f.add_subplot(111)
ax.plot(x, x, label='$ y = x $', color='b')
ax.plot(x, x ** 2, label='$ y = x^2 $', color='g')
ax.plot(x, x ** 3, label='$ y = x^3 $', color='r')
# 网格
ax.grid(linestyle='-.', color='y')
# 图例，根据label
ax.legend()

# 调整坐标轴范围(x1,x2,y1,y2)
plt.axis([0, 10, 0, 500])

plt.show()
