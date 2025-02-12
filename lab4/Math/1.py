import math

def radian(deg):
    p=math.pi
    r = deg * (p/180)
    return r



deg = int(input("degree = "))
print(radian(deg))