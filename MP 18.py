#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
#We ask for input for number
x=int(input("Enter at least (2-digit) number: "))
#We string the input
y=str(x)
#We make variable to get the reverse
reverse = y[::-1]
#We display the the revesed number
print("REVERSE:",reverse)
#We use if and else structure to identify if its Palindrome or not
if(y==reverse):
    print("PALINDROME")
else:
    print("NOT A PALINDROME")

