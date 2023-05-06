#codeup 2023
n=int(input())
sum=[]
while n>0:
    tmp=n%27
    n//=27
    sum.append(chr(64+tmp))
    sum.reverse()
for i in sum:
    print(i,end='')