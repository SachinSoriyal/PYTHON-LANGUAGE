# file I/O in python
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

# reading a file
f = open("demo.txt","rt")
data = f.read(3)
print(data)
print(type(data))
f.close()



# or 
f = open("demo.txt", "r")

line1 = f.readline()
print(line1)


line2 = f.readline()
print(line2)
f.close() 


#  writing to a file 
f = open("demo.txt","w")
f.write("I want to learn javascript")

f.close()

#  as apend 
f = open("demo.txt","a")
f.write("I will learn c++")

f.close()

# if we want to write the sentence in next line or print new sentence
f = open("demo.txt","a")
f.write("\nthen i start DSA")

f.close()


#python automatically created file for us 
file = open("sample file" , "a")
file.close


#  eg of "r+"
f = open("demo.txt","r+")
f.write("i live in dehradun")
f.close

#  if we want to read   (ponter in stream)
f = open("demo.txt","r+")
f.write("i live in dehradun")
print(f.read())
f.close

#  in w+ file is truncate 
f = open("demo.txt","w+")
f.write("i am sachin")
print(f.read())
f.close()


# in a+ mode
f = open("demo.txt","a+")
f.write("i am sachin")
print(f.read())
f.close()


#  with syntax
with open("demo.txt","r") as f :
    a = f.read()
    print(a)


#  if we write
with open("demo.txt","w") as f:
    f.write("I am cool")

# deleting a file 
import os 

os.remove("sample file")
