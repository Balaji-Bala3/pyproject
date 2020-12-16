# # Q1 Create a new list with values and find the length of it
# l = [10,20,30,90,10,10,40,50]
# print(l)
# print(type(l))
# print(len(l))
# # 
# # # Q2  Create a new list with values and find the length of it
# l=[105,205,305,405,505,605,705,805]
# print(len(l))
# # 
# # # Q3 Create a new list with values and find the length of it
# l=['Java','Python','Selenium','java',10,20,10]
# print(len(l))
# 
# # Q4.1  Get the  index value of 10 
# l=[10,20,30,90,10,50]
# print(l[0])
# print(l[4])
# print(l[5])
# 
# #Q4.7 Add a value [100,200,300] at the last position of list and find index value of 200
# l=[10,20,30,90,10,10,40,50]
# l.append([100,200,300])
# print(l)
# 
# # Q4.8 Add a value [100,200,300] at the last position of list and find index value of 200
# l=[10,20,30,90,10,10,40,50,100,200,300]
# l.append([100,200,300])
# print(l)

# Q5.1  Get the value present at 2nd index
# l=[10,20,30,40,50,60]
# print(l[2])
# l=[100,200,300,400,500,600,700]
# print(l[4])
# l=[105,205,305,405,505,605,705,805]
# print(l[-2])
# l=[105,205,305,405,505,605,705,805]
# print(l[-10]) ----------IndexError

# Q6  Remove the value present at 2nd index and print the removed value
# a=[10,20,30,40,50,60]
# a.remove(20)
# print(a)
# 
# l=[10,20,30,90,10,10,40]
# l.remove(40)
# print(l)
# 
# l=[10,20,30,90,10,10,40]
# l.remove(10)
# print(l)
# 
# l=[10,20,30,90,10,10,40]
# l.remove(40)
# print(l)
# 
# l=[10,20,30,90,10,10,40,60,80,100]
# l.remove(80)
# print(l)
# 
# l=[10,20,30,90,10,10,40,60,80,100]
# l.remove(50)
# print(l)

# Q6.8 delete the value  present in (-5th to -1st) index in the list
# l=[10,20,30,90,10,10,40,60,80,100]
# del l[-5:-1]
# print(l)
# 
# # Q6.9 delete the value  present in (2nd to last) index in the list
# l=[10,20,30,90,10,10,40,60,80,100]
# del l[2:9]
# print(l)
# 
# # Q6.9 clear all the value  present in the list 
# l=[10,20,30,90,10,10,40,60,80,100]
# l.clear()
# print(l)
# 
# # Q7 Replace the value 300 into 350 in the list
# l=[100,200,300,400,500,600,700]
# l[2]=350
# print(l)
# 
# # Q7.1 Replace the value present in 7th index as 90 
# l=[10,20,30,90,10,10,40,50,10]
# l[7]=90
# print(l)
# 
# # Q7.2  Replace the 10 into 100 in List
# l=[10,20,30,90,10,10,40,50,30]
# l[0]=100
# print(l)

# Q8 Add a value 50 in the 2nd index and display the list after adding.
# l=[10,20,30,90,10,10,40,50]
# l.insert(2,50)
# print(l)
# 
# # Q8.1 Add a value 70 at the end of the list
# l=[10,20,30,90,10,10,40,50]
# l.append([70])
# print(l)
# # Q8.2 Add a value 80 at the 30th index of list
# l=[10,20,30,90,10,10,40,50]
# # l[30]=80 ---------- IndexError
# 
# #Q8.3 Add a value 100 at the last index of 10 in the list
# l=[10,20,30,90,10,10,40,50]
# l.insert(10,100)
# print(l)
# 
#  #Q8.4 Add a value 100,200,300 at the last position of list
# l=[10,20,30,90,10,10,40,50]
# l.append([100,200,300])
# print(l)
# 
#  #Q10 Add a value [100,200,300] at the last position of list
# l=[10,20,30,90,10,10,40,50]
# l.append([100,200,300])
# l.append(20)
# print(l)
# print(l[9])

# Q10 count the 10 value present in the list
# l=[10,20,30,90,10,10,40,50]
# print(l.count(10))
# l=[10,20,30,90,10,10,40,50]
# print(max(l))
# print(min(l))
# l=['java','python','selenium','Java','Python','Selenium']
# print(max(l))
# print(min(l))
# 
# # Q11 Reverse the values present in list
# l=[10,20,30,50,90,40,100,60,10,70]
# l.sort(reverse=True)
# print(l)
# 
# #Q11.2 Sort the values (Ascending &Descending ) order present in list
# l=[10,20,30,50,90,40,100,60,10,70]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# 
# #Q12 Copy the values in list
# l=[10,20,30,90,10,10,40,50]
# c=l.copy()
# print(l)
# 
# # Q12.1 Create a lists with values and compare the two list
# l=[10,20,30,90,10,10,40,50]
# l1=[30,40,50,60,80]
# print(l==l1)

#q13 Get the each value of list by using  Enumarate for loop
# l=[105,205,305,405,505,605,705,805]
# for i in enumerate(l):
#     print(i)
# 
# l=[105,205,305,405,505,605,705,805]
# for i in range(0,len(l)):
#  print(l[i])

#  Get the each value of list by using  Enumarate for loop and print only odd index value
# l=[105,205,305,405,505,605,705,805]
# for i in enumerate(1,7,2):
#     print(l[i])
# for i in enumerate(l):
#      print(i)

    
    




