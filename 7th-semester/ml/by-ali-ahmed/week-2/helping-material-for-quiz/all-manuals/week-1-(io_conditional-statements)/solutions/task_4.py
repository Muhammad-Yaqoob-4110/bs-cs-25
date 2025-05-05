from math import sqrt

#Function for checking Quadrant
def quardrants(a,b):
    if a>0 and b>0:
        return 1
    if a<0 and b>0:
        return 2
    if a<0 and b<0:
        return 3
    if a>0 and b<0:
        return 4

#Functions to extract values of x and y from given string
def value_of_x(coordinate):
    a,b=coordinate.find("("),coordinate.find(",")
    x=int(coordinate[a+1:b])
    return x
def value_of_y(coordinate):
    a,b=coordinate.find(","),coordinate.find(")")
    y=int(coordinate[a+1:b])
    return y

#Main Function
one=input("Enter first coordinate:")
two=input("Enter second coordinate:")
x1,y1=value_of_x(one),value_of_y(one)
x2,y2=value_of_x(two),value_of_y(two)
print(f"The Quadrant of point {x1,y1} is =",quardrants(x1,y1))
print(f"The Quadrant of point {x2,y2} is =",quardrants(x2,y2))
dis=sqrt((x2-x1)**2+(y2-y1)**2)
print(f"The Distance between these two points is ={dis:.3f}")