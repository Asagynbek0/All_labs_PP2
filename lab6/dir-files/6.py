import os
import string

# Удаление файлов A.txt - Z.txt в текущей папке
for i in string.ascii_uppercase:
    file_path = f"{i}.txt"
    if os.path.exists(file_path):  # Проверяем, существует ли файл
        os.remove(file_path)

print("Deleted old files (A.txt - Z.txt) from the current folder.")