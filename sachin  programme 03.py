# tab (using escape sequence button) 
str1 =  " This is my tutorial.\t I create it into python"
print(str1)


# next line (using escape sequence button)
str1 = " This is my tutorial.\n I create it into python"
print(str1)


# concatenation  which simple meaning is adding same data type variable
# str1 = "sachin"
# str2 = "singh"
print(str1 + str2) 


#length function for string 
str1 = "sachin"
len = len(str1)
print(len)


#role of tab when we use len function
str1 = "sachin"
str2 = "singh"
final_str = str1 + str2 +" "
print(len(final_str))


#indexing
str ="Sachin"
print(str[2])


#slicing
str = "apnacollege"
print(str[1:4])
print(str[ :4])
print(str[1: ])

# negative slicing 
str =  "sachin"
print(str[-3:-1])


#string functions
#01 (ends with function)
str = "i am a coder"
str1 =str.endswith("er")
print(str1)


#02
str = "sachin singh"
print(str.endswith("ingh"))


# capitalize function
str = "i am learning python"
print(str.capitalize())


#in capatilize 
str = "i am learning python"
print(str.capitalize())
print(str)


#replace function 
str  = "i am learning python "
print (str.replace("a" , "o"))


# replace function (word)
str = "i am learning python in manual way"
print(str.replace("python","javascript"))


#find function
str = "i am learning python from aapna college"
print(str.find("o"))
print(str.find("python")) 
print(str.find("z"))


#count function 
str =  "i am learning python am  from am  aapna college"
print(str.count("am"))


#conditional statements  
a = 20 
b = 30
if( a > b ):
    print(True)
if( a == b ):
    print(False)
else:
    print(True)


#01
age = 20
if(age >= 18):
    print("can vote and drive easily")


# 02
age = 21
if(age >= 18):
    print("apply for voting card and eligible for driving liscense")
    print("also can drive")


#03 (eg. of traffic Light )
light = "green"
if(light == "Red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
    
    
#eg. 04 
colour = "black"
if(colour == "white"):
    print("peace")
elif(colour == "green"):
    print("nature")
elif(colour == "red"):
    print("angerness")
else:
    print("darkness")
    
    
#eg. 05
num = 5
if(num > 2 ):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")
    
    
#else eg.
Room = "Dark"

if( Room == "bright"):
    print("beauty")
elif( Room == "green"):
    print("nature")
else:
    print("darkness")


#eg. 
age = 24

if(age >= 18):
    print("can vote")
else:
    print("can drive")


#comditioanl statement question 
#writa a programme to manage the grades of studnent on the basis of marks
marks =int(input( "enter students marks :"))
if( marks >= 90):
    print("grade 'a'")
elif(90 > marks >= 80):
    print("grade'b'")
elif(80 < marks >= 70):
    print("grade'c'")
else:
    print("grade'd'")
    
    
#02 way
marks = int(input("enter student marks"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->",grade)


# nesting
age = int(input("enter your age:"))

if(age >=18):
    if(age >=80):
       print("cannot drive")
    else:
       print("can drive")
