l=input("Enter a binary number:")
sum=0
for i in range(len(l)):
    j=(int(l[i])*(2**((len(l)-1)-i)))
    sum+=j
print("The decimal number is ",sum)
