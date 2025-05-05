class Rectangle:
    length=0
    width=0
    def __init__(self):
        self.length=8
        self.width=3
    def perimeter(self):
        plus=(2*self.length)+(2*self.width)
        print(f"The Perimeter of Rectangle is {plus}")
    def area(self):
        minus=self.length*self.width
        print(f"The Area of Rectangle is {minus}")
saar=Rectangle()
saar.perimeter()
saar.area()
