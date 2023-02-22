import argparse

import requests

def get_rate(code: str) -> float:
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{code}"
    response = requests.get(url)
    if response.status_code == 200: 
        rate = response.json()
        return rate['rates'][0]['mid']
    else:
        raise ValueError("Invalid currency code")

def convert(amount: float, currency_code: str) -> None:
    rate = get_rate(currency_code)
    return round(amount * rate, 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("amount", type=float, help="Amount of money")
    parser.add_argument("currency_code", type=str, help="Currency code")
    args = parser.parse_args()

    result = convert(args.amount, args.currency_code)
    print(result)