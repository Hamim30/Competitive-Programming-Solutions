for i in range(int(input())):
    input()
    a=input()
    for i in a:
        if i=="D":
            print("U",end="")
        elif i=="U":print("D",end="")
        else: print(i,end="")
    print()
