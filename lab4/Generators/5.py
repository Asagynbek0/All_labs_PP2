def all_n(n):
    numb = n
    while numb >= 0:
        yield numb
        numb-=1 
        
n = int(input("n : "))
gen = all_n(n)
for i in gen:
    print(i,end = " ")