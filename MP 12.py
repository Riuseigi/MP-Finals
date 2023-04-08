#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
#We ask 3 input Values
a=int(input("Enter three numbers:\n"))
b=int(input(""))
c=int(input(""))
#We use if and else structure to sort the ascending, descending values and Equal Values
if(a<b<c):
    #We display of each acending and descending
    print("ASCENDING: ",a,b,c)
    print("DESCENDING: ",c,b,a)
elif(a>b and b>c):
    #We display of each acending and descending
    print("ASCENDING: ",c,b,a)
    print("DESCENDING: ",a,b,c)
elif(b>a and a>c):
    #We display of each acending and descending
    print("ASCENDING: ",c,a,b)
    print("DESCENDING: ",b,a,c)
elif(c>b and b>a):
    #We display of each acending and descending
    print("ASCENDING: ",c,b,a)
    print("DESCENDING: ",a,b,c)
elif(a>c and c>b):
    #We display of each acending and descending
    print("ASCENDING: ",b,c,a)
    print("DESCENDING: ",a,c,b)
elif(c>a and a>b):
    #We display of each acending and descending
    print("ASCENDING: ",b,a,c)
    print("DESCENDING: ",c,a,b)
elif(b>c and c>b):
    #We display of each acending and descending
    print("ASCENDING: ",b,c,a)
    print("DESCENDING: ",a,b,c)
elif(a==b==c):
    #We display the equal values input
    print("Equal Values")
   
    
    
