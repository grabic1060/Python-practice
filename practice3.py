T=int(input())
for i in range(0,T):
    n=int(input())
    hak=0
    gpa=0
    for j in range(0,n):
        a,b=input().split()
        hak+=int(a)
        gpa+=float(b)*float(a)
    print(hak, round(gpa/hak,1))