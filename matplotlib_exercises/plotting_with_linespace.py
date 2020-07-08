import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(1, 2, 5)
count = 0

for i in x:
    count += 1
    ax.plot(i, count, 'o')
plt.show()
