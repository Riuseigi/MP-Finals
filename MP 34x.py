#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#1BSIT-01
#Display the message in one line
#We display this message in one line
container = []
print("Input Number")
for x in range(10):
    lagay=int(input(""))
    container.append(lagay)
a=container.count(max(container))
print("Occurence of the biggest number: ",a)
b=str(a)
c=str(container)
d=max(container)
e=str(d)
f=open("MP 34.txt",'w')
f.write("==================================================================\n")
f.write("NUMBERS INPUTED: \n")
for future in range(len(container)):
    f.write(str(container[future]))
    f.write("\n")
f.write(("Occurence of the biggest number: "))
f.write(str(b))
f.write("\n==================================================================")
f=open("MP 34.txt",'r')
f.close
print("Successfully Done")
