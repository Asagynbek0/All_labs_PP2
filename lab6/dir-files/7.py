import os

file = open("C:/Users/alinu/Documents/new_folder/labs/lab6/dir-files/a.txt")
copy = open("copy.txt", "w")
for i in file:
    copy.write(i)