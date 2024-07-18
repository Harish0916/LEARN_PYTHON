# Make flexible functions
# *operator or *args


# def total(*args):
#   sum = 0
#   for i in args:
#     sum+=i
#   return sum

# print(total(7,2,10))
# print(total())


# def multiply(num1, num2, *args):
#   print(args)
#   sum=1
#   for i in args:
#     sum*=i
#   return sum
# print(multiply(3,4,2,5,2))


# def multiply(*args):
#   print(args)
#   sum=1
#   for i in args:
#     sum*=i
#   return sum

# ls = [4,3,2,5]
# # print(multiply(ls))
# print(multiply(*ls)) # unpack using '*'

# ls = (4,3,2,5)
# # print(multiply(ls))
# print(multiply(*ls)) # unpack using '*'

# def to_power(num, *args):
#   if args:
#     return [i**num for i in args]
#   else:
#     return "You didn't pass any argument"
# ls = [2,3,4,5,6]
# print(to_power(3,*ls))

# OR
# n,ls = 3,[1,2,3,4,5]
# print([i**n if ls else "You didn't pass any argument" for i in ls])

# ============================
# Kwargs

# def func(name, **kwargs):
#   print(name,end = "")
#   for k,v in kwargs.items():
#     print(f'{v}',end = " ")
  
# func('Welcome, ',fn = 'Harish', Ln = 'ojha')

#------------------------
# Dictionary unpacking

# def func(name, **kwargs):
#   print(name,end = "")
#   for k,v in kwargs.items():
#     print(f'{v}',end = " ")
  
# dic = {'First Name':'Harish','Last Name':'Ojha'}
# func('Welcome, ', **dic)

# -----------------

# functions wiht all parameters very important to understand
# PADK - Parameters, Arguments, Default paramenters, Kwargs

# def func(name = 'unknown', age = 24):
#   print(name,age)
# func()
# ---------------

# def func(name = 'unknown', age = 24):
#   print(name,age)
# func('harish', 25)
# ---------------

# def func(name, *args, last_name = 'unknown', **kwargs):
#   print(name,args,last_name,kwargs,sep="\n")
# func('Harish',1,2,3,a='Aadhar',b='7373 0029 8231')
# -----------------

# Exercise
# def func(l, **kwargs):
#   if kwargs.get('reverse_str') == True : 
#     return [i[::-1].title() for i in l ]
#   return [i.title() for i in l]
# ls = ['harish', 'dayananad']
# print(func(ls , reverse_str = True))

# # Or

# def func(l, **kwargs):
#   return[ i[::-1].title() if kwargs.get('reverse_str') else i.title() for i in l]
# ls = ['harish', 'dayananad']
# print(func(ls))

# -----------------

# def add(a,b):
#   return a+b
# print(add(5,3))
# ---------------

# def new_add(*args):
#   total = 0
#   for num in args:
#     total+=num
#   return total

# print(new_add(1,2,3))
# l=[1,2,3,4] # list
# t = (1,2,3,4,5) # tuple
# print(new_add(*l)) # unpack
# print(new_add(*t)) # unpack

# ===============

# Lambda expressions (anonymous function) No name and define in a line

# def add(a,b):
#   return a+b;
# print(add(4,5))
# print(add)

# # but

# add2 = lambda a,b : a+b
# print(add2(2,3))
# print(add2)

# multiply = lambda a,b : a*b
# print(multiply(2,3))
# print(multiply)

# -------------

# def is_even(a):
#   return a%2 == 0
# print(is_even(2)) # True
# print(is_even(3)) # False

# OR

# is_even = lambda a : a%2 == 0
# print(is_even(4))
# print(is_even(5))
# -----------

# def last_char(strr):
#   return strr[-1]
# print(las_char("Hello"))

# OR

# last_char = lambda strr : strr[-1]
# print(last_char('Hitler'))
# -------------

# def func_len(s):
#   return len(s)>5
# print(func_len('Hitle'))
# print(func_len('Hitler'))

# OR

# func_len = lambda s : len(s)>5
# print(func_len('Hari'))
# print(func_len('Harish'))

# ===============

# Enumerate() function...
# We use enumerate function with for loop to track position of our item in iterable

# names = ['abc', 'abcdef', 'harshit']
# for pos, name in enumerate(names):
#   print(f'{pos} --> {name}')

# OR

# How we can do this without enumerate function

# names = ['abc', 'abcdef', 'harshit']
# pos = 0
# for name in names:
#   print(f'{pos} --> {name}')
#   pos+=1

# -----------

# With dictionary

# dic = {'name':'Harish', 'Age':'25'}
# for pos, name in enumerate(dic):
#   print(f'{pos} --> {name}')
  
# dic = {'name':'Harish', 'Age':'25'}
# for pos, (key, value) in enumerate(dic.items()):
#   print(f'{pos} --> {key} : {value}')

# ------------

# Define a function that take two arguments
# 1. list containing string
# 2. String that want to find in your list
# and this function will return the index of string in your list and if string isn't present then return -1

# def find_pos(s,*l):
#   return l.index(s) if s in l else -1
# # Calling    
# ls = ['daya', 'komal', 'harish', 'ravi']
# s='harish'
# print(f'Location of {s} : {find_pos(s,*ls)}')

# OR

# def find_pos(s, *l):
#   if s in l : 
#     return l.index(s)
#   else:
#     return -1

# # Calling    
# ls = ['daya', 'komal', 'harish', 'ravi']
# s='komal'
# print(f'Location of {s} : {find_pos(s,*ls)}')

# OR But you can do this with enumerate

# def find_pos(s, *l):
#   for pos, name in enumerate(l):
#     print(f'{pos} --> {name}')
#     if name == s:
#       return pos
#   else:
#     return -1

