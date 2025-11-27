#right side triangle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#
#     for k in range(i+1):
#         print("*",end="")
#
#     print()


#right sided inverted
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(i,n):
        print("*",end="")

    print()