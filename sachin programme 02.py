# input in  python 
name = (input("enter your name :")) 
print("welcome", name)
 
# 02 type of input in type casting conversion 
age = input("enter your age :")
print("your age is ", age)

# result of input is always string type
val = input("enter a value :")
print(type(val),val) 

# type casting conversion for interger  value for input
vaL = 7654
val = int(input("enter your value:"))
print(type(val),val)

# type casting conversion for floating value
val = 12.3467
val = float(input("enter your value:"))
print(type(val),val)

# if we want to take the input of our age , name and marks
name = input("enter your name :")
age = int(input("enter your age :"))
marks = float(input("enter your marks :"))

print("welcome",name)
print("your age is",age)
print("your marks is",marks)

print(type(name),name)
print(type(age),age)
print(type(marks),marks)