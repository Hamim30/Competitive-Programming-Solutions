import math
for i in range(int(input())):
    a,b= [int(i) for i in input().split()]
    if a==1 or a==2:
        print(1)
    else:
        a-=2
        floors=(a/b)
        floors= math.ceil(floors)
        print(floors+1)
