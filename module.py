import numpy as np
from datetime import datetime

m = 8192
loop = 1000000

print('start time: ' + str(datetime.now()))

for i in range(0, loop):
    tmp = np.log2(m)

print('finish time: ' + str(datetime.now()))

