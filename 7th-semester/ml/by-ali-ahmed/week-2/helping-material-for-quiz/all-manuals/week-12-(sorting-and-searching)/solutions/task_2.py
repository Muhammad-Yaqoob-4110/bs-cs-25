l=eval(input("Enter an unsorted list:"))
ol=[]
s=0
b=0
for i in range(0,len(l)):
    s=l[i]
    ol=[]
    for j in range(i,len(l)):
        if s>l[j]:
            s=l[j]
            ol.append(l[j])
            b+=1
    if ol!=[]:
        s = min(ol)
        p = l.index(s)
        pl = l[p]
        l[p] = l[i]
        l[i] = pl
    else:
        pass
print(l,b)