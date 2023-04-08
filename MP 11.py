a=int(input("Enter 1st integer: "))
b=(input("Enter Operator: "))
c=int(input("Enter 2nd integer: "))
add=(a+c)
subt=(a-c)
multi=(a*c)
divide=(a/c)
mod=(a%c)
if(b=="+"):
    print(a,b,c,"\nsum: ",add)
elif(b=="-"):
    print(a,b,c,"\ndifference: ",subt)
elif(b=="*"):
    print(a,b,c,"\nproduct: ",multi)
elif(b=="/"):
    print(a,b,c,"\ndivision: ",divide)
elif(b=="%"):
    print(a,b,c,"\nmodulos: ",mod)
else:
    exit()
