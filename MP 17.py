#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
#We use  Define Variation to make repitition
def Menu():
    def fibonacci(a):
        #we make a list to contain the inputs
        container=[]
        #Inputs
        x=int(input("Enter two numbers:\n"))
        y=int(input(""))
        #If and else structure for geeting fibonacci structure
        if (a==0 or a==1):
            print(a)
        else:
            #We add the input to the container
            container.append(x)
            container.append(y)
            #We use loop for appear the fibonacci
            while len(container)!=a:
                comp=x+y
                container.append(comp)
                x=y
                y=comp
        print(container)
    #Closing of Fibbonacci Menu
    fibonacci(12)
    #We created other input for terminating and reptition
    menu=input("Do you want to Exit? (Y/N): ")
    if(menu=='Y' or menu=='y'):
        exit()
    elif(menu=='n' or menu=='N'):
        Menu()
#Close the menu
Menu()

        
        
        
    
