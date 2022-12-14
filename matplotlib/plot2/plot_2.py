import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 10)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')

plt.xlim(-1, 2)
plt.ylim(-2, 3)

plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'tick1', r'tick2', r'tick3', r'tick4', r'tick5'])
plt.show()