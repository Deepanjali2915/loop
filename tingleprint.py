# rows = int(input("Enter the number of rows:"))  
# k = 2 * rows - 2  # It is used for number of spaces  
# for i in range(0, rows):  
#     for j in range(0, k):  
#         print(end=" ")  
#     k = k - 2   # decrement k value after each iteration  
#     for j in range(0, i + 1):  
#         print("* ", end="")  # printing star  
#     print("")  



# row=int(input("Enter the number;"))
# k=2
# i=0
# while i<=row:
#     j=k
#     while j<=k:
#         print(end='')
#         k=k-2
#     j=0
#     while j==i+1:
#         print("*",end='')
#     j=j+1
# i=i+1
# print("")         



row=int(input("Enter the number;"))
z=0
i=0
while i<=row:
    j=1
    while j<=row-i:
        print(" ",end='')
        j=j+1
    j=0
    while j<=z:
        print(i,end='')   #we use i ,j ,z
        j=j+1
    z=z+2
    print()
    i=i+1         
