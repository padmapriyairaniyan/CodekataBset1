n=int(input("enter a number"))
flag=0
if(n==1):
    print("neither prime nor composite")
elif(n<=0):
    print("invalid input")
else:
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break

    if(flag==0):
        print("it is a prime")
    else:
        print("it is not a prime")
