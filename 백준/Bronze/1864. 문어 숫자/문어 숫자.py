mydict= {'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1}
m=[]
result=0
while True:
    m.clear()
    m=list(map(str,input()))
    if m[0]=="#":
        break
    else:
        sum=0
        j = 0
        for i in range(len(m)-1,-1,-1):
            sum=sum+int((mydict[m[i]]*(8**j)))
            j=j+1
        print(sum)