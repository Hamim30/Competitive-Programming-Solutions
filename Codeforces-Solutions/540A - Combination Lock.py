input()
a=input()
b=input()
c=0
for i in range(len(a)):
    x=int(a[i])
    y=int(b[i])
    if abs(x-y) < (10-abs(x-y)):
        c+=abs(x-y)
    else:
        c+=(10-abs(x-y))
print(c)
