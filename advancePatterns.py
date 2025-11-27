#1
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")

#     for k in range(2*(n-i)-2):
#         print(" ",end="")

#     for k in range(i+1):
#         print("*",end="")

#     print()   


#2
#upper
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")

#     for k in range(2*(n-i)-2):
#         print(" ",end="")

#     for k in range(i+1):
#         print("*",end="")

#     print()             

# #lower
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")

#     for k in range(2*(i+1)-2):
#         print(" ",end="")

#     for k in range(n-i):
#         print("*",end="")

#     print()



#3
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(n):
#         print("*",end="")

#     print()    

#4
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for k in range(i):
        print(i,end=" ")

    print()                
