import numpy as np
import matplotlib.pyplot as plt

n = 81
a = np.random.uniform(0, 1, n).reshape(9, 9)    # 81 values are obtained from a uniform distribution, and reshape the array

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')     # read them

plt.xticks(())              # let x-axis disappear
plt.yticks(())              # ...
plt.colorbar(shrink=0.9)    # color-bar:right the img, and let its height is 0.9 times the height of img
plt.show()
