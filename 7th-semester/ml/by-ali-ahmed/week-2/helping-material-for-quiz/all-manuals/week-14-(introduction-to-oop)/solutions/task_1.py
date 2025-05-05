class Students:
    name=""
    age=0
    grade=""
    def __init__(self):
        self.name="Javaria Ahmad"
        self.age=18
        self.grade="A"
    def print_(self):
        print(f"My name is {self.name}. I am {self.age} years old and my grade is {self.grade}",sep="")

stud=Students()
stud.print_()


