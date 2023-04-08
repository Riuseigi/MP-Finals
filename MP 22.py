#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#1BSIT-01
#Control Structure
#We use define variation
def table():
    #We ask a multiplier Value
    a=int(input("ENTER MULTIPLIER VALUE: "))
    a+=1
    #We use for looping staement to make table
    for x in range(1,a):
        for y in range(1,a):
            #We display of each
            print(x * y,end=" ")
            #We seperate
            print("\n")
    menu=input("Do you want to Exit? (Y/N): ")
    #We make if and else structure for repitition
    if(menu=='Y' or menu=='y'):
        exit()
    elif(menu=='n' or menu=='N'):
        table()
#Close the define variation
table()
