# print("Hello how are you")
# print('Hello how are you')
# print("Hello, 'World'")
# print('Hello, "World"')
# print("Hello \"World\"") # Escape Sequence
# print('Hello \'World\'')
# print(r"Hello \"World\"")
# print(r'Hello \'World\'')
# print(r'Hello\t \'World\'')
# print('Hello\tWorld')
# print('Hello\nWorld')
# print('Hello\bWorld')
# print('Hello\\World')
# print(r'Hello\World')
# print("\U0001F602") 😂
# =======================

# Python as calculator    **,  *,/,//,%,    +,-
# print(9%4)
# print(9/4) # float division
# print(9//4) # Integer division
# print(2**3)
# print(2**0.5)
# print(round(2**0.5, 3))
# print(2**3/2*6-4*(3-4/2))
# print(2**3**2) # RTL 3**2 then 2**9
# print((2+3)*5/2%6)

# =======================
# Convention of variable naming
# Variable mean that takes different type of value , in other word "Changable"
# It's process called "Dynamic programming"
# num = 12 ; print(num)
# num = 15 ; print(num)
# num = 20.2 ; print(num)
# num = 'harish' ; print(num)
# num = True ; print(num)
# Don't use special symbol(@#$%&*^) and can't use digits as starting character
# user_first_name = "Harish" # Snake case writing (default)
# userLastName = "Ojha"      # Camel case writing

# ======================

# 17 - String Concatination
# Fn, Ln  ="Harish","Ojha"
# print(Fn+" "+Ln)
# print(Fn,Ln)
# # print(Fn + 3) # error
# print(Fn + str(3))
# print(Fn+"3") # no error
# print(Fn*3)
# print(3*Fn)
# print(3*(Fn+Ln))
# print((Fn,Ln)*3)   # Working as Tuple
# print(3*(Fn,Ln)*3) # Working as Tuple
# print(3*Fn,Ln)
# print(3*Fn,Ln*3)

# ===========================

# User input using input() function
 
# name = input("Type your name : ")
# Age = input("Enter your age : ")
# print("Hello,",name,"you are",Age,"yr old",sep="*") # sep() working correctly
# print("Hello,"+name+"you are"+Age+"yr old")
# print("Hello,"+name+"you are"+Age+"yr old",sep="*") # sep() not working
# print("Hello,"+name+"you are"+Age+"yr old",",what are you doing?",sep="*") # sep() not working
# It mean sep() function working between comma seperted inputs not between + seperated or concatinated

# =========================

# # int() function
# Fn = int(input("Enter first number : "))
# Sn = int(input("Enter second number : "))
# print("Total of ",Fn,"and",Sn,"is",str(Fn+Sn)) # here Fn and Sn didn't cast into str, have in int
# print("Total of "+str(Fn)+"and"+str(Sn)+"is"+str(Fn+Sn)) 
      # here Fn and Sn must cast into str, don't have in int

# num1, num2 = 12, 10.5
# print(num1+num2) # output in float always

# ============================
# Declare variable in a line or in a line declare multiple variables

# name, Age = "Harish", 24
# print(name,"you are",Age,"yr old.")
# x=y=z=10
# print("output of",x,y,z,"is", x+y+z)

# ============================

#  Two or more input in a line

# name, age = input("Enter your name and age : ").split()
# print(name); print(age)

# name, age = input("Enter your name and age : ").split(",") 
# print(name); print(age)

# name, age = input("Enter your name and age : ").split(", ") # a comma and a space
# print(name); print(age)

# ====================

# String formatting

# name, age = "Harish", 25

# # python 2
# print("Hello,"+name+"your age is"+str(age)) # ugly syntax
# # python 3
# print("Hello,{} your age is {}".format(name,age))
# # python 3.6 and above
# print(f"Hello,{name} your age is {age}.")
# print(f"Hello,{name} your age is {age+2}.")
# f_name,L_name,age = "Harish", "ojha",25
# # print(f"Hello,{f_name+' '+L_name} your age is {age+10}")
# print(f"Hello{*f_name,*L_name} your age is {age+10}") 
            # using '*' to unpacking (or seperate all character from a string)

# =====================================
# Find the average of three input numbers
# a,b,c = input("Enter comma-space seperated three number : ").split(", ")
# print(f"Average of {a},{b} and {c} is {(int(a)+int(b)+int(c))/3}")

# ============================

# print('{} {}'.format('Python','Format'))
# print('{} {}'.format(10,30))
# print('{1} {0}'.format('Python','Format'))

# print('{:15}'.format('Python'),'Hello',sep='')
# print('{:<15}'.format('Python'),'Hello',sep='')
# print('{:^15}'.format('Python'),'Hello',sep='')
# print('{:>15}'.format('Python'),'Hello',sep='')

# print('{:{}}'.format('Python',15),'Hello',sep='')
# print('{:<{}}'.format('Python',15),'Hello',sep='')
# print('{:^{}}'.format('Python',15),'Hello',sep='')
# print('{:>{}}'.format('Python',15),'Hello',sep='')

# print('{:*{}}'.format('Python',15),'Hello',sep='') #will create error
# print('{:*<{}}'.format('Python',15),'Hello',sep='')
# print('{:*^{}}'.format('Python',15),'Hello',sep='')
# print('{:*>{}}'.format('Python',15),'Hello',sep='')

#Truncating long strings:
# print('{:.10}'.format('Python Tutorial'),'Hello',sep='')
# we have truncated ten characters from the left side of a specified string.
# print('{:.{}}'.format('Python Tutorial',10),'Hello',sep='')

#Combining truncating and padding
# print('{:10.10}'.format('Python Tutorial'),'Hello',sep='')
# print('{:18.10}'.format('Python Tutorial'),'Hello',sep='')
# print('{:*<18.10}'.format('Python Tutorial'),'Hello',sep='')
# print('{:*^18.10}'.format('Python Tutorial'),'Hello',sep='')
# print('{:*>18.10}'.format('Python Tutorial'),'Hello',sep='')

#Numbers:
#Integers:
# print('{:d}'.format(24))
# print('{:f}'.format(5.12345678123))

#Padding numbers:
#Similar to strings numbers.
# print('{:*>5d}'.format(24))
# print('hello{:*>5d}'.format(24))
# print('{:*>5.2f}'.format(5.12345678123))
# print('hello{:*>5.2f}'.format(5.12345678123))

#signed numbers:
#By default only negative numbers are prefixed with a sign,
#but you can display numbers prefixed with the positive sign also.
# print('{:+d}'.format(24))
# print('{:d}'.format(+24))
# print('{:d}'.format(-24))
# #You can use a space character to indicate that negative numbers 
# # (should be prefixed with a minus symbol) and a leading space should 
# # be used for positive numbers.
# print('{: d}'.format(-24))
# print('{:+d}'.format(24))

# #You can control the position of the sign symbol relative to the padding.
# print('{:6d}'.format(-24))
# print('{:=6d}'.format(-24))
# print('{:*>6d}'.format(-24))
# print('{:*=6d}'.format(-24))

#Named Placeholders:
#Both formatting styles support named placeholders. Here is an example:
# data = {'First Name':'Harish', 'Last Name':'Ojha'}
# print('{First Name} {Last Name}'.format(**data))
# print('{Last Name} {First Name}'.format(**data))
# print('{first} {last}'.format(first = "Harish", last = "Ojha"))

# # #DataTime:
# from datetime import datetime
# print('{:%Y-%m-%d %H:%M}'.format(datetime(2019,2,15,3,25)))
# print('{:%y-%m-%d %H:%M}'.format(datetime(2019,2,15,3,25)))

# ==========================

# String Indexing, String Slicing / Selecting sub Sequences

# lang = "Python"
# positions(index number)

# p = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2
# n = 5, -1

# print(lang[4])
# print(lang[6]) # error out of range
# print(lang[-2])
# print(lang[-7]) # error out of range

# syntax - [start argument : stop argument - 1]
lang = "Python"
# print(lang[3:6])  # hon
# print(lang[-3:6]) # hon
# print(lang[-1:6]) # n
# print(lang[3:])   # hon
# print(lang[:])    # python
# print(lang[-2:])  # on
# print(lang[:-1])  # pytho
# print(lang[:-3])  # pyt
# print(lang[:-5])  # p
# print(lang[2:-1]) # tho
# print(lang[4:-1]) # o
# print(lang[::])   # python
# print(lang[::2])  # pto
# print(lang[::-1]) # nohtyp
# print(lang[::-2]) # nhy
# print(lang[::-3]) # nt
# print(lang[::-4]) # ny
# print(lang[::-5]) # np
# print(lang[::-6]) # n

