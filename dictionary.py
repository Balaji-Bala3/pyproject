# # Q1 Create a Dictionary with the below key , values and find the length of  it
# d={100:'java',200:'sql',300:'oops',400:'Sql',500:'oracle',600:'DB',100:'selenium',500:'psql',400:'Hadoop'}
# print(len(d))
# print(type(d))
# print(d)
# 
# d={'vel':'Selenium','Ganesh':'framework','Dinesh':'oracle','Vengat':'python','subash':'jira'}
# print(len(d))
# print(type(d))
# print(d)
# 
# # Q2 Create a Dictionary  with the below key and values and get(print) the values only in the Dictionary 
# d={'a':10,'b':20,'c':30,'d':40,'e':50}
# print(d.get('a'))
# print(d.values())
# 
# d={10:10+10j,20:20+2j,30:30+3j,40:40+4j,50:50+5j,60:60+6j,10:10+10j,50:50+5j,40:40+4j}
# print(d.get(50))
# print(d.values())
# # Q3 Create a Dictionary  with the below key and values and get(print) the keys only in the Dictionary
# d={'a':10,'b':20,'c':30,'d':40,'e':50}
# print(d.keys())
# k=d.keys()
# print(type(k))

# Q4 Create a Dictionary  with the below key and values and iterate
# d={10:101,20:202,30:303,40:404,50:505,60:606,10:101,50:505,40:404}
# for i in d:
#     print(i)
# for i in d.items():
#     print(i)
# d={ 'vel':'Selenium','Ganesh':'framework','Dinesh':'oracle','Vengat':'python','subash':'jira'}
# for i in d:
#     print(i)
# for i in d.items():
#     print(i)
# 
# # Q5 Add a key and value pair [10:sql] at the last position of Dictionary
# d={10:'python',20:'selenium',30:'java',40:'c',50:'c++',60:'oracle'}
# d[10]='sql'
# print(d)
# 
# d={55.56:60,98.65:50,35.09:40,46.90:30,67.450:20,25.89:10}
# d[100]=30
# print(d)
# 
# # Q6 Create a Dictionary with below key and Value  and Remove the key [50]
# d={10:100,20:200,30:300,40:404,50:500,60:600}
# p=d.pop(50) 
# print(p)
# print(d)
# #  Remove the key and value[10.9:python] pair
# d={10.9:'python',20.1:'selenium',30.2:'java',40.3:'c',50.4:'c++',60.5:'oracle'}
# p= d.pop(10.9)
# print(d)
# print(p)
# 
# # Q7 Create a Dictionary with below key and Value and Add the value(900) using " Slice " operator
# d={10:100,20:200,30:300,40:404,50:500,60:600}
# d[70]=900
# print(d)

# Q8 print all value in list
# l=[{'id':10,'name':'vel','email':'vel@gmail.com'},{'id':20,'name':'nisha','email':'nisha@gmail.com'},{'id':30,'name':'bala','email':'bala@gmail.com'}]
# for i in l:
#     for j in i.values():
#         print(j)
# # Q9 print all value in tuple
# t=([10,'vel','vel@gmail.com'],[20,'nisha','nisha@gmail.com'],[30,'bala','bala@gmail.com'])
# for i in t:
#     for j in i:
#         print(j)
#  
# t=((10,'vel','vel@gmail.com'),(20,'nisha','nisha@gmail.com'),(30,'bala','bala@gmail.com'))
# for i in t:
#     print(i)

































