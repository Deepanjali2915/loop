# n=int(input(" number:"))
# i=1
# tsum=0
# while i<=n:
#     sum=int(input("enter the number:"))
#     tsum=tsum+sum
#     i+=1
# print("Total:",tsum)    

# n=int(input("Enter the number:"))
# prime=int(input("Enter the number:"))
# i=1
# count=0
# while i>0:
#     if prime%i==0:
#         count+=1
#     i+=1    
# if count==2:
#     print("it is a prime no.:") 
# else:
#     print("It is not a prime number")

n=int(input("Enter the number:"))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1    
if count==2:
    print("prime number:")
else:
    print("not prime number:")        