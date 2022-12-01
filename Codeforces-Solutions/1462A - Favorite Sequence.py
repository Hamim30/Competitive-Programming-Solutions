for _ in range(int(input())):
    input()
    a=[int(i) for i in input().split()]
    s=[]
    i=0
    j=len(a)-1
    while i<=j:

        s+=[a[i]]
        if i==j:
            i+=1
            j-=1
            continue
        s+=[a[j]]
        i+=1
        j-=1
    for i in s:
        print(i,end=" ")
