
for _ in range(int(input())):
    input()
    a=input()
    b=[0]*6
    for i in a:
        if i=="T":
            b[0]+=1
        elif i=="i":
            b[1]+=1
        elif i =="m":
            b[2]+=1
        elif i =="u":
            b[3]+=1
        elif i =="r":
            b[4]+=1
        else:
            b[5]+=1
    if b !=[1,1,1,1,1,0]:
        print("NO")
    else:
        print("YES")