# print(lang[-1::-1]) # nohtyp
# print(lang[-3::-1]) # htyp
# print(lang[-5::-1]) # yp
# print(lang[-6::-1]) # p
# print(lang[-7::-1]) # won't show

# print(lang[:-1:-1]) # won't show -1+1=0
# print(lang[:-2:-1]) # n -2+1=-1
# print(lang[:-3:-1]) # no -3+1=-2
# print(lang[:-4:-1]) # noh -4+1=-3
# print(lang[:-5:-1]) # noht -5+1=-4
# print(lang[:-6:-1]) # nohty -6+1=-5
# print(lang[:-7:-1]) # nohtyp -7+1=-6

# we had to add +1 to the mid argument

# print(lang[-3:-7:-1]) # htyp -7+1=-6
# print(lang[4:-7:-1])  # ohtyp -7+1=-6
# print(lang[-3:1:-1])  # ht 1+1=2
# print(lang[-4:1:-1])  # t 1+1=2
# print(lang[-5:0:-1])  # y 1+1=2
# print(lang[-5::-1])   # yp 1+1=2

# ================================
# String methods- strings are immutable

# len(), lower(), upper(), title(), count()
# string = 'harish ojha'
# print(string)
# print(len(string))
# print(string.lower())
# print(string.upper())
# print(string.title())
# print(string.count('h'))
# print(string)

# Strip() method- lstrip() + rstrip()

# name = '     Harish     '
# dots = '................'
# print(name+dots)
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)
# print(name.strip()+dots)
# # if you want to remove spaces using another mehtods then
# print(name.replace(' ','')+dots)

# string = "Harshit" # case insensitive
# sb = 'h'
# print(len(string))
# print(string.strip().lower().count(sb.strip().lower())) 

# replace() and find() methods---
string = "she is beautiful and she is good dancer"

# print(string.replace('is','was'))
# print(string.replace('is','was',1))

# print(string)
# is_pos1 = string.find("is")
# is_pos2 = string.find("is",is_pos1+1)
# print(f'position of first \'is\' is {is_pos1}')
# print(f'position of second \'is\' is {is_pos2}')

# Center() method- put star more than string length to show
# name = 'Harish'
# print(name)
# print(name.center(8,'*'))
# print(name.center(9,'*'))
# print(name.center(10,'*'))
# print(name.center(11,'*'))

# String are immutable

# string = "harish"
# # string[2] = 'o' # error
# s = string.replace('r','o')
# print(s) # new string
# print(string) # previous string

# You can use concatinatation not assignment
# name = 'harsh'
# name += 'it'
# print(name) # harshit

# ==========================
# Statements
# age = 20
# if age>18 :
#       pass  # pass mean don't write
# else:
#       print("not allow")

# age = int(input("Enter age : "))
# if 0<age<=3:
#       print("Hello")

# print('h' in 'Harish') # True

# check string is empty or not
# msg = ""
# if msg:
#       print("String is fill")
# else:
#       print("String is empty")

# Problem
# 12345
# calculate 1+2+3+4+5 and print

# num = '12345'
# total = 0
# i=0
# while i<len(num):
#       total+=int(num[i])
#       i+=1
# print(total)

# problem
# ask a user for name
# Example - Harshit Vashistha
#
# name = input("Enter user name to count characters, in it : ")
# i = cnt = 0
# char = []
# while i<len(name):
#       if  name[i].lower() not in char:
#             cnt = name.lower().count(name[i].lower())
#             print(f'{name[i]} : {cnt}')
#             char.append(name[i].lower())
#       i+=1

# infinite loop --
# i = 0
# while i<=10:
#       print("Hello world") # To stop infinte printing press Ctrl + 'c'

# i = 0
# while True: 
#       print(f"hello world : {i}")
#       i+=1 # infinite loop stop by pressing Ctrl + 'c'


# for i in range(1,10,2):
#       print(f'hello world {i}')

# for i in range(-1,-10,-2):
#       print(f'hello world {i}')

# 12345 ----> 1+2+3+4+5
# t = 0
# for i in "12345":
#       t += int(i)
# print(t)      

# name = input("Enter name to count : ")
# a = []
# for i in name:
#       if i not in a:
#             print(f'{i} : {name.lower().count(i.lower())}')
#       a.append(i.lower())


# import random
# win_num = random.randint(1,100)
# or
# guess = 1
# win_num = 43
# game_ove = False
# while not game_ove:
#       guess_num = int(input("Guess number : ")) 
#       if guess_num == win_num:
#             print(f'You have won the match in {guess} times')
#             game_ove = True
#       elif guess_num < win_num:
#             print('Too low')
#             guess += 1
#       elif guess_num > win_num:
#             print('Too high')
#             guess += 1
#       else:
#             print('guess correct number not in negative or alpabate')

# or coad short or remove reusabilty

# guess = 1
# win_num = 43
# while True:
#       guess_num = int(input("Guess number : ")) 
#       if guess_num == win_num:
#             print(f'You have won the match in {guess} times')
#             break
#       elif guess_num < win_num:
#             print('Too low')
#       elif guess_num > win_num:
#             print('Too high')
#       else:
#             print('guess correct number not in negative or alpabate')
#       guess += 1

# =================

# function

# def odd_even(n):
#       return n%2 == 0
# print(odd_even(int(input("Enter num is evne :  "))))


# function inside function
# greater(a,b) ---> a or b
# greater(a or b, c) ---> greatest

# def greater(a,b):
#       return a if a>b else b
# # print(greater(5,4))

# def greatest(a,b,c):
#       if a > b and a > c:
#             return a
#       elif b > c and b > a:
#             return b
#       else :
#             return c
# # print(greatest(5,4,3))

# def new_greatest(a,b,c):
#       return greater(greater(a,b),c)
# print(new_greatest(12,10,11))


# Define is_palindrome function that take one word in string as input

# def is_palindrome(name):
#       return name == name[::-1]
# print(is_palindrome(input("To check palindrome enter string : ")))

# Fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 ....when n = 11

# while True: # to break press Ctrl + 'c'
#       a,b = 0,1
#       num = int(input("Enter num otherwise press '0' to exit : "))
#       if num == 0:
#             break
#       elif num == 1:
#             print("Enter atleast two numbers.")
#       elif num == 2:
#             print(a,b)
#       else:
#             print(a,b, end=" ")
#             for i in range(num-2):
#                   t = a+b
#                   a = b
#                   b = t
#                   print(b, end = " ")
#       print("\n")

# or using function

# def fibonacci_Series():
#       while True: # to break press Ctrl + 'c'
#             a,b = 0,1
#             num = int(input("Enter num otherwise press '0' to exit : "))
#             if num == 0:
#                   break
#             elif num == 1:
#                   print("Enter atleast two numbers.")
#             elif num == 2:
#                   print(a,b)
#             else:
#                   print(a,b, end=" ")
#                   for i in range(num-2):
#                         t = a+b
#                         a = b
#                         b = t
#                         print(b, end = " ")
#             print("\n")          
# fibonacci_Series()


# default paramenter- you should compulsory make last parameter as default

# def user_info(fn, ln = 'unknown', age=None):
#       print(f"{fn} {ln} {age}")
# user_info("harish")
# user_info("harish","ojha")
# user_info("harish","ojha",25)

# Scope of variable

# x = 10  # global variable
# def func1():
#       x = 7 # local variable
#       print(x)
# def func2():
#       print(x)
# func1()
# func2()
# func1()


# x = 10  # global variable
# def func1():
#       global x
#       x = 7 # local variable
#       print(x)
# def func2():
#       print(x)
# func1()
# func2()
# func1()


# x = 10 # global variable
# def func1():
#       global x
#       x = 7 # local variable
#       print(x)
# def func2():
#       print(x)
# func2()
# func1()
# func2()

# ===================
# list
# mutable
# data structures 
# ordered collection of items
# you can store anything in lists int, float, string

# numbers = [1, -2 , 2.0, 5j, None, 'hello', True, [1,2,3,4,6]]

# print(numbers[:])
# for i in numbers:
#       print(f'{i} : {type(i)}')

# numbers[1]='Two'
# print(numbers[::-1])

# numbers[2:] = "Three"   # breaking of string
# print(numbers)

# numbers[2:] = ['one', 'two', 'three']  # breaking of list
# print(numbers)

# how to add items to our list
# li = ['a','b','c','d']
# print(li)

# li[:] = ['e','f']
# print(li)   # ['e','f']

# li[1:] = ['e','f']
# print(li) # ['a', 'e', 'f']

# li[3:] = ['e','f']
# print(li)   # ['a', 'b', 'c', 'e', 'f']

# li[4:] = ['e','f']
# print(li) # ['a', 'b', 'c', 'd', 'e', 'f']

# li[:1] = ['e','f']
# print(li)   # ['e', 'f', 'b', 'c', 'd']

