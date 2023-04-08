#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#1BSIT-01
#Control Structure
#We asking a number and contain to the variable
x=input("Enter a number:")
#We use If and else structure to identify if it is Positive,Negative,Zero and Invalid
try:
    if(int(x)>0):
        print("POSITIVE")
    elif(int(x)<0):
        print("NEGATIVE")
    elif(int)(x==0):
        print("ZERO")
except(ValueError):
    print("Invalid")
