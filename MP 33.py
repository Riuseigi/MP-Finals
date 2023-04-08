#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
container=[]
print("Input Numbers")
for x in range(10):
    a=int(input(""))
    container.append(a)
print("Index Number\tList")
for y in range(len(container)):
     print(y," . ","\t\t",container[y])
b=input("\n[M]Modify\n[R]Remove \n\n Choose One: ")
if(b=='M' or b=='m'):
    input1=int(input("Index Number to be Modify: "))
    input2=int(input("Enter number to change: "))
    container.remove(container[input1])
    container.insert(input1,input2)
elif(b=='R' or b=='r'):
    f=int(input("Index Number to be deleted: "))
    container.remove(container[f])
print("Index Number\tList")
for z in range(len(container)):
    print(z," . ","\t\t",container[z])
a = open("MP 33.txt","w")
a.write("==================================================================\n")
if(b=='M' or b=='m'):
    a.write("\nIndex Number to be Modified: ")
    a.write(str(input1))
    a.write("\nEnter number to changed: ")
    a.write(str(input2))
elif(b=='R' or b=='r'):
    a.write("Index Number to be deleted: ")
    a.write(str(f))
a.write("Index Number\t\tList")
for future in range(len(container)):
    a.write("\n")
    a.write(str(future))
    a.write(". ")
    a.write("\t\t\t")
    a.write(str(container[future]))
    a.write("\n==================================================================")
a.close()
print("Successfully Done")
