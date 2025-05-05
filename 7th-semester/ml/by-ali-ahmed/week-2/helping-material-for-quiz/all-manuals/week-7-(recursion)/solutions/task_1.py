def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*(fact(n-1))
N=int(input("Enter the value of n="))
R=int(input("Enter the value of r="))
permutation=(fact(N))/(fact(N-R))
combination=(fact(N))/((fact(N-R))*(fact(R)))
print(f"The Permutation of {N} and {R} is {permutation}")
print(f"The Combination of {N} and {R} is {combination}")


