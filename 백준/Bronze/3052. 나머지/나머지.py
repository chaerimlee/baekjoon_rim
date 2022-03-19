a=[]
for i in range(1,11,1):
    a.append((int(input()))%42)

print(len(list(set(a))))