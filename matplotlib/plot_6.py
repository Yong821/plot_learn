import numpy as np
import matplotlib.pyplot as plt
n = 1000
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

T = np.arctan2(Y, X)
ax = plt.gca()
ax.spines['right'].set_color('none')    # to hide the right frame
ax.spines['top'].set_color('none')      # ...
ax.spines['bottom'].set_color('none')      # ...
ax.spines['left'].set_color('none')      # ...

plt.scatter(X, Y, s=15, c=T, alpha=.5)
# plt.xlim(-1.5, 1.5)
# plt.ylim(-1.5, 1.5)
plt.xticks(())
plt.yticks(())
plt.show()
