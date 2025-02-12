class Shape():
    def __init__(self):
        self.area = 0
    def printArea(self):
        print(self.area)
        
class Rectangle(Shape):
    def __init__(self,length,width):
        self.lenght=length
        self.width=width
        self.area=length*width
    def printArea(self):
        print(self.area)

class Cub(Shape):
    def __init__(self,length):
        self.length=length
        self.V=(length)**3
    def printV(self):
        print(self.V)
        
        
rectangle=Rectangle(5,8)
rectangle.printArea()

V=Cub(4)
V.printV()