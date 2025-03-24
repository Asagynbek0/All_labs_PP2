import os
import string

for i in string.ascii_uppercase:
    file = f"{i}.txt"
    with open(file, "w") as f:  # "w" создаст файл или перезапишет его
        f.write(f"This {file}\n")

print("Created 26 files (A.txt - Z.txt).")
