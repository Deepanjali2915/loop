year=int(input("Enter the number;"))
i=1
while i<=year:
    if year%4==0:
        print("leap year")
    else:
        print("notleap year:")
    i=i+1    
    break