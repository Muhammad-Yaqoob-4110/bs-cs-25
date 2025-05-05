class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14* self.radius ** 2
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
    def volume(self):
        return self.area() * self.height
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
cylinder = Cylinder(radius, height)
volume = cylinder.volume()
print("The volume of the cylinder is:", volume)