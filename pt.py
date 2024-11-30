import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 1000)
y = 5**x

plt.axhline(y=0, color='grey')
plt.axvline(x=0, color='grey')

plt.plot(x, y, color='blue')

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel('Time')
plt.ylabel('Uploaded Sites')
plt.title('Spread of Internet Information')
plt.grid()

plt.show()