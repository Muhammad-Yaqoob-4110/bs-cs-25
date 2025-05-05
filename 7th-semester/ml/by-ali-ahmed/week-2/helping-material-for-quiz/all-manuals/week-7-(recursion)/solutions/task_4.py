def power (n,e):
    c=0
    if e==1:
        return n
    else:
       c=n* power(n,e-1)
    return c
N=int(input("Enter the number:"))
P=int(input("Enter the power for that number:"))
print("The final number is",power(N,P))