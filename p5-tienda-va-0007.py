import matplotlib.pyplot as plt
import numpy as np
# Alexandro Aguilar NC 0007

num_mes = np.array([1, 2, 3, 4, 5, 6])
venta_manda2 = np.array([0, 2000, 3500, 7000, 15000, 20000])

plt.plot(num_mes, venta_manda2,
         marker = "o",
         markersize = 11,
         markerfacecolor = "#D4D7F8",
         markeredgecolor = "Cyan"
)

plt.show()
print("Alexandro Aguilar NC 0007")