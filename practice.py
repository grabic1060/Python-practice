base = [[0 for i in range (101)] for j in range (101)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            base[j][k] = 1

result = 0
for i in base:
    result += sum(i)
print(result)
