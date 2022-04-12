N=int(input())
mylist=[1,2,3]
def change(a,b):
    A = mylist.index(a)
    B = mylist.index(b)
    mylist[A],mylist[B]=mylist[B],mylist[A]
    return mylist
try:
    for i in range(1,N+1,1):
        a, b = map(int,input().split())
        result = change(a,b)
        mylist=result
    print(mylist[0])
except:
    print(-1)