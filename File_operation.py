# Create a File  in "D:\\File Operations\\read.txt with "r" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
# f=open("read.txt",'r')
# print(f.name)
# print(f.writable())
# print(f.readable())
# print(f.closed)


# Read all content in file  uing read() method

# f=open("edit.txt","r")
# p=f.read()
# print(p)
# f.close()

# Read all content in file after 100th index 
# f=open("edit.txt","r")
# print(f.tell())
# print(f.seek(100))
# print(f.read())
# f.close()
# print(f.closed)
# readlines() method:
# f=open("edit.txt","r")
# rd=f.readlines()
# # print(f.readlines())
# for i in rd:
#     print(i)
# f.close()
# import csv
# Create a CSV File for  Employee Details 
# with open('new csv','w',newline="")as f:
#     w=csv.writer(f)
#     w.writerow([100,"ram","ram@gmail.com"])
#     w.writerow([200,"raj","raj@gmail.com"])
#     w.writerow([300,"kumar","kumar@gmail.com"])
#     w.writerow([400,"ragu","ragu@gmail.com"])
#     w.writerow([500,"raju","raju@gmail.com"])
# with open("edit csv",'w',newline="")as g:
#     e=csv.writer(g)
#     e.writerow([600,'ram',"ram@gmail.com"])
#     
# from zipfile import *
# with ZipFile("out.zip",'w',ZIP_DEFLATED)as f:
#     f.write("hello.txt")
#     f.write("read.txt")
#     f.write("edit.txt")
# 
# #read from zip file
# with ZipFile("out.zip","r",ZIP_STORED)as f:
#     list_name=f.namelist()
#     print(type(list_name))
#     print(list_name)
#     for i in list_name:
#         print(i)    
# 
# # Read each File Content in Zip File
# with ZipFile("out.zip",'r',ZIP_STORED) as f:
#     list_name=f.namelist()
#     print(list_name)
#     for i in list_name:
#         f=open(i,"r")
#         r=f.read()
#         print(r)
# import os
# f=os.makedirs(r"C:\Users\User\eclipse-workspace\\A\C")
# print(f)

# to check file or folder:
# f=os.path.isfile(r"C:\Users\User\eclipse-workspace\\A\C")
# print(f)
# 
# f=os.path.isdir(r"C:\Users\User\eclipse-workspace\\A\C")
# print(f)
# 
# # Display list of folder present in particular folder using Listdir? 
# list_dir=os.listdir(r"C:\Users\User\eclipse-workspace")
# print(list_dir)
# for i in list_dir:
#     print(i)

# Display sub list of folder present in particular folder using walk?
# f=os.walk(r"C:\Users\User\eclipse-workspace")
# print(f)
# for i in f:
#     print(i)

# Remove a folder
# os.rmdir(r"C:\Users\User\eclipse-workspace\\A\c")














