# 子图
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)

fig, axes = plt.subplots(ncols=2,nrows=2)
axe1,axe2,axe3,axe4 = axes.ravel()

# 上面的写法等效于下面的写法
# fig = plt.figure()
# axe1 = fig.add_subplot(221)
# axe2 = fig.add_subplot(222)
# axe3 = fig.add_subplot(223)
# axe4 = fig.add_subplot(224)

axe1.plot(x, [i ** 3 for i in x])
axe2.scatter(x, x)
axe3.hist(x, bins=9)
axe4.plot(x, -x)

plt.show()
