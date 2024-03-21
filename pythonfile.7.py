'''''
2.) python program to determin if
the given sets are disjoint
or not without using inbuilt-in functions

set1 = {'python', 'java','data science'}
set2 = {'ML', 'AL', 'R Language', 'python'}
set3 = {'data analytics', 'Robtics', 'dep learning'}
c = 0
flag=0
for val in range(3):
    c=c+1
    if c==1:
     for val in set1:
        if val in set2 or val in set3:
            flag=1
            break
        
  if c ==2:
     for val in set2:
        if val in set1 or val in set3:
             flag=2
             break
        
  if c==3:
     for val in set3:
        if val in set2 or val in set1:
               flag=3
               break
            

if flag==0:
    print("disjoint")
else:
    print("joint")



3.)
list1 = ["M", 'name', 'is', 'kelly']
list2 = ['y', 'me', 's', 'lly']

l3 = []
for val in range(len(list1)):
    ans = list1[val]+list2[val]
    l3.append(ans)
print(l3)

i =
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)

Hacker rank --> casar cipher



# o/p --> ['My', 'name', 'is', 'kelly']

# ! or
c = 0
for val in set1, set2:
    c=c+1
    if c==1:
        

# i=0
while i<len(list1):
    l3.append(list1[i]+list[i])
    i+=1
print(l3)




# ! Functions
#? DEF
Function is a block of code which is used to perform a spcific functionality
function can be created using def keyword

# ? generally function declaration
# ? Function has 3 parts
function declaration
function defanition
function call

# ! Eg:1
def greet():  +function defanition
    print("greetings user !!")

greet()
greet()
greet()
greet()
greet()
greet()
greet() # function calling


# ! Eg:2
def adding():
    a = 8
    b = 6
    c = 5
    d =a+b+c
    print(d)
adding()
adding()

# ! Eg:2
# ? function with parameter
def greeting(name):
    print("welcome", name)

for val in range(3):
    username = input("Enter the name: ")
    greeting(username) # username is argument
    
''''
# ! Eg:3
def profile(name, age, place):
    print(name, age, place)
profile("sid", 29, "cbe")


 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number






















