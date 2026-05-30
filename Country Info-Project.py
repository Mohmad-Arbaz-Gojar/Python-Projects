import requests

def country_info(name):
    try:
        url = f"https://restcountries.com/v3.1/name/{name}"
        response = requests.get(url)
        if response.status_code == 404:
            print(f"{name} not found. Please check the spelling and try again.")
            return
        data = response.json()

        country = data[0]
        print(f"Name of Country :{country['name']['common']}")
        print(f"Capital : {country['capital'][0]}")
        print (f"Population : {country['population']:,}")
        currency_code = list(country['currencies'].keys())[0]
        currency_name = country['currencies'][currency_code]['name']
        print(f"Currency Name : {currency_name}")
 
    except Exception as e:
        print(f"Error fetching country information:{e}")
while True:
    name = input("Enter the name of the country (or 'quit' to exit): ")
    if name.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break
    country_info(name)