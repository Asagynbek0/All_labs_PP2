import os
file = "C:/Users/alinu/Documents/new_folder/labs/lab6/dir-files/a.txt"
with open(file, 'r') as f:
    ct = 0
    for i in f:
        ct += 1

print(ct)