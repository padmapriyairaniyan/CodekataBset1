n1=int(input("enter starting number"))
n2=int(input("enter ending number"))
l=[]
for i in range(n1,n2):
    if(i%2==0):
        l.append(i)
print(l)
