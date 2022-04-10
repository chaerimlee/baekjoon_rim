import sys
x=sys.stdin.read()
maxnum=0
maxalph=[]
for i in range(97,123,1):
    n=x.count(chr(i))
    if n>maxnum:
        maxnum=n
        maxalph.clear()
        maxalph.append(chr(i))
    elif n==maxnum:
        maxalph.append(chr(i))
maxalph.sort()
for j in maxalph:
    print(j, end="")