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
        
rectangle=Rectangle(5,8)
rectangle.printArea()