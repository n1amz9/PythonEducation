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
  
def converter(num1, cur1, cur2):
    outputCurrents = get_currents()
    
    for outputCurrent in outputCurrents :
        isFound = False
        if outputCurrent:
            for getOutput in outputCurrent["ValCurs"]["Valute"]:
                if getOutput.get["CharCode"] == cur1:
                    print (getOutput.get["Value"])
                    result = float(getOutput.get["Value"]) / num1
                    isFound = True
        return (result, cur1, cur2 , isFound)
        
def check_converter(result, isFound):
    try:
        if (isFound == False):
            raise ValueError("Вашей валюты нет в списке!")
    except Exception as e:
        print(f"Произошла ошибка!: {e}")
        
def start():
    print ("Welcome to the Currency converter owo")
    print ("==================================")
    num1 = input("Введите количество валюты: ")
    cur_or = input ("Введите название валюты: (к примеру RUB, BYN): ")
    cur_dest = input ("Введите валюту, в которую нужно перевести: (USD, EUR, etc) ")
    
    return (int(num1), cur_or, cur_dest)  # возвращаем кол-во валюты, конвертируемую валюту, и конечную валюту

def main() :
    # num1, cur_or, cur_dest = start()
    # converter(num1, cur_or, cur_dest)
    outputCurrents = get_currents()
    a = "RUB"
    print(outputCurrents["ValCurs"]["Valute"])
    for outputCurrent in outputCurrents:
        print(outputCurrent[1])
    
if __name__ == "__main__":
    main()