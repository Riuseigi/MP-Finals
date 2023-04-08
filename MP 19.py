#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
def digit():
    x=int(input("Enter a Number: "))
    sum=0
    while(x!=0):
        b=x%10
        sum=sum+b
        x=x//10
    print("Total: ",sum)
    menu=input("Try Again? (Y/N): ")
    if(menu=='Y' or menu=='y'):
        digit()
    elif(menu=='n' or menu=='N'):
        exit()
digit()
        
