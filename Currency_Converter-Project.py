import requests

def currency_converter(amount, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        rate = data['rates'][to_currency]
        result = amount * rate
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
    
while True:
    print("\n\33[30m1. Convert Currency")
    print("2. Exit")
    choice = input("\33[32mEnter your choice: ")
    if choice == '2':
        print("Allah Hafiz!")
        break
    amount = float(input("\33[32mEnter the amount: "))
    from_currency = input('\33[33mEnter the currency you want to conver from (e.g.,INR): ').upper()
    to_currency = input('\33[34mEnter the currency you want to convert into (e.g.,USD): ').upper()
    currency_converter(amount, from_currency, to_currency)