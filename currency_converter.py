import requests

CURRENCIES = ("USD", "EUR", "CHF", "GBP", "NOK")


def get_rate(code: str) -> float:
    url = f"http://api.nbp.pl/api/exchangerates/ratezzz/a/{code}"
    response = requests.get(url)
    if response.status_code == 200: 
        rate = response.json()
        return rate['rates'][0]['mid']
    else:
        raise Exception("Invalid currency code")


def fetch_input_amount():
    input_str = input("Enter an amout of money: \n")
    
    input_str = input_str.replace(",", ".")
    try:
        input_amount = float(input_str)
        return input_amount
    except ValueError:
        print("Invalid input data!\n")
        return 


def fetch_currency_code() -> str:
    input_code = input("Enter an currency_code: \n[USD, EUR, CHF, GBP, NOK] \n")

    if input_code not in CURRENCIES:
        raise ValueError("Invalid currency code!")

    return input_code


def currency_converter():
    amount = fetch_input_amount()
    print("\n")
    if amount == None:
        return

    rate_code = fetch_currency_code()
    if rate_code == None:
        return

    rate = get_rate(rate_code)
    if rate == None:
        return

    result = amount * rate
    result = round(result, 2)
    print("\n")
    print(str(result) + ' PLN (Currency rate: ' + str(rate) + ')')    


if __name__ == "__main__":
    currency_converter()