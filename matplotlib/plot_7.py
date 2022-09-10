import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)

Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1, n)

plt.bar(X, +Y1, edgecolor='black', facecolor='white')
plt.bar(X, -Y2)

for x, y in zip(X, Y1):
    plt.text(x, y + 0.005, '%.2f' % y, ha='center', va='bottom')    # ha mean horizontal alignment

for x, y in zip(X, Y2):
    plt.text(x, -y - 0.1, '%.2f' % y, ha='center', va='bottom')    # ha mean horizontal alignment

plt.show()
