import os
import shutil

source = "/Users/sakinalalani/Desktop/Downloads"
destination = "/Users/sakinalalani/Desktop/document_files/Docs"
list_of_files = os.listdir(source)
print(list_of_files)
for i in list_of_files:
    name,extension = os.path.splitext(i)
    if extension == '' :
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + "/" + i
        path2 = destination + "/" + "Document_Files"
        path3 = destination + "/" + "Document_Files" + "/" + i
        if os.path.exists(path2):
            print("moving..." + i + ".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving..." + i + ".....")
            shutil.move(path1,path3)

