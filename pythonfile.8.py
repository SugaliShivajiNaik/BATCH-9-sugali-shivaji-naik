#
# ! Eg:4
# ? function with return statement

# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement

def f1():
    z = 8
f1()
print(z) # error --> cannot use outside the function

def f1(a, b):
    c = a*b
    return c
print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

e    print("not palindrome")
a = int(input("Enter the value: "))
palindrome(a)

# ? Based om the declaration of parameter and args
# ? functions are divided into 5 catagories

popsitional args
keyword args
default args
variable length args
keyword variable length args

# * positional args
#? the position of parameter above to be same as position as arguments
# Eg:1
def profile(name, phone, mark):
    txt = "my name is {}. my phone number is {}. i got {} marks."
    print(txt.format(name, phone, mark))


profile(name="sid", 123445567, mark=98,

# todo ---> Exception of keyword args function
def profile(name, phone, mark):
    txt= "my name is {}. my phone number is {}. i got {} mak."
    print(txt.format(name, phone, mark))

# profile(name="sid", 123445567, mark=98) # error -> positional args follow keywords
profile(123445567, name="sid",

profile("sid", 8767676767, "guntur")

# ! Eg:2
def profile(name,phone, plac="kadapa"):
    txt = "my name is {}. my phone number is {}. i am from {}."
    print(txt.format(name, phone, place))

profile"sid", 8767676767, "guntur")

Exception
 ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Sid",9876543210)

# * variable length params
# ! Eg:1

def profile(name):
    print("my name is",name)
profile("sid", "name2", "name3")


name = "sid", "name2", "name3"
def profile(*name):
    for val in name:
        print("my nam is", val)
profile("sid", "name2", "name3")

# ! Eg:2
def profile(*name, age):
    for val in name:
        print("my name is", val, "may age is", age)
profile("sid", 'name2', 'name3', 28) #error --> age has no args

def profile(age, *name):
    for val in name:
        print("my name is", val, "may age is", age)
profile(28, "sid", 'name2', 'name3')

# * keyword variable length args
kwargs --> which is used to provide the args in the form of key value pair
# ! Eg:1
def price(**price_list):
    print(price_list):

print(shirt=1000, iphone=80000)

n = 5
{1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter the number: "))

def diict1(n):
    d1 = {}
    for val in range(1, n+):
        d1[val] = val**2
    print(d1)
dict1(5)

# ! --------> object oriented programming
the paradigms of objects oriented programming are

class
objects
inheritance
polymorphism
abstraction
encapsulation

# ! class is a blue print of an object

l1 = [1,2,3,4,5,6]

# ? Eg:1
class c1:
    name1 ="sidhu"
    rint(name1)



# ? Eg:2
class person:
    name = "sidhu"

    c = person() # c os object
    the process of cration of an object is called as instantiation 
    print(c.name)

# ? Eg:3
create of a method
when the function is created with a class is called as method

class person:
    def display(person):# it is a method
        print("Hello welcome to classes")

p = person()
p.display()

# ? Eg:4
# ! method with parameter
class person:
    def display(person, name, age):
        print(name, age)

p = person()
p.display("sidhu", 28)

# ! Eg:5
class person1:
    name = "sidhu" # attribute or static variable
    iname = "t"

    def first_name(self):
        print(self.fname)

    def full_name(self):
        print(self.fname+" "+self.iname)

p = person1()
p.first_name()
p.full_name()


# ? Eg:6
constructors -->__int__()
this is a special method which has th ability to execute iotself without
calling it manually theorugh the process of instantiation

class profile:
    def__ init__(self): # constructor method
        print("hey")

p = profile() #xecution of constructor through this process


d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)









''''
1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number







































