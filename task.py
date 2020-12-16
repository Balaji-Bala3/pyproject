#fabinocci series:
# def fabi(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:    
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
#  
# fabi(10)
# 
# def fabi(n):
#     a=0
#     b=1    
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         if c<100:
#             print(c)
# fabi(100)
# Function to print all Quadruplet present in a list with given sum
# def quadTuple(A, sum):
# 
#     # sort the list in ascending order
#     A.sort()
#     print(A)
#     # check if Quadruplet is formed by A[i], A[j] and a pair from
#     # sublist A[j+1..n)
#     for i in range(len(A) - 3):
#         for j in range(i + 1, len(A) - 2):
# 
#             # k stores remaining sum
#             k = sum - (A[i] + A[j])
# 
#             # check for sum k in sublist A[j+1..n)
#             low = j + 1
#             high = len(A) - 1
# 
#             while low < high:
#                 if A[low] + A[high] < k:
#                     low = low + 1
#                 elif A[low] + A[high] > k:
#                     high = high - 1
#                 # Quadruplet with given sum found
#                 else:
#                     print((A[i], A[j], A[low], A[high]))
#                     (low, high) = (low + 1, high - 1)
# 
# 
# if __name__ == '__main__':
# 
#     A = [2, 7, 4, 5, 9, 5, 1, 3]
#     sum = 20
# 
#     quadTuple(A, sum)
#     
# # Function to return the count of the required quadruplets 
# def countQuadruplets(P, Q, R, S, sum): 
#       
#     # To store the count of required quadruplets 
#     cnt = 0
#       
#     # Using four loops generate all possible quadruplets 
#     for elem1 in P: 
#         for elem2 in Q: 
#             for elem3 in R: 
#                 for elem4 in S: 
#                     if elem1 + elem2 + elem3 + elem4 == sum: 
#                         cnt = cnt + 1
#     return cnt 
#   
# # Driver code 
# P = [ 0, 2] 
# Q = [-1, -2] 
# R = [2, 1] 
# S = [ 2, -1] 
# sum = 0
#   
# print(countQuadruplets(P, Q, R, S, sum)) 

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# l=(int(input(("enter the number : " ))))
# u=(int(input(("enter the number : " ))))
# print('prime numbers are :')
# for num in range(1,u+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)

# for num in range(7+1):
#     if num>1:
#         for i in range(2,num):
#             if num%2==0:
#                 break
#         else:

#             print(num)

# bin(25)
# a=bin(11)
# print(hex(11))
# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     if i%2==0:
#         print(i)

