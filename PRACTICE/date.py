# import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))


# import datetime
# x = datetime.datetime(2020, 5, 17)
# print(x)
# print(x.strftime("%B"))

# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()

# for i in range(5):
#     for j in range(i):
#         print("*", end="")
#     print()

for i in range(5):
    for j in range(5-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()
