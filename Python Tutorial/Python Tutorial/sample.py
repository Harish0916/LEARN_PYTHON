# a = 'Banana'
# b = 'Banana'
# print(a is b) # True, Identical
# print(a == b) # True, Equivalent

# a = b = 'Banana'  # object is aliased
# print(a is b) # True, Identical
# print(a == b) # True, Equivalent
# # In this example, Python only created one string object, and both a and b refer to it.

# -------------------
# a = (1,2,3)
# b = (1,2,3)
# print(a is b) # True, Identical
# print(a == b) # True, Equivalent

# a = b = (1,2,3) # object is aliased
# print(a is b) # True, Identical
# print(a == b) # True, Equivalent

# ---------------------
# a = [1,2,3]
# b = [1,2,3]
# print(a is b) # False, Identical
# print(a == b) # True, Equivalent

# a = b = [1,2,3] # object is aliased
# print(a is b) # True, Identical
# print(a == b) # True, Equivalent

# -------------------
# a = {1:'h', 2:'o'}
# b = {1:'h', 2:'o'}
# print(a is b) # False, Identical
# print(a == b) # True, Equivalent

# a = b = {1:'h', 2:'o'}  # object is aliased
# print(a is b) # False, Identical
# print(a == b) # True, Equivalent

# ====================
# If the aliased object is mutable, changes made with one alias aﬀect the other:
# a = b = [1,2,3]
# b[0] = 11
# print(a)

# ====================

# abs()--
# print(abs(123)) # 123
# print(abs(-123))  # 123
# print(abs(123.23))  # 123.23
# print(abs(-123.23)) # 123.23
# print(abs(123j))  # 123.0
# print(abs(123.23j)) # 123.23

# all()--
# print(all([]))  # True
# print(all([True, True]))  # True
# print(all([True, False])) # False
# print(all([False, False]))  # False

# any()--
# print(any([]))  # False
# print(any([True,True])) # True
# print(any([True,False]))  # True
# print(any([False,True]))  # True
# print(any([False,False])) # False


#  ===============================
# num = [1,2,3,4,5,63,3,4,51,2,3,5,1,8,96,4,2,21]
# f = 0
# f = num.index(3,f+1,len(num))
# print(f)
# =============
