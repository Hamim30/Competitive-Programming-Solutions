for i in range(int(input())):
    input()
    m=0
    n=input().split()
    c=0
    for i in n:
        if i=="0":
            c+=1
        elif i=="1":
            if m<c:
                m=c
            c=0
    if m<c:
        m=c       
    print(m)
