#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
#We ask a input for alphabet
x=input("Enter an alphabet: ")
#We use if and else structure to identify if its Consonant or vowel and Uppercase and lower case
if(x=='B' or x=='C'or x=='D'or x=='F'or x=='G'or x=='H'or x=='J'or x=='K'or x=='L'or x=='M'or x=='N'or x=='O'or x=='P'or x=='Q'and x=='R'or x=='S'or x=='T'or x=='V'or x=='W'or x=='X'or x=='Y'or x=='Z'):
    #and we display each of it
    print("CONSONANT\nUPPERCASE")
elif(x=='b' or x=='c'or x=='d'or x=='f'or x=='g'or x=='h'or x=='j'or x=='k'or x=='l'or x=='m'or x=='n'or x=='o'or x=='p'or x=='q'or x=='r'or x=='s'or x=='t'or x=='v'or x=='w'or x=='x'or x=='y'or x=='z'):
    print("CONSONANT\nLOWERCASE")    
elif(x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
    print("VOWEL\nUPPERCASE")
elif(x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
    print("VOWEL\nLOWERCASE")
else:
    #We display if the input is invalid
    print("INVALID INPUT")
    
