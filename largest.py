print("enter three numbers")
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))
if n1>n2 and n1>n3:
    print("n1 is the largest"+str(n1))
elif n2>n3:
    print("n2 is thr largest"+str(n2))
else:
    print("n3 is the largest"+str(n3))
