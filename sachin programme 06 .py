#          LOOPS 
# Take an eg. 
#  we want to print "Hello" 10 times 
count = 1
while count <= 5 :
    print("hello")
    count += 1
    
print(count)


#      or
i = 1 
while i <= 5 :
    print("sachin")
    i+=1


# write  a programme to print ("sachin") 100 times 
i = 1 
while i <= 100 : 
    print("sachin" ,i )
    i += 1 

 
#  print no. from 1 to 5 
i = 1 
while i <=5 :
    print(i)
    i += 1
    

# print no. from 5 to 1
i = 5 
while i>=1 :
    print(i)
    i -= 1


# eg. of infinite loop
i = 5
while i < 6:
    print(i)
    i -= 1


#    BREAK
i = 1
while i <= 5:
        print(i)
        if (i == 3):
            break
        i += 1
        
print("end of loop")


#        OR 
num = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)
x = 36 

i = 0 

while i < len(num):
    if(num[i] == x):
        print("found at index",i)
        break
    else:
        print("finding")
        i +=1
        
print("end of loop")


#        CONTINUE
i = 0 
while i <= 5:
    if(i == 3):
        i += 1
        continue  
    print(i)
    i += 1


#  we want to skip  even numbers only want to print odd numbers 
i = 1 
while i <= 10:
    if (i % 2 == 0):
        i += 1 
        continue
    print(i)
    i += 1
    
    
#  we want to skip  odd  numbers only want to print even numbers
i = 1 
while i <= 10:
    if (i % 2 != 0):
        i += 1
        continue
    print(i)
    i+=1


#  for loops (for list) 
list = [ 1 , 2 , 3 ]
for  a in list:
    print(a)
    
    
# for loop (for string)
name = ["sachin" , "abhay" , "aman" , "krish" , "lucky"]
for friends in name:
    print(friends)
    
    
#  for loop (for tuple) 
nums = [ 1 , 2 , 3 , 4 , 5 ]
for z in nums:
    print(z)
    
    
#  for loops (for string)
str = "sachin"
for char in str:
    print(char)


#  for loop with else
str = "sachin" 
for char in str:
    if(char == 'c'):
        print("c found")
        break 
    print(char)
else: 
    print("end")
    
    
#  if we are not using else 
str = "sachin" 
for char in str:
    if(char == 'c'):
        print("c found")
        break 
    print(char)
print("end")


#            RANGE
print(range(5))


#      or 
seq = range(5)
print(seq[0])
print(seq[1])


       Or
seq = range(10)
i = 0
for i in seq:
    print(i)
    
    
#         or 
for i in range(10):
    print(i)
    

# 1st 
for i in range(10):
    print(i)


#  2nd 
for i in range(2, 10):
    print(i)


# 3rd 
for i in range(2 , 10 , 2 ):
    print(i)


# if we only want to print even no. (using for loop)
for i in range(2 , 20 , 2):
    print(i)


# if we only want to print odd no. (using for loop)
for i in range(1,20,2):
    print(i)


#  Pass statement  
for i in range(5):
    pass
print("always happy")
