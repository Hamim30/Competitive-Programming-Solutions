n=int(input())
a=[[1]*n]*n
for i in range(1,len(a)):
    for j in range(1,len(a[1])):
        a[i][j]=a[i-1][j]+a[i][j-1]
print(a[-1][-1])
