#Group Members
#1.Troy Liam Jarata
#2.Marc Janel Quita
#Joanna Marie Biason
#October 13,2018
#Control Structure
#We display the messgae and separate the input because this the logic it comes in our mind about this staemnet
print("Enter birthdate (dd/mm/yyyy):")
day=input("")
month=input("")
year=int(input(""))
#We use If and Else Structure to string the month and display it
if month=='1':
    print("JANUARY",day,year)
elif month=='2':
    print("FEBRUARY",day,year)
elif month=='3':
    print("MARCH",day,year)
elif month=='4':
    print("APRIL",day,year)
elif month=='5':
    print("MAY",day,year)
elif month=='6':
    print("JUNE",day,year)
elif month=='7':
    print("JULY",day,year)
elif month=='8':
    print("AUGUST",day,year)
elif month=='9':
    print("SEPTEMBER",day,year)
elif month=='10':
    print("OCTOBER",day,year)
elif month=='11':
    print("NOVEMBER",day,year)
elif month=='12':
    print("DECEMBER",day,year)
#We compute the Year today and Birth year
print("AGE(This Year)",2018-year)
