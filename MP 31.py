#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#1BSIT-01
list1 = []
list2 = []
print("INPUT 10 NUMBER: ")
for x in range(10):
    y = int(input(""))
    list1.append(y)
minis = int(input("\nEnter minimum value: "))
maxs = int(input("Enter maximum value: "))
for y in range(10):
    if ((list1[y]>=minis) and (list1[y]<=maxs)):
        list2.append(list1[x])
value=len(list2)
print("WITHIN THE MIN AND MAX VALUE: ",value )
z=open("MP 31.txt",'w')
z.write("============================================================\n")
z.write("Numbers Inputed:\n")
for a in range(len(list1)):
    z.write(str(list1[a]))
    z.write("\n")
z.write("WITHIN THE MIN AND MAX VALUE: ")
z.write(str(value))
z.write("\n============================================================")
z=open("MP 31.txt",'r')
z.close



