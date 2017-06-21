n=int(input("enter a number to find factorail"))
def fact(n):

    if(n==1 or n==2):
        return n
    else:
        return(n*fact(n-1))
print(fact(n))
