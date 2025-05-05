def prime_numbers(u):
    k=2
    if u==1 or u==0:
        return 0
    if u==2:
        print(u)
        return u
    while k<=u//2:
        if u%k==0:
            return 0
            break
        k+=1
    else:
        print(u)
        return u

start=int(input("Enter Starting Range:"))
end=int(input("Enter the ending Range:"))
sum=0
while start<=end:
    y=prime_numbers(start)
    y=int(y)
    start+=1
    sum=sum+y
print(sum)





