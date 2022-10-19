for _ in range(int(input())):
    a,b,d= [int(i) for i in input().split()]
    c=1
    l=1
    if a==0 or b==0:
        c=0
    elif (a%2==0) or (b%2==0):
        while (a%2)!=1:
            a=a/2
            c+=l
            l*=2
        while (b%2)!=1:
            b=b/2
            c+=l
            l*=2
    else:
        c=1

    if c>=d:
        print("YES")
    else:
        print("NO")
