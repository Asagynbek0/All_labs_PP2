import math

def pol_area(n,l):
    A = round((n * pow(l,2) / (4 * math.tan(math.pi / n))))
    return A
    
n = int(input("Input number of sides:"))
l = int(input("Input the length of a side:"))

print(f"The area of the polygon is: {pol_area(n,l)}")