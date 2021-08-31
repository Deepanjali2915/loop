# row=int(input("Enter the the rows:"))
# for i in range(0,row+1):
#  for j in range(i):
#      print("*",end='')
#  print()   


# Extra Question for mentor

# i=7
# row=int(input("Enter the number:"))
# while i<=row:
#     j=1
#     while j<=i:
#         print(j,end='')
#         j=j+1
#     i=i+1
#     print()
     


num=int(input("enter the number"))
row=0
while row<num:
    star=row+1
    while star>0:
        print("*",end="")
        star=star-1
    row=row+1
    print()






