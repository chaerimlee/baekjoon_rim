N=int(input())
result=0
sum=0
for i in range(1,N,1):
    result=(i*N)+i
    sum=sum+result
print(sum)