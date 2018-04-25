# 效果：多重y轴，同一个axe中的两个线采用不用的刻度，这个时候需要两条对应的坐标轴，左右并列分别对应两条数据线

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(0, 11)
# y1 = x ** 2
# y2 = -3 * x + 3
# plt.plot(x, y1, color='r', label='$y1=x^2$')
# plt.legend(loc=1)
# # 添加一条并列坐标轴
# plt.twinx()
# plt.plot(x, y2, color='b', label='$y2=-3*x+3$')
# # 此时两条线y1 y2就在同一个axe上对应不同的y轴
# plt.legend(loc=2)
# plt.show()

# -----------------OOP方式--------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11)
y1 = x ** 2
y2 = -3 * x + 3
fig = plt.figure()
ax = fig.add_subplot(111)
l1, = ax.plot(x, y1, color='r', label='$y1=x^2$')
ax2 = ax.twinx()
l2, = ax2.plot(x, y2, color='b', label='$y2=-3*x+3$')
# 这里需要了解axe和figure的范围，若gcf()再legend，图例会滑到整个图的四个角，坐标轴外面
# 若gca()表示获取到轴，再legend，图例画在轴范围内
plt.gca().legend((l1, l2), ('$y1=x^2$', '$y2=-3*x+3$'), loc=0)
plt.show()
# ---------------------
# 同理，twiny可以获得并列的x轴共用一个y轴
