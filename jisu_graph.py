import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-99,-98,1000000)
y = np.exp(2*x)

#그래프 설정
fig = plt.figure()

plt.plot(x,y, 'b-')
plt.title('Exponential Wave')

plt.xlabel('X')
plt.ylabel('Exp(x)')

plt.grid()

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()