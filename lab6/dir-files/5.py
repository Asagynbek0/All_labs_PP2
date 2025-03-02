import os
file = open("C:/Users/alinu/Documents/new_folder/labs/lab6/dir-files/a.txt","w")
list = [2,4,6,8,10,12]

for i in list:
    if i == list[0]:
           file.write("[")
    if i != list[-1]:
        file.write(f"{str(i)}, ")
    if i == list[-1]:
        file.write(f"{str(i)}]")
file.close()
file = open("C:/Users/alinu/Documents/new_folder/labs/lab6/dir-files/a.txt")
print(file.read())