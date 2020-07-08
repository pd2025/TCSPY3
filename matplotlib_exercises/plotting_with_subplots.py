import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)
ax[0].plot([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
ax[1].plot([0, 0.5, 1, 1.5, 2], [0, 1, 2, 3, 4], linestyle='dashed')
plt.show()