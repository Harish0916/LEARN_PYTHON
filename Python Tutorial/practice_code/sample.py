# import sys
# print (sys.version)
# x=5
# y= john
# print (x)
# print (y)
# x =str(3) # x will be '3'
# y=int(3)  # y will be 3
# z =float(3) # z will be 3.0
# print(x*2)
# print(y*2)
# print(z*2)
    
# x="john"
# print(x)
# x='john'
# print(x) 

# a=4
# print(a)
# A="sally"
# print(A)

# myvar= "john"
# print(myvar)
# my_var= "john"
# print( my_var)
# _my_var= "john"
# print( _my_var)
# myVar= "john"
# print( myVar)
# MYVAR= "JOHN"
# print(MYVAR)
# myvar2= "john"
# print(myvar2)

# 2myvar="john"
# print(2myvar)
# my-var="john"
# print(my-var)
# my var="john"
# print(my var)

# x,y,z="Orange","Banana","Cherry"
# print(x)
# print(y)
# print(z)
# x=y=z="Orange"
# print(x)
# print(y)
# print(z)
# fruits=["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x="python is awesome"
# print(x)
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x=5
# y="john"
# print(x+y)
# x = 5
# y = "John"
# print(x + y)
# x = 5
# y = "John"
# print(x, y)

# x=5
# print(type(x))
# y=5.5
# print(type(y))
# s=5j
# print(type(s))

# x = 1
# y = 2.8 
# z = 1j 
# print(type(x))
# print(type(y))
# print(type(z))

# x = 1
# y = 35656222554887711
# z =-3255522
# print(type(x))
# print(type(y))
# print(type(z))

# fruits = ("apple", "banana", "cherry")
# print(fruits * 2)
# ---------------------


# list1 = ["abc", 34, True, 40, "male"]
# print(list1)
# -----------------------------------------------!
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))
# --------------------------------------------!/
# thislist = list(("apple", "banana", "cherry")) # note the double
# print(thislist)
# --------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# print(thislist[0])
# --------------------------------------------!

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-2])
# -----------------------------------!
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon",
# "mango"]
# print(thislist[2:5])
# ----------------------------------------------------!
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon",
#  "mango"]
# print(thislist[:4])
# -------------------------------------------------------------------------!
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon",
#  "mango"]
# print(thislist[2:])
# ---------------------------------------------------------!
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon",
#  "mango"]
# print(thislist[-4:-1])
# -----------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# if "cherry" in thislist:
#     print("Yes, 'cherry' is in the fruits list")
# ------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist[0] = "blackcurrant"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# -------------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
# ---------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist[0:2] = ["watermelon"]
# print(thislist)
# -----------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "watermelon")
# print(thislist)
# --------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
# ------------------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)
# ------------------------------------------!

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
# --------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# ------------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
# =============================================================!
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("apple")
# print(thislist)
# ----------------------------------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(2)
# print(thislist)
# ---------------------------------------------------!
# thislist = ["apple", "banana", "cherry"]
# # thislist.pop(0)
# print(thislist)
# -----+++++++++++++++++++++++++++++++++++++++++++++++++++++!/

# thislist = ["apple", "banana", "cherry"]
# del thislist[2]
# print(thislist)
# ------------------------------------------------------------!'
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
# ---------------------------------------------------------!

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
    
#     print(x)

# function definition
# def sum():
   
#     a,b,c,d,e = map(int, input().split())
#     avg = (a+b+c+d+e)//5
#     print(avg)

# # function calling
# sum()

# Argumented function

# def calc():
#     a,b = map(int, input("Enter two numbers: ").split())
#     op = input("Enter Operator(+,-,*,/): ")

#     if(op=="+"):
#         print(a+b)
#     elif(op=='-'):
#         print(a-b)
#     elif(op=='*'):
#         print(a*b)
#     elif(op=='/'):
#         print(a/b)
#     else:
#         print("try again")

# calc()  # function calling
    


# def calc(a,b, op):
#     if(op=="+"):
#         print(a+b)
#     elif(op=='-'):
#         print(a-b)
#     elif(op=='*'):
#         print(a*b)
#     elif(op=='/'):
#         print(a/b)
#     else:
#         print("try again")

# #function calling with arguments      
# a,b = map(int, input("Enter two numbers: ").split())
# op = input("Enter Operator(+,-,*,/): ")
# calc(a, b, op)  # function calling
    


# def my_function(fname):     # parameters
#     print(fname + " Happy Birthday")

# my_function("Emil")     # arguments
# my_function("Tobias")
# my_function("Linus")

# def greeting(name):
#     print(f"Happy Birthday {name}")

# greeting("Meet")
# greeting("Khushi")



# def my_function(fname="rahul", lname="arya"):   # default condition
#     print(fname + " " + lname)

# my_function("Khushi", "jain")

# def my_function(fname="rahul", lname="arya"):   # default condition
#     print(fname + " " + lname)

# my_function(fname="kaushlendra", lname="bhadoriya")


# def my_function(fname="rahul", lname="arya"):   # default condition
#     print(fname + " " + lname)

# my_function(lname="bhadoriya")


# def values(*num):
#     print(num)

# values(12,13,14,15,16)

# def avg(*num):
#     av = (num[0]+num[1])/len(num)
#     print(av)

# avg(12,13)


# def avg(*num):
#     sum=0
#     for i in num:       #(12,13,14)
#         sum=sum+i
#     av=sum/len(num)
#     print(av)

# avg(12,13,14)

# def num_sum(num):
#     sum=0
#     i=1
#     while i<=num:
#         sum=sum+i
#         i+=1
#     print(sum)

# num_sum(int(input("Number:")))


# def detail(**data):
#     print(data.get('fname'))

# detail(fname="Nitin", lname="Yadav")



# def my_function(x):
#     return 5 * x
# op = my_function(12)
# print(op)
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_function(a, b, /, *, c, d):
#     print(a + b + c + d)
    
# my_function(5, 6, 8, 9, c = 7, d = 8)


# # -----LAMBDA FUNCTION-------------

# double = lambda a : a**2
# print(double(13))

# avg = lambda *a : sum(a)/len(a)
# print(avg(13,14,15))


# def double(n): 
#     return lambda a: a*n
# print(double(12)(3))


# def myfunc(n):
#     return lambda a : a * n

# # mydoubler = myfunc(2)
# # print(mydoubler(11))
# #    or
# print(myfunc(2)(11))


# def myfunc(n):
#     return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(12))


# l1 = [12,13.2,'14', 0]
# l2= [ True, False]
# l3 = ["ram", "shyam"]


# class MyClass :
#     pass

# print(type(MyClass))


# class MyClass :
#     x = 12
#     y = 13

# print(MyClass.x,MyClass.y)


def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x


print(myfunc1())









