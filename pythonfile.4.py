'''
# ----->whil loop
# ------> break using while loop

# eg:1
# 1.) Iterate from 20 to 30 and break the loop in 27

#i = 20
while i< 31:
    if i ==27:
        break
    print(i)
    i+=1

# 2.)
#i = 20
#while i<31:
#    print(i
#     i+=1
#    if i==27:
#      break


# 3.)
#i = 20
#while i<31:
#    print(i)
#    if i==27:
#      break
#      i+=1


# i = 20
# while i<31:
#     print(i)
#     if i==27:
#       break
#       i+=1

# ! -----> continue
# ---> Eg:1
# i = 20
# while i<31:
#     if i==27:
#         continue
#     print(i)
#     i=i+1


# i = 20
# while i<31:
#     i=i+1
#     if i==27:
#         continue
#     print(i)


# ! Eg:5
# while o iterate from 12 to 22
# find the sum of all numbers

# i = 12
# sum=0
 while i i<23
    sum=0
    sum=sum+i
    i+=1
 print(sum)

 ! Eg:6
 Find the average of value from 20 to 25
# i =  20
# sum = 0
# while i<=25
#      sum = sum+i
#      count+=1
#      i+=1
# print(sum/count)

# !  -------> Nested for loop
# Eg:1

# for row in ramge(1, 3+1):
#     for j in range(1, 4+1):
#       print(row, col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

row = int(inputt("Enter the rows: "))
cols = int(input("enter the cols: "))

#for ow in range(rows):
#    forb col in range(cols):
#        print("*", end=" ")
#     print()

sum = 0
#or ow in range(5):
#    forb col in range(5):
#        print("*", end=" ")
#     print()


#! to print start in right angled triangle


for row in range(0, 6):
    for col in range(0, row):
        print("*", end=" ")
    print()

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for row in range(6, 0, -1):
#    for col in range (0, row):
#        print("*", end=" ")
#    print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# for row in range(5):
#    for col in range(5):
#        if col==0 or col==5-1 or row ==0 or row ==5-1#print("*", end=" ")
#        else:
#            print(" ", end=" ")
#     print()

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *


for row in range(0, 5):
    for col in range(0, 6):
        if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col<=4) or
                                                                      (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# *
# * *
# *   *
# *     *
# *       *
# * * * * * *


#  -------->list

# ---> Datatypes
# primary

# number ---> int, float complex
# string
# Boolen 
# none

# collection
# list
# tuple
# set
# dictionary

# ? ----> list

# 1.) if the collection of element of elements are sorrounded by square brackets, it is considered
# to be list
# ! Eg:
   # 11 = [4, 7, 9, 89, "hello", 7+9j, [8, 9, 0]]

# * charactristics of list
# 1.) list have to be sorrounded by []
# 2.) it is mutable (the elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) it can hold duplicate values
# 6.) its heterogeneous


;//,,,,
# to access the elements in list
11 = [1, 4, 1, 7, 89, 7, 7.5, "p", "i"]
# print(11)

# ---> Indexing 
# in the collection datatypes like list, tuple, string, the elements will be alloted
# with pre-defined unique value called inedx value

# we have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand


# ? --> positive indexing
# lst1 = [1, 4, 1, 7, 89, 7, 7.5, "p", "i"]
# print(lst[0])
# print(lst[4])



# ? --> negative indexing
lst1 = [1, 4, 1, 7, 89, 7, 7.5, "p", "i"]
print(lst1[-1])
print(lst1[-5])


# ? ---> slicing
lst = [, 4, 1, 7, 89, 7, 7.5, "p", "i"]
# lst[start_index:end_index:step]


 print(lst1[0:4])
 print(lst1[6:8])
 print(lst1[3:6])
 print(lst1[:5])
 print(lst1[3:1])
 print(lst1[:])

# print(lst1[0:7:1])# lst1[0:7] --> both are same
# print(lst1[0:7:2])


# trail = int(input())

lst1 = [1, 4, 1, 7, 89, 7, 7.5, "p", "i"]
# print(lst1[-4:-1])
# print(lst1[-1,-4]) -->[]
# print(lst1[-7:-1])
# print(lst1[-7:-1:2])

# ! To insert ot add element inside list

# append() --> used to add element at last positino of list
# 11 = [9, 8, 0, 6]
# 11, appnd("car")
# print(11)

# n = int(input("Enter the number of inputs: "))
# for i in range (0, n):
#    a, b = list(map(int, input().split()))
#    print(a, b)




    



















