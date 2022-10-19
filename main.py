from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

def main():
    
    location_data = FlightSearch.get_iata_code("stockholm")
    pprint(location_data)


if __name__ == "__main__":
    main()