#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
number=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even=0
odd=0
for x in range (len(number)):
    if number[x]%2==0:
        even+=1
    else:
        odd+=1
a=str(odd)
b=str(even)
print("====================================================")
print("Number of odd number: ",a)
print("Number of even number: ",b)
print("====================================================")
z=open("MP 35.txt",'w')
z.write("====================================================")
z.write("\nNumber of odd number: ")
z.write(str(odd))
z.write("\n")
z.write("Number of even number: ")
z.write(str(even))
z.write("\n====================================================")
z.close()



        
