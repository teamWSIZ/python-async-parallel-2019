# import matplotlib
# import numpy as np

# https://matplotlib.org/3.1.0/tutorials/introductory/sample_plots.html
# Data for plotting
# t = np.arange(0.0, 2.0, 0.01)   # from, to, step
# print(t)
# s = 1 + np.sin(2 * np.pi * t)

#  conda install -c conda-forge matplotlib
import matplotlib.pyplot as plt

x = []
y = []

for i in range(15):
    x.append(i)
    y.append(4 + 0.1 * i + 0.02 * i * i)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x-axis', ylabel='y-axis', title='title_')
ax.grid()

# fig.savefig("test.png")
plt.show()
