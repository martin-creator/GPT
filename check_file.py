import os

file_path = './resources/ASTRONAUTS.jpg'

if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")