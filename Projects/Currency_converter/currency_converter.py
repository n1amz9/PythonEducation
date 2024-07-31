import json
import requests
import xmltodict

# https://app.freecurrencyapi.com/dashboard
# https://www.cbr-xml-daily.ru/daily_utf8.xml

URL = "https://www.cbr-xml-daily.ru/daily_utf8.xml"
path = "D:/CodingForDummies/Python/PythonEducation/Projects/Currency_converter/currency_values.json"

def get_currents():
    with open (path, mode="r", encoding="utf-8") as read_file:
        allCurrencies = json.load(read_file)
        return(allCurrencies)
  
def converter():
    return "TEST"

def start():
    print ("Welcome to the Currency converter owo")
    print ("==================================")
    num1 = input("Введите количество валюты: ")
    cur_or = input ("Введите название валюты: (к примеру RUB, BYN): ")
    cur_dest = input ("Введите валюту, в которую нужно перевести: ")
    
    return (int(num1), cur_or, cur_dest)

def main() :
    start()
    
    
if __name__ == "__main__":
    main()