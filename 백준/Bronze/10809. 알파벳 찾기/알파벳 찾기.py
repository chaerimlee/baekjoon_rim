rlist=[]
mylist=list(map(ord,input()))
for i in range(97,123,1):
    try:
        rlist.append(mylist.index(i))
    except:
        rlist.append(-1)
for j in rlist:
    print(j,end=" ")