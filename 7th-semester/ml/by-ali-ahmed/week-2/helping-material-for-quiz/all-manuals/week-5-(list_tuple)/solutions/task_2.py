p=eval(input("Enter a list of numbers:"))
p.sort()
if p[1]>p[0]:
    i = p[1]
    print(i)
else:
    for i in range (1,len(p)):
        if p[i+1]>p[i]:
            print(p[i+1])
            break
        else:
            continue

