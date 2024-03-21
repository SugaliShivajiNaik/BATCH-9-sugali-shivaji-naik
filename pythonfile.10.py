# ! -----> tasks 
# write the code for the below tasks using function
# 1.)d1 = {"shirt": 1000, "pant":1500, "shoes": "900", "handkey": 30}

d1 = {"shirt": 1000, "part": 1500, "shoes": 900, "handkey": 30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    of d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswitch('s') or val.startswith('s'):
        print(val)




# a.) find the min ans max priced product
# b.) find the product starts with 's' and 's'

# 2.) find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5, 6, 1,2,3,4]
# n=3 --> [4,5,6, 1,2,3]
    
# polymorphiem in classes
# we can achieve polymorphism in 2 ways
# 1.) method overloading --> it is not possible un python
# 2.) method overriding

# ! method riding
# * polymorphism in classes using inheritance
# ? Eg:1
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

# ? Eg:2
class USA:
    def language(self):
        print("English")
        
    def capital(self):
        print("Washington DC")

class India(USA):
    def language(self):
        print("none")
        
    def capital(self):
        print("New delhi")

I = India()
I.language()
I.capital()

# Eg:3
# polymorphism using objects

# c1, c2 --> c1 = print(c1),ArithmeticError print(c2)
f1, f2


class c1:
    def f1(self):
        print("self 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

# obj1 = c2():
obj1.f1()

def display(a):
    a.f1()
display(obj1)
display(obj2)

# * changing the functionality of builtin functions
class shoping:
    def __init__(self, l1):
        self.items = (l1)

     def__len__(selflength = len(self.items)
         length = len(self.items)
         return length
s = shooping([1,2,3,4,5])
print(len(s))

# ! --> Method overloading
# ! Eg:1
class suming:
    def add(self, a, b):
        print(a+b+c)
        
    def add(self, a, b):
        print(a+b+c)
        
s = suming()
s.add(4, 3) # ! ----->error
s.add(4, 5, 1)


# Eg:2
class summing:
    def add(self, a=None, b=none, c=none):
        if a!=none and b!=None and c!=none:
            print(a+b+c)
        elif a!=none and b!=none:
            print(a+b)
        else:
            print(a)
obj = summing()
obj.add(2)
obj.add(3, 4)
obj.add(1,2,3)


# ! --------> Abstraction
the procss of hiding the implimentation details is abstraction

# ? Eg:1
from abc import abc,abstractmethod
class shaps(abc):
    @abstractmethod
    def sides(self):
        print('all shapes have sides except circle')
        
class triangle:
    def triangle_sides(self):
        print("3 sides")


class square(shapes):
    def square(self):
        print("4 sides")

tr = triangle()
tr.sides()



def decor(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()

@decor
def greet():
    return 'good morning'
print(greet)

class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam traingle")

   def sides (self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
        
tr triangle()
tr.traingle_sides()
tr.name()

# ! Rules to define abstract class1
1.) abract class cannot be instantiated
2.) from abc import abc, abstractmethod
3.) subclass the normal class with ABC
4.) convert the normal method inside the abstract class to abstract method
5.) all the child classes have to be subclassed with abstract class
6.) the abstract method should be present in the
child classes

# ! Eg:2
# * super() --> used to access the parent class method from class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmthod
    def m1(self):
        print("this is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("iam child 1")

    def m1(self):
        pass

class1 = c1()
class2.m2()

class2 = c2()
class.m2()

# *Eg:3
from abc import ABC, abstractmethod
class password:
    @abstractmethod
    def pwd(self):
    pswd = "sidd1994$"
    return pswd

class login(password):
    def valindate(self, name, passwrd):
        if super().pwd() ==passwrd
        print(name, password)
        print("Welcome", name,'!!')
    else:
        print("please check the password")

    def pwd(self):
        pass

login = login()
name = input("Enter the name: ")
pwd = input("Enter the password: ")
login.validate(name, pwd)

# ! Encapsulation
# * ---> Eg:1
class car:
    __name = "BMW" # private variable
    print(__name)

c1 = car()
print(c1.name) # error
c1.name = "Audi"
print(c1.name) # error

# * --->Eg:2
# ? Accessing private date outside the class
class c1:
    __phone = '7656567687'

    def display(self):
        print(self.__phone)
c = c1()
c.display()

# * ----> Eg:3
# ? declare private method
class class1:
    def __m1(self): # Private method
        print("Iam private method")

    def __init__(self):
        self.__m1()
c = class1()
c.__m1() # error

# ? nested class
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)
    obj1 = class2()

obj = class1()
obj.obj1.display()






a = 9
b = 6
print(a+b)
# print(a.__add__(b)) ? dunder method or mafic method

# int()
print(a.__sub__(b))
len()































