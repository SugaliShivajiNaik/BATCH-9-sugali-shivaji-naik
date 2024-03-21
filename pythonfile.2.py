# a, b, c = 9, 8, 7, 6,
# print(a, b, c)
#a, b=c=7,8
# print(a)
# print(b)
#print(c)

#a=b, c= 4,2
# print(a,b,c)

#----> swapping of variables
a= 7
b=5

temp =a #temp =7
a=b #a=5
b=temp #b=7

# a=5, b=7
print(a, b)

# Eg:2
a=a+b  #a=12
b=a-b  #b=12-7=5
a=a-b #a=12-5=7

# print(a, b)

# a, b=b, a# only in python
# print(, b)

a=a*b #a=35
b=a/b  #bn=35/7 = 5.0
a=a/b  #a=35/5 = 7.0
print(int(a), int(b))

# id()  ----> used ti fimthe memory address of the variables
# a = 7
# b = 8
# print(id(a))
# print(id(b))

#-----> keywords
 # keywords are reserved works which provides special meaning to
 # compiler or interpretor

 # import keyword
 # print(keyword.kwlist)
 # print(type(keyword.kwlist))
 # print(type(keyword.kwlist))


 # To check if the string is keyword or not
 #print(keyword.iskeyword("sid")) # False


# !-----> Literals
Literal is the onstant value assigned to a variabls
# A variables is considers to be constant when it is defines
# in caps

a= 78 # a is variable
# A=78 # A is constant

# hash() --> it creates a hash value for constant datatypes and
 provides rror for non constant datatypes
n1 = 89+7j
print(hash(n1))

f1 = [7, 8, 9]
print(hash(f1)) # error  --> list s non-constant or mutual dadatype

# a = 9
# b = 9
# b = 90
# print(id(a))
# print(id(b))

# ! ----> Operators
# ? Operators are symbols which is used to perform various opearions
# ? between 2 or more operands

# arithmetic
# Logial
# Relational or comparison
# Bitwise
# Identity
# Mmbership

#  * ---> Arithmetic  --> +, -, *, /, %, //, **
# Eg:1
# a = 8
# b = 6
# c = 9
# print (a+b+c)

# input() --> used to get the runtime input
n1 = input("Enter the value: ")
print(typ(n1))


a = 4
b = 2
print(a/b) # is sd to get the quotient value
print(a%b) # is used to get rmainder value

# ! // --> floor division

# a = 765433
# b = 19
# print(a/b) # -. the output will be inn integer & the output will be
#based on floor value

#!  ** --> used for power of a number
#print(2**4) # --> 16

# ! Assignment --> +-=, -=, /=, *=, //=, **=, &=, |=


# a= 8
# a+=2
# print(a)

#a=30
# a-=5
# print(a)

# ! comparison --> ==, >, <, !=, ,<=, >=
# a = 8
# b = 7
# print(a>b) # True

# a = 9
# b = 5
# print(a==)

# ! Bitwise operator --> &, |, ^, ~, <<, >>
a = 7
b = 6
print(a|b)


# AND
# A B  A&B
# 0 0  0
# 0 1  0
# 1 0  0
# 1 1  1

# OR
# A B  A*B
# 0 0  0
# 1 0  1
# 0 1  1
# 1 1  0
# XOR
# A B  A|B
# 0 0  0
# 0 1  1
# 1 0  1
# 1 1  0

# 32 16 8 4 2 1 
# 0  0  1  0 1 0  # --> 10
# 1  0  0  1 1 0 ^ # -->
# -----------
# 1     1   1

# 2^4 2^3 2^2 2^1 2^0
# 8     4    2   1

# 0     1    1   1   # -->7
# 0     1    0   0   # --> 6 &
# ----------------------
# 0     1     0    0
# 0

# ~ --->
# a = 9
# print(~a+1)

# a = 9

# 128 64 32 16 8 4 2 1
# 0    0  0  0 1 0 0 1 # --> 9

# 1    1  1  1 0 1 1 0 # --> -10

# 0 0 0 0 1  0 10 --> 10

# 1 1 1 1 0 1 0 1  -> 1s compliment of 10
              # 1  -> 2s compli, ent
# -------------------------
#  1 1 1 1 0 1 1 0  --> -10

# 256 128 64 32 16 8 4 2 1
#  0   0   0  0  0 0 1 0 1  3>
#  0   0   0  1  0 1 0 0 0 --> 40
# 107

# <<, >>
print(5<<1)
# 16>4

# ! Logicl --> usd to compare the expressions
# and, or, not
a = 6
# print(a>3 and a<10)
# print(a>7 or a<10)
print(not(a>8 and a<10))

# ! Idntity operator

# ? are stored

# is, is not
a = 8
b = 8
print(a is b)
print(a==b)

a =(1, 2, 3)
b =(1, 2, 3)
print(a is b)

# ! Memberhip operator
# in, not in

11 = [7, 8, 9 , 0,6, 5]
num = 55
print(num in 11)
# print(num not in 11)

num = 678
print(8 in num) # rror

# ! conditional statement
# if, elif, else

# eg:1
# --> c syntax
if (condition){
#   statement;
#   statement;
#   statement;
#}
# pthon syntax
# if condoition:
#   statement
#   statement
#   statement
# statement

# eg:1
# a=6
# if a:
#    print("hello")
    
# eg:2
#a = 6
#if a>3:
#    print("hey")
#else:
#    print("no")

# eg:4
# a = 0
# a = none
# a =false
# a=""
# if a:
#    print("yes")
# else:
#    print("no")


# a number is even or odd
n = int(input("enter the number: "))
if n %2==0:
    print(n, "is even")
else:
    print(n, "is odd")

# sum:2
# name, age, nationality
# 18 above, Indian


name = input("Enter the name:")
age = int(input("enter the age:")
nationality=input("enter the nation;")

if age>=18 and nationality=="Indian":
   print("eligible for vote")
else:
    print("not eligible")



















