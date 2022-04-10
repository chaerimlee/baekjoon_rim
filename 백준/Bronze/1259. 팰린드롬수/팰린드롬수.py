while True:
    m=str(input())
    if m=="0":
        break
    else:
        n=list(m)
        result=""
        for i in range(len(n)-1,-1,-1):
            result=str(result)+str(n[i])
        if result==m:
            print("yes")
        else:
            print('no')