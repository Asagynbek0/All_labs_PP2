def temp(F):
    C = (5 / 9) * (F - 32)
    return C

F=int(input("Fahrenheit = "))
print(f"{F} F = {temp(F)} C")