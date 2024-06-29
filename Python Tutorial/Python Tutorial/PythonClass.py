
# The basic idea behind and object-oriented programming (oop)
# is to combine both data and associated procedures (known as methods)
# into a single unit which operate on the data. Such a unit is called an object.

# Python is and object-oriented language, everything in Python is an object.

# We have already worked with some objects in Python, for example strings, lists are
# objects defined by the string and list classes which are availabel by default into Python.
# Let's declare two objects a string and a list and test their type with type() function.

# string1 = "GOOD MORNING"
# print(type(string1))

# ls = [1,12,13,4,5]
# print(type(ls))

# As string1 is and object, strings "GOOD MORNING" can produce and uppercase or lowercase version
# themselves calling upper() and lower() methods associated with the string. Check it in the Python IDLE.

# print(string1.upper())
# print(string1.lower())

# Note : To see the list of string methods execute the following command in Python IDLE 
# print(help(str))

# ----------

# Before introducing classes we must discuss something about local variables, global statement
# and a nonlocal statement as well as Namespaces and scope rules.

# Local variables
# When a variable is declared inside a function, that variable is accessible only from that function
# or statements block where it is declared. The variable has no relation with any other variable with the same
# name declared outside the function, therefore the variable is local to the function. See the following example.

# python-local-variable.py
# def function_local(a):
# 	print('a is -> ',a)
# 	a = 50
# 	print('After new value within the function a is -> ',a)
# a = 100
# function_local(40)
# print('Value of a is ->',a)


# Global statement
# The purpose of the global statement is to assign a value to a variable
# which is declared outside the function. Free variables( See Line No.42
# in the previous example) may refer to global without declaring global.
# The syntax of global statement is -> global var_name1, var_name2,....
# See the following exaple

# python-global-variable.py
# def function_local():
#         global a
#         print('a is -> ',a)
#         a = 50
#         print('After new value within the function a is -> ',a)
# a = 100
# function_local()
# print('Value of a is ->',a)

# Explanation:

# Line No.- 56 : The variable 'a' is declared as a global variable,
#               therefore the value of a is now 100. 
# Line No.- 58 : Assign the value 50 to 'a' and it will hold same value 
#               inside and outside the function unless we assign a new value.


# Nonlocal statement
# The nonlocal statement is used to rebind variables found outside of the
# innermost scope. See the following example without a nonlocal statement.

# def outside():
#        a = 10
#        def inside():
#            a = 20
#            print("Inside a ->", a)
#        inside()
#        print("outside a->", a)
# outside()

# In the above example the first print() statement simply print the value of 
# 'a', which is 20 as 'a' is local within inside() function. The second print() statement 
# prints the value 'a', which is 10 as the inside() function has no effect. Now we introduce 
# a nonlocal statement in inside() function and the code will be:

# def outside():
#        a = 10
#        def inside():
#               nonlocal a
#               a = 20
#               print("The value of a in inside() function - ", a)
#        inside()
#        print("The value of a in outside() function -  ", a)
# outside()

# The second print() statement prints the value 'a', which is 20 as the variable 'a' is rebound..

#butttt...

# def outside():
#        a = 10
#        def inside():
#               global a
#               a = 20
#               print("The value of a in inside() function - ", a)
#        inside()
#        print("The value of a in outside() function -  ", a)
# outside()
# print("The value of a globally",a)

# ----------

# Python Scopes and Namespaces:
# In general, a namespace is a naming system to create unique names. 


# ----------

# Defining a class

# In object oriented programming classes and objects are the main features.
# A class creates a new data type and objects are instances of a class
# which follows the definition given inside the class.
# 
# class Student: 
    # Statement-1 
    # Statement-1 
    # .... 
    # .... 
    # .... 
    # Statement-n
# A class definition started with the keyword 'class' followed by the
# name of the class and a colon.

# The statements within a class definition may be function definitions,
# data members or other statements.

# When a class definition is entered, a new namespace is created,
# and used as the local scope. 


# Creating a Class:
# class Student:
#     stu_class = 'V'
#     stu_roll_no = 12
#     stu_name = "David"

# Class Objects:

# There are two kind of operations class objects supports : attribute 
# references and instantiation. Attribute references use the standard syntax,
# obj.name for all attribute references in Python. Therefore if the class definition 
# (add a method in previous example) look like this

