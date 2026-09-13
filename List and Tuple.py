 #lists
# eg. we want to stores the marks of students in a list 
# one method for the above problem solution
marks = [89.8 ,87.9 ,76.6 ,56.8 , 67.8]
print(marks)
print(type(marks))


# indexing in python
marks = [56,67,58,78,89]
print(marks[0])


# length in list 
marks = [45 , 67 , 68 , 78 , 89]
print(len(marks))


## we can store different types of element in python List 
student = [ 98 , "sachin" , 18 ,"Gairain"]
print(student[0])
print(type(student[0]))


#  #Item assignment
student = [98 , "sachin" , 18.7 , "Gairsain"]
student[0] = 234
print(student[0])
print(student)


# list slicing 
marks = [ 45,56,67,87,98]
print(marks[ :4])
print(marks[0:len(marks)])
print(marks[0: ])
print(marks[1:4])
print(marks[-5:-1])


# list method 
# append method (IT MEANS ADD SOMETHING NEW IN THE END)
list = [1 ,2 ,3]
list.append(4)
print(list)


list = ["sachin" , 12.34 , 18 , "gairsain"]
list.append(56)
print(list)


# sort method (IT MEANS SORTED OUT SOMETHING / arrange in the assending order)
list = [2 , 1 , 3 , 5 , 4]
list.sort()
print(list)

#02
list = [4,3,5,1,2]
print(list.append(4))
print(list.sort())
print(list)


#eg. by fruit
list = ["banana" , "litchi" , "apple"]
print(list.append("grapes"))
print(list.sort())
print(list)


# reverse method 
list = [1,4,3,2,5]
list.sort(reverse = True)
print(list)


# eg by fruits
list = ["banana" , "litchi" , "apple"]
print(list.append("grapes"))
print(list.sort(reverse = True))
print(list)



# wrire a programme  of a list initially it into ascending order than into desending order
list = [ 1 ,5 ,3 ,4 ,2 ]
list.sort()
print(list.sort())
print(list)
list.sort(reverse = True)
print(list.sort( reverse = True)) 
print(list)


# reverse method (02)
list = [1 , 3 , 2 , 4 ]
list.reverse()
print(list)


# insert method (IT MEANS ADDING UP AN PARTICULAR INDEX)
list = [1 , 2 , 4 , 5]
list.insert(2,3)
print(list)


list = ["abhay" ,"bhuwan" ,"Deepak"]
list.insert(2,"Chandu")
print(list)


#  remove function
list = [1 , 2 , 3 , 4 , 1 ]
list.remove(1)
print(list)


# pop  function( IT MEANS TO GO A PARTICULAR INDEX THAN REMOVE THE VALUE)
list = [1 ,2 , 2 ,3 ,4]
list.pop(2)
print(list)


#  copy method
list = [1 ,2 ,3 ,4 ,5]
list.copy()
print(list.copy())
print(list)


# count method { TO COUNT THE OCCURENCE OF A PARTICULAR ELEMENT}
list = [1 ,2 ,3 ,3 ,2 ,1]
list.count(1)
print(list.count(1))


#  TUPLES 
tup = (12 ,24 ,36 ,48 ,60)
print(type(tup))
print(tup)


# AXIS OF INDEX IN TUPLE 
tup = (23 ,34 ,45 ,56)
print(tup[0])  
print(tup[1])


# #
tup = ()
print(type(tup))
print(tup)


#  01 
tup = (1 ,)
print(tup)
print(type(tup))



#  02 ( basicaly in this python thinks that we wrote a integer value in paranthesis
tup = (1)
print(tup)
print(type(tup))


# 03 
tup = (1.0)
print(tup)
print(type(tup))


# 04
tup = ("sachin")
print(tup)
print(type(tup))


# 05
tup = (1,)
print(tup)
print(type(tup))


# 06
tup = (1.0 ,)
print(tup)
print(type(tup))


# 07
tup = ("sachin",)
print(tup)
print(type(tup))


#  slicing  in the tuple 
tup = ( 1 , 2 , 3 , 4 , 5)
print(tup[0:3])
print(tup)


# TUPLE METHOD
# 01 (INDEX METHOD) IT means  that we find the index of first element that when it is come first time
tup = ( 2 , 3 , 4 , 2 , 4 )
tup.index(2)
print(tup.index(2))
print(tup.index(3))


# count method 
tup = ( 2 , 4 , 3 , 2 , 4 )
print(tup.count(2))


# or 
tup = ("sachin" , "abhay" , "kanak" , "sonam" , "sachin")
print(tup.count("sachin"))


# palindrome (it is a conceptr which is same if we start it from starting as well as ending)
list = [ 1 , 2 , 3 ]
list.copy()
print(list)
