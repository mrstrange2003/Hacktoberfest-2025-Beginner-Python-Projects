import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"].get(to_currency)

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        return amount * rate
    else:
        return None

print("Currency Converter")
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g. USD): ").upper()
to_currency = input("To currency (e.g. EUR): ").upper()
result = convert_currency(amount, from_currency, to_currency)
if result:
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
else:
    print("Conversion not available.")