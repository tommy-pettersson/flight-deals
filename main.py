from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

def main():

    cities = DataManager.get_sheet_data()
    for city in cities:
        if city["iataCode"] == "":
            sheet_id = city["id"]
            iata_code = FlightSearch.get_iata_code(city["city"])
            DataManager.populate_iata_code(sheet_id, iata_code)

if __name__ == "__main__":
    main()