import os

path = input("Input your path of file: ")

if os.path.exists(path):
    print(f"File name : {os.path.basename(path)}")
    print(f"Directory: {os.path.dirname(path)}")
else:
    print("This path doesn`t exist")
    