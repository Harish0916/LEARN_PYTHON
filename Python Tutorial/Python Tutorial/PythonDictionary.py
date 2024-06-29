#Create a new dictionary in Python
# new_dict = dict()
# new_dict = {}
# print(new_dict)

# color = {"col1" : "Red", "col2" : "Green", "col3" : "Orange" }
# print(color)

# Get value by key in Python dictionary
# dict = {1:20.5, 2:3.03, 3:23.22, 4:33.12}
# print(dict[1])
# print(dict.get(3))

# dic = {'pdy1':'DICTIONARY'}
# print(dic)
# dic['pdy2']='STRING'
# print(dic)

# Using update() method to add key-values pairs in to dictionary
# d = {0:10, 1:20}
# print(d)
# d.update({2:30,3:40,'Name':'Harish'})
# print(d)

# Iterate over Python dictionaries using for loops
# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', d[color_key])
# #   OR
# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for color_key, value in d.items():
#     print(color_key, 'corresponds to ', value)

# Remove a key from a Phthon dictionary
# myDict = {'a':1, 'b':2, 'c':3, 'd':4}
# print(myDict)
# if 'a' in myDict:
#     del myDict['a']
# print(myDict)

# Sort a Python dictionary by key
# color_dict = {
#     'red':'#FF0000',
#     'green':'#008000',
#     'black':'#000000',
#     'white':'#FFFFFF'
# }
# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))


# Find the maximum and minimum value of a Python dictionary
# my_dict = {'x':500, 'y':5874, 'z': 560}

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])


# Concatenate two Python dictionaries into a new one
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): 
#     dic4.update(d)
# print(dic4)


# Test whether a Pyhton dictionary contains a specific key
# fruits = {}
# fruits["apple"] = 1
# fruits["mango"] = 2
# fruits["banana"] = 4

# # Use in.
# if "mango" in fruits:
#     print("Has mango")
# else:
#     print("No mango")

# # Use in on nonexistent key.
# if "orange" in fruits:
#     print("Has orange")
# else:
#     print("No orange")


# Find the lenght of a Python dictionary
# fruits = {"mango":2, "orange":6}
# print("Length : ",len(fruits))


# --------------------------

# Tutorialssssss Video terms

# dic = dict(
#   user1 = dict(name = "Harish Ojha", Age = 25, fav_mov = ['kaal', 'zaadu']),
#   user2 = {'name':'Dayanand Ojha', 'Age':24, 'fav_mov':['The hind','The indian']}
# )

# for i, j in dic.items():
#   for k,l in j.items():
#     print(k,":",l)

# ----------------------

# d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d)

# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# print(d)

# d= dict.fromkeys(('name', 'age', 'height'), 'unknown')
# print(d)

# d = dict.fromkeys('abc', 'unknown')
# print(d)

# d = dict.fromkeys(range(1,11), 'unknown')
# print(d)

# d = dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d)

# d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d['name'])

# d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d['names']) # error

# d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d.get('name'))

# d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d.get('names'))# none

# d = {'name' : 'unknown', 'age' : 'unknown'}
# if 'names' in d:
#   print('present')
# else:
#   print('not present')

# d = {'name' : 'unknown', 'age' : 'unknown'}
# if d.get('names'):     # if none False else True
#   print('present')
# else:
#   print('not present')

# d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d)
# d.clear()
# print(d)

# d = {'name' : 'unknown', 'age' : 'unknown'}
# d1 = d.copy()
# print(d);print(d1)
# # d1.pop('age')
# d1.popitem()
# print(d);print(d1)

# d = {'name' : 'unknown', 'age' : 'unknown'}
# d1 = d
# print(d1==d)   # it checks values
# print(d1 is d) # it checks memory location

# d = {'name' : 'unknown', 'age' : 'unknown'}
# d1 = d.copy()
# print(d1==d)   # it checks values
# print(d1 is d) # it checks memory location

# user = {'name':'Harish Ojha', 'Age':25}
# print(user.get('name','Not found!!!'))
# print(user.get('names','Not found!!!'))

# user = {'name':'Harish Ojha', 'Age':25, 'age':35} # Case sensitive
# print(user)

# user = {'name':'Harish Ojha', 'Age':25, 'Age':35}  # Will print last only
# print(user)

# def dect_cube(n):
#   d = {}
#   for i in range(1,n+1):
#     # d.update({i:i*i*i})
#     d[i] = i*i*i
#   return d
# print(dect_cube(5))


# ----------------------------

# Word count
# harshit
# def word_counter(s):
#   count = {}
#   for char in s:
#     count[char] = s.count(char)
#   return count

# print(word_counter(input("Enter String : ")))

# -----------------------------

# def user(key, value):
#   info = {}
#   info.update({key : value})
#   return info   

# i=""
# d = {}  
# while not(i=="\n"):
#   k,v = input("Enter key and value comma separated : ").split(", ")
#   d.update(user(k, v))

# ---------------------

# name = input("Enter Name : ")
# Age = int(input("Enter Age : "))
# fav_movies = input("Enter Movies : ").split(", ")
# fav_songs = input("Enter Songs : ").split(",")

# user = {}

# user['name'] = name
# user['Age'] = Age
# user['fav_moveis'] = fav_movies
# user['fav_songs'] = fav_songs
# print("\n---------User's input is below :-------- \n")
# for key, value in user.items():
#   print(f"{key} : {value}")

# -----------------------
