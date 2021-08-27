i=10
while 1<=i:
    game=int(input("enter the number"))
    if game<5:
        print("number is Smaller:")
    elif game>5:
        print("number is Bigger:")
    else:    
        print("correct guess")
        break
    i=i-1
    print("you have only",i,"chances.")





