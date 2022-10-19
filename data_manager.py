import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
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