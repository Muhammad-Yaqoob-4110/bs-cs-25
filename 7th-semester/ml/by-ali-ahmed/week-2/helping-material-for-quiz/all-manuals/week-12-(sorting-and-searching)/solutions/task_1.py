unso=[-9,82,-38,2,6,7]
c=0
for i in range(0,5):
    for j in range(0,len(unso)-i-1):
        mik=0
        if unso[j]>unso[j+1]:
            mik=unso[j]
            unso[j]=unso[j+1]
            unso[j + 1]=mik
            c+=1
        else:
            continue
print(unso,c)