# li[:2] = ['e','f']
# print(li)   # ['e', 'f', 'c', 'd']

# li[:3] = ['e','f']
# print(li)   # ['e', 'f', 'd']

# li[:4] = ['e','f']
# print(li)   # ['e','f']

# li[1:1] = ['e','f']
# print(li)   # ['a', 'e', 'f', 'b', 'c', 'd'] confuse

# li[1:2] = ['e','f']
# print(li)   # ['a', 'e', 'f', 'c', 'd']

# li[1:3] = ['e','f']
# print(li)   # ['a', 'e', 'f', 'd']

# li[1:4] = ['e','f']
# print(li)   # ['a', 'e', 'f']


# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]

# l1.append(l2)
# print(l1) # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]

# l1.extend(l2)
# print(l1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(l1+l2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# delete data from list elements

# l1 = [1,2,3,4,5]

# print(l1.pop()) # 5
# print(l1) # [1,2,3,4]

# print(l1) # [1,2,3,4,5] delete by index
# del l1[2] # del operator
# print(l1) # [1, 2, 4, 5]

# l1 = ['apple', 'banana', 'cheeku', 'dry fruits']
# print(l1) # delete by value
# l1.remove('banana')
# print(l1)

# li = ['apple','banana','grapes','mango','papaya','guava','peach']
# print('banana' in li) # True
# print('litchi' in li) # False

# some of the mehtod

# li = ['apple','banana','grapes','apple','mango','papaya','guava','peach']
# print(li.count('apple'))
# print(li.sort())
# print(li)

# print(sorted(li))
# print(li)

# print(li[::-1]) # reverse order of original list

# l = li.copy()
# print(l)
# li.clear()
# print(li)
# print(l)

# Compare lists

# li1 = ['apple','banana','grapes','peach']
# li2 = ['apple','mango','papaya','guava']
# li3 = ['apple','mango','papaya','guava']
# print(li3 == li2) # True chk according value
# print(li3 is li2) # False chk according memory location

# ===================
# Exercise:
# ls = [
#   {'Name':'harish'},
#   {'Age':25},
#   {'Songs':['s1','s2','s3']},
#   {'Movies':('M1','M2','M3')},
#   {'Class':{1:'One',2:'Two',3:'Three'}},
#   (1,2,3),
#   [4,5,6]
# ]
# for i in ls:
#   if type(i)==dict:
#     for k,v in i.items():      
#       if type(v)==dict: 
#         print(f'{k}--->')
#         for ke,vl in v.items():
#           print(f'      {ke}--->{vl}')
#       elif type(v)==list or type(v)==tuple:
#         print(f'{k}--->')
#         for i in v:
#           print(f'     {k} {v.index(i)+1} --> {i}')
#       else:
#         print(f'{k}--->{v}')
#   else:
#     print(i)

# ====================

# Take value runtime in list

# l = list(range(4))
# print(l)
# for i in l:
#       l[i] = input('Enter list items : ')
# print(l)

# ============

# Join() and split() methods

# user_info = 'Harish 24'.split() # split from spaces
# print(user_info)

# user_info = 'Harish,24'.split(',') # split form comma
# print(user_info)

# name, age = input("Enter name and age : ").split()
# print(f'Name = {name}, Age={age}')

# user_info = ['Harish', '24'] # 24 must be string only not int
# print(','.join(user_info)) # join using comma
# print(' '.join(user_info)) # join using space
# print(', '.join(user_info)) # join using comma + space

# ===================

#  looping in list

# fruits = ['orange', 'Apple', 'Banana', 'Grapes', 'Pineapple', 'Papaya']

# for f in fruits:
#       print(f)

# for f in range(len(fruits)):
#       print(fruits[f])

# i = 0
# while i<len(fruits):
#       print(fruits[i])
#       i+=1

# ==================

# list inside list
# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# print(matrix[2])

# for sublist in matrix:
#       for i in sublist:
#             print(i, end = " ")

# print(matrix[1][1])

# print(type(matrix))

# ====================

# create list with range function
# l = list(range(10,110,10))
# print(l)
# print(l.pop())
# print(l)
# print(l.index(50))

# num = [1,2,3,4,5,63,3,4,51,2,3,5,1,8,96,4,2,21]
# f = 0
# f = num.index(3,f+1,len(num))
# print(f)

# =====================

# list with function

# def negativeList(l):
#       li = []
#       for i in l[::-1]:
#             li.append(i)
#       return li


# def negativeList(l):
#       return l[::-1]


# def negativeList(l):
#       li = []
#       for i in range(len(l)):
#             li.append(l.pop())
#       return li


# def negativeList(l):
#       l.reverse()
#       return l


# def negativeList(l):
#       li = []
#       for i in l:
#             li.append(-i**2)
#       return li

# l = list(range(1,11))
# print(negativeList(l))

# ===================
# Exercise:
# ['abc','tuv','xyz']---->['cba', 'vut', 'zyx']


# def reverseList(ls):
#       return ls[::-1]

# ls = ['abc','tuv','xyz']
# print(reverseList(ls))  # ['xyz', 'tuv', 'abc']


# def reverseList(ls):
#       ls.reverse()
#       return ls

# ls = ['abc','tuv','xyz']
# print(reverseList(ls))  # ['xyz', 'tuv', 'abc']


# def reverseList(ls):
#       l = []
#       for i in ls:
#             l.append(i[::-1])
#       return l

# ls = ['abc','tuv','xyz']
# print(reverseList(ls))  # ['cba', 'vut', 'zyx']

# =============

# Exercise
# [1,2,3,4,5,6,7,8,9] ---->[[1,3,5,7,9],[2,4,6,8]]

# def filterOddEven(l):
#       even_l, odd_l = [], []
#       for i in l:
#             if i%2 == 0:
#                   even_l.append(i)
#             else : 
#                   odd_l.append(i)
#       return [odd_l, even_l]

# l = list(range(1,11))
# print(filterOddEven(l))

# =====================

# input --- [1,2,5,8], [1,2,7,6]
# ouput --- [1,2]


# def common_List(l1,l2):
#       l = []
#       for i in l1:
#             if i in l2:
#                   l.append(i)
#       return l
# l1, l2 = [1,2,5,8], [1,2,7,6]
# print(common_List(l1,l2))

# OR

# l1,l2 = [1,2,3,4],[5,2,1,6]
# print([i for i in l1 if i in l2])

# =====================
# Exercise : [1,3,5,7,9], [2,4,6,8]---------> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def add_odd_even(l1,l2):
#       l = []
#       l = l1+l2
#       l.sort()
#       return l
      # or
#       return sorted(l1+l2)

# l1, l2 = [1,3,5,7,9], [2,4,6,8]
# print(add_odd_even(l1,l2))

# ================

# input = [1,2,3,[1,2],[3,4]]
# output = 2 list are present inside a list

# def chk_list_inside_list(l):
#       count = 0
#       for i in l:
#             if type(i) == list:
#                   count += 1
#       return f'{count} list(s) are present'

# l = [1,2,3,[1,2],[3,4]]
# print(chk_list_inside_list(l))

# ==================

# tuples are immutable
# once created then can't be change
# tuples are faster than Lists
# no pop, no remove, no insert
# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# Some functions that you can use with tuples

# mixed = (1,2,3,4,5)
# for i in mixed:
#       print(i)


# num = 1; print(type(num))
# numtup = 1, ; print(type(numtup))
# numt = 1,2,3,4 ;print(type(numt))


# f = ('Apple', 'Banana', 'Grapes')
# f1, f2, f3 = f
# print(f1,f2,f3, sep = '\n')
# f1 = f2 = f3 = f
# print(f1,f2,f3, sep = '\n')


# fruits = ('Apple', 'Banana', ['Papaya', 'Grapes','Pineapple'], 'Pear', 'Water melon')
# print(fruits)     # ('Apple', 'Banana', ['Papaya', 'Grapes', 'Pineapple'], 'Pear', 'Water melon')
# fruits[2].pop()
# print(fruits)     # 'Apple', 'Banana', ['Papaya', 'Grapes'], 'Pear', 'Water melon')
# fruits[2].append("We Made it")
# print(fruits)     # ('Apple', 'Banana', ['Papaya', 'Grapes', 'We Made it'], 'Pear', 'Water melon')

# =================================

# function returning two values

# def func(int1,int2):
#       add = int1 + int2
#       mul = int1 * int2
#       return add, mul
# print(func(2,3))      # (5, 6)
# add, mul = func(4,3)
# print(add,mul,sep="\n") 
# 7
# 12

# =======================

# nums = str((1,2,3,4,5,6))
# print(nums) # (1, 2, 3, 4, 5, 6)
# print(type(nums))  # <class 'str'>

