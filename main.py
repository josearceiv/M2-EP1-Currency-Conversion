def convert_currency():
    print("Choose the currency to convert from:")
    print("1 - USD")
    print("2 - YEN")
    print("3 - WON")
    print("4 - PESO")
    print("5 - CAD")
    print("6 - EURO")
    
    from_currency = int(input("Enter the number corresponding to the currency you want to convert from: "))
    
    print("\nChoose the currency to convert to:")
    print("1 - USD")
    print("2 - YEN")
    print("3 - WON")
    print("4 - PESO")
    print("5 - CAD")
    print("6 - EURO")
    
    to_currency = int(input("Enter the number corresponding to the currency you want to convert to: "))
    
    amount = float(input("Enter the amount of currency you have: "))
    
    # Conversion rates
    usd_to_yen = 109.69
    usd_to_won = 1151.93
    usd_to_peso = 19.88
    usd_to_euro = 0.84
    usd_to_cad = 1.25
    
    # Convert from selected currency to USD
    if from_currency == 1:
        usd_amount = amount
    elif from_currency == 2:
        usd_amount = amount / usd_to_yen
    elif from_currency == 3:
        usd_amount = amount / usd_to_won
    elif from_currency == 4:
        usd_amount = amount / usd_to_peso
    elif from_currency == 5:
        usd_amount = amount / usd_to_cad
    elif from_currency == 6:
        usd_amount = amount / usd_to_euro
    else:
        print("Invalid input for 'from' currency.")
        return
    
    # Convert from USD to selected currency
    if to_currency == 1:
        result = usd_amount
    elif to_currency == 2:
        result = usd_amount * usd_to_yen
    elif to_currency == 3:
        result = usd_amount * usd_to_won
    elif to_currency == 4:
        result = usd_amount * usd_to_peso
    elif to_currency == 5:
        result = usd_amount * usd_to_cad
    elif to_currency == 6:
        result = usd_amount * usd_to_euro
    else:
        print("Invalid input for 'to' currency.")
        return
    
    print(f"\nResult: {amount} in currency {from_currency} is equivalent to {result} in currency {to_currency}")

# Run the program
convert_currency()
