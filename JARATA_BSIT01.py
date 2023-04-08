#Troy Liam Jarata
#1BSIT-1
#August 20, 2018
#CONTROL STRUCTURE
choice=(input("[O]ODD/EVEN\n[V]VOWEL/CONSONANT\n[G]GRADE IDENTIFIER\n\nSelect:"))
if(choice=='O' or choice=='o'):
    print("You have Selected ODD/EVEN\n\n")
    number=int(input("Enter a Number:"))
    if((number%2)==0):
          print("Even")
          exit()
    else:
          print("odd")
elif(choice=='V' or choice=='v'):
    print("You have Selected VOWEL/CONSONANT\n\n")
    let=input("Input a Letter:")
    if(let=='A' or let=='a'or let=='E' or let=='e' or let=='I' or let=='i' or let=='O' or let=='o' or let=='U' or let=='u'):
        print("Vowel")
    elif(let=='b'or let=='B'  or let=='c'or let=='C' or let=='d'or let=='D' or let=='f'or let=='F' or let=='g'or let=='G' or let=='h'or let=='H' or  let=='J' or let=='j' or let=='k'or let=='K' or let=='l'or let=='L' or let=='m'or let=='M' or let=='n'or let=='N' or let=='p'or let=='P' or let=='q'or let=='Q' or let=='r'or let=='R' or let=='s'or let=='S' or let=='t'or let=='T' or let=='v' or let=='V'or let=='w'or let=='W' or let=='x'or let=='X' or let=='y'or let=='Y' or let=='z'or let=='Z' ):
        print("Consonant")
    else:
        print("Invalid Input, The program will terminate")
        exit()
elif(choice=='G' or choice=='g'):
    print("You have Selected GRADE IDENTIFIER\n\n")
    x=float(input("Enter Grade:"))
    if(x>=94.8 or x==100.0):
        print("Numerical equivalent: 5.00")
        print("PASSING")
    elif(x>=89.2 or x==94.7):
        print("Numerical equivalent: 1.25")
        print("PASSING")
    elif(x>=83.6 or x==89.1):
        print("Numerical equivalent: 1.50")
        print("PASSING")
    elif(x>=78.0 or x==83.5):
        print("Numerical equivalent: 1.75")
        print("PASSING")
    elif(x>=72.4 or x==77.9):
        print("Numerical equivalent: 2.00")
        print("PASSING")
    elif(x>=66.8 or x==72.3):
        print("Numerical equivalent: 2.25")
        print("PASSING")
    elif(x>=61.2 or x==66.7):
        print("Numerical equivalent: 2.50")
        print("PASSING")
    elif(x>=55.6 or x==61.1):
        print("Numerical equivalent: 2.75")
        print("PASSING")
    elif(x>=50.0 or x==55.5):
        print("Numerical equivalent: 3.00")
        print("PASSING")
    elif(x>=0 or x==49.9):
        print("Numerical equivalent: 0")
        print("Failing")
    else:
        print("Invalid Input, The program will terminate")
        exit()
        
    
    
else:
    print("Invalid Input, The program will terminate")
    exit()
    
    
