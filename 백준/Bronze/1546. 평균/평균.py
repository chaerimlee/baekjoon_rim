N=int(input())
a=list(map(int,input().split()))
M=max(a)
for j in range(0,N,1):
    a[j]=a[j]/M*100
print(sum(a)/N)