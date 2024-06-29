# abs() - used to get the absolute(positive) value
# argument may be an integer or a floating point number.
# if the argument is a complex number, its magnitude is returned.

# print(abs(-100))
# print(abs(1023))
# print(abs(123.25))
# print(abs(-2033.66))
# print(abs(3+4j))

# print(type(abs(-100)))
# print(type(1023))
# print(type(123.25))
# print(type(-2033.66))
# print(type(3+4j))

# --------------

# all() - used to test whether all elements of an iterable are ture or not.

# Example: Python all() function with Strings
# str = "Priyansh is a good boy"
# print(all(str)) #True

# # 0 is False
# # '0' is True
# str = '000'
# print(all(str)) #True

# str = ''
# print(all(str)) #True


# Python: all() example with Lists
# all values true
# num = [23, 45, 10, 30]
# print(all(num)) #True

# # all values false
# num = [0, False]
# print(all(num)) #False

# # one false value
# num = [1, 3, 4, 0]
# print(all(num)) #False

# # one true value
# num = [0, False, 5]
# print(all(num)) #False

# # empty iterable
# num = []
# print(all(num)) #True


#Python: all() example with Dictionaries

# dict = {0: 'False', 1: 'False'}
# print(all(dict)) #False

# dict = {1: 'True', 2: 'True'}
# print(all(dict)) #True

# dict = {1: 'False', 2: False} # working according keys
# print(all(dict)) #True

# dict = {1: 'True', False: 0}
# print(all(dict)) #False

# dict = {}
# print(all(dict)) #True

# # 0 is False
# # '0' is True
# dict = {'0': 'True'}
# print(all(dict)) #True


#Python: all() example with Tuple
#Test if all items in a tuple are True:
# tup = (0, True, False)
# x = all(tup)
# print(x) #False
# tup = (1, True, True)
# x = all(tup)
# print(x) #True


# Python: all() example with Set
#Test if all items in a set are True:
# sss = {0, True, False}
# x = all(sss)
# print(x) #False
# sss = (1, True, True)
# x = all(sss)
# print(x) #True

# -------------

# any() - return true if any element of the iterable is true.
# The function returns False if the iterable is empty.

# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
# print(any("Hello, how are you."))
# print(any([0]))

# Python: any() example with Strings:
# str = "Ram is good boy"
# print(any(str))

# # 0 is False
# # '0' is True
# str = '000'
# print(any(str))

# str = ''
# print(any([str]))


# Python: any() example with Lists:
# num = [23, 45, 0, 30]
# print(any(num)) #True

# num = [0, False]
# print(any(num)) #False

# num = [0, False, 5]
# print(any(num)) #True

# num = []
# print(any(num)) #False


# Python: any() example with Dictionaris:
# dict = {0: 'False'}
# print(any(dict))

# dict = {0: 'False', 1: 'True'}
# print(any(dict))

# dict = {0: 'False', False: 0}
# print(any(dict))

# dict = {}
# print(any(dict))

# # 0 is False
# # '0' is True
# dict = {'0': 'False'}
# print(any(dict))


# Python: any() example with Tuple
#Test if all items in a tuple are True:
# tup = (0, True, False)
# x = any(tup)
# print(x) #True
# tup = (2, 3, 4)
# x = any(tup)
# print(x) #True


# Python: any() example with Set
#Test if all items in a set are True:
# sss = {0, True, False}
# x = any(sss)
# print(x) #True
# sss = (1, True, True)
# x = any(sss)
# print(x) #True

# --------------------

# ascii() - returns a string containing a printable representation
# (escape the non-ASCII characters) of an object.

# the repr() function returns a string containing a printable representation
# of an object and escapes the not-ASCII characters in the string returned by
# repr() using \x,\u or \U escapes. This generates a string similar to that 
# returned by repr() in python 2

# print(ascii("русский язык"))
# print('\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a')

# py_list = ['Python', 2, 'Pythön', 3]
# print(ascii(py_list))

# ----------------

# bin() - used to convert an integer number to a binary string.
# Note: If x is not a Python int object, it has to define an __index__() method that returns an integer.

# print(bin(10))

# --------------------

# bool() - If x is false or omitted, this returns False; otherwise it returns True.
# bool is also a class, which is a subclass of int. Class bool cannot be subclassed
# further. Its only instances are False and True.

# x = bool(1)
# print(x)
# y = bool()
# print(y)

