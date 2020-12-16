# # Q1 Create a new set with values and find the length of it
# s={10,20,30,90,10,10,40,50}
# print(len(s))
# print(s)
# s={'python','selenium','sql','java'}
# print(len(s))
# print(s)
# s={10,20,30,90,10,10,40,50,'python','java',22.4,True,2+5j}
# print(len(s))
# print(type(s))
# print(s)
# 
# # Q2 Find the maximum value in set
# s={ 10,20,30,90,10,10,40,50,10 }
# print(max(s))
# print(min(s))
# 
# # Q3 Update set by following data {100,200,500} 
# # s={10,20,30,40,50,60}
# # s.update(100,200,300)
# # print(s)  ----------------not iterable
# 
# # Q4 Update set by following data ['java','sql']
# s={100,200,300,400,500,600,700}
# s.update('java','sql')
# print(s)
# 
# # Q4.1 Update set by following data ['greens']
# s={105,205,305,405,505,605,705,805}
# s.update("greens")
# print(s)

# Q4.3 Update set by following data (100,200,500) 
# s={105,205,305,405,505,605,705,805}
# g={100,200,500}
# s.update(g)
# print(s)
# print(g)
# 
# # Q4.4 Update set by following data ('j'+'greens') 
# s={105,205,305,405,505,605,705,805}
# s.update('j''+','greens')
# print(s)
# 
# # Q5 Convert string into set
# s='python'
# print(set(s))
# 
# # Q5.1 Convert list into set
# l=['java','python',20,10,60]
# print(set(l))
# 
# # Q5.2 Convert tuple into set
# t=(105,205,305,405,505,605,705,805,'java','python',20,10,60)
# print(set(t))
# 
# # Q6 To check weather value 200 is present or not in set
# s={ 105,205,305,405,505,605,705,805}
# print(200 in s)

# Q6.3 Create a set with values and compare the another set
# s1={10,20,30,40,50,60}
# s2={10,20,30,40,50,60}
# print(s1==s2)
# 
# s1={10,20,30,40,50,60}
# s2={60,20,30,40,50,10}
# print(s1==s2)
# 
# # Q7 Get the each value of set by using  for loop
# s={105,205,305,405,505,605,705,805}
# for i in s:
#     print(i)
# 
# # Q7.2 Get the each value of set by using  Enumarate for loop
# s={105,205,305,405,505,605,705,805}
# for i in enumerate(s):
#     print(i)
# 
# # Q8 Create a set with values and perform union between two set
# s={10,20,30,40,50,60}
# s1={60,80,90,40,50,10}
# print(s.union(s1))
# print(s | s1)
# 
# # Q8.1 Create a set with values and perform intersection between two Set
# s1={10,20,30,40,50,60}
# s2={60,80,90,40,50,10}
# print(s1.intersection(s2))
# print(s1 & s2)

# Q9 Create a set with values and perform difference between two list
# s={10,20,30,40,50,60}
# s1={60,80,90,40,50,10}
# print(s.difference(s1))
# print(s-s1)
# 
# # Q9 Create a set with values and perform symmetric_difference between two Set
# s={10,20,30,40,50,60}
# s1={60,80,90,40,50,10}
# print(s.symmetric_difference(s1))
# print(s^s1)



















