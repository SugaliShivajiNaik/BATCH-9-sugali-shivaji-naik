# ! Eg:5
# Write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria:

#    cost prce (in Rs)                     tax
#    > 100000                              15 % + discount 6%
#    >50000 and  <= 100000                 10%
#    <= 50000                              5%

price = int(input("eenter the price:"))
amount = 0
if price>=100000:
    discount = price*(6/100)
    value = pric-discount
    amount=value*(15/100)
    print=value+tax
else:
    tax = price*(5/100)
    total = price+tax
print("the onroad cost of bike is :",total)

# ! ------> if elif els
# Eg:1
a = 7
b = 9
c = 3

if a>b and a>c:
    print("A is greater")
else b>a and b>c:
    print("B is greater")
else c>a and c>b:
    print("C is greater")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. above 80 - A
# Ask to enter marks and print the corresponding grade.

mark = int(input("Enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("fail")
    
# ! Eg:6
# ? accent the age of 4 peole and display the oldest one

# Eg:1
a = 9
b = 60
# if a>b:
#      print("A")
# else:
#     print("B")
# ? ---> using shart hand if else
# * Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.) Always it have to end with else

# print("A") if a>b else print("B")

# ! code to check the given char is vowel or consonent
char = input("Enter the char: ")
# if char=="a" or char =='e' or char =='i' or char =='o' or char =='u':
#     print("is a vowel")
# else:
#    print("its consonent")

# ? or

# str1 = "aeiouAEIOU"
#if char in str1:
#     print("vowel)
# else:
#     print("consonnt")

# ! shorthand if else
char = input("Enter the char:")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")


# ! ---> elif ladder using short hand if else
a = 8
b = 5
c = 9

print("A is greater") if a>b and a>c else print("B is greater")
if b>a and b>c else print("C is greate")

# ! --------> looping


# looping can be imlimented using
# for loop
# while loop

# ---> for loop
# ? for loop is used for iteartion, if we know the number of times the loop have to run
# ? it is used to iterate the iterables eg(string, list, tuple, etc...)

# todo --> syntax for loop

# ! for syntax in c
# for(i=0;i<10;i++){
#     print("hello");
# }

# ! for syntax in python
# for userdefined_variable in range(start, end, step): default setp value is 1
#      statement
#      statement
#      statement

# ? Eg:1
# To print the value from 1 to 10 using for loop

# for i in range(0, 10): #(n, n-1)
#     # print(i)
#     print("hello")

# ? Eg:2
# for val in range(1, 15, 2):
#    print(val)
    
# for val in range(1, 15, 3):
#     print(val)

# ? Eg:3
# to decrement the value

#for val in range(10, 0, -1):
#    print(val)


#for val in range(10, 0, -2):
#    print(val)

#for val in range(10, 0, 1):
#    print(val) # no output

# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
for val in range(1, 10+1,):
   # print('7','x', val,'=',val*7) --> method:1

   # --> method:2
   # ans="7x"{}={}"
   # print(ans.format(val, val*7))

   # --> method:3
   print(f"7 x {val}={val*7}")


# ? Eg:5
# break  --> used to terminat the loop

#for val in range(1, 10):
#    if val ==6:
#        break
#    print(val)
    
    
# ? Eg:6
#for val in range(1, 10):
#    print(val)
#    if val ==6:
#       break

# ? Eg:7
#for val in range(1, 10):
#    if val ==6:
#    print(val)
#     break

# ! --------> while loop
# ? while is used when we do not know the number of times the loop to run
# ? to itrate the non iterable ekements while loop is used

# ! Eg:1
# to iterate nimber from 1 to 10

# i = 0
# while i<11:
#    print(i)
#    i=i+1 OR I+=1

# Eg:2
# to decrement using hile loop
# i=10
# while i>0:
#     print(i)
#     i-=1


# ! ----> 1-4+9-16+25=15
#n =int(input("enter number: "))
#for val in range(1, n+1):
#    sq=val*val
#    if val %2!=0:
#        sum=sum+sq
#    lse:
#        sum=sum-sq
# print(sum)

i = 0
for val in range(1, 6):
    i=val+i
    print(1)


# For loop practisee
# write a program to display sum of odd number and ven
# numbers that fall between
# 12 and 37(including both numbers)


# Assesment
#1.) cats and mouse:Hacker rank
#2.)print the factorla of 8 using for loop
#3.) write a program to display sum of odd numbers and even
numbers that fall betwen
# 12 and 37(including both number)
#4.) write code to pint the sum of number using while loop
#n1 = 

































































