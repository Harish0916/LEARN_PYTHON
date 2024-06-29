# A set object is an unordered collection of distinct hashable objects.
# It is commonly used in membeship testing, removing duplicates
# from a sequence, and computing mathematical operations such as 
# intersection, union, difference, and symmetric difference.

# Sets support x in the set, len(set), and for x in set like other
# collections. Set is an unordered collection and does not record element
# position or order of insertion. Sets do not support indexing, slicing, or
# other sequence-like behavior.

# There are currently two built-in set types, set and frozenset. The set type
# is mutable - the contents can be changed using methods like add() and remove().
# Since ite is mutable, ite has no hash value and cannot be used as either a dictionary
# key or as an element of another set. The frozenset type is immutable and hashable - 
# its contents cannot be altered after it is created; it can, therefore, be used as a
# dictionary key or as an element of another set.



# Create a set in Python:

# st = set() #Empty set
# print(st)

# st = set([0,1,2,3,4,5])
# print(st)


# Iteration Over sets

# num_set = set([0,1,2,3,4,5])
# for n in num_set:
#     print(n)


# Add member(s) in Python set

# color_set = set()
# color_set.add("Red") # Take only one argument
# print(color_set)
# color_set.update(["Blue","Green"])
# print(color_set)
# color_set.update(["Orange","Violet","Black","White"])
# print(color_set)
# not set element one by one it set only simultaneously different


# Remove item(s) from Python set
# pop(), remove() and discard() functions are used to remove individual item
num_set = set([10,11,12,13,14,15])

# pop() function
# print(num_set)
# num_set.pop()
# print(num_set)
# num_set.pop()
# print(num_set)

# # remove() function
# print(num_set)
# num_set.remove(10)
# print(num_set)
# num_set.remove(14)
# print(num_set)

# # discard() function
# print(num_set)
# num_set.discard(12)
# print(num_set)
# num_set.discard(15)
# print(num_set)


# # Intersetion of sets (A ∩ B)
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx & sety
# print(setz)


# # Union of sets (A ∪ B)
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx | sety
# print(setz)


# # Set difference:
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx & sety
# print(setz)

# setb = setx - setz
# print(setb)


# Symmetric difference
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx ^ sety
# print(setz)


# # issubset and issuperset
# setx = set(["green", "blue"])
# sety = set(["blue"])
# issubset = setx <= sety # is setx is subset of  sety
# print(issubset)
# issuperset = setx >= sety # is sety is subset of  setx or is setx is superset of sety
# print(issuperset)

# setx = set(["green", "blue"])
# sety = set(["blue", "green"])
# issubset = setx <= sety
# print(issubset)
# issuperset = setx >= sety
# print(issuperset)


# Shallow copy of sets
# setx = set(["green", "blue"])
# sety = set(["blue", "green"])
# setd = setx.copy()
# print(setd)


# Clear sets
# setx = set(["green", "blue"])
# #Clear AKA empty AKA erase
# sete = setx.copy()
# sete.clear()
# print(sete)


# ===============

# Video tutorials
# print(list(set([2,1,3,2,5,2,6,3,7,1,8])))

# s = set([2,1,1.0,1.1,3,2,2.3,5,2,6,3,7,1,8])
# s.add(4)
# s.add(5)
# s.add(8)
# print(list(s))
# s.remove(3)
# print(list(s))
# s1 = s.copy()
# s1.discard(4)
# print(f'Set : {list(s)}')
# print(f'Set_copy : {list(s1)}')

# you cannot store list and dictionary in your set
# Set is unordered collection of item

# s = {'a','b','c'}
# if 'a' in s:
#   print("present")
# else:
#   print("not present")


# # for loop
# for item in s:
#   print(item) # o/p - abc, bac, cab

# l = [1,2,3,4,5,4,3,2,1]
# print(set(l))

# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6,7}
# print(s1 & s2) # Intersection
# print(s1 | s2) # Union
# print(s1^s2)   # Not common