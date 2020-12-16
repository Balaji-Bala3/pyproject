# a=12
# while a<=15:
#     print(a)
#     try:
#        a=a+"1"
#     except TypeError:
#         print("handled")
#     break
# # no of exception for 1 try:
# a=12
# while a<=15:
#     print(a)
#     try:
#        a=a+"1"
#     except ValueError:
#         print("error 1")
#     except TypeError:
#         print("handled")
#     break
# #we can give only one one solution for 1st error
# a=12
# while a<=15:
#     print(a)
#     try:
#         a=a/0
#         a=a+"1"
#     except TypeError:
#         print("handled")
#     except ZeroDivisionError:
#         print("error 2")
#     break
# a=12
# while a<=15:
#     print(a)
#     try:
#         a=a/0
#         a=a+"1"
#     except Exception:
#         print("handled")
#     except BaseException:
#         print("error 2")
#     break
# a=12
# while a<=15:
#     print(a)
#     try:
#         a=a/0
#         a=a+"1"
#     except TypeError:
#         print("handled")
#     except ZeroDivisionError:
#         print("error 2")
#     finally:
#         print("I'm finally")
#         break
# a=12
# while a<=15:
#     print(a)
#     try:
#         a=a/0
#         a=a+"1"
#     except TypeError:
#         print("handled")
# 
#     finally:
#         print("I'm finally")
#         break
# 
# print(10)
# try:
#     print(10)
# except TypeError:
#     print("error 2")
# else:
#     print("i am else")
# finally:
#     print("I'm finally")
#         
# try:
#     print(54/0)
#     try:
#         print(10+"1")
#     except TypeError:
#         print("i'm inner except")
#     finally:
#         print("I'm in inner finnaly")
# except Exception as m:
#     print("i'm outer exception")
#     print(m)
# finally:
#     print("i'm outer finally")

# empid=1235
# if empid==1234:
#     print('valid id')
# else:
#     try:
#         raise ValueError
#     except ValueError:
#         print("handled")
# class EmployeeIdNotFoundError(Exception):
#     msg="Employee not present"
# 
# empdid=12345
# if empid==1234:
#     print("valid id")
# else:
#     try:
#         raise EmployeeIdNotFoundError
#     except EmployeeIdNotFoundError as m:
#         print("handled")
#         print(m.msg)














