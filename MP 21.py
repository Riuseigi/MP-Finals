#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#1BSIT-01
#Control Structure
#We ask a input for alphabet
num1=int(input("Please enter an integer: "))
num2=int(input("Please enter an integer: "))
num3=int(input("Please enter an integer: "))

print("\n==============================")
print("Enter integer:  ",num1,"\n\t\t",num2,"\n\t\t",num3)
print("==============================")
print("\nSum: ",(num1+num2+num3),"\n")

if num1%2==0 and num1>0:
    print("even")
elif num1==0:
    print("neutral")
else:
    print("odd")

if num2%2==0 and num2>0:
    print("even")
elif num2==0:
    print("neutral")
else:
    print("odd")

if num3%2==0 and num3>0:
    print("even")
elif num3==0:
    print("neutral")
else:
    print("odd")

