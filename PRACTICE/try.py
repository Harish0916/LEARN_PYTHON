# try:
#     x=12
#     print(x)
# except:
#     print("An exception occurred")
# else:
#     print("No error")
# finally:
#     print("bye bye")


# x =-1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")


x = 12
if not type(x) is int:
    raise TypeError("Only integers are allowed")
else:
    print("x is ", x)