import os
import shutil
def manager():
    print('''What do you want?
    -if you want work with file press f or F.
    -if you want work with directory press d or D.''' )
    a=str(input())
    if a=='d' or a=='D':
        Work_directory()
    elif a=='f' or a=='F':
        Work_file()
def Work_file():
    print('''What do you want?
    -if do you want delete the file, please press 1.
    -if do you want rename the file, please press 2.
    -if do you want  add content to this file, please press 3.
    -if do you want rewrite content of file, please press 4.
    -if do you want return to the parent directory, please press 5.''')
    a=input()
    if a=='1':
        delete_file()
    elif a=='2':
        rename_file()
    elif a=='3':
        add_content_file()
    elif a=='4':
        rewrite_file()
    elif a=='5':
        parent_directory()
def rename_file():
    print('''Choose the ways.''')
    a=input()
    b=input()
    if os.path.exists(a):
        os.rename(a,b)
        print("Rename the file done successfully.")
    else:
        print("The file doesn't exist.")
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass
def delete_file():
    print('''Write the name file.''')
    name_file=input()
    location='/Users/kozhahmet/PP 2/Week 6' #Mynau location-y vobshe kerek emes, onsyzda file-dy tauyp alyp oshyryp tastaidy.
    if os.path.exists(name_file):
        os.remove(name_file)
        print("Delete the file done successfully.")
    else:
        print("The file doesn't exist.")
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass
    #directory osyruge bolmaidy, bundai jolmen.
def add_content_file():
    print("Please write the name of file.")
    file_name=input()
    if os.path.exists(file_name):
        f = open(file_name, "w")
        print("Write the content to this file what you want to add.")
        text=input()
        f.write(text)
        f.close()

        print('''Do you want see the file?
    -If yes, please write YES or yes.
    -If no, please write NO or no. ''')
        print_file=input()
        if print_file=="YES" or "yes":
            f=open(file_name,'r')
            print(f.read())
        elif print_file=="NO" or "no":
            pass
    else:
        print("The file doesn't exist.")
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass
def rewrite_file():
    print("The first choose the file, and write the name of file.")
    name_file=input()
    if os.path.exists(name_file):
        print("Then you can rewrite content of file, please write the content. ")
        f=open(name_file,'w')
        text=input()
        f.write(text)
        f.close()
        print('''Do you want see the file?
    -If yes, please write YES or yes.
    -If no, please write NO or no. ''')
        print_file=input()
        if print_file=="YES" or "yes":
            f=open(name_file,'r')
            print(f.read())
        elif print_file=="NO" or "no":
            pass
    else:
        print("The file doesn't exist.")
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass
def parent_directory():
    a=os.getcwd()
    print(a)
def Work_directory():
    print('''What do you want?
    -if do you want rename the directory, please press 1.
    -if do you want print number of files, please press 2.
    -if do you want print number of directories, please press 3.
    -if do you want list content of the directory, please press 4.
    -if do you want add file to this directory, please press 5.
    -if do you want add new directory to this directory, please press 6.''')
    a=input()
    if a=='1':
        rename_directory()
    elif a=='2':
        number_file_directory()
    elif a=='3':
        number_directory_directory()
    elif a=='4':
        list_directory()
    elif a=='5':
        add_file()
    elif a=='6':
        add_directory()
def rename_directory():
    print("Please write the names of directory.")
    dir1=input()
    dir2=input()
    if os.path.exists(dir1) and os.path.exists(dir2):
        os.rename(dir1,dir2)
        print("The Directory has been successfully renamed!")
    else:
        print("The file doesn't exist.")
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass
def number_file_directory():
    print("You should write the way of directory what do you want print number of filies in this directory.")
    way_directory=input()
    count_file(way_directory)
def count_file(way):
    totalFiles = 0
    for base, dirs, files in os.walk(way):
         for Files in files:
            totalFiles += 1
    print('Total number of files:',totalFiles)
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass
def number_directory_directory():
    print("You should write the way of directory what do you want print number of directories in this directory.")
    way_directory=input()
    count_directory(way_directory)
def count_directory(way):
    totalDir=0
    for base, dirs, files in os.walk(way):
        for directories in dirs:
            totalDir += 1
    print('Total number of directories:',totalDir)
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass
def list_directory():
    print("Write the way.")
    way=input()
    print(os.listdir(way))
def add_file():
    print("You should write the way of file and write the way of directory which add file to this directory.")
    file_name=input()
    directory_name=input()
    if os.path.exists(file_name) and os.path.exists(directory_name):
        shutil.move(file_name,directory_name)
        print("Add a file to directory done successfully.")
    else:
        print("The file or directory doesn't exist.")
    print("Do you want to continue working?")
    ans=input()
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass

def add_directory():
    print("You should write the way of directory and write the way of directory which add new directory to this directory.")
    new_directory=input()
    directory_name=input()
    if os.path.exists(new_directory) and os.path.exists(directory_name):
        shutil.move(new_directory,directory_name)
        print("Add a new directory to directory done successfully.")
    else:
        print("The directory doesn't exist.")
    print("Do you want to continue working?")
    ans=str(input())
    if ans=="YES" or ans=="yes":
        manager()
    elif ans=="NO" or ans=="no":
        print("Good bye.")
    else:
        pass

manager()