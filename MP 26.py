#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
x=int(input("How many asterisk do you want: "))
menu=input("What do you want:\n\n[H] Horizontal Display\n[V] Vertical Display\n\nChoice: ")
counter="* "*x
if (menu=='V' or menu=='v'):
    for x in range(x):
        print("\t\t\t*\t\t\t")
elif (menu=='H' or menu=='v'):
    ##We display the vertical
        print("\t\t\t\t",end=counter)