# class Student:
#     """A simple example class"""
#     stu_class = 'V'
#     stu_roll_no = 12
#     stu_name = "David"
#     def messg(self):
#             return 'New Session will start soon.'

# then Student.stu_class, Student.stu_roll_no, Student.stu_name are valid attribute reference
# and returns 'V', 12, 'David'. Student.messg returns a function object. In Python self is a 
# name for the first argument of a method which is different from ordinary function. Rather than
# passing the object as a parameter in a method the word self refers to the object itself.
# For example if a method is defined as avg(self, x, y, z), it should be called as a.avg(x, y, z).
# See the output of the attributes in Python Shell.

# print(Student.stu_class)
# print(Student.stu_roll_no)
# print(Student.stu_name)
# print(Student.messg)
# print(Student.__doc__)

# __doc__ is also a valid attribute which returns the docstring of the class.

# ------

# __init__method:

# There are many method names in Python which have special importance. 
# A class may define a special method named __init__ which does some initialization
# work and serves as a constructor for the class. Like other functions or methods __init__
# can take any number of arguments. The __init__ method is run as soon as an object of 
# a class is instantiated and class instantiation automatically invokes __init__() for the 
# newly-created class instance. See the following example a new, initialized instance can be obtained by:

#studentdetailsinit.py
# class Student:
#     """A simple example class"""
#     def __init__(self, sclass, sroll, sname):
#         self.c = sclass
#         self.r = sroll
#         self.n = sname
#     def messg(self):
#             return 'New Session will start soon.'

# x = Student('V', 12, 'Sara')
# print(x.c,x.r,x.n)


# --------------

# Inheritance

# The concept of inheritance provides an important feature to the
# Object-oriented proramming is reuse of code. Inheritance is the 
# process of creating a new class (derived class) to be based on an
# existing (base class) one where the new class inherits all the 
# attributes and methods of the existing class. Following diagram shows
# all the inheritance of a derived class from the parent(base) class. 

# like othe object-oriented language, Python allows inheritance from a 
# parent (or base) class as well as multiple inheritances in which a 
# class inherits attributes and methods from more than one parent.
# See the single and multiple inheritance syntaxes.

# class DerivedClassName(BaseClassName):
#     Statement-1 
#     Statement-1 
#     .... 
#     .... 
#     .... 
#     Statement-n
# class DerivedClassName(BaseClassName1, BaseClassName2, BaseClassName3):
#     Statement-1 
#     Statement-1 
#     .... 
#     .... 
#     .... 
#     Statement-n

# Example:

# In a company, Factory staff and Office staff have certain common properties - all 
# have a name, designation, age etc. Thus they can be grouped under a class called CompanyMember.
# Apart from sharing those common features, each subclass has its own characteristic - FactoryStaff 
# gets overtime allowance while OfficeStaff gets traveling allowance for an office job. 
# The derived classes ( FactoryStaff & OfficeStaff) has its own characteristic and, in addition,
# they inherit the properties of the base class (CompanyMember). See the example code.

# # python-inheritance.py
# class CompanyMember:
# 	'''Represents Company  Member.'''
# 	def __init__(self, name, designation, age):
# 		self.name = name
# 		self.designation = designation
# 		self.age = age
# 	def tell(self):
# 		'''Details of an employee.'''
# 		print('Name: ', self.name,'\nDesignation : ',self.designation, '\nAge : ',self.age)

# class FactoryStaff(CompanyMember):
# 	'''Represents a Factory Staff.'''
# 	def __init__(self, name, designation, age, overtime_allow):
# 		CompanyMember.__init__(self, name, designation, age)
# 		self.overtime_allow = overtime_allow
# 		CompanyMember.tell(self)
# 		print('Overtime Allowance : ',self.overtime_allow)

# class OfficeStaff(CompanyMember):
# 	'''Represents a Office Staff.'''
# 	def __init__(self, name, designation, age, travelling_allow):
# 		CompanyMember.__init__(self, name, designation, age)
# 		self.travelling_allow = travelling_allow
# 		CompanyMember.tell(self)
# 		print('Traveling Allowance : ',self.travelling_allow)


# FactoryStaff('Harish', 'Computer Engineer', 25, 250)
# OfficeStaff('Geetansh', 'Electrical Engineer', 24, 200)
