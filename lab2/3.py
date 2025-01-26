#Python Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Access Tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
#Join Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
