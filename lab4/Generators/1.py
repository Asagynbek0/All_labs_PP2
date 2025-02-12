def Square_gen():
    s = 1
    while True:
        yield s**2
        s+=1
        
n = int(input("num = "))
gen=Square_gen()
for i in range(n):
    print(next(gen))