# nums = str([1,2,3,4,5,6])
# print(nums) # [1, 2, 3, 4, 5, 6]
# print(type(nums)) # <class 'str'>


# =======================

# Dictionaries

# user = {'name':'Harish', 'Age':25}
# print(user)
# print(type(user))

# user1 = dict(name = 'Harish', Age = 25)
# print(user1)
# print(type(user1))
# print(user1['name'])
# print(user1['Age'])

# Dictionary can store any type of data e.g. numbers, string , list, dictionary

# user_info = {
#       'user1' : {
#             'name' : 'Harish Ojha',
#             'Age' : 25,
#             'Movies' : ['Koi mil gaya', 'Jaal']
#       },
#       'user2' : {
#             'name' : 'Dayanand Ojha',
#             'Age' : 24,
#             'Movies' : ['Tare Jami per','Kaal']
#       },
#       'user3' : dict(
#             name = 'Komal Ojha',
#             Age = 26,
#             Movies = ['Koko', '3 Idiot']
#       )
# }

# for i, j in user_info.items():
#       print(f"Value of {i} : ")
#       for k,l in j.items():            
#             if type(l)==list:
#                   print(f'                {k}:')
#                   for i in l:
#                         print(f'                      {l.index(i)+1}: {i}')
#             else:
#                   print(f"                {k} = {l}")
#       print()

# =====================
# Project:
# How to add data to blank dictionary runtime

# user_info = {}
# for i in range(1,4):
#       fn = input(f'Enter field {i} name : ')
#       fv = input(f'Enter field\'s {i} value : ')
#       user_info[fn] = fv
#       if fv == 'list':
#             f = []
#             for j in range(2):
#                   f.append(input(f'              Enter {fn} : '))
#             user_info[fn] = f
      
#       print()

# for i, j in user_info.items():
#       print(f"Value of {i} = {j} ")

# OR

# def user_info(ch):
#       f = int(input("How many fields do you want enter : "))
#       user_detials = {}
#       for i in range(1,f+1):
#             field, name = input(f"{i} : Enter fields and field\'s name using '-' seperated --->\n\t").split('-')
#             if name == 'list':
#                   name = list(range(int(input('How many items do you want enter in the list : '))))
#                   for item in name:
#                         name[item]=input(f'Enter item {item+1} : ')
#             user_detials.update({field:name})       
#       print()           
#       return user_detials

# ch = input("Do you want Enter user's details press 1, otherwise press (q/Q) to quit : ")
# while not ch == 'q' or ch =='Q':
#       for k,v in user_info(ch).items():
#             print(f'{k} : {v}')    
#       print('-------------------------------------')
#       ch = input("Do you want Enter details of user press enter otherwise '(q/Q) : ")

# =========================

# user_info = {
#       'Name':'Harish',
#       'Age':25
# }       
# if 'Name' in user_info: # check for key only not value, you pass key
#       print('Present')
# else:
#       print('Not present')


# if 'Name' in user_info.keys(): # check for key only not value, you pass value
#       print('Present')
# else:
#       print('Not present')


# if 'Harish' in user_info: # check for key only not value, you pass value
#       print('Present')
# else:
#       print('Not present')


# if 'Harish' in user_info.values(): # if you want to check through value then use user_info.values() instead user_info.
#       print('Present')
# else:
#       print('Not present')


# Using loop access all keys and values saparately

# for i in user_info:
#       print(i)
      
# for i in user_info.keys():
#       print(i)
      
# for i in user_info.values():
#       print(i)

# check type
# print(type(user_info.keys()))       # <class 'dict_keys'>
# print(type(user_info.values()))     # <class 'dict_values'>


# # items() method
# print(user_info.items())      # dict_items([('Name', 'Harish'), ('Age', 25)])
# print(type(user_info.items()))      # <class 'dict_items'>

# for k, v in user_info.items(): # unpacking tuples inside dictionary
#       print(f'key is {k} and value is {v}')

# =========================

# user_info = {
#       'Name':'Harish',
#       'Age':25,
#       'song':'koi mil gaya',
#       'movies':'3 Idiot'
# }       
# print(user_info)
# user_info['Songs'] = ['Tara ram', 'Jaadoo teri nazar', 'koi mil gaya']
# print(user_info)
# print(user_info.pop('Songs')) # pop() method required one argument only in dictionary but not in list
# print(type(user_info.pop('Age')))
# print(user_info)

# print(user_info.popitem())    # Returning tuple, Always delete last item
# print(type(user_info.popitem())) # <class 'tuple'>
# print(user_info)  # Returning dictionary

# ==================
# Update() method

# user_info = {
#       'Name':'Harish',
#       'Age':25,
#       'song':'koi mil gaya',
#       'movies':'3 Idiot'
# }   
# more_info = {
#       'Name' : 'Komal',
#       'roll_no' : '0919cs',
#       'Country' : 'India',
#       'Mobile' : 8958888888
# }
# print(user_info.update(more_info))
# print(user_info)

# user_info.update({})
# print(user_info) # don't delete

# ====================
# If you want insert same value to the different keys then use fromkeys() method
# fromkeys() method - use to create dictionary

# d = {'Name':'unknown', 'Age': 'unknown'}

# d = dict.fromkeys(['Name', 'Age', 'Email', 'Mobile_no'],'unknown') # with list
# print(d)

# d = dict.fromkeys(('Name', 'Age', 'Email', 'Mobile_no'),'unknown') # with tuple
# print(d)

# d = dict.fromkeys(range(1,11),'unknown')
# print(d)

# you can also access key using get() method
d = {'Name':'unknown', 'Age': 'unknown'}

# print(d['Name'])  # unknown
# print(d.get('Age'))     # unknown
# print(d.get('song'))    # None

# if 'Name' in d:
#       print("Present")
# else:
#       print('Not Present')
#       # Or
# if d.get('Name'):
#       print("Present")
# else:
#       print('Not Present')


# d = {'Name':'unknown', 'Age': 'unknown'}
# d1 = d
# # d1 = d.copy()
# d.clear()
# print(d,d1,sep="\n")


# d = {'Name':'unknown', 'Age': 'unknown'}
# d1 = d      # key and value both same as addresses
# print(d1 == d)    # True, check value
# print(d1 is d)    # True, check address
# print(d.__dir__)  # <built-in method __dir__ of dict object at 0x024D64E0>
# print(d1.__dir__) # <built-in method __dir__ of dict object at 0x024D64E0>


# d = {'Name':'unknown', 'Age': 'unknown'}
# d1 = d.copy()     # value same but different addresses
# print(d1 == d)    # True, check value
# print(d1 is d)    # False, check address
# print(d.__dir__)  # <built-in method __dir__ of dict object at 0x021E64E0>
# print(d1.__dir__) # <built-in method __dir__ of dict object at 0x021E64B0>

# ====================

# More about get() method
# user = {'name':'Harish','Age':25}
# print(user.get('name'))
# print(user.get('names','not present'))


# user = {'Age':25, 'name':'Harish', 'Age':20}
# print(user.get('Age')) # 20, take last value for same key

# =================
# Exercise Cube
# def cube_finder(n):
#       cube = {}
#       for i in range(1,n+1):
#             cube[i] = i**3
#       return cube
# print(cube_finder(5))

# ========================

# Word Counter

# def wordCount(name):
#       t = 0
#       s = ''
#       for i in name.replace(' ',''):
#             if i.lower() not in s: 
#                   t = name.lower().count(i.lower())
#                   print(f'{i} : {t}')
#                   s += i.lower()
# wordCount('Harish OjHa')

# OR

# def char_count(name):
#   name = name.lower()
#   t=0
#   r = ''
#   for c in name.replace(' ',''):
#     if c not in r:
#       t=name.count(c)
#       print(f'{c} : {t}')
#       r+=c

# char_count('Harish OjHA')


# With Dictionary

# def wordCount(name):
#       d ={}
#       for i in name.replace(' ',''):
#             d[i.lower()] = name.lower().count(i.lower())
#       return d
# print(wordCount('Harish OJHA'))

# OR

# def char_count(name):
#   name=name.lower()
#   d={}
#   for i in name.replace(' ',''):
#     d.update({i:name.count(i)})
#   return d
# print(char_count('Harish Ojha'))

# =======================
# Exercise

# d = {}
# key = ['Name', 'Age', 'Songs', 'Movies']
# for i in key:
#       d[i] = input(f'Enter {i} : ')
# for j,k in d.items():
#       print(f'{j} : {k}')

# ======================================

# Set data type
# unordered collection of unique item

# s = {1,2,3,4,5,2,4,3,5}
# print(s)

# remove duplicate
# l = [1,2,3,5,1,2,5,7,3,1]
# print(l)
# l2 = list(set(l)) # remove duplicate
# print(l2)

