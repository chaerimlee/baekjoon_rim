def d(n):
    n=n+sum(map(int,str(n)))
    return n
mylist=set()
for k in range(1,10001,1):
    mylist.add(d(k))

for j in range(1,10001):
    if j not in mylist:
        print(j)
