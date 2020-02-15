import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
import numpy as np
import math

# --- data
# just need two np-arrays (or just lists) for x,y + 2D array for z
# x = np.arange(-3, 3, 0.01)
# y = np.arange(-3, 3, 0.01)
# z = np.array([[math.sin(xx + yy) for yy in y] for xx in x])  # to są dane, czyli funkcja(x,y)
xx = []
yy = []
zz = []

for i in range(100):
    x = i * 0.1
    for j in range(100):
        y = j * 0.1
        xx.append(x)
        yy.append(y)
        zz.append(x**2 + y**2)

fig, ax = plt.subplots(1, 1)
ax.tricontourf(xx, yy, zz, 50, cmap=cm.hot, norm=plt.Normalize(vmin=10, vmax=100))  # , norm=LogNorm()
ax.set(xlabel='opis x', ylabel='opis y',
       title='Tytuł wykresu')
fig.set_dpi(600)
plt.show()