# s = {5,1,2,3,4,12,0}
# print(s)    # {0, 1, 2, 3, 4, 5, 12} sorted in ascending order
# # s.add([6,7])  # Error unhashable type 'list' you can't store list and dictionary
# s.add(3)
# s.add(4)
# s.add((1,2,9,8))
# print(s)
# s.remove(3)
# # s.remove(11) # Give error, because don't have but you can use discard() method instead
# s.discard(11) # Don't give error, and can't discard 11 because 11 isn't present in set
# print(s)
# s1 = s.copy()
# s.clear()
# print(s,s1,sep='\n')

# s = {'a','b','c'}
# if 'a' in s:
#       print('present')
# else:
#       print('not present')

# s = {'a','b','c'}
# for i in s:
#       print(i)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(s1 | s2) # Union  {1, 2, 3, 4, 5, 6, 7, 8}
# print(s1 & s2) # Intersection  {4, 5}
# print(s1^s2)  # Union-Interection  {1, 2, 3, 6, 7, 8}

# ===========================
# List Comprehension

# print([i**2 for i in range(1,11)])

# print([-i for i in range(1,11)])

# s = ['Harish','Dayanand','Komal']
# print([i[0] for i in s])

# l = ['abc','tuv','xyz']
# print([ i[::-1] for i in l])  # ['cba', 'vut', 'zyx']

# List Comprehension with if statement
# print('even_nums : ', [i for i in range(1,11) if i%2==0])

# # Exercise:
# l = [1,1.2,True,[11,22,33],'hello']
# print([str(i) for i in l if (type(i) == int or type(i) == float)])


# List comprehension with if-else
# print([i*2 if i%2==0 else -i for i in range(1,21)])
      # [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20, -11, 24, -13, 28, -15, 32, -17, 36, -19, 40]

# List comprehension in nested list
# print([[j for j in range(1,4)] for i in range(3)])
      # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# print([[j+3*(i-1) for j in range(1,4)] for i in range(1,4)])
      # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Dictionary comprehension
# print({i:i**2 for i in range(1,11)})

# we want, square of 2 is 4 .................

# for k,v in {f'Square of {i}' : i**2 for i in range(1,11)}.items():
#       print(f'{k} : {v}')
# OR
# for k,v in {i:i**2 for i in range(2,9)}.items():
#   print(f'Square of {k} : {v}')

# Count character using dictionary comprehension
# name = 'HarisH OjhA'
# print({i.lower() : name.lower().count(i.lower()) for i in name})

# name='Harish OJHA'
# print({f'{ch}':name.lower().count(ch) for ch in name.replace(' ','').lower()})


# Sets Comprehension--- unordered
# print({k**2 for k in range(1,11)})
# print({name[0] for name in ['Ha', 'Ka', 'Ja']})

# =====================
# Make flexible function( * args)

# def total(a,b):
#       return a+b
# print(total(2,3))

# def all_total(sq, *args): # Receving arguments as tuple 
#       s = 0
#       print(args) # printing tuple
#       for i in args:
#             s += i
#       return f'Square of {s} is {s**sq}'
# print(all_total(2,2,3,4,5,6)) # Square of 20 is 400
# print(all_total(2))     # Square of 0 is 0


# Args as argument(unpacking)

# def multiply_nums(*args): # Receving arguments as tuple
#       multiply = 1
#       print(args) # printing list in tuple
#       for i in args:
#             multiply *= i
#       return multiply
# nums = [2,3,4]
# print(multiply_nums(*nums))   # Unpack, here
# nums = (2,3,4)
# print(multiply_nums(*nums))   # Unpack, here
# # OR
# print(multiply_nums(*(2,3,4)))  # Unpack, here
# print(multiply_nums(*[2,3,4]))  # Unpack, here

# print([1,2,3])    # [1, 2, 3]
# print(*[1,2,3])   # 1 2 3

# =================
# Exercise:
# def to_power(p, *num):
#       l = []
#       print(f'We want to power {p} of each numbers that are present in {num}')
#       if num:
#             for i in num:
#                   l.append(i**p)
#             return l
#       else:
#             return 'Hey you didn\'t pass any argument'      
# num = []
# print(to_power(3,*num))
# print()
# num = [1,2,3]
# print(to_power(3,*num))


# Using list comprehension
# def to_power(p, *num):
#       return ([i**p if num else 'Hey you didn\'t pass any argument' for i in num])

# num = []
# print(to_power(3,*num))
# print()
# num = [1,2,3]
# print(to_power(3,*num))

# ==========================

# Kwargs(Keyword arguments) only for dictionary

# def func(msg, **kwargs):
#       print(type(kwargs))
#       for k,v in kwargs.items():
#             print(f'{msg} >>>>> {k} : {v}')

# func('Welcome----', first_name = 'Harshit', last_name = 'Vashistha')
# d = {'First Name':'Harish','Last Name':'Ojha'}
# func('Hello.....', **d)

# =========================
# Function with all type of parameters
# PADK - Parameters, Argument, Default parameter, Kwargs

# def func(name, *args, age = 24, **kwargs):
#       print(name,args,age,kwargs,sep='\n')      
# func('Harish', 1,2,3, a=1,b=2)

# ====================
# Exercise:

# def return_first_letter_capital(*args):
#     capital_letters = [(i[0].upper()+i[:0:-1])for i in args]
#     return capital_letters
# names = ['zeeshan','akram']
# print(return_first_letter_capital(*names))


# def return_first_letter(*args, reverse_str = False):
#       l = []
#       for i in args:
#             if reverse_str:
#                   l.append(i[::-1].title())
#             else:
#                   l.append(i.title())
#       return l
# li = ['har','car','dog']
# print(return_first_letter(*li, reverse_str = True))

# OR

# def return_first_letter(*args, **kwargs):
#       l = []
#       for i in args:
#             if kwargs.get('reverse_str') == True:
#                   l.append(i[::-1].title())
#             else:
#                   l.append(i.title())
#       return l
# li = ['har','car','dog']
# print(return_first_letter(*li, reverse_str = True))

# OR

# def return_first_letter(*args, **kwargs):
#       if kwargs.get('reverse_str') == True:
#             return [name[::-1].title() for name in args]
#       else:
#             return [name.title() for name in kwargs]
# li = ['har','car','dog']
# print(return_first_letter(*li, reverse_str = True))

# OR

# def reverse_word(*l, **kwargs):
#   return [c[::-1].title() if kwargs.get('reverse') else c.title() for c in l]
  
# l = ['hari','kavita','salini','ravi']
# print(reverse_word(*l,reverse = True))

# OR

# def return_first_letter(l, **kwargs):
#       if kwargs.get('reverse_str') == True:
#             return [name[::-1].title() for name in l]
#       else:
#             return [name.title() for name in kwargs]
# li = ['har','car','dog']
# print(return_first_letter(li, reverse_str = True))

# OR

# def return_first_letter(l, **kwargs):
#       return [name[::-1].title() if kwargs.get('reverse_str') else name.title() for name in l]
# li = ['har','car','dog']
# print(return_first_letter(li, reverse_str = True))

# OR
# reverse_str = input('Do you want reverse string (y/n) : ')
# print([name[::-1].title() if reverse_str == 'y' else name.title() for name in ['rat','cow','dog']])


# =================================
# lambda expression (Anonymous function)

# def add1(a,b):
#       return a+b
# print(add1(2,3))
# print(add1)    # <function add1 at 0x01DD0810>

# add2 = lambda a,b : a+b
# print(add2(3,4))
# print(add2) # No name,  <function <lambda> at 0x022594B0>

# Mostly we use lambda function with builtin, map, reduce, filter etc. functions

# multiply = lambda a,b : a*b
# print(multiply(2,3))

# Practice:

# is_even = lambda num : num%2==0
# print(is_even(2)) # True
# print(is_even(3)) # False

# To find last element of string
# last_char = lambda s : s[-1]
# print(last_char('Hari')) # i

# str_len = lambda s : True if len(s) > 5 else False
# OR
# str_len = lambda s : len(s) > 5
# print(str_len('hello')) # False
# print(str_len('welcome')) # True

# =====================

# Enumerate function
# We use enumerate function with for loop to track position of our item in iterable

# working without enumerate fucntion

# names = ['abc', 'abcd','abcde','abcdef']

# Track position without enumerate function
# pos = 0
# for name in names:
#       print(f"{pos} ----> {name}")
#       pos += 1


# Track position with enumerate function
# for pos,name in enumerate(names):
#       print(f"{pos} ----> {name}")

      # OR

# print([f'{pos} ----> {name}' for pos, name in enumerate(['a','ab','abc','abcd'])])

# Exercise : 
# def find_pos(l, target = None):
#       for pos,name in enumerate(l):
#             if name == target:
#                   return pos
#       return -1

