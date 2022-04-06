import math
A,B,C=map(int,input().split())
if(C>B):
    result = A / (C - B)
    if(result-int(result)>0):
        print(math.ceil(result))
    else:
        print(math.ceil(result)+1)
else:
    print(-1)