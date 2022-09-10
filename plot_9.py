import numpy as np
import matplotlib.pyplot as plt

n = 81
a = np.random.uniform(0, 1, n).reshape(9, 9)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')

plt.xticks(())
plt.yticks(())
plt.colorbar(shrink=0.9)
plt.show()
