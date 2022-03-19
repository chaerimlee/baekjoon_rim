n=int(input())
i=0
p=n
while True:
    i=i+1
    a=(p//10)
    b=(p%10)
    p=b*10+((a+b)%10)
    if(p==n):
        break
print(i)