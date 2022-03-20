n = int(input())
hap=0
for i in range(1, n + 1, 1):
    a=[]
    a = list(str(input()))
    if a[0] == "O":
        sc = 1
    else:
        sc = 0
    hap=sc
    for j in range(1, len(a), 1):
        if a[j] == "O":
            if a[j] == a[j - 1]:
                sc = sc + 1
            else:
                sc = 1
        else:
            sc = 0
        hap = hap + sc
    print(hap)
