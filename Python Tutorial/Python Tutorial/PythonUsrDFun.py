# def printt():
#     print("This is Python 3.2 Tutorial")
#     print("This is Python 3.2 Tutorial")
#     print("This is Python 3.2 Tutorial")
# printt()


# def avg_number(x, y):
#     print("Average of ",x," and ",y, " is ",(x+y)/2)
# avg_number(3, 4)


# def nsquare(x, y):
#     return (x*x + 2*x*y + y*y)
# print("The square of the sum of 2 and 3 is : ", nsquare(2, 3))
 

# def nsquare(x, y = 2):
#     return (x*x + 2*x*y + y*y)
# print("The square of the sum of 2 and 2 is : ", nsquare(2))
# print("The square of the sum of 2 and 4 is : ", nsquare(2,4))


# Keyword Arguments

# def marks(english, math = 85, science = 80):
#     print('Marks in : English is - ', english,', Math - ',math, ', Science - ',science)
# marks(71, 77)
# marks(65, science = 74)
# marks(science = 70, math = 90, english = 75)


# Arbitrary Argument List
# The arbitrary argument list is an another way to pass arguments
# to a function. In the function body, theses arguments will be 
# wrapped in a tuple and it can be defined with *args construct.
# Before this variable you can define a number of arguments or no argument.

# def sum(*numbers):
#      s = 0
#      for n in numbers:
#            s += n
#      return s

# print(sum(1,2,3,4))
# print(sum())


# Lambda Forms
# In Python, small anonymous (unnamed) functions can be created with
# lambda keyword. Lambda forms can be used as an argument to other function
# where function objects are required but syntactically they are restricted to
# a sigle experesssion. A fucntion like this.

# def average(x, y):
#     return (x+y)/2
# print(average(4,3))

# may also be defined using lambda

# print((lambda x,y : (x+y)/2)(4,3))
# # OR
# lmb = lambda x,y : (x+y)/2
# print(lmb(3,4))


# Python Documentation Strings
# In Python, a string literal is used for documenting a module,
# function, class, or method. You can access string literals by __doc__
# (notice the double underscores) attribute of the object(e.g. my_function.__doc__)

# Docstring Convetions
# -String literal must be enclosed with a triple quote.
#  Docstring should be informative
# -The first line may briefly describe the object's purpose. The line should
#  begin with a capital lettter and ends with a dot.
# -If a documentation string is a multi-line string then the second line should
#  be blank followed by any detailed explanation starting from the third line.
#  See the following example with multi-line docsting.

# def avg_number(x, y):
#     """Calculate and Print Average of two Numbers.
    
#     Created on 29/12/2012. python-docstring-example.py
#     """
#     print("Average of ",x," and ",y, " is ",(x+y)/2)

# print(avg_number.__doc__)
# print(avg_number(12,13).__doc__)