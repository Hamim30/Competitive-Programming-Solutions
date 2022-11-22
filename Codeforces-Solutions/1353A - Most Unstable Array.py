for i in range (int(input())):
    le,su= [int(i) for i in input().split()]
    if le==1:
        print(0)
    elif le==2:
        print(su)
    else:
        print(su*2)
