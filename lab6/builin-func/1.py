from functools import reduce

def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3]
print(f"Product of all numbers = {multiply(numbers)}")
