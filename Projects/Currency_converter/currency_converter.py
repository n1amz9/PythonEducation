import requests
import json

# https://app.freecurrencyapi.com/dashboard

URL = "https://www.cbr-xml-daily.ru/daily_utf8.xml"
new_path="D:/CodingForDummies/Python/PythonEducation/Projects/Currency_converter/currency_values.json"

def get_currents():
    with open ("D:/CodingForDummies/Python/PythonEducation/Projects/Currency_converter/currency_values.json", mode='r') as read_json :
        allCurrencies = json.load(read_json)
        return(allCurrencies)

    
def converter():
    return None


def main() :
    test = get_currents()
    print (test)
    print (type(test))
    
if __name__ == "main":
    main()