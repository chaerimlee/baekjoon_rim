ex=['c=','c-','dz=','d-','lj','nj','s=','z=']
data=input()
num=len(data)
for i in ex:
    if i in data:
        num=num-data.count(i)*(len(i)-1)
if 'z=' and 'dz=' in data:
    num=num+data.count('dz=')
print(num)