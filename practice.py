import random
num=random.randint(1,100)
print('시도 횟수 설정')
attempt=int(input())
print('범위: 1~100\n시작!')
for i in range(0,attempt):
    ipt=int(input())
    if ipt < num:
        print('Up')
    if ipt > num:
        print('Down')
    if ipt == num:
        print('성공!')
        exit()
    print(attempt-i-1,'회 남았습니다')
print('실패..')