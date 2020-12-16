# Q1 Create a new tuple with values and find the length of it
# t=(10,20,30,90,10,10,40,50)
# print(len(t))
# 
# # Q1.2 Create a new tuple with values and find the length of it
# t=('python','selenium','sql','java')
# print(len(t))
#  
# t=(10,20,30,90,10,10,40,50,'python' ,'java ',22.4,True)
# print(len(t))
# 
# # Q2 Get the first index value of 10 
# t=(10,20,30,90,10,10,40,50)
# print(t.index(10))
# 
# # Q2.2  Get the last index value of 10 
# t=(10,20,30,90,10,10,40,50)
# print(t.index(10,5,len(t)))
# 
# # Q2.3 Get the index value of 50 
# t=(10,20,30,90,10,10,40,50)
# print(t.index(50))
# 
# # Q2.4 Get the index value of 200 
# t=(10,20,30,90,10,10,40,50)
# # print(t.index(200)) ----------ValueError
# 
# #Q2.5  Get the each index value of 10 present in below tuple
# t=(10,20,30,90,10,10,40,50)
# print(t.index(10,0,7))
# print(t.index(10,1,7))
# print(t.index(10,5,7))

# Q3 Get the value present at 2nd index
# t=(10,20,30,40,50,60)
# print(t[2])
# 
# # Q3.1 Get the value present at 4th index
# t=(100,200,300,400,500,600,700)
# print(t[4])
#         
# # Q3.2 Get the value present at 12th index        
# t=(105,205,305,405,505,605,705,805)
# # print(t[12]) ------Index error       
#         
# # Q3.3 Get the value present at -3rd index        
# t=(105,205,305,405,505,605,705,805)        
# print(t[-3])        
#         
# # Q3.4 Get the value present at -8th index        
# t=(105,205,305,405,505,605,705,805)        
# print(t[-8])        
        
# Q4 Add a value 100 at the last position of tuple        
# t=(10,20,30,90,10,10,40,50)        
# t.append(100)        
# print(t) ------------- AttributeError
       
# Q5 Count the 10 value present in tuple       
# t=(10,20,30,90,10,10,40,50,10)
# print(t.count(10))
#         
# # Q5.2 Find the maximum value  in tuple        
# t=(10,20,30,90,10,10,40,50,10)        
# print(max(t))   
# print(min(t))
# 
# t=('python','selenium','sql'',java')
# print(max(t))
# print(min(t))
# 
# # Q6 Convert string into tuple
# a="python"
# print(tuple(a))
# 
# # Q6.2 Convert list into tuple
# l=['java','python',20,10,60]
# print(tuple(l))
# 
# # Q7 To check weather value 200 is present or not in tuple
# t=(105,205,305,405,505,605,705,805)
# print(200 in t)
# 
# # Q7.2To check weather value 505 is present or not in tuple
# t=(105,205,305,405,505,605,705,805)
# print(505 in t)

# Q7.3Create a tuples with values and compare the two tuple
# t=(10,20,30,40,50,60)
# t1=(10,20,30,40,50,60)
# print(t==t1)
# 
# # Q8 Get the each value of tuple by using  for loop
# t=(105,205,305,405,505,605,705,805)
# for a in range(0,len(t)):
#     print(t[a])
# 
# # Q8.1 Get the each value of tuple by using  Enumarate for loop
# t=(105,205,305,405,505,605,705,805)
# for a in enumerate(t):
#     print(a,"-------b")
# 
# # Q8.1 Get the each value of tuple by using  Enumarate for loop and print only even index value
# t=(105,205,305,405,505,605,705,805)

# l=print(t)
# if l%2==0:
#  for a in enumerate(l):
#     print(a)
# exit(0)