# l = ['rajni','daya','harish']
# print(find_pos(l,'daya'))

# OR

# def find_pos(l, target = None):
#   if target in l:
#     return l.index(target)
#   return -1
# l = ['Harish','Daya','Komal']
# print(find_pos(l,'Komal'))

# OR

# def find_pos(l, target = None):
#   if target:
#     for pos, name in enumerate(l):      
#       if name == target:
#         return f'{name} is at {pos} position'
#     else:
#       return 'Can\'t find!'
#   return -1

# l = ['Harish','Daya','Komal']
# print(find_pos(l))
# print(find_pos(l,'daya'))
# print(find_pos(l,'Daya'))

# =======================

# Map() function

# num = [1,2,3,4,5]

# def square(a):
#       return a**2

# new_list = []
# for n in num:
#       new_list.append(square(n))
# print(new_list)

# OR

# print(list(map(square,num)))  # [1, 4, 9, 16, 25]

# OR

# print(list(map(lambda a: a**2, [1,2,3,4,5])))


# names = ['abc', 'abcd', 'abcde']
# print(list(map(len, names)))
# # map object is iterator
# Iterate only one time
# l = map(len,names)
# for i in l:
#       print(i) # working
# for j in l:
#       print(j) # Not working

# If you want iterate this multiple time then you must compulsory to convert it into tuple, list

# even = list(map(lambda a:a%2==0, range(1,5)))
# for e1 in even:
#       print(e1)   # Working
# for e2 in even:
#       print(e2)   # working

# print(list(map(lambda a:a%2==0, range(1,11))))  
      # [False, True, False, True, False, True, False, True, False, True]

# =======================

# Filter() function

# def is_even(a):
#       return a%2==0
# nums = list(range(1,11))
# print(list(filter(is_even, nums)))

# OR

# print(list(filter(lambda a:a%2==0, range(1,11))))

# # Iterate only one time
# even = filter(lambda a:a%2==0, range(1,11))
# for e1 in even:
#       print(e1)   # Working
# for e2 in even:
#       print(e2)   # Not working


# If you want iterate this multiple time then you must compulsory to convert it into tuple, list

# even = list(filter(lambda a:a%2==0, range(1,11)))
# for e1 in even:
#       print(e1)   # Working
# for e2 in even:
#       print(e2)   # working

# ====================
# Difference b/w map() and filter() function

# print(list(map(lambda a:a%2==0, range(1,11))))  # [False,True,False,True,False,True,False,True,False,True]
# print(list(filter(lambda a:a%2==0, range(1,11))))     # [2, 4, 6, 8, 10]

# ================
# Difference b/w iterator & iterable

# nums = [1,2,3,4]      # Iterables, list, tuple, string
# squares = map(lambda a:a**2, nums)      # Iterator

# for i in nums:
#       print(i)    # Working
# for j in nums:
#       print(j)    # Working

# for i in squares:
#       print(i)    # Working
# for j in squares:
#       print(j)    # Not Working

# Explain working
# iter() --> iterable & next() --> iterator


# nums = [1,2,3,4]
# num_iter = iter(nums)
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter,'this line not working'))


# nums = [1,2,3,4]
# squares = map(lambda a:a**2, nums)
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))


# if we print nums without iter() function then we get error
# nums = [1,2,3,4]
# print(next(nums)) # TypeError: 'list' object is not an iterator


# if we print squares with iter() function then it doesn't effect your program result would be same as without iter() fucntion

# nums = [1,2,3,4]
# squares = map(lambda a:a**2, nums)
# num_iter = iter(squares)
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# OR
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))


# To remove error you have to convert map into list or tuple, and use iter() function
# nums = [1,2,3,4]
# squares = list(map(lambda a:a**2, nums))
# num_iter = iter(squares)
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter)) # working

# =================

# Zip() function- comma separated tuples in side list

# user_id = ['User1', 'User2','User3']
# names = ['Harshit','Mohit','Rohit']
# print(list(zip(user_id, names)))
# print(dict(list(zip(user_id, names))))
# # OR
# print(dict(zip(user_id, names)))

# example = [('a',1),('b',2)]
# print(dict(example))


# user_id = ['User1', 'User2','User3']
# f_name = ['Harshit','Mohit','Rohit']
# l_name = ['Vashistha','Sharma','Dhaketa']
# print(list(zip(user_id, f_name, l_name))) # Working
# print(dict(zip(user_id, f_name, l_name))) 
#       # ValueError: dictionary update sequence element #0 has length 3; 2 is required


# l = [(1,2),(3,4),(5,6),(7,8)] # zipped
# print(*l)   # (1, 2) (3, 4) (5, 6) (7, 8)
# print(list(zip(*l)))    # [(1, 3, 5, 7), (2, 4, 6, 8)]
# l1 , l2 = zip(*l) # unzip
# print(l1)   # (1, 3, 5, 7)
# print(l2)   # (2, 4, 6, 8)

# l1 = [11,3,15,7]
# l2 = [2,4,6,8]

# l = []
# for pair in zip(l1,l2):
#       l.append(max(pair))
# print(l)    # [11, 4, 15, 8]

# OR

# print([max(p) for p in zip(l1,l2)])

# --------------------------------------

# Exercise: using list comprehension (Average)

# def averageZip(*args):
#       l = []
#       print(args)       # ([1, 2, 3], [4, 5, 6], [7, 8, 9])
#       print(*args)      # [1, 2, 3], [4, 5, 6], [7, 8, 9]
#       for p in zip(*args): # Unpacking
#             l.append(sum(p)/len(p))
#       return l

# l1,l2,l3 = [1,2,3],[4,5,6],[7,8,9]

# print(averageZip(l1,l2,l3))   # [4.0, 5.0, 6.0]

# # OR

# print([sum(p)/len(p) for p in zip(l1,l2,l3)])   # [4.0, 5.0, 6.0]

# OR

# average_finder = lambda *args : [sum(p)/len(p) for p in zip(*args)]
# print(average_finder(l1,l2,l3))     # [4.0, 5.0, 6.0]

# ===========================

# any() and all() function

# print(all([True, True, True, True, True]))      #-->True
# print(all([True, True, True, True, False]))      #-->False

# print(any([True, True, True, True, True]))      #-->True
# print(any([True, True, True, True, False]))     #--> True
# print(any([False, False, False, False, False])) #-->False

# num1 = [2,4,6,8,10]
# num2 = [1,2,3,4,5,6]

# evens1 = []
# for num in num1:
#       evens1.append(num%2==0)
# print(evens1)
# print(all(evens1))

# OR

# print(all([num%2==0 for num in num1]))

# For most use of any & all try below example
# def my_sum(*args):
#       if all([(type(i) == int or type(i) == float) for i in args]):
#             total = 0
#             for num in args:
#                   total+=num
#             return total
#       else:
#             return 'Wrong Output'
# t1 = 10,20.5
# print(my_sum(*t1))      # Unpacking

# t2 = 10,20.5,'he'
# print(my_sum(*t2))      # Unpacking

# OR

# def sum_of_right_input(*args):
#   return sum([t for t in args]) if all([type(i)==int or type(i)==float for i in args]) else 'wrong input'
# l1 = [1,3.3]
# print(sum_of_right_input(*l1))
# l1 = [1,3.3,'sss']
# print(sum_of_right_input(*l1))

# ==========================

# Advance min() and max()


# def length(item):
#       return len(item)
# names = ['Harish Ojha', 'Mohit', 'ab','z']
# print(max(names, key = length))     # Harish Ojha
# print(min(names, key = length))     # z

# # OR using lambda function

# names = ['Harish Ojha', 'Mohit', 'ab','z']
# print(max(names, key = lambda i : len(i)))     # Harish Ojha
# print(min(names, key = lambda i : len(i)))     # z
# # key is inbuild parameter

# print(max('harish','komal','daya', key = lambda l : len(l)))     # Harish

# Example

# students_1 = {
#       'Harish' : {'score':90,'age':24},
#       'Raheem' : {'score':74,'age':19},
#       'Jeetesh' : {'score':80,'age':23}
# }
# print(max(students_1, key = lambda item : students_1[item]['score']))

# students_2 = [
#       {'name':'Raaj', 'score':40,'age':21},
#       {'name':'Reshma', 'score':54,'age':25},
#       {'name':'Jeetendra', 'score':90,'age':20}
# ]

# print(max(students_2, key = lambda item: item['score']))
# print(max(students_2, key = lambda item: item['score'])['name'])
# print(max(students_2, key = lambda item: item['age'])['name'])
# # # OR
# print(max(students_2, key = lambda item: item.get('score')))
# print(max(students_2, key = lambda item: item.get('score')).get('name'))
# print(max(students_2, key = lambda item: item.get('age')).get('name'))

