for j in range (int(input())):
    a,b=[int(i) for i in input().split()]
    if a==1 or b==1:
        print(a,b)
    else:
        if a==3 and b==3:
            print("2 2")
        elif a==2 and b==3:
            print("2 2")
        elif a==3 and b==2:
            print("2 2")
        else:
            print(a,b)
