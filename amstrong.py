n=int(input("enter a number"))
n1=n
n1=str(n1)
l=len(n1)
result=0
while n!=0:
    r=n%10
    result+=(r**l)
    n=n//10
print(result)
if(int(n1)==result):
    print("Amstrong number")
else:
    print("Not an Amstrong Number")
