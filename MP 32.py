#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#1BSIT-01
integerVal = [42,12,0,75,100,19,1,200,90]
x=min(integerVal)
y=max(integerVal)
print("====================================================")
print("Minimum: ",x,"\nMaximum: ",y)
print("====================================================")
z=open("MP 32.txt",'w')
z.write("====================================================\n")
z.write("Minimum: ")
z.write(str(x))
z.write("\n")
z.write("Maximum: ")
z.write(str(y))
z.write("\n")
z.write("====================================================\n")
z=open("MP 32.txt",'r')
z.close
