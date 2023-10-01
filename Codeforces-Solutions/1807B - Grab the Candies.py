for p in range(int(input())):
    (input())
    x=[int(i) for i in input().split()]
    e=0
    o=0
    for i in x:
        if i%2==0: e+=i
        else: o+=i
    if e>o:
        print("YES")
    else: print("NO")
