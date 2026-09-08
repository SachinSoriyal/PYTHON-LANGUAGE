# #  OOP(object oriented programme)
# #  class
# class Student:
#     name = "karan"
    
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# #  we make many cars and want the color of all car is same and brand is(BMW)
# class Car:
#     color = "blue"
#     brand = "BMW"
    
# c1 = Car()
# print(c1.color)
# print(c1.brand)

# c2 = Car()
# print(c2.color)
# print(c2.brand)


# #  init function
# class Student:
#     name = "sachin"
#     def __init__(self):
#         print(self)
#         print("adding new student in database..")
        
# s1 = Student()




# 
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new sudent in database..")
        
        
# s1 = Student("sachin", 98)
# print(s1.name,s1.marks)

# s2 = Student("karn", 95)
# print(s2.name,s2.marks)
        
        
        
# #  class and instance attribute 
# class Student:
#     college_name = "DBUU"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database...")
        
# s1 = Student("sachin", 98)
# print(s1.name,s1.marks)

# s2 = Student("karn", 95)
# print(s2.name,s2.marks)
# print(s2.college_name)



# #  object attribute > class attribute
# class Student:
#     college_name = "DBUU"
#     name = "sachin singh"
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks
#         print("adding new data")
        
# s1 = Student("karan",90)
# print(s1.college_name)


# #  methods 
# class Student:
    
    
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks
        
#     def welcome(self):
#         print("welcome student,",self.name)
        
    
#     def get_marks(self):
#         print(self.marks)

# s1 = Student("sachin" , 97)
# s1.welcome()
# s1.get_marks()


# #  abstraction)  eg.take a car
# class Car:
#     def __init__(self):
#         self.acc = 0
#         self.brk = 0
#         self.clu = 0
        
#     def start(self):
#         self.clu = 1
#         self.acc = 1
#         print("car start")
            
# car1 = Car()
# car1.start()

# # del keyword
# class Student:
#     def __init__(self,name):
#         self.name = name 
#         print(name)
    
        
# s1 = Student("sachin")
# del s1
# print(s1)
