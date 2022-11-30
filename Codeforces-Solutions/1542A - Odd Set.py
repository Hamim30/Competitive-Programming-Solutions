for _ in range(int(input())):
    input()
    a=[int(i) for i in input().split()]
    c=0
    for i in a:
        if i%2==0:
            c+=1
        else:
            c-=1
    if c==0:
        print("YES")
    else:
        print("NO")
