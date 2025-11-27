#numbers 1
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()    


#numbers 2
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    


#numbers 3
n=5
sum=1
for i in range(n):
    for j in range(i+1):
        print(sum,end=" ")
        sum+=1

    print()    