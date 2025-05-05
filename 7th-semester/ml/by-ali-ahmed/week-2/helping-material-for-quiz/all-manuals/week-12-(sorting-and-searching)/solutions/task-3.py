l=eval(input("Enter an unsorted list:"))
sl=[]
b=0
for j in range (len(l)):
    s=l[j]
    a=0
    for i in range (len(sl)):
        if s>sl[i]:
            a+=1
        else:
            break
    b+=a
    sl.insert(a,s)
itera=b+len(l)
print("The Sorted list is",sl,itera)