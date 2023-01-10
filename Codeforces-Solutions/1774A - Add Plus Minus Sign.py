for k in range(int(input())):
    input()
    a=input()
    c=""
    b=0
    if a[0]=="1":
        b=1
    for i in a[1:]:
        if i=="1" and b==0:
            b=1
            c+="+"
        elif i=="1" and b==1:
            b=0
            c+='-'
        elif i=="0":
            c+='+'
    print(c)
