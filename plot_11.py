from mpl_toolkits import mplot3d    # import 3d tool
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()                  # create a figure
ax = plt.axes(projection='3d')      # create 3d zone in this figure(fig)


# construct our point
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)

# ax.plot3D(x, y, z, 'gray')                  # line
ax.scatter3D(x, y, z, c=y)   # scatter fig, param 'c' = y means every point with different y will be dyed different color
ax.set_title('3D plot')                     # title
plt.show()
