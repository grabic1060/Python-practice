import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-0.0001, 0.0001, 0.00000000001)

amplitude = np.log2(x)

plt.xlabel('x')
plt.ylabel('log(x)')

plt.grid(color = "gray", alpha=.5,linestyle='--')
plt.plot(x, amplitude, label='log(x)')

plt.show()