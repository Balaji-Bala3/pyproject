# def a():   
#   emp_Id=12
#   emp_Name="Bala"
#   emp_Dob='12.02.1995'
#   emp_Phone=12346
#   emp_Email='bala@gmail.com'
#   emp_Address="12,north street,chennai"
#   print(emp_Id,emp_Name,emp_Dob,emp_Phone,emp_Email,emp_Address)
# a()
# 
# # Create the above functions with passing some arguments
# def add(*m):
#   print(m)
# add('greens_Omr(),greens_Adayar(),greens_Tambaram(),greens_Velacherry(),greens_Anna_Nagar()')

# def emp_Id():
#     print(5)
# emp_Id()
# def emp_Name():
#   a="bala"
#   print(a)
# def emp_Dob():#,
#   b="12.01.1989"
#   print(b)
# def emp_Phone():
#     b= 2132
#     print(b)
# def emp_Email():
#     c="bala@gmail.com"
#     print(c)
# def emp_Address():
#     d="12,north st, chennai"
# emp_Name()
# emp_Dob()
# emp_Phone()
# emp_Email()
# emp_Address()
      
# function with arguments:
# def greens_Omr(c,d):
#     c=20
#     d=40
#     e=c/d
#     print(e)
# greens_Omr(20,40)
# def greens_Adayar(name,age):
#      print(name,age)
# greens_Adayar(name='bala',age=25)
#            
# def greens_Tambaram(name="bala",age=25):
#     print(name,age)
# greens_Tambaram("bala",age=25)
# greens_Tambaram()

# Create the above function and pass two arguments and returntype of one value
# def add(a,b):
#  a=155
#  b=214
#  c=a+b
#  return c
# v=add(0,214)
# print(v)
# def sub(a,b):
#  a=155
#  b=214
#  c=a-b
#  return c
# v=sub(155,214)
# print(v)

# Create the above function and pass two arguments and  returntype of multiple values
# def calc(a,b):
#  mul=a*b
#  div=a/b
#  return mul,div
# a,b=calc(10,20)
# print(a)
# print(b)
# v=calc(5,5)
# print(v)

# def my_function(fname, lname):
#   print(fname + " " + lname)
# 
# my_function("Harry")-----------------1 arg missing

# def my_function(country = "Norway"):
#   print("I am from " + country)
# 
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# Create the below functions with three arguments with the default return type
# def company_details(name,age,email):
#    name='bala'
#    age=25
#    email="bala@gmail.com"
#    return name,age,email
# v= company_details("bala",25,"bala@gmail.com")
# print(v)
#   
# # Create the below functions with variable argument length
# def details(**de):
#     print(de)
#     print(type(de))
#     for i in de.items():
#         print(i)
# details(name='bala',age=25,email="bala@gmail.com")
# 
# def computer_names(*names):
#   print(names)
# computer_names(name1="hp",name2="sony",name3="dell")-----error

# Create a recursive function of your own and print the word "Welcome"
# def func():
#   print('welcome')
#   func()
# func()

# count=0
# def fun():
#   global count
#   count=count+1
#   print('python')
#   if count<=100:
#       fun()
# fun()
        
#  Using lambda function perform addition,subtraction and multiplication
# def cube(a):
#     print(a*a*a)
#     print(lambda a:a*a*a)
# cube(5)
############# lambda incomplete





