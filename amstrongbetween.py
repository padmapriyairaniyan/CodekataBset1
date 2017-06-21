a=int(input("enter a number"))
b=int(input("enter a number"))
k=[]
for i in range(a,b):
    n1=i
    n1=str(n1)
    l=len(n1)
    result=0
    while i!=0:
        r=i%10
        result+=(r**l)
        i=i//10

    if(int(n1)==result):

        k.append(str(result))
    else:
        pass
print(k)
