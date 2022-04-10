x=int(input())#목표길이x
n=64
s=0
cnt=0
if x==64:
    print(1)
else:
    while x > s:
        n = n / 2
        if n+s<=x:
            s = s + n
            cnt = cnt + 1
            if n+s<=x:
                n=n*2
    print(cnt)