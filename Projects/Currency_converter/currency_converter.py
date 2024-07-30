import requests
import xmltodict

APIurl = "https://www.cbr-xml-daily.ru/daily_utf8.xml"

def get_current_currents():
    try:
        upd_currents = requests.get(APIurl)
        upd_currents = xmltodict.parse(upd_currents)
    except Exception as e:
        print (f"!ERROR!: {e}")
        return None
    
def converter():
    return None


def main() :
    test = get_current_currents()
    
if __name__ == "main":
    main()