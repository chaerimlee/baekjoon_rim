N=int(input())
k=1
t=0
while(N!=0):
    if N>=k:
        N=N-k
        t=t+1
        k=k+1
    else:
        k=1
        pass
print(t)