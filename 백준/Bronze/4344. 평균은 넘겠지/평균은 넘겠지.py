n=int(input())
for j in range(1,n+1,1):
    st = list(map(int, input().split()))
    s = 0
    sq = 0
    g = 0
    for i in range(1, st[0]+1, 1):
        s = s + st[i]
    sg = s / (len(st) - 1)
    for k in range(1,st[0]+1,1):
        if st[k]>sg:
            g=g+1
    print("{:.3f}%".format((g/(len(st)-1))*100))