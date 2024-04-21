def code():
    a,c,d=[int(i) for i in input().split()]
    x=[int(i) for i in input().split()]
    minimum=min(x)
    lis=[[0 for i in range(a)] for j in range(a)]
    match=[]
    for i in range(a):
        for j in range(a):
            if i==0 and j==0:
                lis[i][j]=minimum
            elif i==0:
                lis[i][j] = lis[i][j-1] + d
            elif j==0:
                lis[i][j] =lis[i-1][j] +c
            else:
                lis[i][j]=lis[i][j-1] +d
            match+=[lis[i][j]]
            
    match.sort()
    x.sort()
    if x!=match:
        return "NO"
    return "YES"
for i in range(int(input())):
    print(code())
