#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
#We ask a input for Peso Value
x=float(input("Enter PESO value:"))
#We use a input of choice in Menu
y=input("Menu:\n[A] Dollar\n[B] Yen\n[C] Rial\nChoice:")
#W use if and else structure to covert the peso value to the Dollar,Yen and Rial
if(y=='A' or y=='a'):
    #We display the Value of each choice
     print("Dollar Value:",round(x/44.52,3))
elif(y=='b' or y=='B'):
    print("Yen Value:",round(x/0.437,3))
elif(y=='C' or y=='c'):
    print("Rial Value:",round(x/0.084,3))
