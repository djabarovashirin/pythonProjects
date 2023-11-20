
### This Python script is designed to check if a file exists at a specified path and
### if it does, delete the file

import os

file_path = 'File PATH'
print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been deleted!")
else:
    print("This file does NOT exist!!!")