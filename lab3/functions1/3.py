def solve(numheads, numlegs):
    c= (numlegs - 2 * numheads)/2
    r=numheads-c
    return int(c),int(r)
numheads = int(input("numheads = "))
numlegs = int(input("numlegs = "))
res=solve(numheads,numlegs)
print(f"Chikens numbe = {res[0]} , Rabbits number = {res[1]} ")