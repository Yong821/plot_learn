import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 10)
y1 = 2 * x + 1

plt.figure(num=1, figsize=(8, 8))
plt.plot(x, y1)

ax = plt.gca()
ax.spines['right'].set_color('none')    # to hide the right frame
ax.spines['top'].set_color('none')      # ...

ax.xaxis.set_ticks_position('bottom')   # reshape scale of x-axis like bottom frame
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='green')    # 's' means the size of dot
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)  # use point1(x0, 0) and point2(x0, yo) to draw and line and choose the shape of 'k--' to describe it

plt.annotate(r'$2x+1=3%$', xy=(x0, y0), xycoords='data', xytext=(-80, -80), textcoords='offset points',
             fontsize=10, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
# first param is the content of annotation, 'xy' means its cords, 'xycords' means its cords is based on data
# 'xytext' and 'textcoords' means the annotation position is base on the position of 'xy' plus 30px
plt.show()
