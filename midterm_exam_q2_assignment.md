# Midterm Exam Question 2

## Question 2: Determining the User's Shipping Tax based on what State they reside in

In this scenario, I was assigned to do the following:
"Write a Python program to get the price of the sale item from the user. (For example: Enter 3.99 or 5.00, etc ) Get the state to which the item to be shipped (ex: TX, LA, CA, etc) from the user as well."
"If the state to be shipped is TX or LA then the shipping tax is 1.25, if the state to be shipped is CA, then the shipping tax is 3.25, otherwise all other states shipping tax is 0.50."
"Just display the shipping tax for the user accordingly."

## My Assignment and Process

This assignment was another demonstration of utilizing the IF-ELSE statement to solve the scenario with additional steps to consider. I first prompted the user to input the value of the sale price on the item by using the 'float' value due to currency being in decimal form. I then added another prompt that has the user input the state on where they are from, utilizing the 'string' value since the user will input plain text rather than numbers. Additionally, I had to emphasize that the user uses capitalization when inputting the string value in order to possibly prevent any forms of issues that may occur ( such as skipping "blocks" because it didn't recognize tx as TX ). 

Once that was issues, I then created the IF-ELIF-ELSE statements as followed. If the user input the value of "TX" OR the value of "LA", then the shipping tax of 1.25 will be displayed. It then skips to the next block if the user inputs a value of CA, which will then display 3.25. Then finally, it skips straight to the ELSE statement if the value does not match any of the prior ones, which will display a tax value of 0.50. 

As an addition, I added an extra step to demonstrate my understanding of the Python topic, as well as needed practice. I created a different statement with the first prompt that the user inputs and utilized it to calculate the total cost of what everything would look like, with the dedicated shipping tax included.

## Submission

There are exactly 4 files that will be submitted:
- File 1: The Python Program, which will demonstrate the working program
- File 2: A Screenshot, where it demonstrates what the message will print if the user inputs a string value of TX
- File 3: A Screenshot, where it demonstrates what the message will print if the user inputs a string value of CA
- File 4: A Screenshot, where it demonstrates what the message will print if the user inputs a string value of AL
