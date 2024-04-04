import os

def list_directories_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    print("\nAll directories and files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

path = 'D:\VsCode\python'
list_directories_files(path)

#2
path = r'D:/Users/karbozzhansaya/Desktop/Принципы программирования/6lab' 
p = os.listdir(path)
for item in p:
    full_path = os.path.join(path, item)
    print('Exists:', os.access(full_path, os.F_OK))
    print('Readable:', os.access(full_path, os.R_OK))
    print('Writable:', os.access(full_path, os.W_OK))
    print('Executable:', os.access(full_path, os.X_OK))
    print()

#3
def analyze_path(given_path):
    if os.path.exists(given_path):
        print("The path exists.")
        filename = os.path.basename(given_path)
        directory = os.path.dirname(given_path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("The path does not exist.")

given_path = 'D:\VsCode\python'

analyze_path(given_path)
#4
f = open(r"/Users/karbozzhansaya/Desktop/Принципы программирования/6lab/1.txt")
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")
#5
f = open(r"D:\VsCode\python\lab6\dir-and-files\5.txt", "a")
a = ["bmw ", "m5 ", "f90 "]
for i in a:
    f.write(i)

#6
def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            file.write(f"This is the content of file {filename}\n")
        print(f"File {filename} has been created.")

generate_files()
#7
def copy(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


source_file = '4.txt'
destination_file = '5.txt'

copy(source_file, destination_file)
#8
p=(r"/Users/karbozzhansaya/Desktop/Принципы программирования/6lab/delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")
