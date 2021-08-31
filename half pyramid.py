# row=int(input("Enter the number:"))
# for i in range(row+1,0,-1):
#     for j in range(0,i-1):
#       print("*",end='')
#     print("")    


row=int(input("Enter the number:"))
i=1
while i<row+1:
    j=1
    while j<i:
        print(i,end='')
        j=i+1
    i=i+1
    print("")            