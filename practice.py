def find(n):
    for i in range(1,n+1):
        tmp1=i
        tmp2=0
        while tmp1>0:
            tmp2+=tmp1%10
            tmp1//=10
        if tmp2+i==n:
            return 0
    return n
#codeup 1615
a,b=input().split()
a=int(a)
b=int(b)
sum=0
for a in range(a,b+1):
    sum+=find(a)
print(sum)