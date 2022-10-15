for i in range(int(input())):
    x=[int(i) for i in input().split()]
    a,b,c,d=x
    win1=a
    if a>b:
        win1=a
    else:
        win1=b
    win2 = c
    if c>d:
        win2=c
    else:
        win2=d

    x.sort(reverse=True)

    if win1>win2:
        if x[0]==win1 and x[1]==win2:
            print("YES")
        else:
            print("NO")
    else:
        if x[0]==win2 and x[1]==win1:
            print("YES")
        else:
            print("NO")
