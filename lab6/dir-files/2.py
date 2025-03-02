import os

path = input("Input your path of file: ")
print(f"Existence: {os.path.exists(path)}")
print(f"Readability: {os.access(path, os.R_OK)}")
print(f"Writability: {os.access(path, os.W_OK)}")
print(f"Executablity: {os.access(path, os.X_OK)}")