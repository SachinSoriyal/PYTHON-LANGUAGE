# functions (It means the code design that perform specific Task)
def calc_sum(a,b):
    return a + b


# 1
a = calc_sum(2,5)
print(a)


# 2
b = calc_sum(5,4)
print(b)


# 3
c = calc_sum(124,23231)
print(c)


#  for hello 
def print_hello():
    print("Hello")
    
    
#1
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()


# make a function to calculate the average of three numbers 
def calc_avg(a,b,c):
    sum = a+b+c 
    avg = sum/3
    print(avg)
    return avg

calc_avg(59,69,89)


#  Types of function
# 01 built in system 
print("sachin")
print("singh")


#  or 
print("sachin ", end = " ")  #sep =  " "
print("singh")


# default parameters
#  create a function to calculate the product of two numbers
def cal_prod(a=1 , b=1):
    print(a*b)
    return a * b 

cal_prod()


# or 
def cal_prod(a , b= 1):
    print(a*b)
    return a * b 

cal_prod(1)


#      RECURSION
# recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("end")
    
show(5)
show(3)
show(1)
show(0)


# return n!
def fact(n): 
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
 
print(fact(4))
