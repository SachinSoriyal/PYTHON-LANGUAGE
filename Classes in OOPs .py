class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
        
        
acc1 = Account("12345","ABCDE")
print(acc1.acc_no)
print(acc1.acc_pass)


# private attributes  ( focus on the change in line 16 and compare it with above code)
# It(2nd code) shows error so when you run programme so comment out this first

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        

        
        
acc1 = Account("12345","ABCDE")
print(acc1.acc_no)
print(acc1.__acc_pass)


#  for reset pass 
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
        
    def reset_pass(self):
        print(self.__acc_pass)
        
        
acc1 = Account("12345","ABCDE")
print(acc1.acc_no)
print(acc1.reset_pass())


#  eg of private and public 
class Person:
    name = "sachin"
    
p1 = Person()
print(p1.name)


#  asusual we can private methods 
class Person:
    __name = "Sachin"
    
    def __hello(self):
        print("hello  person")
    
    def welcome(self):
        self.__hello()
        
p1 = Person()

print(p1.welcome())


#  eg of inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stoped.")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("Aqua")

print(car1.name)
print(car2.start())
print(car1.color)


  #  eg of inheritance  (multilevel inheritance)
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stoped.")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
        
car1 = Fortuner("diesel")
car1.start()
print(car1.type)



  #  eg of inheritance  (multiple level inheritance)
class A:
    varA = "welcome to class A"
class B:
    varB ="welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)


#  super method 
class Car:
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod 
    def stop():
        print("car stoped.")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()
        
car1 = ToyotaCar("prius","electric")
print(car1.type)


#  instance method 
class Person:
    name = "poonam"
    
    def changename(self,name):
        self.name = name
        
p1 = Person()
p1.changename("rishi shah")
print(p1.name)


#  for above method when we use class method
class Person:
    name = "sachin"
    
    @classmethod 
    def changename(cls,name):
        cls.name = name
        
p1 = Person()
p1.changename("amandeep")
print(p1.name)
print(Person.name)


# property decorator
class Student:
    def __init__(self,phy,chy,math):
        self.phy = phy
        self.chy = chy 
        self.math = math
        self.percentage = str((self.phy + self.chy + self.math)/3)+"%"
        
stu1 = Student(90,98,97)
print(stu1.percentage)


# now i realised that i want to chamge the marks of phy 
class Student:
    def __init__(self,phy,chy,math):
        self.phy = phy
        self.chy = chy 
        self.math = math
        self.percentage = str((self.phy + self.chy + self.math)/3)+"%"
        
stu1 = Student(90,98,97)
print(stu1.percentage)

stu1.phy = 99
print(stu1.phy)
print(stu1.percentage)


#  now no. is easily change but  percentage is still remains unchanged so solve it
class Student:
    def __init__(self,phy,chy,math):
        self.phy = phy
        self.chy = chy 
        self.math = math
        self.percentage = str((self.phy + self.chy + self.math)/3)+"%"
        
    def calcpercentage(self):
        self.percentage = str((self.phy + self.chy + self.math)/3)+"%"
        
stu1 = Student(90,98,97)
print(stu1.percentage)

stu1.phy = 99
print(stu1.phy)

stu1.calcpercentage()
print(stu1.percentage)


# property method
class Person:
    def __init__(self,phy,chy,math):
        self.phy = phy
        self.chy = chy
        self.math = math
        
        
    @property
    def percentage(self):
        return str((self.phy + self.chy + self.math)/3)+"%"
        
stu1 = Person(90,98,97)
print(stu1.percentage)

stu1.phy = 99
print(stu1.percentage)


# polymorphism  (operator overloading)
print(1+2)
print(type(1))

print("sachin"+"singh")
print(type("sachin"))

print([1,2,3]+[4,5,6])
print(type([1,2,3]))


#  complex no. 
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
        
num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(3,4)
num2.showNumber()


#  using of  dunder functions and logic for addition of two complex number
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
        
    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
        
        
num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(3,4)
num2.showNumber()

num3 = num1.add(num2) 
num3.showNumber()
