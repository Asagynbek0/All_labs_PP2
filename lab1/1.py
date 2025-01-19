#python HOME
print("Hello, World!")

#python intro
print("Hello, World!")

#python Get Started
print("Hello,World!")

#python Syntax
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")
        
#python Comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#python Variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Output Variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#python Data types
x = 5
print(type(x))
#python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#python Casting
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#python Strings
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Slicing strings
b = "Hello, World!"
print(b[-5:-2])

#Modify strings
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Format strings
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."


