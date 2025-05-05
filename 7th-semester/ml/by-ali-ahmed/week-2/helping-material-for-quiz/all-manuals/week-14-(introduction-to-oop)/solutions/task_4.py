class Calculator:
    num_one=0
    num_two=0
    def __init__(self):
        self.num_one=14
        self.num_two=10
    def add(self):
        print("ADDITION:",self.num_two+self.num_one)
    def sub(self):
        print("SUBTRACTION:", self.num_one - self.num_two)
    def mul(self):
        print("MULTIPLICATION:", self.num_two * self.num_one)
    def div(self):
        print("DIVISION:", self.num_one / self.num_two)
ong=Calculator()
ong.add();ong.sub();ong.mul();ong.div()
