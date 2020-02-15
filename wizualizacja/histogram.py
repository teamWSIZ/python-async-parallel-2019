# from random import random
import random

import matplotlib
import numpy as np  # conda install -c anaconda numpy
import matplotlib.pyplot as plt

# ----------- generowanie danych
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(100000)
# print(x)  # just an array

# x = []
# for i in range(10):
#     x.append(random.randint(1,6))

# ------- histogram, zakładając, że liczby są w liście "x"

num_bins = 80

fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=1)
ax.set(xlabel='x', ylabel='count', title='title_')
fig.tight_layout()
plt.show()