# ========================================

# Sorted method

# fruits = ['grapes', 'mango', 'apple'] # list, mutable
# print(fruits)
# print(sorted(fruits))
# print(fruits)
# fruits.sort()
# print(fruits)

# fruits = ('grapes', 'mango', 'apple') # tuple, immutable
# print(fruits)     # ('grapes', 'mango', 'apple')
# print(sorted(fruits))   # ['apple', 'grapes', 'mango']
# print(sorted(fruits, reverse=True)) # ['mango', 'grapes', 'apple']
# print(fruits)     # ('grapes', 'mango', 'apple')


# guitars = [
#       {'model':'yamaha f310','price':8400},
#       {'model':'faith naptune','price':50000},
#       {'model':'faith apollo venus','price':35000},
#       {'model':'taylor 814ce','price':450000}
# ]
# print(sorted(guitars, key = lambda d:d['model'], reverse = True))
# print()
# for i in sorted(guitars, key = lambda d:d['model'], reverse = True):
#       print(f'Item {guitars.index(i)+1} ', end = ':')
#       tab ='  '
#       for k,v in i.items():
#             print(f'{tab}{k} --> {v}')
#             tab*=5

# Output:
# Item 1 :  model --> yamaha f310
#           price --> 8400
# Item 4 :  model --> taylor 814ce
#           price --> 450000
# Item 2 :  model --> faith naptune
#           price --> 50000
# Item 3 :  model --> faith apollo venus
#           price --> 35000

# ===================
# More about function
# What are doc strings
# how to write doc string
# how to see doc strings
# what is help function

# def add(a,b):
#       '''This function takes 2 numbers and return their sum '''
#       return a+b
# print(add.__doc__)
# print(add(2,3))

# You can read docstrings of many functions like sum, len, max, min, sorted
# print(f'Len() : {len.__doc__}')
# print()
# print(f'Sum() : {sum.__doc__}')
# print()
# print(f'Max() : {max.__doc__}')
# print()
# print(f'Min() : {min.__doc__}')
# print()
# print(f'Sorted() : {sorted.__doc__}')


# you can use help() function

# print(f'Len() : {help(len)}')
# print()
# print(f'Sum() : {help(sum)}')
# print()
# print(f'Max() : {help(max)}')
# print()
# print(f'Min() : {help(min)}')
# print()
# print(f'Sorted() : {help(sorted)}')

# ========================

# Intro to Decorator

# def square(a):
#       return a**2
# s = square
# print(s(4)) # 16
# print(s.__name__) # square
# print(square.__name__)  # square
# print(s)    # <function square at 0x00720810>
# print(square)     # <function square at 0x00720810>

# ====================

# function as a argument

# def square(a):
#       return a**2

# l = [1,2,3,4]
# print(list(map(square , l)))  # square() function as a argument for map() function

# Now, we are creating self

# def my_map(func,l):
#       new_list = []
#       for item in l:
#             new_list.append(func(item))
#       return new_list

# print(my_map(square, l))
# print(my_map(lambda a : a**3, l))      # Using lambda expression

# Using list comprehension

# def square(a):
#       return a**2
      
# l = [1,2,3,4]

# def my_map2(func, l):
#       return [func(i) for i in l]

# print(list(my_map2(square, l)))
# print(list(my_map2(lambda a : a**3, l)))      # Using lambda expression

# ============================

# function returning function (closure)

# def outer_func():
#       def inner_func():
#             print('inside inner func')
#       return inner_func

# var = outer_func()
# var() # inside inner func
# # OR
# outer_func = outer_func()
# outer_func() # inside inner func


# def outer_func(msg):
#       def inner_func():
#             print(f'Massage is {msg}')
#       return inner_func

# var = outer_func('Welcome')
# var()       # Massage is Welcome

# outer_func = outer_func("thankyou..")
# outer_func()      # Massage is thankyou..


# Function returning function (closure) practice

# def to_power(n):
#       def calc_power(x):
#             return x**n
#       return calc_power

# cube = to_power(3)
# print(cube(5))    # 5**3 = 125


# def to_power(n):
#   def to_base(l):
#     def to_func(func):
#       return func(l,n)
#     return to_func
#   return to_base

# def square(l,n):
#   return [i**n for i in l]

# var=to_power(3)
# va = var([1,2,3,4,5])
# print(va(square))
## OR
# to_power = to_power(3)
# to_power = to_power([1,2,3,4,5])
# print(to_power(square))

# =================

# Decorators - enhance the functionality of other functions
# @ - use for decorators

# def decorator_function(any_function):
#       def wrapper_function():
#             print('This is awesome function')
#             any_function()
#       return wrapper_function

# # this is awesome function
# def func1():
#       print('This is function 1')

# # this is awesome function
# def func2():
#       print('This is function 2')

# var = decorator_function(func1)
# var()
# decorator_function = decorator_function(func2)
# decorator_function()

# Or

# func1 = decorator_function(func1)
# func1()
# func2 = decorator_function(func2)
# func2()

# Or

# func2 = decorator_function(func1)
# func2()
# func1 = decorator_function(func2)
# func1()

# --------------
# Syntactic Shogar

# def decorator_function(any_function):
#       def wrapper_function():
#             print('This is awesome function')
#             any_function()
#       return wrapper_function

# # this is awesome function
# @decorator_function
# def func1():
#       print('This is function 1')

# func1()

# # this is awesome function
# @decorator_function
# def func2():
#       print('This is function 2')
# func2()

# -----------------------

# def decorator_function(any_function):
#       def wrapper_function(*args, **kwargs):
#             print('This is awesome function')
#             any_function(*args, **kwargs)
#       return wrapper_function

# # this is awesome function
# @decorator_function
# def func1():
#       print('This is Simple function')
# func1()

# # this is awesome function
# @decorator_function
# def func2(a):
#       print(f'This is function with argument {a}')
# func2('cool')

# # this is awesome function
# @decorator_function
# def add(a,b):
#       print(f'Sum of {a} and {b} is {a+b} ')
# add(2,3)

# -----------------

# def decorator_function(any_function):
#       def wrapper_function(*args, **kwargs):
#             '''This is wrapper function'''
#             print('This is awesome function')
#             return any_function(*args, **kwargs)
#       return wrapper_function

# # this is awesome function
# @decorator_function
# def add(a,b):
#       '''This is add function'''
#       return f'Sum of {a} and {b} is {a+b} '

# print(add.__name__)     # wrapper_function
# print(add.__doc__)      # This is wrapper function


# ------------------------

# To avoid above problem use module...

# from functools import wraps

# def decorator_function(any_function):
#       @wraps(any_function)
#       def wrapper_function(*args, **kwargs):
#             '''This is wrapper function'''
#             print('This is awesome function')
#             return any_function(*args, **kwargs)
#       return wrapper_function

# # this is awesome function
# @decorator_function
# def add(a,b):
#       '''This is add function'''
#       return f'Sum of {a} and {b} is {a+b} '

# print(add.__name__)     # add
# print(add.__doc__)      # This is add function

# -------------------------

# Exercise: docstring should always be on top of defined function
# Output :
# you are calling add function
# This function takes two numbers as parameters and return their sum
# 9

# from functools import wraps

# def print_function_data(function):
#       @wraps(function)
#       def wrapper_function(*args, **kwargs):
#             print(f'You are in calling {function.__name__} function')
#             print(f'{function.__doc__}')
#             return function(*args, **kwargs)
#       return wrapper_function

# @print_function_data
# def addition(a,b):
#       '''This function takes two numbers as arguments and return their sum'''
#       return a+b

# print(addition(4,5))

# -------------------

# Exercise:

# from functools import wraps
# import time
# def calculate_time(function):
#       @wraps(function)
#       def wrapper(*args, **kwargs):
#             print(f'Executing....{function.__name__}')
#             t1 = time.time()
#             return_value = function(*args, **kwargs)
#             t2 = time.time()
#             total_time = t2 - t1
#             print(f'This function took {total_time} seconds')
#             return return_value
#       return wrapper

# @calculate_time
# def square_finder(n):
#       return [i**2 for i in range(1,n+1)]

# square_finder(1000)

# --------------------

# Exercise:

# def add_all(*args):
#       total = 0
#       for i in args:
#             total+=i
#       return total

# print(add_all(1,2,3,4,5))# working 
# print(add_all(1,2,3,4,5,[1,2,3])) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# if you want rid from 'multi data passing as argument' then, you should have to use decorator

# from functools import wraps

# def only_int_allow(function):
#       @wraps(function)
#       def wrapper(*args, **kwargs):

