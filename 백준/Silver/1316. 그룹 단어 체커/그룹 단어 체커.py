count=0
N=int(input())#개수
for j in range(1,N+1,1):
    A = input()
    leng = len(A)
    B = []
    result = 0
    while True:
        try:
            if A[0] not in B:
                B.append(A[0])
                A = A.lstrip(A[0])
            else:
                result = 1
                break
        except:
            break
    if result == 0:
        count = count + 1
print(count)