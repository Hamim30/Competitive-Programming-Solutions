for i in range (int(input())):
    a,b,c,d= [int(i) for i in input().split()]
    x=0
    if a<b:
        x+=1
    if a<c:
        x+=1
    if a<d:
        x+=1
    print(x)
