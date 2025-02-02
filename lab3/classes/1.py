class String():
    def __init__(self):
        self.string=" "
    def getstring(self):
        self.string=input("Input : ")
    def printstring(self):
        print(self.string.upper())

string = String()

string.getstring()

string.printstring()