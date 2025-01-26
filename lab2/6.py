#Python If...else
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
#Python While Loops
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)