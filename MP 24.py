#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
def line():
    print("    *\n  *   *\n *     *  \n*       *\n*********\n**     **\n* *   * *\n*  * *  *\n*   *   *\n*  * *  *\n* *   * *\n**     **\n*********")
    menu=input("Do you want to repeat? (Y/N): ")
    if(menu=='Y' or menu=='y'):
        line()
    elif(menu=='n' or menu=='N'):
        exit()
#Close the menu
line()

       
