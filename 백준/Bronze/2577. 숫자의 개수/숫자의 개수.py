A=int(input())
B=int(input())
C=int(input())
num=list(str(A*B*C))
for j in range(0,10,1):
    n=0
    for i in range(0, len(num), 1):
        if int(num[i]) == j:
            n=n+1
    print(n)

