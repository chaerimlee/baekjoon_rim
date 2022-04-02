A,B=map(list,input().split())
for i in range(2,-1,-1):
    if A[i]>B[i]:
        for j in range(2,-1,-1):
            print(A[j],end="")
        break
    elif A[i]<B[i]:
        for j in range(2,-1,-1):
            print(B[j],end="")
        break