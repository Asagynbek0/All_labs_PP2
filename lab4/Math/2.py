import math

def area_trap(h,b1,b2):
    A = 0.5*(b1 + b2) * h
    return A

h = int(input("height: "))
b1 = int(input("Base, first value:"))
b2 = int(input("Base, second value:"))

print(f"Expected Output: {area_trap(h,b1,b2)}")