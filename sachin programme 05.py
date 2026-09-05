# DICTIONARY AND SET 
# e.g of dictionary 
dict = {
    "name" : "sachin",
    "learning" : "coding",
    "class" : 12,
    "is_adult" : True
}

print(dict)

# 2nd e,.g 
info = {
    "name" : "sachin",
    "subject" : ["mathematics" , "chemistry" , "PHYSICS"], 
    "topics" : ("dictionary" , "sets"),
    "college" : "DBUU", 
    "class" : 12 
    
}

print(info)


# if we want , we can make our key any number either integer value or floating value
dict = { 
        "name" : "sachin", 
        12 : 80.01,
        12.23 : 98.98,
        "fault" : True
}
print(dict)
print(type(dict))


# we can axis the value of dictionary 
dict = { 
        "name" : "sachin", 
        12 : 80.01,
        12.23 : 98.98,
        "fault" : True
}
print(dict["name"])
print(dict["fault"])


# we can change the value of any key or asign a new value so, 
dict = {
    "name" : "sachin",
    "class" : 12,
    "language" : "python"
}
dict["name"] = "sachin singh "
print(dict)


#  in dictionary to get the nestedness we can make any key's own value as a dictionary 

student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
    
print(student)
print(student["subject"])

# we create a dictionary into a dictionary  so it is known as "NESTED DICTIONARY" 
# if we want to axis the marks of  a particular subject 
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}

print(student["subject"]["chemistry"])


# methods of dictionary 
# 1) Key method 
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
print(student.keys())


# we can use type casting 
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
} 
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))

  
  
# # 2)  values method '
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
} 
print(student.values())
print(list(student.values()))


# 3 ) items method 
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
} 
print(student.items())
print(list(student.items()))

#  we can also access these tuples individually
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
a = list(student.items())
print(a[1])


# 4)  get method 
# 01 method of (.get )
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
print(student["name"])


# 02) method of (.get)
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
print(student.get("name"))
print(student.get("name2"))



# 5)  update method
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
student.update({"city" : " Dehradun " })
print(student)
a = list(student.items())
print(a[2])

#      OR 
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
new_dict ={ "city" : "Dehradun", "age" : 16 }
student.update(new_dict)
print(student)

 
# ....
student = {
    "name" : "sachin singh " ,
    "subject" : {
        "physics": 98, 
        "chemistry" : 95,
        "mathematcs" : 100
    }
}
new_dict ={ "name" : "krishna", "age" : 16 }
student.update(new_dict)
print(student)

# set in python 
bunch = {1 , 2, 3, 4,"poonam" , "sachin"}
print(bunch)
print(type(bunch))

#        OR 
group = { 1 , 2 , 3 , 2 , 2 , "sachin" , "sachin" }
print(group)
print(len(group))


# how to create an empty set 
collection = set()
print(collection)
print(type(collection))

# set methods 
# 01 ) add method   [ in this method we cannot add a list or a dictionary]
group = set()
group.add(1)
group.add("sachin")
group.add((1,2,3))
print(group)


# remove method
group = set()
group.add(1)
group.add("sachin")
group.add((1,2,3))
print(group)
group.remove("sachin")
print(group)


#      OR
group = {1,2,3}
group.remove(1)
print(group)


#  clear method
collection = {1 , 2 , 3 , 4}
collection.remove(1)
print(collection)
collection.clear()
print(collection)


# pop method 
set = {1 ,2 ,3 ,4 ,5 ,6}
print(set.pop())
print(set.pop())
 

# UNION METHOD 
set1 = {1 , 2 , 3 }
set2 = {3 , 4 , 5 }
print(set1.union(set2))
print(set1)
print(set2)



#        OR 
set1 = { "sachin" , "abhay" , "aman" }
set2 = { "sachin" , "deepak" , "lucky"}
print(set1.union(set2))
print(set1)
print(set2)


# INTERSECTION METHOD 
set1 = {1 , 2 , 3 }
set2 = {3 , 4 , 5 }
print(set1.intersection(set2))
print(set1)
print(set2)


#        OR
set1 = { "sachin" , "abhay" , "aman" }
set2 = { "sachin" , "deepak" , "lucky"}
print(set1.intersection(set2))
print(set1)
print(set2)

