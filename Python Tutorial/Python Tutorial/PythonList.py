#List
# l = [5,24,43,22]
# print(l)

# l = ['red','green','blue']
# print(l)

# l = [100,'Harish',12.13,-1020]
# print(l)

# l = []
# print(l)
# print(type(l))

#concatenation of two or more list using '+'
#And multiple of list using '*'
# l1 = ['Red','Green']
# l2 = ['Blue','Black']
# l3 = ['White']
# l=l1+l2+l3
# print(l)
# l=['hello']
# print(type(l))
# print(l*4)

# l=[100]
# print(type(l))
# print(l*4)

# l=[100]
# print(l[0]*4)

#List indices

# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list[0])
# print(color_list[4]) #error

#Add an item to the end of the list
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.append('White'))
# print(color_list)


# Insert an item at a given position
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.insert(1,'White'))
# print(color_list)


# Modify an element by using the index of the element
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# color_list[2]='Yellow'
# print(color_list)

# Remove an item from the list
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.remove("Black"))
# print(color_list)

# Remove all items from the list
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.clear())
# print(color_list)

# List Slices
# color_list=["Red", "Blue", "Green", "Black"]
# The list have four elements indices start at 0 and end at 3
# print(color_list[0:2]) # cut first two items

# The list have four elements indices start at 0 and end at 3
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list[1:2])
# print(color_list[1:-2])

# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list[1:3])
# print(color_list[1:-1])

# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list[:3])
# print(color_list[:-1])

# Create copy of original list
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list[:])

# Remove the item at the given position in the list, and return it
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.pop(2))
# print(color_list)

# Return the index in the list of the first item whose value is x
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.index('Blue'))
# print(color_list.index('Green'))

# Return the number of times 'x' appear in the list
# color_list=["Red", "Blue", "Green", "Black", "Blue", "Green","Blue"]
# print(color_list.count("Blue"))
# print(color_list.count("Green"))

# # Sort the items of the list in place
# color_list=["Red", "Blue", "Green", "Black"]
# color_list.sort(key = None, reverse = False)
# # print(color_list)
# print(color_list.sort())
# print(color_list)

# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(sorted(color_list))
# print(color_list)

# Reverse the elements of the list in place
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.reverse())
# print(color_list)

# Return a shallow copy of the list
# color_list=["Red", "Blue", "Green", "Black"]
# print(color_list)
# print(color_list.copy())
# print(color_list)

# Convert a list to a tuple in Python
# listx = [1,2,3,4]
# print(listx)
# tuplex = tuple(listx)
# print(tuplex)

# print(type(tuple(list(range(1,11)))))

# How to use the double colon [::]?
# ls = list(range(1,9))
# print(ls)
# list[start:stop:step]
# print(ls[2:7:2])
# print(ls[::3])
# print(ls[8:-6:-2])
# print(ls)

# Find the largest and the smallest item in a list
# ls = [5,6,1,3,45,9,2]
# print(ls)
# print(max(ls))
# print(min(ls))

# Compare two lists in python

# ls1,ls2 = [3,5,7,9],[3,5,7,9]
# print(ls1 == ls2)

# ls1,ls2 = [13,15,17,19],[3,5,7,9]
# print(ls1 == ls2)
# print(not(ls1 == ls2))

# ls1,ls2 = [5,7,9,3],[3,5,7,9]
# print(ls1 == ls2)
# print(ls1.sort() == ls2.sort())

# Nested lists in python
# ls = [["Hello","World"],list(range(1,6))]
# print(ls)
# print(ls[0])
# print(ls[1])
# print(ls[0][0])
# print(ls[0][1])
# print(ls[1][0])
# print(ls[1][4])
# print(ls[1][len(ls[1])-1])
# ls.append([True,False])
# print(ls)
# ls[1][3] = 12
# print(ls)

# How can i get the index of an element contained in the list?
# ls = list([1,2,3,4,5])
# print(ls)
# print(type(ls))

#  ls = list("HELLO WORLD")
# print(ls)
# print(ls.index('L'))
# print(ls.index('L',4))
# print(ls.index('O',3,5))

# Using Lists as Stacks
# color_list = ["Red","Blue","Green","Black"]
# print(color_list)
# color_list.append("White")
# color_list.append("Yellow")
# print(color_list)
# color_list.pop()
# print(color_list)
# color_list.pop()
# print(color_list)

# Using Lists as Queues
# from collections import deque
# color_list = deque(["Red","Blue","Green","Black"])
# color_list.append("White")
# print(color_list)
# color_list.popleft()
# print(color_list)
# color_list.popleft()
# print(color_list)
