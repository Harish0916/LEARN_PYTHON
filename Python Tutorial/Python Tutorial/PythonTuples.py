# A tuple is a container which holds a series of
# comma-separated values(items or elements) between 
# parentheses such as an (x,y) co-ordinate. Tuples are
# like lists, except they are immutable (i.e. you cannot
# change its content once created) and can hold mix data types.
# Tuples play a sort of "struct" role in Python -- a convenient
# way to pass around a little logical, fixed size bundle of values.

# Create a tuple

# tupl = ()
# print(tupl)

# tupl = ('tuple', False, 3.2, 1)
# print(tupl)

# tupl = 4,6,3,2,8,1
# print(tupl)

# tupl = 4,
# print(tupl)
# print(type(tupl))

# tupl = tuple()
# print(tupl)

# tupl = tuple([True, False])
# print(tupl)


# How to get an item of the tuple in Python?

# tupl = ("H","A","R","I","S","H",0,9,1,6)
# print(tupl)
# print(tupl[3])
# print(tupl[-4])

#How to know if an element exists within a tuple in Python?

# tupl = ("H","A","R","I","S","H",0,9,1,6)
# print(tupl)
# print("R" in tupl)
# print(19 in tupl)


# List to tuple

# ls = [5,10,2,8,7,15]
# print(ls)
# print(tuple(ls))


# Unpack a tuple in several variables

# tupl = 4,8,3
# print(tupl)
# n1,n2,n3 = tupl # Unpack a tuple in variables
# print(n1 + n2 + n3)
# n1,n2,n3,n4 = tupl # error "not enough value to unpack"

# t = (1,2)
# t += 12,
# print(t)


# Add item in Python tuple! and don't have update or append method

# tpl = (4,6,1,3,7,8,9)
# print(tpl)
# tpl += (2,)
# print(tpl)
# # adding items in specific index
# tpl = tpl[:5] + (15,20,25) + tpl[5:]
# print(tpl)
# # converting the tuple to list
# print(list(tpl))
# # use different way to add items in list
# ls = list(tpl)
# ls.append(30)
# print(tuple(ls))


# Clone a tuple

# from copy import deepcopy
# # create a tuple
# tpl = ("HELLO", 5,[],True)
# print(tpl)
# # make a copy of a tuple using deepcopy() function
# # tpl_clone =tuple(list(tpl).copy()) # This line of code won't work
# tpl_clone = deepcopy(tpl)
# tpl_clone[2].append(50)
# print(tpl_clone)
# print(tpl)


# In Python how to know the number of times and item has repeated

# tpl = 2,4,6,8,2,3,4,4,7,8
# print(tpl)
# print(tpl.count(4))
# print(tpl.count(2))
# print(tpl.count(8))

# Remove an item from a tuple

tupl = ("H","A","R","I","S","H",0,9,1,6)
print(tupl)
# tuple are immutable, so you can not remove elements
# using merge of tuples with + operator you can remove and item and it will create a new tuple
tupl = tupl[:4]+tupl[4:]
print(tupl)
# converting the tuple to list
ls = list(tupl)
ls.remove("I")
# converting the list to tuple
tupl = tuple(ls)
print(tupl)

# # Slice a tuple
# tpl = (2,4,3,5,4,6,7,8,6,1)
# print(tpl[3:5])
# print(tpl[:6])
# print(tpl[5:])
# print(tpl[:])
# print(tpl[-8:-4])


# Find the index of and item of the tuple
# tpl = tuple("index tuple")
# print(tpl)
# print(tpl.index("e"))
# print(tpl.index("e",tpl.index("e")+1))
# print(tpl.index("e",3,6))
# print(tpl.index("e",tpl.index("e")+1,6)) #error
# index("ToBeSearched","Start","End")


# The size of tuple
# tpl = tuple("Python Tutorial")
# print(tpl)
# print(len(tpl))


# How operators + and * are used with a Python tuple?
# tpl = 5,
# print(tpl*6)
# tpl = (5,10,15)*4
# print(tpl)

# # create tthree tuples
# t1 = (3,6,9,12,15)
# t2 = ("P","Y","T","H","O","N")
# t3 = (True, False)
# print(t1+t2+t3)


# Slice of a tuple using step parameter
# tpl = tuple("HELLO WORLD")
# print(tpl)
# print(tpl[2:9:2])
# print(tpl[::4])
# print(tpl[9:2:-4])
# print(tpl[9:2:-3])


# Modify items of a tuple

# tuplex = ("w", 3, "r", [], False)
# print(tuplex)
# #tuples are immutable, so you can not modify items which are also immutable, as str, boolean, numbers etc.
# tuplex[3].append(200)
# print(tuplex)


