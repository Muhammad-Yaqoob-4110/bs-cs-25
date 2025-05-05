class chair:
    color=""
    height=""
    material=""
    def __init__(self):
        self.color="Brown"
        self.height="4 feet"
        self.material="rose wood"
    def disp(self):
        print(f'''FEATURES OF CHAIR:
Material:{self.material}
Color: {self.color}
Height: {self.height}''')


obj1=chair()
obj1.disp()
