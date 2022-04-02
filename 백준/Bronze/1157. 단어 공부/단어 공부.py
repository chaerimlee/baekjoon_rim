s=list(map(str,input().upper()))
a=list(set(s))
maxcount=0
maxnum=0
result=0
for i in range(0,len(a),1):
    if int(s.count(a[i]))>int(maxcount):
        maxnum=a[i]
        maxcount=s.count(maxnum)
        result=1
    elif int(s.count(a[i]))==int(maxcount):
        result=0
if result==1:
    print(maxnum)
elif result==0:
    print("?")
