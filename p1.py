#right side triangle
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")

    for k in range(i+1):
        print("*",end="")

    print()


#right sided inverted
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i):
#         print("*",end="")

#     print()



#hollow rectangle
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()        