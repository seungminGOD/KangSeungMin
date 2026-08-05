import os

current_working_directory = os.getcwd()
print(current_working_directory)

file_list = os.listdir()
for file_name in file_list:
    print(file_name)

path = os.path.join("data", "08_press.csv")
print(path)

if os.path.exists(path):
    print(f"파일 있음: {path}")
