alp='deepu'        
a=70
i=0
row=int(input("Enter the number:"))
while i<=row:
    j=0
    alpha=chr(a)
    while j<=i:
        print(alpha,end='')
        j+=1
    a-=1
    i+=1
    print() 

