for i in range(int(input())):
    a=input()
    c=len(a)//2
    if (a[:c]==a[c:]):
        print("YES")
    else:
        print("NO")
