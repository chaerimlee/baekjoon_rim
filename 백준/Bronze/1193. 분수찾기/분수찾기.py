N=int(input())
cnt=1
num=1
while N>cnt:
    N=N-cnt
    cnt=cnt+1
    num=num+1
if num%2!=0:
    c=num
    m=1
    for i in range(1,N,1):
        m=m+1
        c=c-1
else:
    m = num
    c = 1
    for i in range(1, N, 1):
        c = c + 1
        m = m - 1
print('{}/{}'.format(c,m))