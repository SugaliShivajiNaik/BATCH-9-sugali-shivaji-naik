# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings
# s1 = "Hello how are you"
# s2 = "Hello how is"

s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

# 3.)Wrire a code print the 8th fibanochi number
0, 1, 1, 2, 3, 5, 8

n1 = 0
n2 = 1
# ans = 0+1 ==> 1

n1 = 1
n2 = 1
# ans = 1+1 ==> 2

n1 = 1
n2 = 2
# ans = 1+2==> 3

n1 = 2
n2 = 3
# ans = 2+3 ==> 5

# ! find the 8th fibanochi number
num = 8
n1 = 0
n2 = 1

for val in range(5):
    ans = n1+n2
    print(ans)
    n1 = n2
    n2 = ans
print(ans)

# ! constructors
# ? Eg:2

class profile:
    def __init__(self):
        print("hello world")

obj = profile()
obj.__init__()

# ? Eg:3
# * parameterised constructor
class profile:
    def__init__(self, id, name, age):
        print(id, name, age)

obj = profile(1, "sid", 29)

# ? Eg:4
class c1:
    email = "sid@gmail.com"
   
    def m1(self):
        name = "sid"
        place = "cbe"
        print(name, place)
        print(slf.email)

object = c1()
object.m1()

# ? Eg:5
class c1:
    def m1(self):
        name = "sid"
        age =28
        return name, age
    def display(self):
       # ! print(name, age)
       # ! print(self.name, self.age)
       print(self.m1())
        
object = c1()
object.display()


# ? Eg:6
# ? to use the variable inside the constructor in another methods 
class class1:
  # email = "sid@gmail.com"      #static variable
   def__init__(self):
       self.name = "sid"          #instance variable
       self.email = "sid@gmail.com"     
       # return name, email # error --> cannot use return with constructor

    def display(self): # instance method
        print(self.name, self.email)


c1 = class1()
c1.display()

# ! --------> inheritance
the process of utilising the methods and attributes of parent class
throught the object of child class it is called as inheritance

# ? 5 types of inheritance
single inheritance
multilevel inheritance
multiple inheritance
hybrid inheritance
heirarichal inheritance

single inheritance

# * single inheritance
# ? it has only one parent class and only one child class
# ! Eg:!
class parent:
    def m1(self):
        print("iam parent class")

class child:
    def m2(self):
        print("iam child class")

p = parent()
p.m2()

obj1 = child()
obj.m1()

# ! Eg:2
class c1:
    def __init__(self):
        print("iam constructor from parent class")

class child1(c1):
    pass

obj = child1()

    
# ! Eg:3
class parent:
    name = "sidhu"

class child(parent):
    name = "name1"

    def display(self:
        print(self.name)
                
d = child()
d.display() 

# ! multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")


class voice:
    def dog_voice(self):
        print("bark")

class voice:
    def cat_voice(self):
        print("meow")

class voice:
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

# ? Eg:2
class honda_city:
    def honda_city_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)
        
    def honda_city__engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)

class amaze(honda_city):
    def amaze_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)


    def amaze_body_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

class civic(amaze):
    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)


class Honda(civic):
    pass

honda = Honda()
honda.honda_city_engin_specs(1500, 230, 2979, "petrol" 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")

# ! multiple inheritance
# ? it has multiple parent and 1 child

class while_petrol:
    def function1_w(self):
        print("used to airplans")

class organic_petrol:
    def function_o(self):
        print("used for bike, cars")

class premium_petrol:
    def function_p(self):
        print("used for bike, cars")

class petrol(while_Petrol, organic_petrol, premium_petrol):
    def defanition(self):
        print("petrols types")

p = petrol()
p.defanition()
p.function_O()

# ! Eg:2
# MRO --> Method resolution order
class addition:
    def add(self, a, b):
        print(a+b)

    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subtract, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc,mul(4, 2)

# ! heirarical inheritance
# ? The one parent classe will asct as parent for all the child classes
class catagory:
    def cat_name(self, weight):
        print("weight")

      def display(self, color, taste):
          print(color, taste)
           
class tomato(catagory):
    def tomato_specs(self):
        color "black"
        taste = "neutral taste"
        self.display(color, taste)

class carrot(catagory):
    def carrot_specs(self):
        color ="green"
        taste = "sweet"


c = carrot()
c.carrot_specs()
c.weight("30gms")

t = Tomato()
t,tomato_specs()
t,weight("20gms")

# ! hybrid inheritance
# ? The combination of above 4 inheritance is called hybrid inheritance
class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class3")

class c4(c3):
    def m4(self):
        print("class4")

    def m3(self):
        print("iam m3 from c4")
        
class c5(c4):
    def m4(self):
        print("class4")
        
class c6(c5, c3):
    def m6(self):
        print("class4")
obj = c6()
obj.m3()

# ! -------------> polymorphism



# * polymorphism in operators
# +
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

# *
print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)


polymorphism in classes
we can achieve polymorphism in 2 ways
1.) method overloading --> it is not possible in python
2.) method overriding

tasks
write the code for the below tasks using function
1.)d1 = {"shirt": 1000, "pant":1500, "shoes": "900", "handkey": 30}
a.) find the min ans max priced product
b.) find the product starts with 's' and 's'

2.) find the n = 67, is strong number or not

3.) l1 = [1,2,3,4,5,6]
n=2 --> [5, 6, 1,2,3,4]
n=3 --> [4,5,6, 1,2,3]
    
              




























    
