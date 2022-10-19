import requests

API_KEY = "65MPkwtrYQKRmCHU_75lyaDUPkUJVn3w"

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

