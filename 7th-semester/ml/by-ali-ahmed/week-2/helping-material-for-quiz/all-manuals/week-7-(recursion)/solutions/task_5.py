def reverse_(n,a=-1):
    a=a+1
    m=""
    if a>(len(n)-1):
        return m
    else:
        m+=n[len(n)-a-1]
        m+=reverse_(n,a)
    return m
p=input("Enter a string:")
print("The reversed string is:",reverse_(p))

