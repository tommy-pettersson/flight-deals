import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")
TOMORROW = (datetime.now() + relativedelta(days= +1)).strftime("%d/%m/%Y")
SIX_MONTHS = (datetime.now() + relativedelta(months= +6)).strftime("%d/%m/%Y")
FLY_FROM = "STO"

class FlightSearch:
    
    def get_iata_code(city_name):
        endpoint = "https://api.tequila.kiwi.com/locations/query"
        header = {
            "apikey": API_KEY,
        }
        parameters = {
            "term": city_name
        }
        try:
            response = requests.get(url=endpoint, params=parameters, headers=header)
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        else:
            data = response.json()
            first_city = data["locations"][0]
            city_code = first_city["code"]
            return city_code

    def get_matching_flights(city_code, max_price):
        endpoint = "https://api.tequila.kiwi.com/v2/search"
        header = {
            "apikey": API_KEY
        }
        parameters = {
            "fly_from": FLY_FROM,
            "fly_to": city_code,
            "date_from": TOMORROW,
            "date_to": SIX_MONTHS,
            "flight_type": "oneway",
            "curr": "SEK",
            "locale": "se",
            "price_to": max_price
        }
        try:
            response = requests.get(url=endpoint, params=parameters, headers=header)
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        else:
            data = response.json()
            flights = data["data"]
            return flights
