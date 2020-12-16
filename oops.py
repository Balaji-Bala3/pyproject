# class Employee():
#     def emp_Id(self):
#         print("Employee ID is 123")
#     def emp_Name(self):
#         print(id(self))
#         print("Employee name is Raj")
#     def emp_Dob(self):
#         print("Employee Dob is 12/3/95")
#         print(id(self))
#     def emp_Phone(self):
#         print("Employee phone no is 123")
#     def emp_Email(self):
#         print("Employee mail ID is 123@gmail.com")
#     def emp_Address(self):
#         print("Employee adsress is 123 north street, Chennai")
# e=Employee()
# e.emp_Id()
# e.emp_Name()
# e.emp_Dob()
# e.emp_Phone()
# e.emp_Email()
# e.emp_Address()
# print(id(e))
# m=Employee()
# m.emp_Address()
# print(id(m))
from symbol import decorator

# class Greentech():
#     def greens_Omr(self,id):
#         print("Greens omr ID is",id)
#     def greens_Adayar(self,name):
#         print(name)
#     def greens_Tambaram(self,address):
#         print(address)
#     def greens_Velacherry(self,count):
#         print(count)
# g=Greentech()
# g.greens_Omr(123)
# g.greens_Adayar('Adayar')
# g.greens_Tambaram("123, North st, Chennai")
# g.greens_Velacherry(1)

# class Employee_details:
#       def __init__(self):
#           print("constructor")
#           print(id(self))
# 
#       def add(self):
#           print("add")
#           print(id(self))
# 
# d = Employee_details()
# d.add()
# 
# class Employee_details1():
#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email
#         print(id)
#         print(name)
#         print(email)
# 
#     def add(self):
#         print(self.id)
# 
# d = Employee_details1(10,"vel","vel@gmail.com")
# d.add()


# class Employee_details2:
#     def __init__(self,id,name,email):
#         self.empid=id
#         self.empname=name
#         self.empemail=email
#     def getId(self):
#         print(self.empid)
#     def getName(self):
#         print(self.empname)
#         print(id(self))
#     def getemail(self):
#         print(self.empemail)
# d = Employee_details2(10,"vel","vel@gmail.com")
# d.getId()
# d.getName()
# print(id(d))

####################TYPES OF VARIABLE CALLING AND ACCESSING###########################
#######LOCAL
# class Employee():
#     def m1(self):
#         a=100
#         print(a)
#         print(id(self))
#     def m2(self):
#         b=200
#         print(b)
#         
# e=Employee()
# e.m1()
# e.m2()

########Instance
# class Employee2():
#     def __init__(self):
#         self.a=100
#         self.b=200
#         self.c=600
#         print(id(self.c))
#         print(self.a)
#         print(self.b)
#     def emp(self):
#         self.d=300
#         self.c=400 ########## if one or more value in same variable it takes only recent one
#         print(self.a)
#         print(self.b)
#         print(self.c)
#         print(id(self.c))
#         print(self.d)
# e=Employee2()
# e.emp()
# print(e.a)
# print(e.d)
# print(e.c)

#######STATIC VARIABLE
# class Employee():
#     alpha="beta"
#     def __init__(self):
#         Employee.a=100
#         self.b=200
#         print("Employee.a is.....",Employee.a)
#         print("self.b is.....",self.b)
#     def m1(self):
#         self.c=300
#         Employee.d=400
#         print("Employee.d is.....",Employee.d)
#         print("self.c is.....",self.c)
#     #############CLASS METHOD############
#     @classmethod             #-------decorator
#     def m2(cls):
#         cls.e=500
#         Employee.f=600
#         print("cls.e is.....",cls.e)
#         print("Employee.f is......",Employee.f)
#         print("D is...",Employee.d)
#     @staticmethod
#     def m3():
#         Employee.g=700
#         print(Employee.g)
#         print("D is...",Employee.d)
# Employee.h=800
# print(Employee.alpha)
# print(Employee.h)
# print("..................")
# e=Employee()
# e.m1()
# e.m2()
# e.m3()
# print("D is...",Employee.d)
    