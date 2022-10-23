from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime
from pprint import pprint
import json

def main():

    # Populate IATA Codes in spreadsheet
    cities = DataManager.get_sheet_data()
    for city in cities:
        if city["iataCode"] == "":
            sheet_id = city["id"]
            iata_code = FlightSearch.get_iata_code(city["city"])
            DataManager.populate_iata_code(sheet_id, iata_code)

    # Find matching flights
    matching_flights = []
    cities = DataManager.get_sheet_data()
    for city in cities:

        iata_code = city["iataCode"]
        price = city["lowestPrice"]
        flights = FlightSearch.get_matching_flights(iata_code, price)

        for flight in flights:

            departure_date = datetime.fromisoformat(flight["local_departure"][:-1]).strftime("%Y-%m-%d")

            new_flight = FlightData(
                city_from=flight["cityFrom"],
                airport_from=flight["flyFrom"],
                city_to=flight["cityTo"],
                airport_to=flight["flyTo"],
                price=flight["price"],
                date=departure_date,
            )

            matching_flights.append(new_flight)

    # Send email about matching flights.

if __name__ == "__main__":
    main()