#             # data_types = []
#             # for arg in args:
#             #       data_types.append(type(arg) == int)
#             # if all(data_types):
#             #       return function(*args, **kwargs)
#             # else:
#             #       return 'Invalid argument'
            
#             # OR

#             # if all([type(arg) == int for arg in args]):
#             #       return function(*args, **kwargs)
#             # return 'Invalid argument'

#             # OR
            
#             return function(*args, **kwargs) if all([type(arg)==int for arg in args]) else 'Invalid argument'
#       return wrapper

# @only_int_allow

# def add_all(*args):
#       total = 0
#       for i in args:
#             total+=i
#       return total

# print(add_all(1,2,3,4,5))     # 15 
# print(add_all(1,2,3,4,5,[1,2,3])) # Invalid argument

# -------------------------
# using input type-int,float,char,str.....

# from functools import wraps
# def decorate_function(type_func):
#   @wraps(type_func)
#   def wrapper_function(*args, **kwargs):
#     print(f'This is calling {type_func.__name__} function',type_func.__doc__,sep='\n')
#     return type_func(*args, **kwargs) if all([type(i)==kwargs.get('data_type') for i in args]) else 'Invalid input'
#   return wrapper_function

# @decorate_function
# def add_list_item(*args,**kwargs):
#   '''This function takes argument'''
#   total = 0  
#   for arg in args:
#     total+=arg
#   return total

# print(add_list_item(1,22,33, data_type = str ))

# OR

# from functools import wraps
# def func_chk_data_type(data_type):
#   def decorate_function(type_func):
#     @wraps(type_func)
#     def wrapper_function(*args, **kwargs):
#       print(f'This is calling {type_func.__name__} function',type_func.__doc__,sep='\n')
#       return type_func(*args, **kwargs) if all([type(i)==data_type for i in args]) else 'Invalid input'
#     return wrapper_function
#   return decorate_function
  
# @func_chk_data_type(int) # int or str
# def add_list_item(*args):
#   '''This function takes argument'''
#   total = 0  
#   for arg in args:
#     total+=arg
#   return total

# print(add_list_item(1,22,33))

# =====================

# Generators
# -generators are iterators
# iterators and iterables-- you can change iterables into iterators

# Create your first generator with generator function
# 1) generator function

# def nums(n):
#       for i in range (1,n+1):
#             print(i)
# nums(10)


# def evenFunc(n):
#       for i in range(1,n+1):
#             if i%2==0:
#                   yield i 

# num = evenFunc(10) # generated here
# for i in num:
#       print(i)

# ====================

# Generator comprehension

# square = (i**2 for i in range(1,11))
# for i in square:
#       print(i)    # working 
# for j in square:
#       print(j)    # not working

# ------------------
# list vs generator

# l = [i**2 for i in range(10000000)] # 10 million
      # Use memory approximate 300mb for above value range

# l = (i**2 for i in range(10000000)) # 10 million
#       # it's take micro seconds

# --------------------
# Use time module
# import time

# t1 = time.time()
# l = [i**2 for i in range(10000000)]
# print(time.time()-t1)   # 24.70443820953369 sec.


# t1 = time.time()
# l = (i**2 for i in range(10000000))
# print(time.time()-t1)   # 0.0 sec.

# =====================================

# OOP - object oriented programming
# to inhance functionality of your program or a style to manage your code

# class(blue-print), object(instance), method

# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD (CONSTRUCTOR)
# WAHT ARE ATTRIBUTES, INSTANCE variables
# HOW TO CREATE OUR OBJECT

# class Person:
#     # self represent object like p1, p2, you can write anything instead of self as well as variables
#       def __init__(self, first_name, last_name, age):
#             # instance variables
#             print('Init method / constructor called')
#             self.first_name = first_name
#             self.last_name = last_name
#             self.age = age

# p1 = Person('Harish', 'Ojha', 25)
# print(p1.first_name)
# p2 = Person('Daya', 'Ojha', 24)
# print(p2.first_name)

# -----------------------

# class laptop:
#       def __init__(self, brand, model_name, price):
#             self.brand = brand
#             self.model_name = model_name
#             self.price = price
#             self.laptop_name = brand + ' ' + model_name

# lap1 = laptop('hp', 'au114tx', 63000)
# print(lap1.laptop_name)

# -----------------------

# l=[1,2,3]
# l.pop()     # here is pop() method

# Create your own method

# class Person:
#       def __init__(self, first_name, last_name, age):
#             self.first_name = first_name
#             self.last_name = last_name
#             self.age = age
#       def full_name(self):
#             return f'{self.first_name} {self.last_name}'
# p1 = Person('Harish', 'Ojha', 24)
# print(p1.full_name())
# p2 = Person('Daya', 'Ojha', 23)
# print(p2.full_name())


# Do you know what about list

# l = [1,2,3]
# print(l)
# print(l.clear())
# print(l)

# OR

# l = [1,2,3]
# print(l)
# print(list.clear(l))
# print(l)


# l = [1,2,3]
# print(l)
# l.append(10)
# print(l)

# OR

# l = [1,2,3]
# print(l)
# list.append(l, 12)
# print(l)

# Similarly for creation your own

# class Person:
#       def __init__(self, first_name, last_name, age):
#             self.first_name = first_name
#             self.last_name = last_name
#             self.age = age
#       def full_name(self):
#             return f'{self.first_name} {self.last_name}'
#       def is_above_18(self):
#             return self.age>18

# p1 = Person('Harish', 'Ojha', 24)
# print(p1.full_name())
# print(p1.is_above_18())

# p2 = Person('Daya', 'Ojha', 15)
# print(p2.full_name())
# print(p2.is_above_18())


# ----------------------

# class laptop:
#       def __init__(self, brand, model_name, price):
#             self.brand = brand
#             self.model_name = model_name
#             self.price = price
#             self.laptop_name = brand + ' ' + model_name

#       def apply_discount(self, num):
#             return self.price*(100-num)/100
            

# lap1 = laptop('hp', 'au114tx', 63000)
# print(lap1.laptop_name)
# print(lap1.apply_discount(10))

# ---------------------
# Example(1):
# class Circle:
#       pi = 3.14
#       def __init__(self, radius):
#             self.radius = radius
           
#       def calc_circumference(self):
#             return 2*Circle.pi*self.radius

# c = Circle(4)
# print(c.calc_circumference())
# cc = Circle(5)
# print(cc.calc_circumference())


# Example(2):
# class laptop:
#       discount_price = 10
#       def __init__(self, brand, model_name, price):
#             self.brand = brand
#             self.model_name = model_name
#             self.price = price
#             self.laptop_name = brand + ' ' + model_name

#       def apply_discount(self):
#             return self.price*(100-laptop.discount_price)/100
            

# lap1 = laptop('hp', 'au114tx', 63000)
# print(lap1.laptop_name)
# print(lap1.apply_discount())


# Example(3):
# class laptop:
#       discount_price = 10
#       def __init__(self, brand, model_name, price):
#             self.brand = brand
#             self.model_name = model_name
#             self.price = price
#             self.laptop_name = brand + ' ' + model_name

#       def apply_discount(self):
#             return self.price*(100-self.discount_price)/100 # here use self instead class name.
            

# lap1 = laptop('hp', 'au114tx', 63000)
# print(lap1.__dict__)
# print(lap1.laptop_name)
# print(lap1.apply_discount())

# lap2 = laptop('hp', 'au114tx', 63000)
# lap2.discount_price = 50
# print(lap2.__dict__)
# print(lap2.laptop_name)
# print(lap2.apply_discount())


# Example(4): return called instance

# class Person:
#       count_instance = 0
#       def __init__(self, first_name, last_name, age):
#             Person.count_instance += 1
#             self.first_name = first_name
#             self.last_name = last_name
#             self.age = age
            

# p1 = Person('Harish', 'Ojha', 25)
# p2 = Person('Harish', 'Ojha', 25)
# p3 = Person('Harish', 'Ojha', 25)
# print(p1.count_instance)

# We can say class variables are class attributes

# ---------------------------

# OOP class methods and difference b/w class method and instance method

class Person:
      count_instance = 0 # class variable / class attribute
      def __init__(self, first_name, last_name, age):
            Person.count_instance += 1
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

      @classmethod
      def count_instances(cls):
            return f"You have created {cls.count_instance} instances of {cls.__name__} class"

      def full_name(self):    # instance method
            return f'{self.first_name} {self.last_name}'
      def is_above_18(self):  # instance method
            return self.age>18

print(Person('hari','sh',25).full_name())
print(Person('hari','sh',25).is_above_18())

p1 = Person('Harish', 'Ojha', 24)
print(p1.full_name())
print(p1.is_above_18())

p2 = Person('Daya', 'Ojha', 15)
print(p2.full_name())
print(p2.is_above_18())

print(Person.count_instances())