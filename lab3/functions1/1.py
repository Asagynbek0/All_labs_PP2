def ounces(grams):
    o = grams * 28.3495231
    return o
grams=float(input("grams = "))
print(f"{grams} grams = {ounces(grams)} ounces")