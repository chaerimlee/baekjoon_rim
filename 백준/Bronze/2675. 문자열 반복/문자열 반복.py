T=int(input())
for t in range(1,T+1,1):
    R, S = input().split()
    mylist = list(str(S))
    for i in mylist:
        print(i*int(R), end="")
    print("")
