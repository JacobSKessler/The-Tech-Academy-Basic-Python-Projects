import os

fPath = 'C:\\Users\\kessl\\OneDrive\\Desktop\\The-Tech-Academy-Basic-Python-Projects\\'
fName = ''


#find and display all files with .txt extension
for file in os.listdir(fPath):
    if file.endswith(".txt"):
        print(os.path.join(fPath, file))
        fName = os.path.join(fPath, file) #might have problems if dir has > 1 txt file

abPath = os.path.join(fPath, fName)

print("time since modified or created\n ", os.path.getmtime(abPath))