# # Calling    
# ls = ['daya', 'komal', 'harish', 'ravi']
# s='harish'
# print(f'Location of {s} : {find_pos(s,*ls)}')

# =====================

# Map function

# def square(ls):
#   l = []
#   for i in ls:
#     l.append(i**2)
#   return l

# ls = [1,2,3,4,5]
# print(square(ls))

# OR using list comprehension
# ls = [1,2,3,4,5,6]
# print([i**2 for i in ls])

# BUT using map function

# def square(a):
#   return a**2
# ls = [1,2,3,4,5,6]
# print(list(map(square,ls)))

# OR using lambda expression

# l = lambda i : i**2
# ls = [1,2,3,4,5,6]
# print(list(map(l,ls)))

# OR lambda in single line

# print(list(map(lambda a : a**2 , range(1,10))))

# OR easily without
# def square(num):
#   return num**2

# new_list = []
# for num in range(1,10):
#   new_list.append(square(num))
# print(new_list)

# -----------------
# Technically map object is an ITERATOR and you will understand why!
# names = ['ab','abc','abcd','abcde','abcdef']
# length = map(len, names)
# for i in length:
#   print(i)
# for j in length:
#   print(j)

# but after converting map function into list you can run loop multi time
# names = ['ab','abc','abcd','abcde','abcdef']
# length = list(map(len, names))
# for i in length:
#   print(i)
# for j in length:
#   print(j)

# BUT

# length = [1,2,3,4,5]
# for i in length:
#   print(i)
# for j in length:
#   print(j)

# ==========================

# Filter function

# def is_even(a):
#   return a%2 == 0
# numbers = [0,1,2,3,4,5,6,7,8,9]
# print(tuple(filter(is_even, numbers)))


# filter function iterate only one time not again
# evens = filter(lambda n : n%2 ==0 , range(0,10))
# for i in evens:
#   print(i)
# for i in evens:
#   print(i)


# But after convert it in tuple or list you can iterate it multiple times
# t=tuple(filter(lambda n : n%2 ==0 , range(0,10)))
# for i in t:
#   print(i)
# for i in t:
#   print(i)


#list comprehension
# print([i for i in range(0,10) if i%2 == 0])

# =================

# Difference b/w iterator vs iterable

# numbers = [1,2,3,4,5] # iterables-- tuples, strings, lists
# squares = map(lambda a:a**2, numbers) # iterator

# for i in numbers:
#   print(i)

# OR

# number_iter = iter(numbers) # iter is an object
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

# step call iter function
# iter(numbers) --> function
# next(iter(numbers))

# But in map function
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))

# # if you do this then you get error
# print(next(numbers)) # list object is not an itertor

# =================
# example = [('a',1),('b',2)]
# print(dict(example))
# -----------------

# user_id = ['user1', 'user2', 'user3']
# names = ['harshit', 'mohit', 'rohit']

# # ('user1','harshit'), ('user2','mohit'), .....
# print(list(zip(user_id, names)))
# print(tuple(zip(user_id, names)))
# print(dict(zip(user_id, names)))
# ------------------

# user_id = ['user1', 'user2']
# names = ['harshit', 'mohit', 'rohit'] # except rohit

# print(list(zip(user_id, names)))

# --------------

# user_id = ['user1', 'user2', 'user3']
# names = ['harshit', 'mohit', 'rohit']
# last_name = ['vashistha', 'sharma', 'saxena']
# # ('user1','harshit'), ('user2','mohit'), .....
# print(list(zip(user_id, names,last_name)))
# print(tuple(zip(user_id, names,last_name)))
# print(dict(zip(user_id, names,last_name))) #error

# -------------------

# l = [(1,2),(3,4),(5,6),(7,8)]
# # '*' operator with zip
# l1, l2 = list(zip(*l))
# print(l1)
# print(l2)
# --------------

# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# new_list = []

# for pair in zip(l1,l2):
#   new_list.append(max(pair))
# print(new_list)
# -----------------

# Advance function

# define a function take any no of lists containing number
# [1,2,3], [4,5,6], [7,8,9] return average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

l1, l2, l3, l = [1,2,3], [4,5,6], [7,8,9], []

# for pair in zip(l1,l2,l3):
#   l.append(sum(pair)/len(pair))
# print(l)


# OR Using list comprehension
# print([sum(pair)/len(pair) for pair in zip(l1,l2,l3)])


# OR Using Defining function
# def average_finder(*args):
#   avg = []
#   for pair in zip(*args):
#     avg.append(sum(pair)/len(pair))
#   return avg
# print(average_finder(l1,l2,l3))


# OR Try to make this anonymous function in one line using lambda
# lam = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
# print(lam(l1,l2,l3))

# =======================

# any() and all() function
num1 = [2,4,6,8,10]
num2 = [1,2,3,4,5]

# even1 = []
# for num in num1:
#   even1.append(num%2 == 0)
# print(even1)
# print(all(even1))

# # or

# print(all([num%2 == 0 for num in num1]))
# ---------------

# print(all([num%2 == 0 for num in num2])) # False
# print(any([num%2 == 0 for num in num2])) # True

# ------------

# x = 1 #int
# y = 2.8 # float
# z = 1j # complex

 #convert from int to float:
# a = float(x)
# print(a)
 #convert from float to int:
# b = int(y)
# print(b)
 #convert from int to complex:
# c = complex(x)
# print(c)
# ======================

# import random
# print(random.randrange(1, 10))
# i=0
# while i<10:
#     print(i)
#     i=i+1

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# secList = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
#     else:
#         secList.append(x)
# print(newlist)
# print(secList)

-----------------