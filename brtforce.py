from datetime import datetime

n = 2
m = 8192
loop = 1000000

def brtforce(tmp):
    tmp = tmp * n
    if tmp == m:
        return
    brtforce(tmp)
    return

print('start time: ' + str(datetime.now()))

for i in range(0, loop):
    brtforce(n)

print('finish time: ' + str(datetime.now()))