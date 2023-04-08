#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
#We create variables to each item
counter=0
uppercase=0
lowercase=0
x=0
#We display this message before getting the input
print("Enter 10 letters:")
#We use for looping staement to ask 10 inputs
for x in range(10):
    y=input("")
    #We use If and else structure to identify the input if Lowercase or Uppercase
    if (y=='A'or y=='B'or y=='C'or y=='D'or y=='E'or y=='F' or y=='G'or y=='H'or y=='I'or y=='J'or y=='K'or y=='L'or y=='M'or y=='N'or y=='O'or y=='P'or y=='Q'or y=='R'or y=='S'or y=='T'or y=='U'or y=='V'or y=='W'or y=='X'or y=='Y'or y=='Z'):
        #We add the number of inputs with Uppercase Letter
        uppercase+=1
    elif(y=='a'or y=='b'or y=='c'or y=='d'or y=='e'or y=='f'or y=='g'or y=='h'or y=='i'or y=='j'or y=='k'or y=='l'or y=='m'or y=='n'or y=='o'or y=='p'or y=='q'or y=='r'or y=='s'or y=='t'or y=='u'or y=='v'or y=='w'or y=='x'or y=='y'or y=='z'):
        #We add the number of inputs with Lowercase Letter
        lowercase+=1
#We print the computed Uppercase and Lowercase and display how many
print("\nUPPERCASE: ",uppercase)
print("\nLOWERCASE: ",lowercase)



    
      
