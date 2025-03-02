import time
def square(n, m):
    n_square = pow(n, 1/2)
    m = float(m / 1000)
    time.sleep(m)
    return f"Square root of {n} after {int(m*1000)} miliseconds is {n_square}"
n = 25100
m = 2123
print(square(n, m))