for _ in range(1,(int(input())+1)):
    a= int(input())
    x=a*3
    y=1
    c=1
    al=[(y,x)]
    if a%2!=0:
        for i in range((a//2)):
            y+=3
            x-=3
            al+=[(y,x)]
            c+=1 
    else:
        for i in range((a//2)-1):
            y+=3
            x-=3
            al+=[(y,x)]
            c+=1 
    print(c)
    for i in al:
        print(i[0],i[1])
    
