import requests

#currencies = {"USD":4.4463, "EUR":4.7847, "CHF":4.8519, "GPB":5.4193, "NOK":0.4412}
currencies = ("USD", "EUR", "CHF", "GBP", "NOK")

def get_rate(code: str):
    url = 'http://api.nbp.pl/api/exchangerates/rates/a/' + code + '/'
    response = requests.get(url)
    if response.status_code == 200:  #raise InvalidURL ??? 
        rate = response.json()
        return rate['rates'][0]['mid']
    else:
        print("Program can't get current currency rate!\n Try again.")
        return


def check_input_amount():
    input_str = input("Enter an amout of money: \n")
    
    input_str = input_str.replace(",", ".")
    try:
        input_amount = float(input_str)
        return input_amount
    except ValueError:
        print("Invalid input data!\n")
        return 


def check_currency_code():
    input_code = input("Enter an currency_code: \n[USD, EUR, CHF, GBP, NOK] \n")

    if input_code in currencies:
        return input_code
    else:
        print("\nInvalid currency code!")
        return 


def currency_converter():
    amount = check_input_amount()
    print("\n")
    if amount == None:
        return

    rate_code = check_currency_code()
    if rate_code == None:
        return

    rate = get_rate(rate_code)
    if rate == None:
        return

    result = amount * rate
    result = round(result, 2)
    print("\n")
    print(str(result) + ' PLN (Currency rate: ' + str(rate) + ')')    

#currency_converter()

if __name__ == "__main__":
    condition = True
    while condition:
        currency_converter()

        if_next = input("\n-----If you want to quit, type q. Otherwise press Enter----- \n")
        if if_next == 'q':
            condition = False
