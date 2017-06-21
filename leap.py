year=(input("enter a year"))
l=len(year)
if(l!=4):
    print("not a valid year")
else:
    n=int(year)
    if(n%4==0):
        print("it is a leap year")
    else:
        print("not a leap year")
