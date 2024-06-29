# List comprehension
# using this can create list in one line

# squares = []
# for i in range(1,11):
#   squares.append(i**2)
# print(squares)

# # OR

# print([i**2 for i in range(1,11)])


# negative = []
# for i in range(1,11):
#   negative.append(-i)
# print(negative)

# # OR

# print([-i for i in range(1,11)])

# --------------

# names = ["harish", "komal", "Rohit"]
# for i in names:
#   print(i[0])


# names = ["harish", "komal", "Rohit"]
# new_list = []
# for i in names:
#   new_list.append(i[0])
# print(new_list)

# # OR

# print([i[0] for i in names])

# -----------------

# l = ['abc', 'tuv', 'xyz']
# new_l = []
# for i in l:
#   new_l.append(i[::-1])
# print(new_l)

# # OR

# print([i[::-1] for i in l])

# --------------------

# Print even and odd
# print([i for i in range(1,11) if i%2 == 0])
# print([i for i in range(1,11) if i%2 != 0])
# print([i for i in range(1,11) if not i%2 == 0])

# ---------------

# def num_to_str(l):
#   li = []
#   for i in l:
#     if( type(i) == int or type(i) == float):
#       li.append(str(i))
#   return li

# print(num_to_str([1,1.2,3,[1,2,3,4,5,6],'Harish',True]))

# # OR

# l = [1,1.2,3,[1,2,3,4,5,6],'Harish',True]
# print([str(i) for i in l if (type(i) == int or type(i) == float)])

# -----------------------

# List comprehension wiht if else

# nums = list(range(1,11))
# new_list = []
# for i in nums:
#   if i%2 == 0:
#     new_list.append(i*2)
#   else:
#     new_list.append(-i)

# print(new_list)

# OR

# nums = list(range(1,11))
# print([i*2 if i%2==0 else -i for i in range(1,11)])

# ----------------------

# List comprehension in nested list

# list1 = []
# for i in range(1,4):
#   list1.append(list(range(1,4)))
# print(list1)
# # OR
# print([list(range(1,4)) for i in range(1,4)])
# # OR
# print([[i for i in range(1,4)] for j in range(3)])
# # OR
# print([[1,2,3] for i in range(1,4)])


# list1 = []
# for i in range(1,4):
#   list1.append(3*[i])
# print(list1)
# OR
# print([3*[i] for i in range(1,4)])

# ---------------

# Dictionary comprehension

# d = {}
# for i in range(1,6):
#   d.update({i:i**2})
# print(d)
# # OR
# print({i:i**2 for i in range(1,6)})

# print({f"Square of {i} is " : i**2 for i in range(1,6)}) # Ordered
# print({f"Square of {i} is  : {i**2}" for i in range(1,6)}) # Unorderd
# OR
# print({f'Square of {k} is {v}' for k,v in {i:i**2 for i in range(1,6)}.items()})

# d = {}
# for i in range(1,6):
#   d.update({i:i**2})
# for k,v in d.items():
#   print(f'Square of {k} is {v}') 
# OR
# d = {i:i**2 for i in range(1,6)}
# for k,v in d.items():
#   print(f'Square of {k} is {v}')
# string = "harshit"
# print({i:string.count(i) for i in string})


# -----------------

# Dictionary comprehension
# print({i:('even' if i%2 == 0 else 'odd') for i in range(1,11)})

# --------------------

# Set Comprehension undordered
# print({k**2 for k in range(1,11)})
# print({name[0] for name in ['harshit','komal','dayanand']})

