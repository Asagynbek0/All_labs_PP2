import os

path = input("Input your path of file: ")

only_directories = []
only_files = []

if os.path.exists(path):
    all_items = os.listdir(path)
    
    for item in all_items:
        full_path = os.path.join(path, item)
        
        if os.path.isdir(full_path):
            only_directories.append(item)
        else:
            only_files.append(item)
    
    print("Only directories:", only_directories)
    print("Only files:", only_files)
else:
    print("The specified path does not exist.")
