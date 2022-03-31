mylist=[]
def han(n):
    N=n
    if n<10:
        N='0'+str(N)
    s = list(map(int,str(N)))
    for i in range(len(s),1,-1):
        try:
            if(s[i]-s[i-1]==s[i-1]-s[i-2]):
                continue
            else:
                result = 0
                break;
        except:
            result = 1
    return result
n = int(input())
count = 0;
for j in range(1,n+1,1):
    if han(j)==1:
        count=count+1
print(count)