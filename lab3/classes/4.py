class Point():
    def __init__(self, x, y):
        self.x= x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def move(self,mvd_x,mvd_y):
        self.x=mvd_x
        self.y=mvd_y
    def dist(self,other_points):
        print(self.x - other_points.x , self.y - other_points.y)
        
point1=Point(3,5)
point1.show()

point1.move(4,6)
point1.show()

point2=Point(7,9)
point1.dist(point2)