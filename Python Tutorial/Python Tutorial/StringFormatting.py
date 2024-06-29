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

# #DataTime:
# from datetime import datetime
# print('{:%Y-%m-%d %H:%M}'.format(datetime(2019,2,15,3,25)))