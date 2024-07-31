# for i in range(0, 5):       # Row
#     for j in range(0, 7):   # Columns
#         print("*", end="")
#     print()


# for i in range(0, 5):       # Row
#     for j in range(0, 5):   # Columns
#         print(i, end="")
#     print()



# for i in range(1, 6):       # Row
#     for j in range(1, 6):   # Columns
#         print(j, end="")
#     print()


# for i in range(1, 6):       # Row
#     for j in range(i):   # Columns
#         print("*", end="")
#     print()


# for i in range(1, 6):       # Row
#     for j in range(6-i):   # Columns
#         print("*", end="")
#     print()



# for i in range(1, 6):       # Row
#     for j in range(6-i):   # Columns
#         print(" ", end="")
#     for k in range(i):
#         print("*", end="")
#     print()



# for i in range(1, 6):       # Row
#     for j in range(6-i):   # Columns
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()



# for i in range(1, 6):       # Row
#     for j in range(i):   # Columns
#         print(" ", end="")
#     for k in range(6-i):
#         print("*", end="")
#     print()


# for i in range(1, 6):       # Row
#     for j in range(i):   # Columns
#         print(" ", end="")
#     for k in range(2*(6-i)-1):
#         print("*", end="")
#     print()



for i in range(1, 5):       # Row
    for j in range(6-i):   # Columns
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print() 
for i in range(1, 6):       # Row
    for j in range(i):   # Columns
        print(" ", end="")
    for k in range(2*(6-i)-1):
        print("*", end="")
    print()