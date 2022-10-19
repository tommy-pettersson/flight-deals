import requests

class DataManager:

    def get_sheet_data():
        
        endpoint = "https://api.sheety.co/d031524d83ceef01e73423e68c794a9e/flightDeals/prices"

        try:
            response = requests.get(url=endpoint)
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        else:
            data = response.json()
            return data["prices"]

    
    def populate_iata_code(object_id, iata_code):

        endpoint = f"https://api.sheety.co/d031524d83ceef01e73423e68c794a9e/flightDeals/prices/{object_id}"

        data = {
            "price": {
                "iataCode": iata_code
            }
        }

        try:
            response = requests.put(url=endpoint, json=data)
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        else:
            print("Data saved succesfully.")