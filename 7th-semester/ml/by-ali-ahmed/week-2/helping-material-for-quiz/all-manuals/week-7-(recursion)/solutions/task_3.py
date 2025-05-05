import random
def addi(n,a=-1):
     sum=0
     a=a+1
     if a>9:
          return sum
     else:
          sum=int(n[a])+addi(n,a)
     return sum
b=[]
for i in range(10):
     p=random.randrange(1000)
     b.append(p)
print("The ten random numbers are:",end="")
for j in b:
     if j==b[9]:
          print(" ",j, ".",sep="", end="")
     else:
          print(" ",j, ",",sep="", end="")
print("\nThe sum of ten random numbers is",addi(b))