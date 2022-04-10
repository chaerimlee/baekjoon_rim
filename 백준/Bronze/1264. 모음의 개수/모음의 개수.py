mylist=['a','e','i','o','u']
while True:
    sum=0
    x=input()
    if x=='#':
        break
    else:
        x=x.lower()
        for i in mylist:
            sum=sum+x.count(i)
        print(sum)