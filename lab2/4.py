#Python Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Access Set Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Add Set items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Remove Set items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#Join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)