import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 100000)
x_exp = np.linspace(-10, 10, 100000)
x_log = np.linspace(-100, 100, 100000)

exp_1 = np.exp2(x_exp) # 기본
exp_2 = -np.exp2(x_exp) # x축 대칭
exp_3 = np.exp2(-x_exp) # y축 대칭

log_1 = np.log2(x_log) # 기본
log_2 = -np.log2(x_log) # x축 대칭
log_3 = np.log2(-x_log) # y축 대칭

y = x

plt.axis('equal')

plt.xticks(np.arange(-20, 20))
plt.yticks(np.arange(-20, 20))

plt.axhline(y=0, color='grey')
plt.axvline(x=0, color='grey')

plt.plot(x, y, color='black')

plt.plot(x_exp, exp_1, color='blue')
plt.plot(x_exp, exp_2, color='red')
plt.plot(x_exp, exp_3, color='green')

plt.plot(x_log, log_1, color='blue')
plt.plot(x_log, log_2, color='green')
plt.plot(x_log, log_3, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('exp & log')
plt.grid()

plt.show()