### Module 2 Extra Project 1 Currency Conversion
In this project, we will be printing and converting different currencies based on user input. This is a currency converter that lists popular currencies that convert to and from USD. It takes in a number, in any listed currency, and the user chooses what to convert to. Or, you could print a list of value for all currencies available.

We will be utilizing the following topics:

Printing
Math
Data types
Type Conversions
Input

## Instructions
# Gameplan
1. Do a bit of research on the currency conversions between different countries. Here's what we're going to use (you don't have to use these):
* USD (United States Dollar)
* YEN (Japanese Yen)
* WON (South Korean Won)
* Peso (Mexican Peso)
* CAD (Canadian Dollar)
* EURO (European currency)
2. Next, let's mathematically breakdown our conversion rates. 1 US dollar equates to the following:
* 109.69 Yen
* 1151.93 Won
* 19.88 Mexican Pesos
* 0.84 Euro
* 1.25 Canadian Dollars
3. Create the equations to calculate USD to any currency:
* USD TO YEN: (Number of US dollars) * 109.69 = (Number of yen)
* USD TO WON: (Number of US dollars) * 1151.93= (Number of Won)
* USD TO PESO: (Number of US dollars) * 19.88 = (Number of Pesos)
* USD TO EURO: (Number of US dollars ) * 0.84 = (Number of Euro)
* USD TO CAD: (Number of US dollars) * 1.25 = (Number of Canadian Dollars)
4. If we want to convert any non USD currency to another non USD currency, it is required that you convert it to USD first, and then convert it to your required currency. Create the formulas to turn any currency to USD:
* YEN TO USD: (Number of Yen ) / 109.69 = (Number of US dollars)
* WON TO USD: (Number of Won ) / 1151.93 = (Number of US dollars)
* PESO TO USD: (Number of Peso) / 19.88 = (Number of US dollars)
* EURO TO USD: (Number of Euro) / 0.84 = (Number of US dollars)
* CAD TO USD: (Number of CAD) / 1.25 = (Number of US dollars)

# The Program
1. Take in an integer input (hint: casting) for converting from in the current options:
* 1 - USD
* 2 - YEN
* 3 - WON
* 4 - PESO
* 5 - CAD
* 6 - EURO
2. Next, take in a second input (integer as well), that will act as our convert-to currency, with the same options as above.
3. Next, write the amount of currency you have in the first option in a third double variable.
4. Next, write a ladder of if statements to check what the "from" currency is. Within those 6, make another 6 if statements for each of them, as seen below in the replit.
5. Finally, print out the result.
