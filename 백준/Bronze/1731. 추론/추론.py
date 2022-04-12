N=int(input())
mylist=[]
myq=[]
for i in range(1,N+1,1):
    num=int(input())
    mylist.append(num)
for j in range(N-1,0,-1):
    q=mylist[j]-mylist[j-1]
    myq.append(q)
if myq.count(q)==N-1:
    print(mylist[N-1]+q)
else:
    myq.clear()
    q = mylist[1] / mylist[0]
    print(int(mylist[N - 1] * q))