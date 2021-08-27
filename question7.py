i=5
while 1<=i:
    game=int(input("enter the number"))
    if game<=10 and game!=6:
        print("incorrect guess")
    elif game==6:
        print("correct guess")
        break
    i=i-1
    print("you have only",i,"chances.")


# i=0
# while i<=5:
#     game=int(input("enter the number"))
#     if game<=10 and game!=6:
#         print("not define")
#         if game==6:
#             print(game,"you are the winner")
#         else:
#             print(game,"define")
#     else:
#         print(game,"you are not winner")
# i+=1



