#Create a Python Program to determine how many hours the baby is going to sleep.
#Based on the amount of milk the baby drinks before sleeping.
#Utilizing If-Else statements to get the end-result

#Ask the User for the total ounces of milk consumed using float
milk_amount = float(input("How many ounces of milk did your child drink before bed tonight?" ))

#Create the if - else statement
if milk_amount >= 6.0:
    print("Your baby will sleep well for 5 hours! Take a Break!")

else:
    print("The baby will not sleep well tonight. So be prepared and plan accordingly!")
