x = int (input())
lev= 0
while True:
    x-=((lev+1)*(lev+2))/2
    if x>=0:
        lev+=1
    else:
        break
print(lev)
