from math import sqrt
a=int(input("Enter value of 'a':"))
b=int(input("Enter value of 'b':"))
c=int(input("Enter value of 'c':"))
disc=(b**2)-(4*a*c)
if disc==0:
    r=(-b+sqrt(disc))/(2*a)
    print("The Roots are real, equal and rational")
    print(f"The value of two roots is: {r:.2f} and {r:.2f}")
elif disc>0:
    r1= (-b + sqrt(disc)) / (2 * a)
    r2=(-b - sqrt(disc)) / (2 * a)
    print("The Roots are real, distinct and irrational")
    print(f"The value of two roots is: {r1:.2f} and {r2:.2f}",)
else:
    rr=(-b)/(2*a)
    rc=(sqrt(-disc)) / (2 * a)
    print("The Roots are imaginary")
    print(f"The value of two Roots is: {rr:.2f}+{rc:.2f}j and {rr:.2f}-{rc:.2f}j ")
