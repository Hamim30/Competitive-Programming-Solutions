a,b = [int(i) for i in input().split()]
c=[]
for i in range (a):
    c+=input().split()
if "C" in c or "M" in c or "Y" in c :
    print('#Color')
else:
    print('#Black&White')
