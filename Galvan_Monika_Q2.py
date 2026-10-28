#Creating a Python Program to calculate shipping tax based on the State the user resides in
#Based on their sales item.
#Create an If-Else statement that mathematically calculate the shipping from sales price

#Have the user input the price of the sale item
item_price = float(input("Please enter the price of the sale item: $"))

#Have the user input the state they are from ( important to emphasize the 'state' value must be capitalized )
state = str(input("Enter the capitalized initials of the State you are from: "))

#Calculate the user's Ship Taxes and Total after Shipping by using If Else statements
if state == "TX" or state == "LA":
    total_price = item_price + 1.25
    print("Based on your current residence, your shipping tax is approximately $1.25! Your total is now $", total_price, "!")

elif state == "CA":
    total_price = item_price + 3.25
    print("Based on your current residence, your shipping tax is approximately $3.25! Your total is now $", total_price, "!")

else:
    total_price = item_price + 0.50
    print("Based on your current residence, your shiopping tax is approximately $0.50! Your total is now $", total_price, "!")
