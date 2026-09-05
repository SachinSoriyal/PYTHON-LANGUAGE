name = "sachin singh"
age = 18 
price = 11.55
print(name)
print(age)
print(price)

# 01
name = "ajjju"
age = 13

age2 = age
print("my age is :",age2)
print("my name is :",name)


#02
name2 = "2sachin"
print(name2)


# 03 (find data type)
name = "sachin singh"
age = -18 
price = 234.56

print(type(name))
print(type(age))
print(type(price))


#04 (string data type)
name1 ='ss'
name2 = "ss"
name3 = '''ss'''

print(name1)
print(name2)
print(name3)

#05 (float data type)
value1 = 45.6
value2 = 98.18

print(type(value1))
print(type(value2))

# 06 (boolean & none data type)
age =  23 
old = False
a = None
print(type(old))
print(type(a))

# print SUM
a = 12
b = 26
sum = a + b 
print(sum)

# print SUBTRACTION
a = 12345
b = 1234
subtraction = a - b
print(subtraction)

# comment in python 
print("sachin")
print("sachin")
print("sachin")


# arithemetic operators
a = 5 
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b )
print(a ** b)

# relational operators
a = 60
b = 80
print(a == b)
print(a !=b)
print(a < b)
print(a > b)
print(a >=b)
print(a <=b)

# assignment operators 
num = 40
num = num + 40
print("num:",num)

#second way
num  = 40
num += 40
print(num)


#  minus equal to operators 
num = 70
num -=40
print(num)

# multiply equal to operator 
num = 30
num *= 40
print(num)

# divide equal to operator
num = 50
num /= 10
print(num)

# remainder equal to operator 
num = 50
num %= 25
print(num)


# power equal to operator
num = 40
num**= 4
print(num)

# logical operators
print(not True)
print(not False)

# second method of logical operators
a = 30
b = 20
print(not (a<b))
print (not (a>b))

val1 = True
val2 = True
print("AND  operator:",val1 and val2)
val1 = True
val2 = False
print("OR operator:",val1 and val2)

# type conversion (typr 01 automatic type conversion)
a = 32
b = 23.4

sum = a + b
print(sum)

# type conversion (type 02 manual type conversion)
a =  int("23")
b = 45.7
sum =  a + b 
print(sum)

# in string 
a = 23
a = str(a)
print(type(a))