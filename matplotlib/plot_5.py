import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1 * x

plt.figure(num=1, figsize=(8, 8))
plt.plot(x, y, lw=10, zorder=1)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')    # to hide the right frame
ax.spines['top'].set_color('none')      # ...

ax.xaxis.set_ticks_position('bottom')   # reshape scale of x-axis like bottom frame
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)                          # reshape the size of ticks, each tick is in a box
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

plt.show()
