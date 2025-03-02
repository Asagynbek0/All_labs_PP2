import os
path = input("Input your path of file: ")
if os.path.exists(path):
    os.remove(path)
else:
    print("Path isn't exists")